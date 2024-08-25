<template>
	<div class="login_container">
		<div class="login_box">
			<!--头像-->
			<div class="avatar_box">
				<img src="/img/avatar.jpg" alt="">
			</div>
			<!--登录表单-->
			<el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" class="login_form">
				<el-form-item prop="username">
					<el-input v-model="loginForm.username" prefix-icon="el-icon-user-solid"></el-input>
				</el-form-item>
				<el-form-item prop="password">
					<el-input v-model="loginForm.password" prefix-icon="el-icon-lock" show-password
						@keyup.enter="login"></el-input>
				</el-form-item>
				<el-form-item class="btns">
					<el-button type="primary" @click="login">登录</el-button>
					<el-button type="info" @click="resetLoginForm">重置</el-button>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>

<script>
import { loginService } from "@/api/login";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";

export default {
	name: "blogLogin",
	setup() {
		const router = useRouter();

		const loginFormRef = ref(null); // ref 用于获取表单实例
		const loginForm = ref({
			username: 'Geralt',
			password: '1223'
		});
		const loginFormRules = ref({
			username: [
				{ required: true, message: '请输入用户名', trigger: 'blur' },
			],
			password: [
				{ required: true, message: '请输入密码', trigger: 'blur' },
			]
		})
		function resetLoginForm() {
			loginFormRef.value.resetFields();
		}
		function login() {
			loginFormRef.value.validate(valid => {
				if (valid) {
					loginService(loginForm.value).then(res => {
						if (res.code === 200) {
							ElMessage.success(res.msg)
							window.localStorage.setItem('adminToken', res.data.token)
							router.push('/home')
						} else {
							ElMessage.error(res.msg)
						}
					}).catch(() => {
						ElMessage.error("请求失败")
					})
				}
			})
		}

		return {
			loginFormRef,
			loginForm,
			loginFormRules,
			resetLoginForm,
			login
		}
	}
}
</script>

<style scoped>
.login_container {
	box-sizing: unset !important;
	height: 100%;
	background-color: #2b4b6b;
}

.login_box {
	width: 450px;
	height: 300px;
	background-color: #fff;
	border-radius: 3px;
	position: absolute;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);
}

.login_box .avatar_box {
	height: 130px;
	width: 130px;
	border: 1px solid #eee;
	border-radius: 50%;
	padding: 10px;
	box-shadow: 0 0 10px #ddd;
	position: absolute;
	left: 50%;
	transform: translate(-50%, -50%);
	background-color: #fff;
}

.login_box .avatar_box img {
	width: 100%;
	height: 100%;
	border-radius: 50%;
	background-color: #eee;
}

.login_form {
	position: absolute;
	bottom: 0;
	width: 100%;
	padding: 0 20px;
	box-sizing: border-box;
}

.btns {
	display: flex;
	justify-content: flex-end;
}
</style>