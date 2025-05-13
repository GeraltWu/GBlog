package fun.wuziran.gblog.viewbackend.util;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/12/22
 */

public class UserContext {
    private static final ThreadLocal<Long> userIdHolder = new ThreadLocal<>();
    private static final ThreadLocal<String> roleHolder = new ThreadLocal<>();
    
    public static void setUserId(Long userId) {
        userIdHolder.set(userId);
    }
    
    public static Long getUserId() {
        return userIdHolder.get();
    }
    
    public static void setRole(String role) {
        roleHolder.set(role);
    }
    
    public static String getRole() {
        return roleHolder.get();
    }
    
    public static void clear() {
        userIdHolder.remove();
        roleHolder.remove();
    }
} 