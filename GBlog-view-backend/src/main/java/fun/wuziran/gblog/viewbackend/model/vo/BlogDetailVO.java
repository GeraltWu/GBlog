package fun.wuziran.gblog.viewbackend.model.vo;

import fun.wuziran.gblog.viewbackend.model.entity.Category;
import fun.wuziran.gblog.viewbackend.model.entity.Tag;
import lombok.Data;

import java.util.List;

/**
 * @Description 博客详情VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class BlogDetailVO {
    // 博客id
    private long id;
    // 博客标题
    private String title;
    // 博客内容
    private String content;
    // 是否发布
    private boolean isPublished;
    // 是否推荐
    private boolean isRecommend;
    // 是否开启赞赏
    private boolean isAppreciationEnabled;
    // 是否开启评论
    private boolean isCommentEnabled;
    // 是否置顶
    private boolean isTop;
    // 是否私密文章
    private String isPrivate;
    // 创建时间
    private String createTime;
    // 更新时间
    private String updateTime;
    // 浏览次数
    private int views;
    // 文章字数
    private int words;
    // 阅读时长(分钟)
    private int readTime;
    // 访问密码
    private String password;
    // 博客分类
    private Category categoryId;
    // 博客标签
    private List<Tag> tags;
}