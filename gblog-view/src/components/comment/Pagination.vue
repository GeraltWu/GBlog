<template>
	<!--评论分页-->
	<el-pagination @current-change="handleCurrentChange" :current-page="commentStore.commentQuery.pageNum"
		:page-count="commentStore.commentTotalPage" layout="prev, pager, next" background hide-on-single-page class="pagination">
	</el-pagination>
</template>

<script setup>
import { useCommentStore } from '@/stores/comment';

const commentStore = useCommentStore();

//监听页码改变的事件
const handleCurrentChange = (newPage) => {
	commentStore.setCommentQueryPageNum(newPage);
	commentStore.setParentCommentId(-1); // 假设你有一个这样的 action
	commentStore.getCommentList(); // 假设这是获取评论列表的 action
}
</script>

<style scoped>
.pagination {
	margin-top: 2em;
	text-align: center;
}
</style>