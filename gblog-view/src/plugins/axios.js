import axios from "axios";
import { ElMessage } from 'element-plus'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

const instance = axios.create({
	baseURL: '/api',
	timeout: 10000,
})

// 用拦截器进行请求拦截，身份标识的获取和保存
instance.interceptors.request.use(
	config => {
		// 显示进度条
		NProgress.start()
		// 从localStorage中获取身份标识
		const identification = window.localStorage.getItem('identification')
		//identification存在，且是基于baseURL的请求
		if (identification && !(config.url.startsWith('http://') || config.url.startsWith('https://'))) {
			config.headers.identification = identification
		}
		return config
	},
	err => {
		NProgress.start()
		//请求错误的回调
		Promise.reject(err)
	}
)

// 用拦截器进行响应拦截，身份标识的获取和保存
instance.interceptors.response.use(
	response => {
		NProgress.done();
		const identification = response.headers.identification;
		if (identification) {
			// 保存身份标识到 localStorage
			window.localStorage.setItem('identification', identification);
		}

		return response.data; // 返回服务器提供的响应数据

	},
	err => {
		NProgress.done();
		return Promise.reject(err);
	}
);


export default instance