package fun.wuziran.gblog.viewbackend.model.entity;

import lombok.Data;

/**
 * @Description 评论entity
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class Comment {
    // 评论id
    private long id;
    // 评论者昵称
    private String nickname;
    // 评论者邮箱
    private String email;
    // 评论者QQ号
    private long qq;
    // 评论者头像
    private String avatar;
    // 评论时间
    private String createTime;
    // 评论者网站
    private String website;
    // 评论者IP
    private String ip;
    // 评论内容
    private String content;
    // 是否公开
    private boolean isPublished;
    // 是否是博主评论
    private boolean adminComment;
    // 评论页面
    private int page;
    // 是否接收邮件提醒
    private boolean isNotice;
    // 父评论id
    private long parentCommentId;
    // 根评论id
    private String rootCommentId;
    // 所属博客id
    private long blogId;
}