<template>
	<div>
		<Comment />
		<Pagination />
	</div>
</template>

<script>
import { useCommentStore } from '@/stores/comment';
import { useRoute } from 'vue-router';
import Comment from "./Comment";
import Pagination from "./Pagination";
import { onMounted, watch} from 'vue';

export default {
	name: "CommentList",
	components: { Comment, Pagination },
	props: {
		page: {
			type: Number,
			required: true
		},
		blogId: {
			type: Number,
			required: false
		}
	},
	setup(props) {
		const commentStore = useCommentStore();

		const init = () => {
			//重置评论查询参数（因为到达其它页面）
			commentStore.setParentCommentId(-1);
			commentStore.setCommentQueryPageNum(1);
			commentStore.setCommentQueryPage(props.page);
			commentStore.setCommentQueryBlogId(props.blogId);
			// 重新获取评论列表
			commentStore.getCommentList();
		}

		// 使用 useRoute 钩子获取当前路由对象
		const route = useRoute();
		// 使用 watch 来观察路由对象的 path 属性
		watch(() => route.path, (newPath) => {
			// 当路由变化时，重新获取评论
			init()
		}); //不设置立即回调

		// 页面挂载时，初始化评论列表
		onMounted(() => {
			init();
		});



	}
}

</script>

<style scoped></style>