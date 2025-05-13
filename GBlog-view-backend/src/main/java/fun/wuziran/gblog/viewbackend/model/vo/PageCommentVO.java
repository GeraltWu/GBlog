package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;

import java.util.List;

/**
 * @Description 页面评论VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class PageCommentVO {
    // 评论id
    private long id;
    // 评论者昵称
    private String nickname;
    // 评论内容
    private String content;
    // 评论者头像
    private String avatar;
    // 评论时间
    private String createTime;
    // 评论者网站
    private String website;
    // 是否是博主评论
    private boolean adminComment;
    // 父评论id
    private String parentCommentId;
    // 父评论昵称
    private String parentCommentNickname;
    // 回复该评论的评论列表
    private List<PageCommentVO> replyComments;
}