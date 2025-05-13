package fun.wuziran.gblog.viewbackend.model.entity;

import lombok.Data;

/**
 * @Description 分类entity
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class Category {
    // 分类id
    private long id;
    // 分类名称
    private String name;
}
