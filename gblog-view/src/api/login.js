import axios from '@/plugins/axios'

export function loginService(loginForm) {
	return axios({
		url: 'login',
		method: 'POST',
		data: {
			...loginForm
		}
	})
}
