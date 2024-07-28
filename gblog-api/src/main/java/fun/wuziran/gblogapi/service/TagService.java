package fun.wuziran.gblogapi.service;

import fun.wuziran.gblogapi.entity.Tag;

import java.util.List;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */
public interface TagService {
    List<Tag> getTagList();

    List<Tag> getTagListNotId();

    List<Tag> getTagListByBlogId(Long blogId);

    void saveTag(Tag tag);

    Tag getTagById(Long id);

    Tag getTagByName(String name);

    void deleteTagById(Long id);

    void updateTag(Tag tag);
}