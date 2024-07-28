<template>
	<div id="app">
<!--		<router-view/>-->
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
	
</script>

<style>

</style>
