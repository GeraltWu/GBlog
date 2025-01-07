import { defineStore } from 'pinia';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

export const useBlogStore = defineStore('blog', () => {
    const router = useRouter()

    const isBlogRenderComplete = ref(false)
    const blogPasswordDialogVisible = ref(false)
    const blogPasswordForm = ref({ blogId: 0, password: '' })
    const focusMode = ref(false)
    const isBlogToHome = ref(false)

    function goBlogPage(blog) {
        if (blog.isPrivate) {
            const adminToken = window.localStorage.getItem('adminToken')
            const blogToken = window.localStorage.getItem(`blog${blog.id}`)
            //对于密码保护文章，博主身份Token和经过密码验证后的Token都可以跳转路由，再由后端验证Token有效性
            if (adminToken || blogToken) {
                return router.push(`/blog/${blog.id}`)
            }
            // 如果没有博主身份token也没有经过密码验证的Token，则弹出密码输入框，验证对于此blog的密码
            setBlogPasswordForm({ blogId: blog.id, password: '' })
            setBlogPasswordDialogVisible(true)
        } else {
            router.push(`/blog/${blog.id}`)
        }
    }

    function setIsBlogRenderComplete(ok) {
        isBlogRenderComplete.value = ok
    }
    //设置博客密码填写框是否可见
    function setBlogPasswordDialogVisible(visible) {
        blogPasswordDialogVisible.value = visible
    }
    //设置博客密码表单信息
    function setBlogPasswordForm(form) {
        blogPasswordForm.value = form
    }
    //设置是否从博客详情页返回首页
    function setIsBlogToHome(BlogToHome) {
        isBlogToHome.value = BlogToHome
    }
    //设置是否为专注模式
    function setFocusMode(focus) {
        focusMode.value = focus
    }

    
    return {
        isBlogRenderComplete,
        blogPasswordDialogVisible,
        blogPasswordForm,
        focusMode,
        isBlogToHome,

        setIsBlogRenderComplete,
        setBlogPasswordDialogVisible,
        setBlogPasswordForm,
        setIsBlogToHome,
        setFocusMode,

        goBlogPage
    }
})