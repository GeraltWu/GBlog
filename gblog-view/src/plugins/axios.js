import axios from "axios";
import { ElMessage } from 'element-plus'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

const instance = axios.create({
	baseURL: import.meta.env.VITE_API_BASE_URL + '/front',  // 直接在这里设置完整的基础URL
	timeout: 10000,
})

// 用拦截器进行请求拦截，身份标识的获取和保存
instance.interceptors.request.use(
	config => {
		// 显示进度条
		NProgress.start()
		// 从localStorage中获取身份标识
		const token = window.localStorage.getItem('adminToken')
		//identification存在，且是基于baseURL的请求
		if (token && !(config.url.startsWith('http://') || config.url.startsWith('https://'))) {
			config.headers.Authorization = `Bearer ${token}`
		}
		return config
	},
	err => {
		NProgress.done()  // 修正为done
		return Promise.reject(err)  // 添加return关键字
	}
)

// 用拦截器进行响应拦截，身份标识的获取和保存
instance.interceptors.response.use(
	response => {
		NProgress.done();
		const authHeader = response.headers.Authorization;
		if (authHeader && authHeader.startsWith('Bearer ')) {
			// 提取Bearer后面的token部分
			const token = authHeader.substring(7);
			// 保存身份标识到 localStorage
			window.localStorage.setItem('adminToken', token);
		}

		return response.data; // 返回服务器提供的响应数据
	},
	err => {
		NProgress.done();
		return Promise.reject(err);
	}
);


export default instance