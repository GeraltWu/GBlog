import axios from '@/plugins/axios'

export function getMomentListByPageNumService(token, pageNum) {
	return axios({
		url: 'moments',
		method: 'GET',
		headers: {
			Authorization: token,
		},
		params: {
			pageNum
		}
	})
}

export function likeMomentService(id) {
	return axios({
		url: `moment/like/${id}`,
		method: 'POST',
	})
}