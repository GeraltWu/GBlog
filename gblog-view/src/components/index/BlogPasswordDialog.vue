<template>
	<!--私密文章密码对话框-->
	<el-dialog title="请输入受保护文章密码" width="30%" v-model="blogStore.blogPasswordDialogVisible" :lock-scroll="false"
		:before-close="blogPasswordDialogClosed">
		<!--内容主体-->
		<el-form ref="formRef" :model="blogStore.blogPasswordForm" :rules="formRules" label-width="80px">
			<el-form-item label="密码" prop="password">
				<el-input v-model="blogStore.blogPasswordForm.password"></el-input>
			</el-form-item>
		</el-form>
		<!--底部-->
		<template v-slot:footer>
			<span>
				<el-button @click="blogPasswordDialogClosed">取 消</el-button>
				<el-button type="primary" @click="submitBlogPassword">确 定</el-button>
			</span>
		</template>

	</el-dialog>
</template>

<script>
import { useBlogStore } from "@/stores/blog";
import { useRouter } from "vue-router";
import { ref } from 'vue';
import { checkBlogPasswordService } from "@/api/blog";

export default {
	name: "BlogPasswordDialog",
	setup() {
		const blogStore = useBlogStore()
		const router = useRouter()
		//表单
		const formRef = ref(null)

		const formRules = ref({
			password: [{ required: true, message: '请输入密码', trigger: 'change' }]
		})
		function blogPasswordDialogClosed() {
			// 注意一定要用.value
			formRef.value.resetFields()
			blogStore.setBlogPasswordDialogVisible(false)
		}
		function submitBlogPassword() {
			formRef.value.validate(valid => {
				if (valid) {
					checkBlogPasswordService(blogStore.blogPasswordForm).then(res => {
						if (res.code === 200) {
							msgSuccess(res.msg)
							window.localStorage.setItem(`blog${blogStore.blogPasswordForm.blogId}`, res.data)
							router.push(`/blog/${blogStore.blogPasswordForm.blogId}`)
							blogPasswordDialogClosed()
						} else {
							msgError(res.msg)
						}
					}).catch(() => {
						msgError("请求失败")
					})
				}
			})
		}
		// 返回给模板的响应式状态和方法
		return {
			blogStore,
			formRef,
			formRules, //表单规则也要返回
			blogPasswordDialogClosed,
			submitBlogPassword
		};
	},
}
</script>

<style scoped></style>