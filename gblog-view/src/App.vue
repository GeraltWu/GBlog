<template>
	
	<div id="app">
	<!--<router-view/>-->
    <router-view v-slot="{Component}">
		<!-- 通过:is将Component的值bind到component组件上，渲染相应的组件 -->
      	<component :is="Component"/>
    </router-view>
	</div>
</template>

<script>
	export default {
		name: 'app'
	}
	console.log(import.meta.env)
</script>

<style>
@font-face {
	font-family: 'facon';
	src: url('@/assets/fonts/blackhawk-webfont.ttf') format('TrueType');
	font-weight: normal;
	font-style: normal;
}
@font-face {
	font-family: 'Frizon';
	src: url('@/assets/fonts/Frizon-2.ttf') format('TrueType');
	font-weight: normal;
	font-style: normal;
}
</style>
