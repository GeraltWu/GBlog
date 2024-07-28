package fun.wuziran.gblogapi.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Data;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import java.util.List;

/**
 * @Description 用户信息
 * @Author Geralt
 * @Date 2024/7/17
 */
@Data
public class User implements UserDetails {
    private Long id;
    private String username;
    private String password;
    private String nickname;
    private String avatar;
    private String email;
    private Date createTime;
    private Date updateTime;
    private String role;

    /**
     * spring security 需要实现 UserDetails 接口，并提供以下方法：
     * getAuthorities()：返回用户的角色信息，用于 Spring Security 进行权限控制
     * getPassword()：返回用户的密码，用于 Spring Security 进行密码校验
     * getUsername()：返回用户的用户名，用于 Spring Security 进行用户认证
     * isAccountNonExpired()：返回用户的账号是否过期，用于 Spring Security 进行用户认证
     * isAccountNonLocked()：返回用户的账号是否被锁定，用于 Spring Security 进行用户认证
     * isCredentialsNonExpired()：返回用户的密码是否过期，用于 Spring Security 进行用户认证
     * isEnabled()：返回用户的账号是否可用，用于 Spring Security 进行用户认证
     * 以上方法均由 UserDetails 接口提供，并由子类实现。
     */

    @JsonIgnore // 对 User 类的实例进行 JSON 序列化和反序列化过程中忽略该方法
    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        List<GrantedAuthority> authorityList = new ArrayList<>();
        authorityList.add(new SimpleGrantedAuthority(role));
        return authorityList;
    }

    @JsonIgnore
    @Override
    public String getPassword() {
        return null;
    }

    @JsonIgnore
    @Override
    public String getUsername() {
        return null;
    }

    @JsonIgnore
    @Override
    public boolean isAccountNonExpired() {
        return UserDetails.super.isAccountNonExpired();
    }

    @JsonIgnore
    @Override
    public boolean isAccountNonLocked() {
        return UserDetails.super.isAccountNonLocked();
    }

    @JsonIgnore
    @Override
    public boolean isCredentialsNonExpired() {
        return UserDetails.super.isCredentialsNonExpired();
    }

    @JsonIgnore
    @Override
    public boolean isEnabled() {
        return UserDetails.super.isEnabled();
    }
}
