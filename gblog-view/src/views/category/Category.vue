<template>
	<div>
		<div class="ui top segment" style="text-align: center">
			<h2 class="m-text-500">分类 <span>{{ categoryName }}</span> 下的文章</h2>
		</div>
		<BlogList :getBlogList="getBlogList" :blogList="blogList" :totalPage="totalPage" />
	</div>
</template>

<script>
import { computed, ref, watch, nextTick, onMounted } from "vue";
import { useRoute } from "vue-router";
import BlogList from "@/components/blog/BlogList";
import { getBlogListByCategoryNameService } from "@/api/category";
import Prism from "prismjs";
import { ElMessage } from "element-plus";

export default {
	name: "blogCategory",
	components: { BlogList },
	setup() {
		const route = useRoute()

		const blogList = ref([])
		const totalPage = ref(0)
		watch(() => route.name, () => {
			if (route.name === 'category') {
				getBlogList()
			}
		})

		onMounted(() => {
			getBlogList()
		})

		// 从路由中也可以获取分类名称
		const categoryName = computed(() => {
			return route.params.name
		})

		function getBlogList(pageNum) {
			getBlogListByCategoryNameService(categoryName, pageNum).then(res => {
				if (res.code === 200) {
					blogList.value = res.data.list
					totalPage.value = res.data.totalPage
					nextTick(() => {
						// eslint-disable-next-line no-undef
						Prism.highlightAll()
					})
				} else {
					ElMessage.error(res.msg)
				}
			}).catch(() => {
				ElMessage.error("请求失败")
			})
		}
		return {
			blogList,
			totalPage,
			categoryName,
			getBlogList
		}
	}
}
</script>

<style scoped></style>