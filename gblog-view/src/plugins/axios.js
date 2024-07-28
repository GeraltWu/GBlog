import axios from "axios";
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

//const baseURL = process.env.VUE_APP_API_URL;
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
	}
)

// 用拦截器进行响应拦截，身份标识的获取和保存
instance.interceptors.response.use(
	config => {
		NProgress.done()
		const identification = config.headers.identification
		if (identification) {
			//保存身份标识到localStorage
			window.localStorage.setItem('identification', identification)
		}
		return config.data
	}
)

export default instance