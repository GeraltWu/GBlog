package fun.wuziran.gblog.viewbackend.model.entity;

import lombok.Data;

/**
 * @Description 关于我页面entity
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class About {
    // 记录id
    private long id;
    // 英文名称
    private String nameEn;
    // 中文名称
    private String nameZh;
    // 设置值
    private String value;
}
