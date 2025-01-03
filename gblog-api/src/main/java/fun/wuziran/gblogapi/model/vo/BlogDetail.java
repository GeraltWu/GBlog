package fun.wuziran.gblogapi.model.vo;

import fun.wuziran.gblogapi.entity.Category;
import fun.wuziran.gblogapi.entity.Tag;
import lombok.Data;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * @Description 文章详情
 * @Author Geralt
 * @Date 2024/7/17
 */
@Data
public class BlogDetail {
    private Long id;
    private String title;//文章标题
    private String content;//文章正文
    private Boolean appreciation;//赞赏开关
    private Boolean commentEnabled;//评论开关
    private Boolean top;//是否置顶
    private Date createTime;//创建时间
    private Date updateTime;//更新时间
    private Integer views;//浏览次数
    private Integer words;//文章字数
    private Integer readTime;//阅读时长(分钟)
    private String password;//密码保护

    private Category category;//文章分类
    private List<Tag> tags = new ArrayList<>();//文章标签
}