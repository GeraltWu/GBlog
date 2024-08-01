<template>
	<div ref="nav" class="ui fixed inverted stackable pointing menu"
		:class="{ 'transparent': $route.name === 'home' && clientSize.clientWidth > 768 }">
		<div class="ui container">
			<router-link to="/">
				<h3 class="ui header item m-blue">{{ blogName }}</h3>
			</router-link>

			<router-link to="/home" class="item"
				:class="{ 'm-mobile-hide': mobileHide, 'active': $route.name === 'home' }">
				<i class="home icon"></i>首页
			</router-link>

			<!-- 下拉菜单 分类 -->
			<el-dropdown ref="dropdown" trigger="click" @command="categoryRoute" :popper-class="popperClass">
				<span class="el-dropdown-link item"
					:class="{ 'm-mobile-hide': mobileHide, 'active': $route.name === 'category' }">
					<i class="idea icon"></i>分类<i class="caret down icon"></i>
				</span>
				<template v-slot:dropdown proper-class="">
					<el-dropdown-menu>
						<el-dropdown-item :command="category.name" v-for="(category, index) in categoryList"
							:key="index">{{ category.name }}</el-dropdown-item>
					</el-dropdown-menu>
				</template>
			</el-dropdown>

			<router-link to="/archives" class="item"
				:class="{ 'm-mobile-hide': mobileHide, 'active': $route.name === 'archives' }">
				<i class="clone icon"></i>归档
			</router-link>

			<router-link to="/moments" class="item"
				:class="{ 'm-mobile-hide': mobileHide, 'active': $route.name === 'moments' }">
				<i class="comment alternate outline icon"></i>动态
			</router-link>

			<router-link to="/friends" class="item"
				:class="{ 'm-mobile-hide': mobileHide, 'active': $route.name === 'friends' }">
				<i class="users icon"></i>友人帐
			</router-link>

			<router-link to="/about" class="item"
				:class="{ 'm-mobile-hide': mobileHide, 'active': $route.name === 'about' }">
				<i class="info icon"></i>关于我
			</router-link>

			<el-autocomplete v-model="queryString" :fetch-suggestions="debounceQuery" placeholder="Search..."
				class="right item m-search" :class="{ 'm-mobile-hide': mobileHide }" popper-class="m-search-item"
				@select="handleSelect">
				<template v-slot:suffix>
					<i class="search icon el-input__icon"></i>
				</template>
				<template v-slot:item>
					<div class="title">{{ item.title }}</div>
					<span class="content">{{ item.content }}</span>
				</template>
			</el-autocomplete>

			<button class="ui menu black icon button m-right-top m-mobile-show" @click="toggle">
				<i class="sidebar icon"></i>
			</button>
		</div>
	</div>
</template>

<script>
import { getSearchBlogList } from "@/api/blog";
import { mapState } from 'vuex'

export default {
	name: "blogNav",
	props: {
		blogName: {
			type: String,
			required: true
		},
		categoryList: {
			type: Array,
			required: true
		},
	},
	data() {
		return {
			mobileHide: true,
			queryString: '',
			queryResult: [],
			timer: null,
			popperClass: ''
		}
	},
	computed: {
		...mapState(['clientSize']),
	},
	watch: {
		//路由改变时，收起导航栏
		'$route.path'() {
			this.mobileHide = true
		},
		'$route.name'() {
			this.updatePopperClass()
		}
	},
	mounted() {
		// 挂载时根据路由名称更新popperClass
		this.updatePopperClass()
		//监听页面滚动位置，改变导航栏的显示
		window.addEventListener('scroll', () => {
			//首页且不是移动端
			if (this.$route.name === 'home' && this.clientSize.clientWidth > 768) {
				// 页面滚动距离大于导航栏高度的一半，导航栏背景才会变黑，否则透明
				if (window.scrollY > this.clientSize.clientHeight / 2) {
					this.$refs.nav.classList.remove('transparent')
					this.popperClass = 'default-popper'
				} else {
					this.$refs.nav.classList.add('transparent')
					this.popperClass = 'transparent-popper'
				}
			}
		})
		//监听点击事件，收起导航菜单
		document.addEventListener('click', (e) => {
			//遍历冒泡
			let flag = e.path.some(item => {
				if (item === this.$refs.nav) return true
			})
			//如果导航栏是打开状态，且点击的元素不是Nav的子元素，则收起菜单
			if (!this.mobileHide && !flag) {
				this.mobileHide = true
			}
		})
	},
	methods: {
		updatePopperClass() {
			if (this.$route.name === 'home' && this.clientSize.clientWidth > 768) {
				this.popperClass = 'transparent-popper';
			} else {
				this.popperClass = 'default-popper';
			}
		},
		toggle() {
			this.mobileHide = !this.mobileHide
		},
		categoryRoute(name) {
			this.$router.push(`/category/${name}`)
		},
		debounceQuery(queryString, callback) {
			this.timer && clearTimeout(this.timer)
			this.timer = setTimeout(() => this.querySearchAsync(queryString, callback), 1000)
		},
		querySearchAsync(queryString, callback) {
			if (queryString == null
				|| queryString.trim() === ''
				|| queryString.indexOf('%') !== -1
				|| queryString.indexOf('_') !== -1
				|| queryString.indexOf('[') !== -1
				|| queryString.indexOf('#') !== -1
				|| queryString.indexOf('*') !== -1
				|| queryString.trim().length > 20) {
				return
			}
			getSearchBlogList(queryString).then(res => {
				if (res.code === 200) {
					this.queryResult = res.data
					if (this.queryResult.length === 0) {
						this.queryResult.push({ title: '无相关搜索结果' })
					}
					callback(this.queryResult)
				}
			}).catch(() => {
				this.msgError("请求失败")
			})
		},
		handleSelect(item) {
			if (item.id) {
				this.$router.push(`/blog/${item.id}`)
			}
		}
	}
}
</script>

<!-- 这里如果加上scoped，那么el-input深层元素的样式（包括传递给深层的参数）全部无法生效 -->
<style>
.ui.fixed.menu .container {
	width: 1400px !important;
	margin-left: auto !important;
	margin-right: auto !important;
}

.ui.fixed.menu {
	transition: .3s ease-out;
}

.ui.inverted.pointing.menu.transparent {
	background: transparent !important;
}

.ui.inverted.pointing.menu.transparent .active.item:after {
	background: transparent !important;
	transition: .3s ease-out;
}

.ui.inverted.pointing.menu.transparent .active.item:hover:after {
	background: transparent !important;
}

.el-dropdown-link {
	outline-style: none !important;
	outline-color: unset !important;
	height: 100%;
	cursor: pointer;
}

.el-dropdown-menu {
	margin: 7px 0 0 0 !important;
	padding: 0 !important;
	border: 0 !important;
	/* background: #1b1c1d !important; */
	background: rgba(255, 255, 255, 0) !important;

}

.el-dropdown-menu__item {
	/* padding: 0 15px !important; */
	color: rgba(255, 255, 255, .9) !important;
	background: rgba(255, 255, 255, 0) !important;
}

.el-dropdown-menu__item:hover {
	background: rgba(255, 255, 255, 0.08) !important;
}

.el-popper .popper__arrow::after {
	content: none !important;
}

.transparent-popper {
	background-color: transparent !important;
}

.default-popper {
	background-color: rgba(0, 0, 0, 0.9) !important;
}

.el-popper {
	border: 1px solid rgba(255, 255, 255, 0.514) !important;
	/* background: rgba(0, 0, 0, 0.9) !important; */
	transition: background-color 0.3s ease-out;
}

.popper__arrow {
	display: none !important;
}

/* 这个地方的层级结构非常逆天，vue和el升级都影响到了层级 */
.m-search {
	width: 220px;
	min-width: 220px;
	padding: 0.65em !important;
}

/* 计算样式中，wrapper的bgcolor使用的是从el-input继承的--el-input-bg-color，这个成功 */
.m-search .el-input {
	--el-input-bg-color: rgba(255, 255, 255, 0) !important;
	--el-input-text-color: rgb(255, 255, 255) !important;
	--el-input-border-color: rgb(255, 255, 255) !important;
	--el-input-placeholder-color: rgb(255, 255, 255) !important;
}

/* 这个均未生效 */
.m-search .el-input {
	:deep(.el-input__wrapper) {
		background-color: rgba(255, 255, 255, 0) !important;
		color: rgba(255, 0, 0, 0.791) !important;
		border: 0px !important;
	}

}

.m-search i {
	color: rgba(255, 255, 255, 0.885) !important;
}

.m-search-item {
	min-width: 350px !important;
}

.m-search-item li {
	line-height: normal !important;
	padding: 8px 10px !important;
}

.m-search-item li .title {
	text-overflow: ellipsis;
	overflow: hidden;
	color: rgba(0, 0, 0, 0.87);
}

.m-search-item li .content {
	text-overflow: ellipsis;
	font-size: 12px;
	color: rgba(0, 0, 0, .70);
}
</style>