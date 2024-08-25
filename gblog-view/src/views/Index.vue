<template>
	<div class="site">
		<!--顶部导航-->
		<Nav :categoryList="categoryList" />
		<!--首页大图 只在首页且pc端时显示-->
		<Header v-if="$route.name === 'home'" class="m-mobile-hide" />

		<div class="main">
			<div class="m-padded-tb-big">
				<div class="ui container">
					<div class="ui stackable grid">
						<!--左侧-->
						<div class="three wide column m-mobile-hide ">
							<Introduction :class="{ 'm-display-none': blogStore.focusMode }" />
						</div>
						<!--中间-->
						<!-- 真正动态路由的地方 -->
						<div class="ten wide column">
							<!-- 渲染匹配当前路由的组件 -->
							<router-view v-slot="{ Component }">
								<!-- 缓存动态组件，以便在它们之间切换时保留其状态，仅限Home组件 -->
								<keep-alive include="Home">
									<component :is="Component" />
								</keep-alive>
							</router-view>
						</div>
						<!--右侧-->
						<div class="three wide column m-mobile-hide">
							<RandomBlog :randomBlogList="randomBlogList"
								:class="{ 'm-display-none': blogStore.focusMode }" />
							<Tags :tagList="tagList" :class="{ 'm-display-none': blogStore.focusMode }" />
							<!--只在文章页面显示目录-->
							<Tocbot v-if="$route.name === 'blog'" />
						</div>
					</div>
				</div>
			</div>
		</div>

		<!--私密文章密码对话框-->
		<BlogPasswordDialog />

		<!--APlayer-->
		<!-- <div class="m-mobile-hide">
			<MyAPlayer />
		</div> -->

		<!--回到顶部-->
		<el-backtop style="box-shadow: none;background: none;z-index: 9999;">
			<img src="/img/paper-plane.png" style="width: 40px;height: 40px;">
		</el-backtop>
		<!--底部footer-->
		<Footer :badges="badges" :newBlogList="newBlogList" :hitokoto="hitokoto" />
	</div>
</template>

<script>
import { useSiteStore } from '@/stores/site'
import { useBlogStore } from '@/stores/blog'
import { useCommentStore } from '@/stores/comment'
import { useRoute } from 'vue-router'
import { ref, onMounted, onBeforeMount } from 'vue';

import { getHitokotoService, getSiteService } from '@/api/index'
import Nav from "@/components/index/Nav";
import Header from "@/components/index/Header";
import Footer from "@/components/index/Footer";
import Introduction from "@/components/sidebar/Introduction";
import Tags from "@/components/sidebar/Tags";
import RandomBlog from "@/components/sidebar/RandomBlog";
import MyAPlayer from "@/components/index/MyAPlayer";
import Tocbot from "@/components/sidebar/Tocbot";
import BlogPasswordDialog from "@/components/index/BlogPasswordDialog";


export default {
	name: "blogIndex",
	components: { Header, BlogPasswordDialog, Tocbot, MyAPlayer, RandomBlog, Tags, Nav, Footer, Introduction },
	setup() {
		const siteStore = useSiteStore();
		const blogStore = useBlogStore();
		const commentStore = useCommentStore();
		const route = useRoute();

		// 定义响应式状态
		const introduction = ref({});
		const categoryList = ref([]);
		const tagList = ref([]);
		const randomBlogList = ref([]);
		const badges = ref([]);
		const newBlogList = ref([]);
		const hitokoto = ref({});

		// // 在dom渲染完之前就要保存好页面大小，便于header调整height以占满页面
		// onBeforeMount(() => {})

		onMounted(() => {
			getHitokoto()
			//从localStorage恢复之前的评论信息
			commentStore.restoreCommentForm()
			getSite()
			console.log('获取Site', siteStore.siteInfo)

			//保存可视窗口大小
			siteStore.saveClientSize({ clientHeight: document.body.clientHeight, clientWidth: document.body.clientWidth })
			window.onresize = () => {
				siteStore.saveClientSize({ clientHeight: document.body.clientHeight, clientWidth: document.body.clientWidth })
			}
		})

		function getSite() {
			getSiteService().then(res => {
				if (res.code === 200) {
					introduction.value = res.data.introduction;
					badges.value = res.data.badges;
					newBlogList.value = res.data.newBlogList;
					categoryList.value = res.data.categoryList;
					tagList.value = res.data.tagList;
					randomBlogList.value = res.data.randomBlogList;
					siteStore.saveSiteInfo(res.data.siteInfo);
					siteStore.saveIntroduction(res.data.introduction);
					document.title = route.meta.title + res.data.siteInfo.webTitleSuffix

				}
			})
		}

		//获取一言
		function getHitokoto() {
			getHitokotoService().then(res => {
				hitokoto.value = res
			})
		}
		return {
			blogStore,

			categoryList,
			tagList,
			randomBlogList,
			badges,
			newBlogList,
			hitokoto,

		}
	},

}
</script>

<style scoped>
.site {
	display: flex;
	min-height: 100vh;
	/* 没有元素时，也把页面撑开至100% */
	flex-direction: column;
}

.main {
	margin-top: 40px;
	flex: 1;
}

.main .ui.container {
	width: 1400px !important;
	margin-left: auto !important;
	margin-right: auto !important;
}

.ui.grid .three.column {
	padding: 0;
}

.ui.grid .ten.column {
	padding-top: 0;
}

.m-display-none {
	display: none !important;
}
</style>