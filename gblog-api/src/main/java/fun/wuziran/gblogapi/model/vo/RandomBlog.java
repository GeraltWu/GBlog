package fun.wuziran.gblogapi.model.vo;

import lombok.Data;

import java.util.Date;

/**
 * @Description 随机博客
 * @Author Geralt
 * @Date 2024/7/17
 */

@Data
public class RandomBlog {
    private Long id;
    private String title;//文章标题
    private String firstPicture;//文章首图，用于随机文章展示
    private Date createTime;//创建时间
    private String password;//文章密码
    private Boolean privacy;//是否私密文章
}
