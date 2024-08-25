import axios from '@/plugins/axios'

export function getBlogByIdService(token, id) {
	return axios({
		url: 'blog',
		method: 'GET',
		headers: {
			Authorization: token,
		},
		params: {
			id
		}
	})
}

export function checkBlogPasswordService(blogPasswordForm) {
	return axios({
		url: 'checkBlogPassword',
		method: 'POST',
		data: {
			...blogPasswordForm
		}
	})
}

export function getSearchBlogListService(query) {
	return axios({
		url: 'getSearchBlogList',
		method: 'GET',
		params: {
			query
		}
	})
}