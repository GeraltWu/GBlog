import axios from '@/plugins/axios'

export function getCommentListByQueryService(token, query) {
	return axios({
		url: 'comments',
		method: 'GET',
		headers: {
			Authorization: token,
		},
		params: {
			...query
		}
	})
}

export function submitCommentService(token, form) {
	return axios({
		url: 'comment',
		method: 'POST',
		headers: {
			Authorization: token,
		},
		data: {
			...form
		}
	})
}