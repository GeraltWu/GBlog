<template>
	<div>
		<div class="ui top attached segment m-padded-lr-big">
			<h2 class="m-text-500" style="text-align: center">{{ about.title }}</h2>
			<meting-js server="netease" type="song" :id="about.musicId" theme="#25CCF7" v-if="about.musicId!==''"></meting-js>
			<div class="typo content m-margin-top-large" v-viewer v-html="about.content"></div>
		</div>
		<!--评论-->
		<div class="ui bottom teal attached segment threaded comments">
			<CommentList :page="1" :blogId="null" v-if="about.commentEnabled==='true'"/>
			<h3 class="ui header" v-else>评论已关闭</h3>
		</div>
	</div>
</template>

<script setup> //setup语法糖，无需手动调用setup函数，无需使用return将变量和数据暴露给template。
import { defineProps } from 'vue';
import { ref, onMounted } from 'vue';
import { getAbout } from "@/api/about";
import CommentList from "@/components/comment/CommentList";

defineProps({
	name: "blogAbout",
	components: { CommentList }
})

const about = ref({
	title: '',
	musicId: '',
	content: '',
	commentEnabled: 'false'
})

// const getData = async () => {
// 	console.log('发送请求');
// 	const res = await getAbout();
// 	console.log(res);
// 	about.value = res.data;
// }
const getData = () => {
	getAbout().then(res => {
		if (res.code === 200) {
			about.value = res.data;
			console.log(res.data);

		} else {
			// msgError(res.msg);
			console.log(res.msg);
		}
	}).catch(() => {
		// msgError("请求失败");
		console.log("请求失败");
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