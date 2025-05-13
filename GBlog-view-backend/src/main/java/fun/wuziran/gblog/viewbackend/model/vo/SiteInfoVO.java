package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;
import java.util.List;

/**
 * @Description 站点信息VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class SiteInfoVO {
    // 博客名称
    private String blogName;
    // 网页标题后缀
    private String webTitleSuffix;
    // 页脚图片标题
    private String footerImgTitle;
    // 页脚图片url
    private String footerImgUrl;
    // ICP备案号
    private String beian;
    // 赞赏码
    private String reward;
    // 博主评论标识
    private String commentAdminFlag;
    // 播放器平台
    private String playlistServer;
    // 播放器歌单id
    private String playlistId;
    // 徽章列表
    private List<BadgeVO> badges;
    // 版权信息
    private CopyrightVO copyright;
} 