package fun.wuziran.gblog.viewbackend.model.vo;

import fun.wuziran.gblog.viewbackend.model.entity.Category;
import fun.wuziran.gblog.viewbackend.model.entity.Tag;
import lombok.Data;
import java.util.List;

/**
 * @Description 基本信息VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class BasicInfoVO {
    // 个人介绍信息
    private IntroductionVO introduction;
    // 随机博客列表
    private List<RandomBlogVO> randomBlogList;
    // 标签列表
    private List<Tag> tagList;
    // 分类列表
    private List<Category> categoryList;
    // 最新博客列表
    private List<NewBlogVO> newBlogList;
    // 站点信息
    private SiteInfoVO sitInfo;
} 