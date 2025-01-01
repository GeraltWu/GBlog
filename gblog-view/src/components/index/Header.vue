<template>
	<header ref="header">
		<div class="view">
			<img ref="imgbg1" :src="defaultSettings.bg1" style="display: none;">
			<div class="bg1" :style="{ backgroundImage: 'url(' + defaultSettings.bg1 + ')' }"></div>
			<div class="bg2" :style="{ backgroundImage: 'url(' + defaultSettings.bg2 + ')' }"></div>
			<div class="bg3" :style="{ backgroundImage: 'url(' + defaultSettings.bg3 + ')' }" v-show="loaded"></div>
		</div>
		<!-- <div class="text-malfunction" :data-word="defaultSettings.malfunctionText">
			{{ defaultSettings.malfunctionText }}
			<div class="line"></div>
		</div> -->
		<div class="cyberpunk">
			<span class="name">Geralt</span>
		</div>
		<div class="wrapper">
			<i class="ali-iconfont icon-down" @click="scrollToMain"></i>
		</div>
		<div class="transition"></div>
		<!-- <div class="wave1"
			style="background: url('https://fastly.jsdelivr.net/gh/Naccl/blog-resource/img/wave1.png') repeat-x;"></div>
		<div class="wave2"
			style="background: url('https://fastly.jsdelivr.net/gh/Naccl/blog-resource/img/wave2.png') repeat-x;"></div> -->
	</header>
</template>

<script>
import { useSiteStore } from '@/stores/site';
import defaultSettings from '@/settings.js'
import { ref, watch, onMounted} from 'vue';

export default {
	name: "blogHeader",
	setup() {
		const siteStore = useSiteStore()

		const loaded = ref(false)
		const header = ref(null)
		const imgbg1 = ref(null)

		// 根据clientHeight动态改变header高度，保证占满整个页面
		watch(() => siteStore.clientSize.clientHeight, () => {
			setHeaderHeight()
		})

		//根据可视窗口高度，动态改变首图大小
		function setHeaderHeight() {
			header.value.style.height = `${siteStore.clientSize.clientHeight}px`
		}

		onMounted(() => {
			/**
 			* 因为bg3.jpg比较小，通常会比bg1.jpg先加载，显示出来会有一瞬间bg1显示一半，bg3显示一半，为了解决这个问题，增加这个判断，让bg1加载完毕后再显示bg3
 			* HTML中使用img标签的原因：我个人想用div作为图片的载体，而只有img标签有图片加载完毕的onload回调，所以用一个display: none的img人柱力来加载图片
 			* 当img中的src加载完毕后，会把图片缓存到浏览器，后续在div中用background url的形式将直接从浏览器中取出图片，不会下载两次图片
 			*/
			imgbg1.value.onload = () => {
				loaded.value = true
			}
			setHeaderHeight()
			let startingPoint

			header.value.addEventListener('mouseenter', (e) => {
				startingPoint = e.clientX
			})
			header.value.addEventListener('mouseout', () => {
				header.value.classList.remove('moving')
				header.value.style.setProperty('--percentage', 0.5)
			})
			header.value.addEventListener('mousemove', (e) => {
				let percentage = (e.clientX - startingPoint) / window.outerWidth + 0.5
				header.value.style.setProperty('--percentage', percentage)
				header.value.classList.add('moving')
			})
		})
		//平滑滚动至正文部分
		function scrollToMain() {
			window.scrollTo({ top: siteStore.clientSize.clientHeight, behavior: 'smooth' })
		}

		return {
			header,
			imgbg1,
			defaultSettings,
			loaded,
			scrollToMain,
		}
	}
}
</script>

<style scoped>
header {
	--percentage: 0.5;
	user-select: none;
}

.view {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	display: flex;
	justify-content: center;
	transform: translatex(calc(var(--percentage) * 100px));
}

.view div {
	background-position: center center;
	background-size: cover;
	position: absolute;
	width: 110%;
	height: 100%;
}

.view .bg1 {
	z-index: 10;
	opacity: calc(1 - (var(--percentage) - 0.5) / 0.5);
}

.view .bg2 {
	z-index: 20;
	opacity: calc(1 - (var(--percentage) - 0.25) / 0.25);
}

.view .bg3 {
	left: -10%;
}

header .view,
header .bg1,
header .bg2 {
	transition: .2s all ease-in;
}

header.moving .view,
header.moving .bg1,
header.moving .bg2 {
	transition: none;
}

/* ----------------------- */


.cyberpunk {
	text-align: center;
	height: 150;
	font-size: 180px;
	font-family: 'Frizon';
	text-shadow: -3px -3px 0px #e13b1b, 9px 3px 0px #e13b1b;
	opacity: 0.9;
	border: 0;
	color: #0096cb;
	letter-spacing: 3px;
	line-height: 160px;
	position: relative;
	margin: auto;
	top: 35%;
}

.name::after {
	--slice-0: inset(50% 50% 50% 50%);
	--slice-1: inset(80% -6px 0 0);
	--slice-2: inset(50% -6px 30% 0);
	--slice-3: inset(10% -6px 85% 0);
	--slice-4: inset(40% -6px 43% 0);
	--slice-5: inset(80% -6px 5% 0);
	content: 'Geralt';
	display: block;
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	text-shadow: -3px -3px 0px #ffffff, 3px 3px 0px var(--red-color);
	clip-path: var(--slice-0);

	animation: 1.2s glitch infinite;
	animation-timing-function: steps(2, end);
}

@keyframes glitch {
	0% {
		clip-path: var(--slice-1);
		transform: translate(-20px, -10px);
	}

	10% {
		clip-path: var(--slice-3);
		transform: translate(10px, 10px);
	}

	20% {
		clip-path: var(--slice-1);
		transform: translate(-10px, 10px);
	}

	30% {
		clip-path: var(--slice-3);
		transform: translate(0px, 5px);
	}

	40% {
		clip-path: var(--slice-2);
		transform: translate(-5px, 0px);
	}

	50% {
		clip-path: var(--slice-3);
		transform: translate(5px, 0px);
	}

	60% {
		clip-path: var(--slice-4);
		transform: translate(5px, 10px);
	}

	70% {
		clip-path: var(--slice-2);
		transform: translate(-10px, 10px);
	}

	80% {
		clip-path: var(--slice-5);
		transform: translate(20px, -10px);
	}

	90% {
		clip-path: var(--slice-1);
		transform: translate(-10px, 0px);
	}

	100% {
		clip-path: var(--slice-1);
		transform: translate(0);
	}
}

/* ----------------------- */

/* .text-malfunction {
	position: absolute;
	top: 40%;
	left: 51.5%;
	transform: translate(-50%, -50%) scale(2.5);
	width: 220px;
	font-size: 34px;
	font-family: sans-serif;
	color: transparent;
}

.line {
	position: absolute;
	width: 200px;
	left: -1px;
	height: 1px;
	background: black;
	z-index: 50;
	animation: lineMove 5s ease-out infinite;
}

.text-malfunction:before,
.text-malfunction:after {
	content: attr(data-word);
	position: absolute;
	top: 0;
	height: 36px;
	overflow: hidden;
	filter: contrast(200%);
}

.text-malfunction:before {
	left: 0;
	color: red;
	text-shadow: 1px 0 0 red;
	z-index: 30;
	animation: malfunctionAni 0.95s infinite;
}

.text-malfunction:after {
	left: -1px;
	color: cyan;
	text-shadow: -1px 0 0 cyan;
	z-index: 40;
	mix-blend-mode: lighten;
	animation: malfunctionAni 1.1s infinite 0.2s;
}

@keyframes lineMove {
	9% {
		top: 38px;
	}

	14% {
		top: 8px;
	}

	18% {
		top: 42px;
	}

	22% {
		top: 1px;
	}

	32% {
		top: 32px;
	}

	34% {
		top: 12px;
	}

	40% {
		top: 26px;
	}

	43% {
		top: 7px;
	}

	99% {
		top: 30px;
	}
}

@keyframes malfunctionAni {
	10% {
		top: -0.4px;
		left: -1.1px;
	}

	20% {
		top: 0.4px;
		left: -0.2px;
	}

	30% {
		left: .5px;
	}

	40% {
		top: -0.3px;
		left: -0.7px;
	}

	50% {
		left: 0.2px;
	}

	60% {
		top: 1.8px;
		left: -1.2px;
	}

	70% {
		top: -1px;
		left: 0.1px;
	}

	80% {
		top: -0.4px;
		left: -0.9px;
	}

	90% {
		left: 1.2px;
	}

	100% {
		left: -1.2px;
	}
} */

.wrapper {
	position: absolute;
	width: 100px;
	bottom: 150px;
	left: 0;
	right: 0;
	margin: auto;
	font-size: 26px;
	z-index: 100;
}

.wrapper i {
	font-size: 60px;
	opacity: 0.5;
	cursor: pointer;
	position: absolute;
	color: var(--white-color);
	top: 55px;
	left: 20px;
	animation: opener .5s ease-in-out alternate infinite;
	transition: opacity .2s ease-in-out, transform .5s ease-in-out .2s;
}

.wrapper i:hover {
	opacity: 1;
}

@keyframes opener {
	100% {
		top: 65px
	}
}

.transition {
	position: absolute;
	bottom: 0;
	width: 100%;
	height: 60px;
	background: linear-gradient(0deg, #262c3a, #ffffff00);
}

/* .wave1,
.wave2 {
	position: absolute;
	bottom: 0;
	transition-duration: .4s, .4s;
	z-index: 80;
}

.wave1 {
	height: 75px;
	width: 100%;
}

.wave2 {
	height: 90px;
	width: calc(100% + 100px);
	left: -100px;
} */
</style>