import axios from '@/plugins/axios'

export function getBlogListByCategoryNameService(categoryName, pageNum) {
	return axios({
		url: 'category',
		method: 'GET',
		params: {
			categoryName,
			pageNum
		}
	})
}