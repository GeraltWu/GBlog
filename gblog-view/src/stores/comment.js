import { defineStore } from 'pinia';

import {getCommentListByQueryService, submitCommentService} from "@/api/comment";
import { ElMessage, ElNotification } from "element-plus";
// 导入表情符号映射文件
import tiebaMapper from '@/plugins/tiebaMapper.json'
import MygoMapper from '@/plugins/MygoMapper.json'
import gbcMapper from '@/plugins/gbcMapper.json'
import BanGDreamMapper from '@/plugins/BanGDreamMapper.json'
// 导入HTML清理库
import sanitizeHtml from 'sanitize-html'

// 你可以任意命名 `defineStore()` 的返回值，但最好使用 store 的名字，同时以 `use` 开头且以 `Store` 结尾。
// (比如 `useUserStore`，`useCartStore`，`useProductStore`)
// 第一个参数是你的应用中 Store 的唯一 ID。
export const useCommentStore = defineStore('comment', {
    state: () => ({
        // 获取comment的请求参数
        commentQuery: {
            page: 0, //用于后端判断该评论所在页面类型(文章、友链、关于我)
            blogId: null,
            pageNum: 1,
            pageSize: 5
        },
        // 返回的评论列表附带的参数统计
        allComment: 0,
        closeComment: 0,
        commentTotalPage: 0,
        // 评论列表
        comments: [],
        // 评论回复的对象（-1代表顶级评论，0以上就是其回复的评论id），父评论id
        parentCommentId: -1,
        // 回复所在的顶级评论id（-1代表顶级评论，0以上代表该回复所在的顶级评论id），根评论id
        rootCommentId: -1,
        // 提交评论的表单
        commentForm: {
            content: '',
            nickname: '',
            email: '',
            website: '',
            isNotice: true,
        },
    }),
    getters: {
    },
    actions: {
        /**
        * 定义获得评论列表函数
        * @param {*} param0 
        */
        getCommentList() {
            //密码保护的文章，需要发送密码验证通过后保存在localStorage的Token
            const blogToken = window.localStorage.getItem(`blog${this.commentQuery.blogId}`)
            //如果有则发送博主身份Token
            const adminToken = window.localStorage.getItem('adminToken')
            const token = adminToken ? adminToken : (blogToken ? blogToken : '')

            //替换表情代码为表情图片函数
            const replaceEmoji = (comment, emoji) => {
                comment.content = comment.content.replace(new RegExp(emoji.reg, 'g'), `<img src="${emoji.src}" width="64px" height="64px">`)
            }
            const convertEmoji = (comment) => {
                tiebaMapper.forEach(emoji => {
                    replaceEmoji(comment, emoji)
                })
                    // 添加其他表情包的转换
                MygoMapper.forEach(emoji => {
                    replaceEmoji(comment, emoji)
                })
                
                gbcMapper.forEach(emoji => {
                    replaceEmoji(comment, emoji)
                })
                
                BanGDreamMapper.forEach(emoji => {
                    replaceEmoji(comment, emoji)
                })
            }

            //真正开始发送请求获取评论列表
            getCommentListByQueryService(this.commentQuery).then(res => {
                if (res.code === 200) {
                    let sanitizeHtmlConfig = {
                        allowedTags: [],
                        allowedAttributes: false,
                        disallowedTagsMode: 'recursiveEscape'
                    }
                    res.data.comments.list.forEach(comment => {
                        //转义评论中的html
                        comment.content = sanitizeHtml(comment.content, sanitizeHtmlConfig)
                        //查找评论中是否有表情
                        if (comment.content.indexOf('@[') != -1) {
                            convertEmoji(comment)
                        }
                        comment.replyComments.forEach(comment => {
                            //转义评论中的html
                            comment.content = sanitizeHtml(comment.content, sanitizeHtmlConfig)
                            //查找评论中是否有表情
                            if (comment.content.indexOf('@[') != -1) {
                                convertEmoji(comment)
                            }
                        })
                    })
                    this.saveCommentResult(res.data)
                }
            }).catch(() => {
                ElMessage.error("请求失败")
            })
        },
        /**
         * 随机选择一个头像
         * @returns {string} 随机头像的路径
         */
        getRandomAvatar() {
            // 假设我们有6个头像文件，命名为1.jpg到6.jpg
            const avatarCount = 6;
            const randomIndex = Math.floor(Math.random() * avatarCount) + 1;
            return `/img/comment-avatar/${randomIndex}.jpg`;
        },
        
        /**
         * 接收用户填写的评论表单数据，调用 submitCommentService API 发送到后端。
         * 提交成功后，会显示成功通知，重置评论表单，并重新获取评论列表。
         * 如果提交失败，则显示错误通知。
         * @param {*} 
         * @param {*} token （adminToken 或 blogToken）
         */
        submitCommentForm(token) {
            // 直接将用户填在state中的commentForm数据拿来，省的到处传参
            let form = { ...this.commentForm }
            form.page = this.commentQuery.page
            form.blogId = this.commentQuery.blogId
            form.parentCommentId = this.parentCommentId
            form.rootCommentId = this.rootCommentId
            
            // 添加随机头像
            form.avatar = this.getRandomAvatar()
            
            submitCommentService(form).then(res => {
                if (res.code === 200) {
                    ElMessage.success("评论成功")
                    // 提交成功后，抹掉之前设置的回复对象id
                    this.setParentCommentId(-1);
                    this.setRootCommentId(-1);
                    // 重新获取评论列表
                    this.resetCommentForm();
                    this.getCommentList();
                } else {
                    ElMessage.error(res.msg)
                }
            }).catch(() => {
                ElMessage.error("网络异常")
            })
        },

        // 保存评论属性和list函数
        saveCommentResult(data) {
            this.allComment = data.allComment;
            this.closeComment = data.closeComment;
            this.commentTotalPage = data.comments.totalPage;
            this.comments = data.comments.list;
        },
        // 设置评论所在页面类型（博客？关于我？）
        setCommentQueryPage(page) {
            this.commentQuery.page = page;
        },
        // 设置评论对应博客id
        setCommentQueryBlogId(blogId) {
            this.commentQuery.blogId = blogId;
        },
        // 设置请求评论页码
        setCommentQueryPageNum(pageNum) {
            this.commentQuery.pageNum = pageNum;
        },
        // 设置父评论id
        setParentCommentId(parentCommentId) {
            this.parentCommentId = parentCommentId;
        },
        // 设置根评论id
        setRootCommentId(rootCommentId) {
            this.rootCommentId = rootCommentId;
        },
        // 重置评论表单，并保存用户信息
        resetCommentForm() {
            // 存好提交的表单信息
            const commentForm = {
                nickname: this.commentForm.nickname,
                email: this.commentForm.email,
                website: this.commentForm.website
            };
            // 保存访客信息，下次评论时自动填充表单
            window.localStorage.setItem('commentForm', JSON.stringify(commentForm));
            this.commentForm.content = '';
            this.commentForm.isNotice = true;
        },
        // 从本地存储中恢复之前保存的评论表单信息
        restoreCommentForm() {
            const lastForm = JSON.parse(window.localStorage.getItem('commentForm'));
            if (lastForm) {
                this.commentForm.nickname = lastForm.nickname;
                this.commentForm.email = lastForm.email;
                this.commentForm.website = lastForm.website;
            }
        },
    },
})