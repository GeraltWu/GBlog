package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;

/**
 * @Description 最新博客VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class NewBlogVO {
    // 博客id
    private String id;
    // 博客标题
    private String title;
    // 访问密码
    private String password;
    // 是否私密文章
    private boolean isPrivate;
} 