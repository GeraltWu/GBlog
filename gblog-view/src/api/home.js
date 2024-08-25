import axios from '@/plugins/axios'

export function getBlogListService(pageNum) {
	console.log('请求的pageNum: ', pageNum)
	return axios({
		url: '/blogs',
		method: 'GET',
		params: {
			pageNum
		}
	})
}