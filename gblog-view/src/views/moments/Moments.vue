<template>
	<div>
		<div class="ui top attached segment" style="text-align: center">
			<h2 class="m-text-500">我的动态</h2>
		</div>
		<div class="ui attached segment m-padding-bottom-large">
			<div class="moments">
				<div class="moment" v-for="(moment, index) in momentList" :key="index" ref="momentItems">
					<div class="avatar">
						<img :src="siteStore.introduction.avatar">
					</div>
					<div class="ui card m-grey1-bg">
						<div class="content m-top">
							<span style="font-weight: 700">{{ siteStore.introduction.name }}</span>
							<span class="right floated">{{ dateFromNow(moment) }}</span>
						</div>
						<div class="content typo" :class="{ 'privacy': !moment.isPublished }" v-viewer
							v-html="moment.content"></div>
						<div class="extra content">
							<a class="left floated" @click="like(moment.id)">
								<i class="heart icon" :class="isLike(moment.id) ? 'like-color' : 'outline'"></i>{{
									moment.likes }}
							</a>
						</div>
					</div>
				</div>
			</div>

			<!-- 这个分页组件的样式被Pagination组件的那个覆盖了，因为那个组建的style非scoped -->
			<el-pagination @current-change="handleCurrentChange" :current-page="pageNum" :page-count="totalPage"
				layout="prev, pager, next" background hide-on-single-page class="pagination">
			</el-pagination>
		</div>
	</div>
</template>

<script>
import { getMomentListByPageNumService, likeMomentService } from "@/api/moment";
import { dateFromNow } from "@/util/dateTimeFormatUtils";
import { ref, computed, onMounted, watch, nextTick } from "vue";
import { ElMessage } from "element-plus";
import { useSiteStore } from "@/stores/site";
import { gsap } from 'gsap';

export default {
	name: "blogMoments",
	setup() {
		const siteStore = useSiteStore()
		const momentItems = ref([])

		// 动画函数
		const animateMoments = () => {
			if (!momentItems.value.length) return

			// 确保元素按照 DOM 顺序排列
			const elements = Array.from(momentItems.value).sort((a, b) => {
				return a.offsetTop - b.offsetTop
			})

			// 重置初始状态
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

		// 获取动态列表
		const momentList = ref([])
		const totalPage = ref(0)
		function getMomentList() {
			getMomentListByPageNumService(pageNum.value).then(res => {
				if (res.code === 200) {
					momentList.value = res.data.list
					totalPage.value = res.data.totalPage
					// 数据更新后执行动画
					nextTick(() => {
						animateMoments()
					})
				} else {
					ElMessage.error(res.msg)
				}
			}).catch(() => {
				ElMessage.error("请求失败")
			})
		}
		onMounted(() => {
			getMomentList()
		})


		// 页面跳转
		const pageNum = ref(1)
		function scrollToTop() {
			window.scrollTo({ top: 0, behavior: 'smooth' });
		}
		function handleCurrentChange(newPage) {
			scrollToTop()
			pageNum.value = newPage
			getMomentList()
		}


		// 点赞
		const likeMomentIds = ref([])
		// 用localStorage本地存储已点赞的动态id数组
		likeMomentIds.value = JSON.parse(window.localStorage.getItem('likeMomentIds') || '[]')
		// 计算属性 isLike  判断该 id 是否存在于 likeMomentIds 数组中。
		const isLike = computed(() => {
			return (id) => likeMomentIds.value.includes(id);
		});
		function like(id) {
			if (likeMomentIds.value.includes(id)) {
				ElMessage.warning('不可以重复点赞哦');
				return;
			}
			likeMomentService(id).then(res => {
				if (res.code === 200) {
					likeMomentIds.value.push(id)
					momentList.value.forEach(item => {
						if (item.id === id) {
							return item.likes++
						}
					})
					ElMessage.success(res.msg);
				} else {
					ElMessage.warning(res.msg);
				}
			}).catch(() => {
				ElMessage.error('异常错误');
			})
		}


		return {
			siteStore,
			momentItems,
			likeMomentIds,
			momentList,
			pageNum,
			totalPage,
			isLike,
			dateFromNow,
			getMomentList,
			handleCurrentChange,
			like,
		}
	}
	// watch: {
	// 	likeMomentIds(newValue) {
	// 		//将likeMomentIds最新值的json数据保存到localStorage
	// 		window.localStorage.setItem('likeMomentIds', JSON.stringify(newValue))
	// 	}
	// },
}
</script>

<style scoped>
.avatar {
	margin-left: -62.5px;
	float: left !important;
}

.avatar img {
	height: 45px;
	width: 45px;
	border-radius: 500px;
}

.moments {
	margin-left: 26px !important;
	padding-left: 40px !important;
	border-left: 1px solid #dee5e7 !important;
}

.moment {
	margin-top: 30px;
}

.moment:first-child {
	margin-top: 0 !important;
}

.card {
	width: 100% !important;
}

.card:before {
	border-width: 0 0 1px 1px !important;
	transform: translateX(-50%) translateY(-50%) rotate(45deg) !important;
	bottom: auto !important;
	right: auto !important;
	top: 22px !important;
	left: 0 !important;
	position: absolute !important;
	content: '' !important;
	background-image: none !important;
	z-index: 2 !important;
	width: 12px !important;
	height: 12px !important;
	transition: background .1s ease !important;
	background-color: inherit !important;
	border-style: solid !important;
	border-color: #d4d4d5 !important;
}

.content.m-top {
	padding: 10px 14px !important;
}

.content .right.floated {
	font-size: 12px !important;
}

.content.typo * {
	font-size: 14px !important;
}

.extra.content {
	padding: 5px 14px !important;
}

.extra.content a {
	color: rgba(0, 0, 0, 0.7) !important;
	font-size: 12px !important;
}

.extra.content a:hover {
	color: red !important;
}

.extra.content .like-color {
	color: red !important;
}

.extra.content i {
	font-size: 12px !important;
}

.pagination {
	justify-content: center;
	/* 将flex子元素居中对齐 */
	margin-top: 3em;
}

.privacy {
	background: repeating-linear-gradient(145deg, #f2f2f2, #f2f2f2 15px, #fff 0, #fff 30px) !important;
}
</style>