package fun.wuziran.gblog.viewbackend.model.entity;

import lombok.Data;

/**
 * @Description 标签entity
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class Tag {
    // 标签id
    private long id;
    // 标签名
    private String name;
    // 标签颜色
    private String color;
}
