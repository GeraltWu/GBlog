import { useSiteStore } from '@/stores/site'
import { ref } from 'vue'

export default function getPageTitle(pageTitle) {
	const siteStore = useSiteStore()
	const title = ref('')
	if (siteStore.siteInfo.webTitleSuffix){
		title.value = siteStore.siteInfo.webTitleSuffix
	}else{
		title.value = ''
	}

	if (pageTitle) {
		if (title.value) {
			return `${pageTitle}${title.value}`
		}
		return pageTitle
	}
	return title.value
}
