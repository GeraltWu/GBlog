package fun.wuziran.gblogapi.service.impl;

import fun.wuziran.gblogapi.constant.RedisKeyConstants;
import fun.wuziran.gblogapi.entity.Tag;
import fun.wuziran.gblogapi.exception.NotFoundException;
import fun.wuziran.gblogapi.exception.PersistenceException;
import fun.wuziran.gblogapi.mapper.TagMapper;
import fun.wuziran.gblogapi.service.RedisService;
import fun.wuziran.gblogapi.service.TagService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */
@Service
public class TagServiceImpl implements TagService {
    @Autowired
    TagMapper tagMapper;
//    @Autowired
//    RedisService redisService;

    @Override
    public List<Tag> getTagList() {
        return tagMapper.getTagList();
    }

    @Override
    public List<Tag> getTagListNotId() {

        return tagMapper.getTagListNotId();
    }

    @Override
    public List<Tag> getTagListByBlogId(Long blogId) {
        return tagMapper.getTagListByBlogId(blogId);
    }

    @Transactional(rollbackFor = Exception.class)
    @Override
    public void saveTag(Tag tag) {
        if (tagMapper.saveTag(tag) != 1) {
            throw new PersistenceException("标签添加失败");
        }
    }

    @Override
    public Tag getTagById(Long id) {
        Tag tag = tagMapper.getTagById(id);
        if (tag == null) {
            throw new NotFoundException("标签不存在");
        }
        return tag;
    }

    @Override
    public Tag getTagByName(String name) {
        return tagMapper.getTagByName(name);
    }

    @Transactional(rollbackFor = Exception.class)
    @Override
    public void deleteTagById(Long id) {
        if (tagMapper.deleteTagById(id) != 1) {
            throw new PersistenceException("标签删除失败");
        }
    }

    @Transactional(rollbackFor = Exception.class)
    @Override
    public void updateTag(Tag tag) {
        if (tagMapper.updateTag(tag) != 1) {
            throw new PersistenceException("标签更新失败");
        }
    }
}

