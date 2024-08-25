import { defineStore } from 'pinia';
import { ref, reactive } from 'vue';

export const useSiteStore = defineStore('site', () => {
    const siteInfo = ref('');
    const introduction = ref({
        avatar: '',
        name: '',
        rollText: [],
        favorites: [],
    });
    const clientSize = ref({
        clientHeight: 0,
        clientWidth: 1080,
    });

    // 将获取的站点信息保存到 state 中
    function saveSiteInfo(siteInfoParam) {
        siteInfo.value = siteInfoParam
    }
    // 将获取的introduction 保存到 state 中
    function saveIntroduction(intro) {
        introduction.value = intro
    }
    //保存客户端的视口大小
    function saveClientSize(clientSizeParam) {
        clientSize.value = clientSizeParam
    }

    return {
        siteInfo,
        introduction,
        clientSize,

        saveSiteInfo,
        saveIntroduction,
        saveClientSize
    }
    
})