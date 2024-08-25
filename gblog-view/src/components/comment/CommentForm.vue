<template>
	<!-- 评论输入表单 -->
	<div class="form">
		<h3>
			发表评论
		</h3>
		<el-form :inline="true" :model="commentStore.commentForm" :rules="formRules" ref="formRef" size="small">
			<el-input :class="'textarea'" type="textarea" :rows="5" v-model="commentStore.commentForm.content"
				placeholder="评论千万条，友善第一条" maxlength="250" show-word-limit :validate-event="false"></el-input>
			<div class="el-form-item el-form-item--small emoji">
				<img src="/img/tieba/1.png" @click="showEmojiBox">
				<!-- 随便点击其他地方隐藏表情选择框 -->
				<div class="mask" v-show="emojiShow" @click="hideEmojiBox"></div>
				<!-- 表情选择框 -->
				<div class="emoji-box" v-show="emojiShow">
					<div class="emoji-title">
						<span>{{ activeEmojiTab === 0 ? '贴吧' : '没别的了' }}</span>
					</div>
					<!-- 表情展示栏 -->
					<div class="emoji-wrap" v-show="activeEmojiTab === 0">
						<!-- 点击表情插入textarea -->
						<div class="emoji-list" v-for="(img, index) in tiebaMapper" :key="index"
							@click="insertEmoji(img.name)">
							<img :src="img.src" :title="img.name">
						</div>
					</div>

					<!-- 表情菜单 -->
					<div class="emoji-tabs">
						<a class="tab-link" :class="{ 'on': activeEmojiTab === 0 }" @click="activeEmojiTab = 2">
							<img src="/img/tieba/1.png">
						</a>

					</div>
				</div>
			</div>
			<el-form-item prop="nickname">
				<!-- bug：focus不跳出popover，拉取昵称和头像没做 -->
				<el-popover placement="bottom" trigger="focus" content="输入QQ号将自动拉取昵称和头像">
					<template #reference>
						<el-input v-model="commentStore.commentForm.nickname" placeholder="昵称（必填）"
							:validate-event="false">
							<template v-slot:prefix>
								<i class="user icon"></i>
							</template>
						</el-input>
					</template>
				</el-popover>
			</el-form-item>

			<el-form-item prop="email">
				<!-- bug：focus不跳出popover -->
				<el-popover ref="emailPopover" placement="bottom" trigger="focus" content="用于接收回复邮件"></el-popover>
				<el-input v-model="commentStore.commentForm.email" placeholder="邮箱（必填）" :validate-event="false"
					v-popover:emailPopover>
					<template v-slot:prefix>
						<i class="envelope icon"></i>
					</template>
				</el-input>
			</el-form-item>

			<!-- <el-form-item>
				<el-popover ref="websitePopover" placement="bottom" trigger="focus" content="可以让我参观一下吗😊"></el-popover>
				<el-input v-model="commentStore.commentForm.website" placeholder="https://（可选）" v-popover:websitePopover>
					<template v-slot:prefix>
						<i class="paperclip icon"></i>
					</template>
				</el-input>
			</el-form-item> -->
			<el-form-item label="订阅回复">
				<el-switch v-model="commentStore.commentForm.notice"></el-switch>
			</el-form-item>
			<el-form-item>
				<button class="ui small primary button" v-throttle="{ value: postForm, event : 'click', time : 3000 }">发表评论</button>
				<!-- 取消回复按钮 仅在回复的时候出现 -->
				<button class="ui small button" @click="commentStore.setParentCommentId(-1)"
					v-show="commentStore.parentCommentId !== -1">取消回复</button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
import { useCommentStore } from '@/stores/comment';
import { checkEmail, checkUrl } from "@/common/reg";
import tiebaMapperJson from '@/plugins/tiebaMapper.json';
import { ref, nextTick, onMounted } from 'vue';
import { ElMessage } from 'element-plus';

export default {
	name: "CommentForm",
	setup() {
		const commentStore = useCommentStore();

		// 评论输入框
		const formRef = ref(null)
		const textarea = ref(null)
		const start = ref(0)
		const end = ref(0)
		const validateWebsite = (rule, value, callback) => {
			if (value) {
				return checkUrl(rule, value, callback);
			}
			callback();
		};
		const formRules = ref({
			nickname: [
				{ required: true, message: '请输入评论昵称' },
				{ max: 18, message: '昵称不可多于15个字符' }
			],
			email: [
				{ required: true, message: '请输入评论邮箱' },
				{ validator: checkEmail }
			],
			website: [
				{ required: false },
				{ validator: validateWebsite }
			]
		})
		
		const postForm = () => {
			const adminToken = window.localStorage.getItem('adminToken')
			// 博主登录后，localStorage中会存储token，在后端设置属性，不校验昵称、邮箱
			if (adminToken) {
				if (commentStore.commentForm.content === '' || commentStore.commentForm.content.length > 250) {
					return ElMessage.warning('评论内容有误');
				} else {
					return commentStore.submitCommentForm(adminToken);
				}
			}
			const blogToken = window.localStorage.getItem(`blog${commentStore.commentQuery.blogId}`)
			formRef.value.validate(valid => {
				if (!valid || commentStore.commentForm.content === '' || commentStore.commentForm.content.length > 250) {
					ElMessage.warning('请正确填写评论');
				} else {
					commentStore.submitCommentForm(blogToken ? blogToken : '');
				}
			});
		}
		onMounted(() => {
			textarea.value = document.querySelector('.el-form textarea');
		})


		// 添加表情
		const emojiShow = ref(false)
		const activeEmojiTab = ref(0)
		const tiebaMapper = ref([])
		const showEmojiBox = () => {
			start.value = textarea.value.selectionStart
			end.value = textarea.value.selectionEnd
			textarea.value.focus()
			textarea.value.setSelectionRange(start.value, end.value)
			emojiShow.value = !emojiShow.value
		}

		const insertEmoji = (name) => {
			let str = commentStore.commentForm.content
			commentStore.commentForm.content = str.substring(0, start.value) + name + str.substring(end.value)
			start.value += name.length
			end.value = start.value
			textarea.value.focus()
			nextTick(() => {
				textarea.value.setSelectionRange(start.value, end.value)
			})
		}
		const hideEmojiBox = () => {
			emojiShow.value = false
			textarea.value.focus()
			textarea.value.setSelectionRange(start.value, end.value)
		}
		onMounted(() => {
			tiebaMapper.value = tiebaMapperJson
		})

		return {
			commentStore,

			formRef,
			textarea,
			start,
			end,
			formRules,
			postForm,

			emojiShow,
			activeEmojiTab,
			tiebaMapper,
			showEmojiBox,
			insertEmoji,
			hideEmojiBox
		}
	}
};
</script>


<style scoped>
.form {
	background: #fff;
	position: relative;
	z-index: 99;
}

.form h3 {
	margin: 5px;
	font-weight: 500 !important;
}

.form .m-small {
	margin-left: 5px;
	padding: 4px 5px;
}

.el-form .textarea {
	margin-top: 5px;
	margin-bottom: 15px;
}

.el-form textarea {
	padding: 6px 8px;
}

.el-form textarea,
.el-form input {
	color: black;
}

.el-form .el-form-item__label {
	padding-right: 3px;
}

.emoji {
	position: relative;
	user-select: none;
}

.emoji>img {
	width: 32px;
	height: 32px;
	cursor: pointer;
	transition: all 0.3s ease-in-out;
	-webkit-transition: all 0.3s ease-in-out;
	-moz-transition: all 0.3s ease-in-out;
	-o-transition: all 0.3s ease-in-out;
}

.emoji>img:hover {
	transform: rotate(360deg);
	-webkit-transform: rotate(360deg);
	-moz-transform: rotate(360deg);
	-o-transform: rotate(360deg);
}

.emoji-box {
	color: #222;
	overflow: visible;
	background: #fff;
	border: 1px solid #E5E9EF;
	box-shadow: 0 11px 12px 0 rgba(106, 115, 133, 0.3);
	border-radius: 8px;
	width: 340px;
	position: absolute;
	top: 40px;
	z-index: 100;
}

.emoji-box * {
	box-sizing: content-box;
}

.emoji-box .emoji-title {
	font-size: 12px;
	line-height: 16px;
	margin: 13px 15px 0;
	color: #757575;
}

.emoji-box .emoji-wrap {
	margin: 6px 11px 0 11px;
	height: 185px;
	overflow: auto;
	word-break: break-word;
}

.emoji-box .emoji-wrap .emoji-list {
	height: 33px;
	color: #111;
	border-radius: 4px;
	transition: background 0.2s;
	display: inline-block;
	outline: 0;
	cursor: pointer;
}

.emoji-box .emoji-wrap .emoji-list:hover {
	background-color: #ddd;
}

.emoji-box .emoji-wrap .emoji-list img {
	margin: 4px;
	width: 25px;
	height: 25px;
}

.emoji-box .emoji-tabs {
	position: relative;
	height: 36px;
	overflow: hidden;
	background-color: #f4f4f4;
	border-radius: 0 0 4px 4px;
}

.emoji-box .emoji-tabs .tab-link {
	cursor: pointer;
	float: left;
	padding: 7px 18px;
	width: 22px;
	height: 22px;
}

.emoji-box .emoji-tabs .tab-link.on {
	background-color: #fff;
}

.emoji-box .emoji-tabs .tab-link img {
	width: 22px;
}

.emoji-box .emoji-tabs .tab-link:hover {
	background: #e7e7e7;
}

.icon {
	height: 2em !important;
}

.mask {
	pointer-events: auto;
	position: fixed;
	z-index: 99;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}
</style>