import axios from '@/plugins/axios'

export function getBlogListByTagNameService(tagName, pageNum) {
	return axios({
		url: 'tag',
		method: 'GET',
		params: {
			tagName,
			pageNum
		}
	})
}