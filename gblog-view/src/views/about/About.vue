<template>
	<div>
		<div class="ui top attached segment m-padded-lr-big">
			<h2 class="m-text-500" style="text-align: center">{{ about.title }}</h2>
			<meting-js server="netease" type="song" :id="about.musicId" theme="#25CCF7" autoplay="false" v-if="about.musicId!==''"></meting-js>
			<!-- <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=1946926778&auto=1&height=66"></iframe> -->
			<div class="typo content m-margin-top-large" v-viewer v-html="about.content"></div>
		</div>
		<!--评论-->
		<div class="ui bottom teal attached segment threaded comments">
			<CommentList :page="1" :blogId="null" v-if="about.commentEnabled"/>
			<h3 class="ui header" v-else>评论已关闭</h3>
		</div>
	</div>
</template>

<script setup> //setup语法糖，无需手动调用setup函数，无需使用return将变量和数据暴露给template。
import { defineProps } from 'vue';
import { ref, onMounted } from 'vue';
import { getAboutService } from "@/api/about";
import CommentList from "@/components/comment/CommentList";
import { ElMessage } from "element-plus";

defineProps({
	name: "blogAbout",
	components: { CommentList }
})

const about = ref({
	title: '',
	musicId: '',
	content: '',
	// 是否允许评论 boolean
	commentEnabled: false

})

const getData = () => {
	getAboutService().then(res => {
		if (res.code === 200) {
			console.log(res.data);
			about.value = res.data;
		} else {
			ElMessage.error(res.msg);
		}
	}).catch(() => {
		ElMessage.error("请求失败");
	});
}
onMounted(() => {
	getData();

})



</script>

<style>
	.content ul li {
		letter-spacing: 1px !important;
	}

</style>