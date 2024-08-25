<template>
	<div class="ui bottom" style="text-align:center">
		<el-pagination @current-change="handleCurrentChange" :current-page="pageNum" :page-count="totalPage"
			layout="prev, pager, next" background hide-on-single-page>
		</el-pagination>
	</div>
</template>

<script>
import { ref, onActivated, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useBlogStore } from '@/stores/blog';
import { useSiteStore } from '@/stores/site';

export default {
	name: "BlogPagination",
	props: {
		getBlogList: {
			type: Function,
			required: true
		},
		totalPage: {
			type: Number,
			required: true
		}
	},
	setup(props) {
		const blogStore = useBlogStore()
		const siteStore = useSiteStore()
		const route = useRoute();

		const pageNum = ref(1);

		// 如果是从博客详情页返回首页，则首页博客列表页码重置为1
		onActivated(() => {
			if (!blogStore.isBlogToHome) {
				pageNum.value = 1;
			}
		});

		// 这个watch函数好像和handleCurrentChange重复了，没必要
		// watch(pageNum, (newPage) => {
		// 	if (route.name === 'home') {
		// 		window.scrollTo({ top: siteStore.clientSize.clientHeight, behavior: 'smooth' });
		// 	} else {
		// 		scrollToTop();
		// 	}
		// 	props.getBlogList(newPage);
		// });

		// 这里定义scrollToTop函数来实现滚动到顶部
		function scrollToTop() {
			window.scrollTo({ top: 0, behavior: 'smooth' });
		}

		// 定义监听页码改变的事件
		function handleCurrentChange(newPage) {
			//如果是首页，则滚动至Header下方
			if (route.name === 'home') {
				window.scrollTo({ top: siteStore.clientSize.clientHeight, behavior: 'smooth' })
			} else {
				//其它页面（分类和标签页）滚动至顶部
				scrollToTop()
			}
			pageNum.value = newPage
			props.getBlogList(newPage)
		}

		return {
			pageNum,
			scrollToTop,
			handleCurrentChange
		};
	}
}
</script>

<style>
/* 分页样式在base中 */
</style>