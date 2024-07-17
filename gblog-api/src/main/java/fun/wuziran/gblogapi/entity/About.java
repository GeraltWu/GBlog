package fun.wuziran.gblogapi.entity;

import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/16
 */
@Data
public class About {
    private Long id;
    private String nameEn;
    private String nameZh;
    private String value;
}