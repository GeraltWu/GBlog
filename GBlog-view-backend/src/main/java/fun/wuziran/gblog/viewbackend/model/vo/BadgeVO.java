package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;

/**
 * @Description 徽章VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class BadgeVO {
    // 徽章完整标题
    private String title;
    // 徽章图片url
    private String url;
    // 徽章主题
    private String subject;
    // 徽章值
    private String value;
    // 徽章颜色
    private String color;
} 