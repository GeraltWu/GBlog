// axios 中配置了拦截器
import axios from '@/plugins/axios'

export const getAbout =() =>{
	// 导入了拦截器，就不需要写then和catch了
	// return axios({
	// 	url: 'about',
	// 	method: 'GET'
	// })
	return axios.get('about')
}