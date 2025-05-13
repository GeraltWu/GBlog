package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;

/**
 * @Description 归档博客VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class ArchiveBlogVO {
    // 博客id
    private long id;
    // 博客标题
    private String title;
    // 发布日期
    private String day;
    // 访问密码
    private String password;
    // 是否私密文章
    private boolean isPrivate;
} 