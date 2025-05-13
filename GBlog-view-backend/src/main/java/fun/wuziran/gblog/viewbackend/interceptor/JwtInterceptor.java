package fun.wuziran.gblog.viewbackend.interceptor;

import com.fasterxml.jackson.databind.ObjectMapper;
import fun.wuziran.gblog.viewbackend.annotation.Admin;
import fun.wuziran.gblog.viewbackend.annotation.Auth;
import fun.wuziran.gblog.viewbackend.util.JwtUtils;
import fun.wuziran.gblog.viewbackend.util.Result;
import fun.wuziran.gblog.viewbackend.util.UserContext;
import io.jsonwebtoken.ExpiredJwtException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.HandlerInterceptor;

import java.lang.reflect.Method;

/**
 * @Description JWT拦截器，用于验证请求中的JWT并进行权限校验
 * @Author Geralt
 * @Date 2024/10/22
 */
@Slf4j
@Component
public class JwtInterceptor implements HandlerInterceptor {

    private final ObjectMapper objectMapper; // 用于将对象转换为JSON字符串
    private static final String BEARER_PREFIX = "Bearer "; // JWT前缀

    public JwtInterceptor(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
    }

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        // 检查处理器是否为HandlerMethod实例
        if (!(handler instanceof HandlerMethod handlerMethod)) {
            return true; // 如果不是，直接放行
        }

        Method method = handlerMethod.getMethod();
        // 检查方法上是否存在@Auth或@Admin注解
        if (!method.isAnnotationPresent(Auth.class) && !method.isAnnotationPresent(Admin.class)) {
            return true; // 如果没有注解，直接放行
        }

        // 获取请求头中的Authorization字段
        String authorization = request.getHeader("Authorization");
        if (authorization == null || !authorization.startsWith(BEARER_PREFIX)) {
            return handleError(response, "请先登录"); // 如果没有token或格式不正确，返回错误
        }

        // 提取JWT
        String token = authorization.substring(BEARER_PREFIX.length());
        log.info("token: {}", token);
        try {
            // 验证JWT
            if (JwtUtils.checkToken(token)) {
                log.debug("token验证成功");
                // 从JWT中提取用户ID
                Long userId = JwtUtils.getUserIdFromToken(token);
                log.info("用户ID：{}", userId);
                UserContext.setUserId(userId); // 将用户ID存储在UserContext中

                // 从JWT中提取用户角色
                String role = JwtUtils.getRoleFromToken(token);
                UserContext.setRole(role); // 将角色存储在UserContext中

                // 如果方法上没有@Admin注解，直接放行
                if (!method.isAnnotationPresent(Admin.class)) {
                    return true;
                }
                log.info("验证管理员权限", role);
                // 检查用户角色是否为admin
                if ("admin".equals(role)) {
                    return true; // 如果是管理员，放行
                }
                return handleError(response, "需要管理员权限"); // 否则返回权限错误
            }
            return handleError(response, "token无效"); // 如果token无效，返回错误
        } catch (ExpiredJwtException e) {
            return handleError(response, "token已过期"); // 如果token过期，返回错误
        } catch (Exception e) {
            log.error("token验证失败", e);
            return handleError(response, "token验证失败"); // 其他异常，返回错误
        }
    }

    // 处理错误响应
    private boolean handleError(HttpServletResponse response, String message) throws Exception {
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().write(objectMapper.writeValueAsString(Result.error(message))); // 返回JSON格式的错误信息
        return false; // 阻止请求继续处理
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, 
                              Object handler, Exception ex) {
        UserContext.clear(); // 清理UserContext，确保线程安全
    }
} 