package fun.wuziran.gblogapi.enums;

import lombok.Getter;

/**
 * @Description 访问行为枚举
 * @Author Geralt
 * @Date 2024/7/17
 */

@Getter
public enum VisitBehavior {
    UNKNOWN("UNKNOWN", "UNKNOWN"),

    INDEX("访问页面", "首页"),
    ARCHIVE("访问页面", "归档"),
    MOMENT("访问页面", "动态"),
    FRIEND("访问页面", "友链"),
    ABOUT("访问页面", "关于我"),

    BLOG("查看博客", ""),
    CATEGORY("查看分类", ""),
    TAG("查看标签", ""),
    SEARCH("搜索博客", ""),
    CLICK_FRIEND("点击友链", ""),
    LIKE_MOMENT("点赞动态", ""),
    CHECK_PASSWORD("校验博客密码", ""),
    ;

    /**
     * 访问行为
     */
    private final String behavior;

    /**
     * 访问内容
     */
    private final String content;

    /**
     * 构造方法
     * @param behavior 访问行为
     * @param content 访问内容
     */
    VisitBehavior(String behavior, String content) {
        this.behavior = behavior;
        this.content = content;
    }

}
