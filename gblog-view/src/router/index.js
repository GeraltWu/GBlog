import { createRouter, createWebHistory } from 'vue-router'
import getPageTitle from '@/util/get-page-title'
import { useBlogStore } from '@/stores/blog'

const routes = [
	{
		path: '/login', // 定义登录页面的路径
		component: () => import('@/views/Login'), // 动态导入登录页面的组件
		meta: { title: '登录' } // 设置页面标题为“登录”
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
				meta: { title: '首页' },
				beforeEnter: (to, from, next) => {
					// 在这里不能直接访问组件实例的属性或方法
					const blogStore = useBlogStore();

					if (from.name !== 'blog') {
						// 从其他页面跳转到首页时，重新请求数据
						blogStore.setIsBlogToHome(false);
						// getBlogList(1);
					} else {
						// 如果文章页面是起始访问页，首页将是第一次进入，即缓存不存在，要请求数据
						// if (!blogStore.getBlogListFinish) {
						// 	getBlogList(1);
						// }
						// 从文章页面跳转到首页时，使用首页缓存
						blogStore.setIsBlogToHome(true);
					}

					next(); // 确保调用 next() 来继续路由导航
				},
			},
			{
				path: '/archives',
				name: 'archives',
				component: () => import('@/views/archives/Archives'),
				meta: { title: '归档' }
			},
			{
				path: '/blog/:id',
				name: 'blog',
				component: () => import('@/views/blog/Blog'),
				meta: { title: '博客' },
				//不会在 params、query 或 hash 改变时触发
				beforeEnter: (to, from) => {
					//这样不行就用inject注入
					const blogStore = useBlogStore();
					blogStore.setIsBlogRenderComplete(false);
					return true;
				},
			},
			{
				path: '/tag/:name',
				name: 'tag',
				component: () => import('@/views/tag/Tag'),
				meta: { title: '标签' }
			},
			{
				path: '/category/:name',
				name: 'category',
				component: () => import('@/views/category/Category'),
				meta: { title: '分类' }
			},
			{
				path: '/moments',
				name: 'moments',
				component: () => import('@/views/moments/Moments'),
				meta: { title: '动态' }
			},
			{
				path: '/friends',
				name: 'friends',
				component: () => import('@/views/friends/Friends'),
				meta: { title: '友人帐' }
			},
			{
				path: '/tools',
				name: 'tools',
				component: () => import('@/views/tools/Tools'),
				meta: { title: '工具箱' },
				children: [

				]
			},
			{
				path: '/heishou',
				name: 'heishou',
				component: () => import('@/views/tools/heishou/Heishou'),
				meta: { title: '黑手' }
			},
			{
				path: '/about',
				name: 'about',
				component: () => import('@/views/about/About'),
				meta: { title: '关于我' }
			}
		]
	}
]

const router = createRouter({
	// hash模式
	// history: createWebHashHistory(),
	history: createWebHistory(),
	// base: process.env.BASE_URL, //获取env的方式从process.env变成了import.meta.env
	base: import.meta.env.VITE_API_BASE_URL,
	routes: routes,
})

//挂载路由守卫
router.beforeEach((to, from, next) => {
	document.title = getPageTitle(to.meta.title)
	next()
})

export default router
