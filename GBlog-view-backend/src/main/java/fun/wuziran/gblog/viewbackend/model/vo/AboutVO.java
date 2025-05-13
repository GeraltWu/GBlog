package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;

/**
 * @Description 关于页面VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class AboutVO {
    // 背景音乐id
    private String musicId;
    // 是否开启评论
    private boolean commentEnabled;
    // 页面标题
    private String title;
    // 页面内容
    private String content;
} 