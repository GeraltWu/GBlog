<template>
	<div>
		<div class="ui top segment" style="text-align: center">
			<h2 class="m-text-500">标签 {{ tagName }} 下的文章</h2>
		</div>
		<BlogList :getBlogList="getBlogList" :blogList="blogList" :totalPage="totalPage" />
	</div>
</template>

<script>
import { onMounted, ref, watch, nextTick, computed } from "vue";
import { useRoute } from "vue-router";
import BlogList from "@/components/blog/BlogList";
import { getBlogListByTagNameService } from "@/api/tag";
import { ElMessage } from "element-plus";
import Prism from "prismjs";

export default {
	name: "blogTag",
	components: { BlogList },
	setup() {
		const route = useRoute()

		/**
		 * 获得某标签下的文章列表
		 * */
		const blogList = ref([])
		const totalPage = ref(0)
		// 计算属性，利用路由名实时获得当前标签名
		const tagName = computed(() => {
			return route.params.name
		})
		const getBlogList = (pageNum) => {
			getBlogListByTagNameService(tagName.value, pageNum).then(res => {
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
		onMounted(() => {
			getBlogList()
		})
		//在当前组件被重用时，要重新获取博客列表
		watch(() => route.fullPath, () => {
			if (route.name === 'tag') {
				getBlogList()
			}
		})

		return {
			blogList,
			totalPage,
			tagName,
			getBlogList
		}
	}
}
</script>

<style scoped></style>