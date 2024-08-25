import axios from '@/plugins/axios'

export function getArchivesService() {
	return axios({
		url: 'archives',
		method: 'GET'
	})
}