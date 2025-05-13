package fun.wuziran.gblog.viewbackend.model.entity;

import lombok.Data;

/**
 * @Description 动态entity
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class Moment {
    // 动态id
    private long id;
    // 动态内容
    private String content;
    // 发布时间
    private String createTime;
    // 点赞数
    private int likes;
    // 是否公开
    private boolean published;
}
