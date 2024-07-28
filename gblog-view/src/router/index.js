import { createRouter, createWebHistory } from 'vue-router'
import getPageTitle from '@/util/get-page-title'


const routes = [
	{
		path: '/login', // 定义登录页面的路径
		component: () => import('@/views/Login'), // 动态导入登录页面的组件
		meta: {title: '登录'} // 设置页面标题为“登录”
	},
	{
		path: '/',
		component: () => import('@/views/Index'),
		redirect: '/home',
		children: [
			{
				path: '/home',
				name: 'home',
				// 通过匿名函数的方式导入 Home 组件
				component: () => import('@/views/home/Home'),
				meta: {title: '首页'}
			},
			{
				path: '/archives',
				name: 'archives',
				component: () => import('@/views/archives/Archives'),
				meta: {title: '归档'}
			},
			{
				path: '/blog/:id',
				name: 'blog',
				component: () => import('@/views/blog/Blog'),
				meta: {title: '博客'}
			},
			{
				path: '/tag/:name',
				name: 'tag',
				component: () => import('@/views/tag/Tag'),
				meta: {title: '标签'}
			},
			{
				path: '/category/:name',
				name: 'category',
				component: () => import('@/views/category/Category'),
				meta: {title: '分类'}
			},
			{
				path: '/moments',
				name: 'moments',
				component: () => import('@/views/moments/Moments'),
				meta: {title: '动态'}
			},
			{
				path: '/friends',
				name: 'friends',
				component: () => import('@/views/friends/Friends'),
				meta: {title: '友人帐'}
			},
			{
				path: '/about',
				name: 'about',
				component: () => import('@/views/about/About'),
				meta: {title: '关于我'}
			}
		]
	}
]

const router = createRouter({
    // hash模式
    // history: createWebHashHistory(),
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes: routes,
})

//挂载路由守卫
router.beforeEach((to, from, next) => {
	document.title = getPageTitle(to.meta.title)
	next()
})

export default router
