package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;
import java.util.List;

/**
 * @Description 个人介绍VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class IntroductionVO {
    // 头像地址
    private String avatar;
    // 昵称
    private String name;
    // github地址
    private String github;
    // telegram账号
    private String telegram;
    // QQ号
    private String qq;
    // B站账号
    private String bilibili;
    // 网易云音乐账号
    private String netease;
    // 邮箱地址
    private String email;
    // 滚动文字
    private List<String> rollText;
    // 收藏夹
    private List<FavoriteVO> favorites;
} 