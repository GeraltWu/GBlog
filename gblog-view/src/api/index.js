import axios from '@/plugins/axios'

export function getHitokotoService() {
	return axios({
		url: 'https://v1.hitokoto.cn/?c=a',
		method: 'GET'
	})
}

export function getSiteService() {
	return axios({
		url: 'site',
		method: 'GET'
	})
}