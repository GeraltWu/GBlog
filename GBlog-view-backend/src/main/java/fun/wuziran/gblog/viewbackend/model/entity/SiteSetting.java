package fun.wuziran.gblog.viewbackend.model.entity;

import lombok.Data;

/**
 * @Description 网站设置entity
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class SiteSetting {
    // 设置项id
    private long id;
    // 设置项英文名
    private String nameEn;
    // 设置项中文名
    private String nameZh;
    // 设置项类型
    private long type;
    // 设置项值
    private String value;
}
