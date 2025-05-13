import axios from '@/plugins/axios'

export function getMomentListByPageNumService(pageNum) {
	return axios({
		url: 'moments',
		method: 'GET',
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