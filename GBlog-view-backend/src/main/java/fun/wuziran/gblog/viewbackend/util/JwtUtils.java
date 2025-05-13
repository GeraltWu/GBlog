package fun.wuziran.gblog.viewbackend.util;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.util.StringUtils;

import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;
import java.util.Date;

/**
 * @Description jwt工具类
 * @Author Geralt
 * @Date 2024/10/22
 */
public class JwtUtils {

    public static final long EXPIRE = 1000 * 60 * 60 * 24 * 7; // token过期时间
    private static final String APP_SECRET = "ukc8BDbRigUDaY6pZFfWus2jZWLPHO12345678901234567890123456789012";
    public static final String SUBJECT = "meeting-scheduler";

    // 使用固定密钥
    private static SecretKey getSecretKey() {
        return Keys.hmacShaKeyFor(APP_SECRET.getBytes(StandardCharsets.UTF_8));
    }

    // 生成token字符串
    public static String createJwtToken(Long userId, String role) {
        return Jwts.builder()
                .header()
                    .add("typ", "JWT")
                    .and()
                .subject(SUBJECT)
                .issuedAt(new Date())
                .expiration(new Date(System.currentTimeMillis() + EXPIRE))
                .claim("userId", userId)
                .claim("role", role)
                .signWith(getSecretKey())
                .compact();
    }

    // 判断token是否存在与有效
    public static boolean checkToken(String jwtToken) {
        if (!StringUtils.hasText(jwtToken)) return false;
        try {
            Jwts.parser()
                .verifyWith(getSecretKey())
                .build()
                .parseSignedClaims(jwtToken);
        } catch (Exception e) {
            throw e; // 抛出异常交给拦截器处理
        }
        return true;
    }

    // 判断token是否存在与有效，从请求头中获取token
    public static boolean checkToken(HttpServletRequest request) {
        try {
            String jwtToken = request.getHeader("token");
            if (!StringUtils.hasText(jwtToken)) return false;
            Jwts.parser()
                .verifyWith(getSecretKey())
                .build()
                .parseSignedClaims(jwtToken);
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }

    // 判断token是否过期
    public static boolean isTokenExpired(String jwtToken) {
        if (!StringUtils.hasText(jwtToken)) return true;
        try {
            Claims claims = getAllClaimsFromToken(jwtToken);
            return claims.getExpiration().before(new Date());
        } catch (Exception e) {
            return true;
        }
    }

    // 从token中获取用户id
    public static Long getUserIdFromToken(String jwtToken) {
        Claims claims = getAllClaimsFromToken(jwtToken);
        if (claims == null) return null;
        
        Object idObj = claims.get("userId");
        if (idObj instanceof Number) {
            return ((Number) idObj).longValue();
        }
        return null;
    }

    // 从token中获取用户角色
    public static String getRoleFromToken(String jwtToken) {
        Claims claims = getAllClaimsFromToken(jwtToken);
        return claims != null ? (String) claims.get("role") : null;
    }

    // 从token中获取所有的claims
    public static Claims getAllClaimsFromToken(String jwtToken) {
        if (!StringUtils.hasText(jwtToken)) return null;
        return Jwts.parser()
                .verifyWith(getSecretKey())
                .build()
                .parseSignedClaims(jwtToken)
                .getPayload();
    }
}

