import axios from '@/plugins/axios'

export function getCommentListByQueryService(query) {
    return axios({
        url: 'comments',
        method: 'GET',
        params: {
            ...query
        }
    })
}

export function submitCommentService(form) {
    return axios({
        url: 'comment',
        method: 'POST',
        data: {
            ...form
        }
    })
}