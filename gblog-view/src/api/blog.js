import axios from '@/plugins/axios'

export function getBlogByIdService(id) {
	return axios({
		url: 'blog',
		method: 'GET',
		params: {
			id
		}
	})
}

export function checkBlogPasswordService(blogPasswordForm) {
	return axios({
		url: 'check-blog-password',
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