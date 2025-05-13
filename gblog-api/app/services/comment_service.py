from sqlalchemy.orm import Session
from app.crud import comment as comment_crud
from app.schemas.comment import PageComment, CommentResponse, CommentForm, CommentQuery
from app.models.comment import Comment
from typing import List, Tuple, Dict, Any, Optional
import math
from app.utils.bit_utils import bit_to_bool
from datetime import datetime  # 添加这一行导入datetime模块

def get_comment_list_by_query(
    db: Session, 
    query: CommentQuery
) -> CommentResponse:
    """
    根据查询条件获取评论列表
    
    Args:
        db: 数据库会话
        query: 评论查询参数
        
    Returns:
        CommentResponse: 评论数据，包含总数、是否关闭评论和评论列表
    """
    # 计算偏移量
    skip = (query.page_num - 1) * query.page_size
    
    # 获取评论总数
    all_comment = comment_crud.get_comments_count(db, page=query.page, blog_id=query.blog_id)
    
    # 获取未发布（被隐藏）的评论数量
    close_comment = comment_crud.get_unpublished_comments_count(db, page=query.page, blog_id=query.blog_id)
    
    # 获取根评论列表
    root_comments = comment_crud.get_comments_by_page_and_blog_id(
        db, 
        page=query.page, 
        blog_id=query.blog_id,
        skip=skip, 
        limit=query.page_size
    )
    
    # 计算总页数
    total_page = math.ceil(all_comment / query.page_size) if all_comment > 0 else 1
    
    # 构建评论树
    comment_list = []
    for root_comment in root_comments:
        # 获取根评论的所有回复
        replies = comment_crud.get_reply_comments(db, root_comment.id)
        
        # 按创建时间排序回复
        replies.sort(key=lambda x: x.create_time)
        
        # 创建一个评论ID到评论对象的映射，包括根评论
        all_comments_dict = {root_comment.id: root_comment}
        for reply in replies:
            all_comments_dict[reply.id] = reply
        
        # 直接构建回复列表，平行处理所有回复
        reply_list = []
        
        for reply in replies:
            # 获取父评论昵称
            parent_nickname = ""
            if reply.parent_comment_id != -1 and reply.parent_comment_id in all_comments_dict:
                parent_nickname = all_comments_dict[reply.parent_comment_id].nickname
            
            reply_vo = PageComment(
                id=reply.id,
                nickname=reply.nickname,
                content=reply.content,
                avatar=reply.avatar,
                create_time=reply.create_time.strftime("%Y-%m-%d %H:%M"),
                website=reply.website,
                admin_comment=reply.is_admin_comment,
                parent_comment_id=reply.parent_comment_id,
                parent_comment_nickname=parent_nickname,
                root_comment_id=reply.root_comment_id,  # 添加根评论ID
                reply_comments=[]  # 不再需要嵌套回复
            )
            reply_list.append(reply_vo)
        
        # 创建根评论对象
        root_comment_vo = PageComment(
            id=root_comment.id,
            nickname=root_comment.nickname,
            content=root_comment.content,
            avatar=root_comment.avatar,
            create_time=root_comment.create_time.strftime("%Y-%m-%d %H:%M"),
            website=root_comment.website,
            admin_comment=bit_to_bool(root_comment.is_admin_comment),
            parent_comment_id=root_comment.parent_comment_id,
            parent_comment_nickname="",  # 根评论没有父评论
            root_comment_id=root_comment.id,  # 根评论的root_comment_id就是自己的id
            reply_comments=reply_list
        )
        
        comment_list.append(root_comment_vo)
    
    # 构造返回结果
    comments_dict = {
        "totalPage": total_page,
        "list": comment_list
    }
    
    # 使用Pydantic模型包装结果
    result = CommentResponse(
        all_comment=all_comment,
        close_comment=close_comment,
        comments=comments_dict
    )
    
    return result


def add_comment(db: Session, comment_form: CommentForm) -> bool:
    """
    添加评论
    
    Args:
        db: 数据库会话
        comment_form: 评论表单数据
        
    Returns:
        bool: 是否添加成功
    """
    try:
        # 创建评论对象
        comment = Comment(
            nickname=comment_form.nickname,
            email=comment_form.email,
            website=comment_form.website,
            content=comment_form.content,
            page=comment_form.page,
            is_notice=comment_form.isNotice,
            parent_comment_id=comment_form.parentCommentId,
            blog_id=comment_form.blogId if comment_form.page == 0 else None,
            is_published=True,  # 默认发布
            is_admin_comment=False,  # 默认非管理员评论
            create_time=datetime.now(),
            ip="",  # 可以从请求中获取
            avatar=comment_form.avatar,  # 使用前端传入的头像
            root_comment_id=comment_form.rootCommentId  # 直接使用前端传入的rootCommentId
        )
        
        # 保存到数据库
        db.add(comment)
        db.commit()
        
        return True
    except Exception as e:
        db.rollback()
        print(f"添加评论失败: {str(e)}")
        return False  # 确保在异常情况下返回False