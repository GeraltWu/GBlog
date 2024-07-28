package fun.wuziran.gblogapi.mapper;

import fun.wuziran.gblogapi.entity.Tag;
import fun.wuziran.gblogapi.model.vo.TagBlogCount;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @Description 博客标签mapper
 * @Author Geralt
 * @Date 2024/7/17
 */
@Mapper
@Repository
public interface TagMapper {
    List<Tag> getTagList();

    List<Tag> getTagListNotId();

    List<Tag> getTagListByBlogId(Long blogId);

    int saveTag(Tag tag);

    Tag getTagById(Long id);

    Tag getTagByName(String name);

    int deleteTagById(Long id);

    int updateTag(Tag tag);

    List<TagBlogCount> getTagBlogCount();
}

