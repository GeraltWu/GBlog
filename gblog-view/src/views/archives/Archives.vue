<template>
	<div>
		<div class="ui top attached segment" style="text-align: center">
			<h2 class="m-text-500">文章归档</h2>
			<p>好! 目前共计 {{ totalQuantity }} 篇日志。 继续努力。</p>
		</div>
		<div class="ui attached segment m-grey1-bg">
			<div class="timeline">
				<div v-for="(monthGroup, index) in blogList" :key="index" :class="colorObj[index % 4]" ref="archiveItems">
					<div class="tl-header">
						<a class="ui large label m-text-500">{{ formatMonth(monthGroup.month) }}</a>
					</div>
					<div class="tl-item" v-for="blog in monthGroup.list" :key="blog.id">
						<div class="tl-wrap">
							<span class="tl-date">{{ blog.day }}</span>
							<a href="javascript:;" @click.prevent="toBlog(blog)"  >
								<div class="ui left pointing label tl-title" @mouseenter="onHover" @mouseleave="onLeave">{{ blog.title }}</div>
							</a>
						</div>
					</div>
				</div>
				<div class="tl-header">
					<a class="ui black large label m-text-500">初火</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { getArchivesService } from "@/api/archives";
import { ref, onMounted, nextTick } from "vue";
import { useBlogStore } from "@/stores/blog";
import { ElMessage } from "element-plus";
import { gsap } from "gsap";

export default {
	name: "blogArchives",
	setup() {
		const blogStore = useBlogStore();

		// 获取文章归档数据
		const blogList = ref([]);
		const totalQuantity = ref(0);
		const archiveItems = ref([]);

		function getArchives() {
			// 调用axios请求数据
			getArchivesService().then(res => {
				if (res.code === 200) {
					blogList.value = res.data.list;
					totalQuantity.value = res.data.totalQuantity;
					nextTick(() => animateItems());
				} else {
					ElMessage.error(res.msg);
				}
			}).catch(() => {
				ElMessage.error("请求失败");
			});
		}

		// 动画效果
		function animateItems() {
			gsap.from(archiveItems.value, {
				y: 20,
				opacity: 0,
				duration: 0.5,
				stagger: 0.1,
				ease: "power2.out"
			});
		}

		// 鼠标悬浮放大
		function onHover(event) {
			gsap.to(event.currentTarget, {
				scale: 1.15,
				duration: 0.3,
				ease: "power2.out"
			});
		}

		// 鼠标离开效果
		function onLeave(event) {
			gsap.to(event.currentTarget, {
				scale: 1,
				duration: 0.3,
				ease: "power2.out"
			});
		}

		onMounted(() => {
			getArchives();
		});

		//定义所有item的颜色集合
		const colorObj = {
			0: 'tl-blue',
			1: 'tl-dark',
			2: 'tl-green',
			3: 'tl-red',
			4: 'tl-purple',
		};

		// 格式化月份显示
		function formatMonth(month) {
			const [year, monthNumber] = month.split('-');
			return `${year}年${parseInt(monthNumber)}月`;
		}

		// 点击跳转文章详情
		function toBlog(blog) {
			blogStore.goBlogPage(blog);
		}

		return {
			blogList,
			totalQuantity,
			colorObj,
			getArchives,
			toBlog,
			formatMonth,
			archiveItems,
			onHover,
			onLeave
		};
	},
};
</script>

<style scoped>
.timeline {
	margin: 20px 0;
}

.tl-header {
	width: 12em;
	text-align: center;
}

.tl-date {
	position: relative;
	top: 10px;
	display: block;
	float: left;
	width: 4.5em;
	margin-left: -7.5em;
	text-align: right;
}

.tl-wrap {
	padding: 15px 0 15px 20px;
	margin-left: 6em;
	border-style: solid;
	border-width: 0 0 0 4px;
}

.tl-wrap:before {
	position: relative;
	top: 15px;
	float: left;
	width: 10px;
	height: 10px;
	margin-left: -27px;
	background: #fff;
	border-color: inherit;
	border-style: solid;
	border-width: 3px;
	border-radius: 50%;
	content: "";
	box-shadow: 0 0 0 4px #fff;
}

.tl-wrap:hover:before {
	background: 0 0;
	border-color: #fff;
}

.tl-title {
	margin-left: 0 !important;
	letter-spacing: 0.3px !important;
	font-size: 14px !important;
	font-weight: 500 !important;
	padding: 12px 15px !important;
}

.tl-blue .tl-header a,
.tl-blue .tl-item .tl-title {
	background: var(--blue-color) !important;
	color: #fff !important;
}

.tl-blue .tl-item .tl-wrap {
	border-color: var(--blue-color);
}

.tl-dark .tl-header a,
.tl-dark .tl-item .tl-title {
	background: var(--grey4-color) !important;
	color: #fff !important;
}

.tl-dark .tl-item .tl-wrap {
	border-color: var(--grey4-color);
}

.tl-green .tl-header a,
.tl-green .tl-item .tl-title {
	background: var(--green-color) !important;
	color: #fff !important;
}

.tl-green .tl-item .tl-wrap {
	border-color: var(--green-color);
}

.tl-red .tl-header a,
.tl-red .tl-item .tl-title {
	background: var(--red-color) !important;
	color: #fff !important;
}

.tl-red .tl-item .tl-wrap {
	border-color: var(--red-color);
}

.tl-purple .tl-header a,
.tl-purple .tl-item .tl-title {
	background: var(--purple-color) !important;
	color: #fff !important;
}

.tl-purple .tl-item .tl-wrap {
	border-color: var(--purple-color);
}
</style>