import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAuthStore = defineStore('auth', () => {
    const token = ref('');
    const isAuthenticated = ref(false);

    // 初始化时从localStorage加载token
    function initToken() {
        const savedToken = window.localStorage.getItem('adminToken');
        if (savedToken) {
            token.value = savedToken;
            isAuthenticated.value = true;
        }
    }

    // 设置token
    function setToken(newToken) {
        token.value = newToken;
        isAuthenticated.value = !!newToken;
        if (newToken) {
            window.localStorage.setItem('adminToken', newToken);
        } else {
            window.localStorage.removeItem('adminToken');
        }
    }

    // 获取token
    function getToken() {
        return token.value;
    }

    // 检查是否已认证
    function checkAuth() {
        return isAuthenticated.value;
    }

    // 登出
    function logout() {
        token.value = '';
        isAuthenticated.value = false;
        window.localStorage.removeItem('adminToken');
    }

    return {
        token,
        isAuthenticated,
        initToken,
        setToken,
        getToken,
        checkAuth,
        logout
    }
});