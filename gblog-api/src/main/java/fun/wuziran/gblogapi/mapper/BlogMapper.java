package fun.wuziran.gblogapi.mapper;

import fun.wuziran.gblogapi.entity.Blog;
import fun.wuziran.gblogapi.model.dto.BlogView;
import fun.wuziran.gblogapi.model.dto.BlogVisibility;
import fun.wuziran.gblogapi.model.vo.*;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */
@Mapper
@Repository
public interface BlogMapper {

    /**
     * 获取博客的ID和标题列表
     * @return 博客ID和标题列表
     */
    List<Blog> getIdAndTitleList();

    /**
     * 根据标题和分类ID获取博客列表
     * @param title 博客标题
     * @param categoryId 分类ID
     * @return 博客列表
     */
    List<Blog> getListByTitleAndCategoryId(String title, Integer categoryId);

    /**
     * 根据查询和是否发布获取搜索博客列表
     * @param query 搜索查询
     * @return 搜索博客列表
     */
    List<SearchBlog> getSearchBlogListByQueryAndIsPublished(String query);

    /**
     * 根据是否发布获取新博客列表
     * @return 新博客列表
     */
    List<NewBlog> getNewBlogListByIsPublished();

    /**
     * 根据是否发布获取博客信息列表
     * @return 博客信息列表
     */
    List<BlogInfo> getBlogInfoListByIsPublished();

    /**
     * 根据分类名称和是否发布获取博客信息列表
     * @param categoryName 分类名称
     * @return 博客信息列表
     */
    List<BlogInfo> getBlogInfoListByCategoryNameAndIsPublished(String categoryName);

    /**
     * 根据标签名称和是否发布获取博客信息列表
     * @param tagName 标签名称
     * @return 博客信息列表
     */
    List<BlogInfo> getBlogInfoListByTagNameAndIsPublished(String tagName);

    /**
     * 根据是否发布获取按年月分组的博客列表
     * @return 按年月分组的博客列表
     */
    List<String> getGroupYearMonthByIsPublished();

    /**
     * 根据年月和是否发布获取归档博客列表
     * @param yearMonth 年月
     * @return 归档博客列表
     */
    List<ArchiveBlog> getArchiveBlogListByYearMonthAndIsPublished(String yearMonth);

    /**
     * 根据限制数量、是否发布和是否推荐获取随机博客列表
     * @param limitNum 限制数量
     * @return 随机博客列表
     */
    List<RandomBlog> getRandomBlogListByLimitNumAndIsPublishedAndIsRecommend(Integer limitNum);

    /**
     * 获取博客的浏览量列表
     * @return 博客浏览量列表
     */
    List<BlogView> getBlogViewsList();

    /**
     * 根据ID删除博客
     * @param id 博客ID
     * @return 影响行数
     */
    int deleteBlogById(Long id);

    /**
     * 根据博客ID删除博客标签
     * @param blogId 博客ID
     * @return 影响行数
     */
    int deleteBlogTagByBlogId(Long blogId);

    /**
     * 保存博客信息
     * @param blog 博客信息，注意是数据展示层的Blog对象，不是实体类Blog
     * @return 影响行数
     */
    int saveBlog(fun.wuziran.gblogapi.model.dto.Blog blog);

    /**
     * 保存博客标签
     * @param blogId 博客ID
     * @param tagId 标签ID
     * @return 影响行数
     */
    int saveBlogTag(Long blogId, Long tagId);

    /**
     * 根据ID更新博客的推荐状态
     * @param blogId 博客ID
     * @param recommend 推荐状态
     * @return 影响行数
     */
    int updateBlogRecommendById(Long blogId, Boolean recommend);

    /**
     * 根据ID更新博客的可见性
     * @param blogId 博客ID
     * @param bv 博客可见性
     * @return 影响行数
     */
    int updateBlogVisibilityById(Long blogId, BlogVisibility bv);

    /**
     * 根据ID更新博客的置顶状态
     * @param blogId 博客ID
     * @param top 置顶状态
     * @return 影响行数
     */
    int updateBlogTopById(Long blogId, Boolean top);

    /**
     * 更新博客的浏览量
     * @param blogId 博客ID
     * @param views 浏览量
     * @return 影响行数
     */
    int updateViews(Long blogId, Integer views);

    /**
     * 根据ID获取博客
     * @param id 博客ID
     * @return 博客对象
     */
    Blog getBlogById(Long id);

    /**
     * 根据博客ID获取标题
     * @param id 博客ID
     * @return 博客标题
     */
    String getTitleByBlogId(Long id);

    /**
     * 根据ID和是否发布获取博客详情
     * @param id 博客ID
     * @return 博客详情对象
     */
    BlogDetail getBlogByIdAndIsPublished(Long id);

    /**
     * 获取博客的密码
     * @param blogId 博客ID
     * @return 博客密码
     */
    String getBlogPassword(Long blogId);

    /**
     * 更新博客信息
     * @param blog 博客信息 注意是数据展示层的Blog对象，不是实体类Blog
     * @return 影响行数
     */
    int updateBlog(fun.wuziran.gblogapi.model.dto.Blog blog);

    /**
     * 计算博客总数
     * @return 博客总数
     */
    int countBlog();

    /**
     * 根据是否发布计算博客数量
     * @return 发布的博客数量
     */
    int countBlogByIsPublished();

    /**
     * 根据分类ID计算博客数量
     * @param categoryId 分类ID
     * @return 分类下的博客数量
     */
    int countBlogByCategoryId(Long categoryId);

    /**
     * 根据标签ID计算博客数量
     * @param tagId 标签ID
     * @return 标签下的博客数量
     */
    int countBlogByTagId(Long tagId);

    /**
     * 根据博客ID获取评论是否启用的状态
     * @param blogId 博客ID
     * @return 评论是否启用的状态
     */
    Boolean getCommentEnabledByBlogId(Long blogId);

    /**
     * 根据博客ID获取发布状态
     * @param blogId 博客ID
     * @return 发布状态
     */
    Boolean getPublishedByBlogId(Long blogId);

    /**
     * 获取分类和博客数量的列表
     * @return 分类和博客数量的列表
     */
    List<CategoryBlogCount> getCategoryBlogCountList();
}

