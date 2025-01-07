<template>
	<div>
		<div class="blog-item" v-for="item in blogList" :key="item.id" ref="blogItems">
			<div class="ui padded attached segment m-padded-tb-large m-margin-bottom-big m-box m-grey1-bg">
				<div class="ui large red right corner label" v-if="item.top">
					<i class="arrow alternate circle up icon"></i>
				</div>
				<div class="ui middle aligned mobile reversed stackable">

					<div class="ui grid m-margin-lr">
						<!--标题-->
						<div class="row m-padded-tb-small">
							<h2 class="ui header m-center m-scaleup">
								<a href="javascript:;" @click.prevent="toBlog(item)" class="m-black">{{ item.title }}</a>
							</h2>
						</div>
						<!--文章简要信息-->
						<div class="row m-padded-tb-small">
							<div class="ui horizontal link list m-center">
								<div class="item m-datetime">
									<i class="small calendar icon"></i><span>{{ dateFormat(item.createTime, 'YYYY-MM-DD')
										}}</span>
								</div>
								<div class="item m-views">
									<i class="small eye icon"></i><span>{{ item.views }}</span>
								</div>
								<div class="item m-common-black">
									<i class="small pencil alternate icon"></i><span>字数≈{{ item.words }}字</span>
								</div>
								<div class="item m-common-black">
									<i class="small clock icon"></i><span>阅读时长≈{{ item.readTime }}分</span>
								</div>
							</div>
						</div>
						<!--分类-->
						<router-link :to="`/category/${item.category.name}`" class="ui red large ribbon label ">
							<i class="small folder open icon m-white"></i><span class="m-text-500 m-white">{{ item.category.name }}</span>
						</router-link>
						<!--文章Markdown描述-->
						<div class="typo m-padded-tb-small line-numbers match-braces rainbow-braces"
							v-html="item.description"></div>
						<!--阅读全文按钮-->
						<div class="row m-padded-tb-small m-margin-top" style="justify-content: center;">
							<button class="ui button large blue-button" @click.prevent="toBlog(item)">阅读全文</button>
							<!-- <a href="javascript:;"  class="color-btn">阅读全文</a> -->
						</div>
						<!--横线-->
						<div class="ui section divider m-margin-lr-no"></div>
						<!--标签-->
						<div class="row m-padded-tb-no">
							<div class="column m-padding-left-no">
								<router-link :to="`/tag/${tag.name}`" class="ui tag label m-text-500 m-margin-small"
									:class="tag.color" v-for="(tag, index) in item.tags" :key="index">{{ tag.name
									}}</router-link>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { ref, onMounted, watch, nextTick } from 'vue'
import { gsap } from 'gsap'
import { dateFormat } from "@/util/dateTimeFormatUtils";
import { useBlogStore } from "@/stores/blog";

export default {
	name: "BlogItem",
	props: {
		blogList: {
			type: Array,
			required: true
		}
	},
	setup(props) {
		const blogItems = ref([])
		const blogStore = useBlogStore();

		const animateBlogs = () => {
			if (!blogItems.value.length) return

			// 确保元素按照 DOM 顺序排列
			const elements = Array.from(blogItems.value).sort((a, b) => {
				return a.offsetTop - b.offsetTop
			})

			// 重置元素初始状态
			gsap.set(elements, {
				opacity: 0,
				y: 50
			})

			// 创建动画
			gsap.to(elements, {
				opacity: 1,
				y: 0,
				duration: 0.8,
				stagger: 0.2,
				ease: "power2.out"
			})
		}

		// 监听 blogList 变化
		watch(() => props.blogList, () => {
			nextTick(() => {
				animateBlogs()
			})
		}, { deep: true })

		// 组件挂载时执行动画
		onMounted(() => {
			animateBlogs()
		})

		function toBlog(blog) {
			blogStore.goBlogPage(blog)
		}

		return {
			blogItems,
			toBlog,
			dateFormat
		}
	}
}
</script>

<style scoped>
.blog-item {
	min-height: 100px; /* 防止加载时页面抖动 */
}

/* .ui.large.ribbon.label {

} */

.ribbon.label {
	max-height: 30px;
	margin-bottom: 10px !important;
	left: -45px !important;
	padding-left: 1rem !important;
	padding-right: 1rem !important;
}

.blue-button {
	background-color: var(--blue-color); /* 选择你想要的蓝色 */
	color: white; /* 确保文字颜色与背景色对比明显 */
	border: none; /* 移除边框 */
}

.blue-button:hover {
	background-color: var(--red-color); /* 鼠标悬停时的颜色 */
	color: white; /* 确保文字颜色与背景色对比明显 */
}
</style>