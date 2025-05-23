/**
评论只有两层，子评论的回复和子评论放在同一级，由parentCommentId和parentCommentNickname来标识回复的是谁，按时间排序就好了

*/
<template>
	<!--评论列表-->
		<CommentForm v-if="commentStore.parentCommentId === -1" />
		<div class="ui threaded comments">
			<h3 class="ui dividing header">Comments | 共 {{ commentStore.allComment }} 条评论
				<span v-if="commentStore.closeComment !== 0">（{{ commentStore.closeComment }} 条评论被隐藏）</span>
			</h3>
			<h3 class="ui header" v-if="commentStore.allComment === 0">快来抢沙发！</h3>
			<!-- 评论列表 -->
			<div class="comment" v-for="comment in commentStore.comments" :key="comment.id" ref="commentItems">
				<!-- 方便点击@XXX跳转到所回复的评论 -->
				<span class="anchor" :id="`comment-${comment.id}`"></span>
				<a class="ui circular image avatar">
					<img :src="comment.avatar">
				</a>
				<div class="content">
					<!-- 提供了跳转到用户website的方式，但我不用 -->
					<a class="nickname" :href="comment.website != '' && comment.website != null ? comment.website : null"
						target="_blank" rel="external nofollow noopener">{{ comment.nickname }}</a>
					<div class="ui black left pointing label" v-if="comment.adminComment">{{
						commentStore.commentAdminFlag
					}}</div>
					<div class="metadata">
						<strong class="date">{{ dateFormat(comment.createTime, 'YYYY-MM-DD HH:mm') }}</strong>
					</div>
					<div class="text" v-html="comment.content"></div>
					<div class="actions">
						<a class="reply" @click="setReply(comment.id, comment.id)">回复</a>
					</div>
				</div>
				<!-- 如果要回复的是文章评论，那么在这里提供一个评论表单 -->
				<CommentForm v-if="commentStore.parentCommentId === comment.id" />
				<!-- 回复列表 -->
				<div class="comments" v-if="comment.replyComments.length > 0">
					<div class="comment" v-for="reply in comment.replyComments" :key="reply.id" ref="replyItems">
						<span class="anchor" :id="`comment-${reply.id}`"></span>
						<a class="ui circular image avatar">
							<img :src="reply.avatar">
						</a>
						<div class="content">
							<!-- 提供了跳转到用户website的方式，但我不用 -->
							<a class="nickname" :href="reply.website != '' && reply.website != null ? reply.website : null"
								target="_blank" rel="external nofollow noopener">{{ reply.nickname }}</a>
							<div class="ui black left pointing label" v-if="reply.adminComment">{{
								commentStore.commentAdminFlag }}
							</div>
							<div class="metadata">
								<strong class="date">{{ dateFormat(reply.createTime, 'YYYY-MM-DD HH:mm') }}</strong>
							</div>
							<div class="text">
								<a :href="`#comment-${reply.parentCommentId}`">@{{ reply.parentCommentNickname }}</a>
								<div v-html="reply.content"></div>
							</div>
							<div class="actions">
								<a class="reply" @click="setReply(reply.id, reply.rootCommentId)">回复</a>
							</div>
						</div>
				<!-- 如果要回复的是评论的回复，那么在这里提供一个评论表单 -->
				<CommentForm v-if="commentStore.parentCommentId === reply.id" />
					</div>

				</div>
				<div class="border"></div>
			</div>
		</div>
</template>

<script>
import { useCommentStore } from '@/stores/comment';
import CommentForm from "./CommentForm";
import { dateFormat } from "@/util/dateTimeFormatUtils";
import { ref, onMounted, watch, nextTick } from 'vue'
import { gsap } from 'gsap'

export default {
	name: "BlogComment",
	components: { CommentForm },
	setup() {
		const commentStore = useCommentStore();
		const commentItems = ref([])
		const replyItems = ref([])

		// 评论动画
		const animateComments = () => {
			if (!commentItems.value.length) return

			// 重置评论初始状态
			gsap.set(commentItems.value, {
				opacity: 0,
				y: 50
			})

			// 创建评论动画
			gsap.to(commentItems.value, {
				opacity: 1,
				y: 0,
				duration: 0.8,
				stagger: 0.2,
				ease: "power2.out"
			})

			// 重置回复初始状态
			if (replyItems.value.length) {
				gsap.set(replyItems.value, {
					opacity: 0,
					y: 30
				})

				// 创建回复动画，延迟执行
				gsap.to(replyItems.value, {
					opacity: 1,
					y: 0,
					duration: 0.6,
					stagger: 0.1,
					ease: "power2.out",
					delay: 0.5 // 等主评论动画完成后再开始
				})
			}
		}

		// 监听评论列表变化
		watch(() => commentStore.comments, () => {
			nextTick(() => {
				animateComments()
			})
		}, { deep: true })

		// 组件挂载时执行动画
		onMounted(() => {
			animateComments()
		})

		function setReply(parentCommentId, rootCommentId) {
			commentStore.setParentCommentId(parentCommentId);
			commentStore.setRootCommentId(rootCommentId);
		}

		return {
			commentStore,
			dateFormat,
			setReply,
			commentItems,
			replyItems
		};
	}
}
</script>

<style scoped>
.comments+.border {
	position: absolute;
	left: 34px;
	top: 47px;
	bottom: 0;
	border-style: solid;
	border-width: 0 0 0 1px;
	border-color: #e0e0e0;
}

.ui.threaded.comments .comment .comments {
	box-shadow: none;
	margin-top: -2em;
	width: 100% !important;
	max-width: 100% !important;
}
/* 覆盖 Semantic UI 的宽度限制 */
:deep(.ui.comments),
.ui.threaded.comments {
  max-width: 100% !important;
  width: 100% !important;
}
.comment {
	padding-right: 1em !important;
	padding-left: 1em !important;
}

.nickname {
	font-weight: bolder;
	color: #000;
}


.comment>.anchor {
	position: absolute;
	left: 0;
	top: -48px;
}

.comments .comment:first-child {
	margin-top: 0 !important;
}

.comment .comments .comment {
	box-shadow: 0 0 5px rgb(0, 0, 0, 0.1);
	border-radius: 5px;
	margin-top: 12px;
	padding-top: 10px !important;
	padding-bottom: 10px !important;
}

.comment .comments .comment>.anchor {
	top: -55px;
}

.ui.comments .comment .avatar {
	width: 40px !important;
	margin: 0;
}

.ui.comments .comment .text {
	white-space: pre-wrap !important;
	line-height: 1.5;
}

.ui.comments .comment .text a {
	cursor: pointer;
	margin-right: 8px;
	font-weight: bolder;
	color: rgba(0, 0, 0, .87);
}

.ui.comments .comment .text div {
	display: inline;
}
.label {
	cursor: default;
	padding: 4px 6px !important;
	font-weight: 500 !important;
}

.comment .form {
	margin-top: 20px;
}

</style>


