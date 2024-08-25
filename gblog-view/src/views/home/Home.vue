<template>
	<div>
		<BlogList :getBlogList="getBlogList" :blogList="blogList" :totalPage="totalPage" />
	</div>

</template>

<script>
import { onMounted, ref, nextTick } from "vue";
import { useBlogStore } from "@/stores/blog";
import BlogList from "@/components/blog/BlogList";
import { getBlogListService } from "@/api/home";
import Prism from "prismjs";
import { ElMessage } from "element-plus";

export default {
	name: "Home",
	components: { BlogList },

	setup() {
		const blogStore = useBlogStore();

		const blogList = ref([])
		const totalPage = ref(0)
		// 请求完毕的标识
		const getBlogListFinish = ref(false)
		
		function getBlogList(pageNum) {
			console.log("获得bloglist")
			getBlogListService(pageNum).then(res => {
				if (res.code === 200) {
					blogList.value = res.data.list
					totalPage.value = res.data.totalPage
					nextTick(() => {
						// eslint-disable-next-line no-undef
						Prism.highlightAll()
					})
					getBlogListFinish.value = true
				} else {
					ElMessage.error(res.msg)
				}
			}).catch((error) => {
				console.log(error)
				ElMessage.error("请求失败")
			})
		}
		onMounted(() => {
			getBlogList(1)
		})
		return {
			blogStore,
			blogList,
			totalPage,
			getBlogListFinish,
			getBlogList
		}
	}
}
</script>

<style scoped></style>