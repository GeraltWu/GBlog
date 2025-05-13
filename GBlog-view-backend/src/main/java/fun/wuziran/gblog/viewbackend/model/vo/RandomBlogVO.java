package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;

/**
 * @Description 随机博客VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class RandomBlogVO {
    // 博客id
    private long id;
    // 博客标题
    private String title;
    // 博客首图
    private String firstPicture;
    // 创建时间
    private String createTime;
    // 访问密码
    private String password;
    // 是否私密文章
    private boolean isPrivate;
} 