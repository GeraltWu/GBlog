package fun.wuziran.gblog.viewbackend.model.entity;

import lombok.Data;

/**
 * @Description 用户entity
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class User {
    // 用户id
    private long id;
    // 用户名
    private String username;
    // 密码
    private String password;
    // 昵称
    private String nickname;
    // 头像
    private String avatar;
    // 邮箱
    private String email;
    // 创建时间
    private String createTime;
    // 更新时间
    private String updateTime;
    // 用户角色
    private String role;
}
