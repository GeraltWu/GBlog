<template>
    <div>
        <div class="ui top attached segment" style="text-align: center">
            <h2 class="m-text-500">神鹰哥语音包</h2>
        </div>
        <div class="ui attached segment">
            <!-- 音频元素，设置display:none隐藏，因为音频播放不需要可视化界面 -->
            <audio ref="audioPlayer" style="display:none" :src="audioSrc"></audio>
            <div class="ui grid doubling column row play">
                <div class="four wide column">
                    <button class="ui button play-btn" @click="playAudio('/public/heishou/别装逼.mp3')" >别装逼</button>
                </div>
                <div class="four wide column">
                    <button class="ui button play-btn" >黑手</button>
                </div>
                <div class="four wide column"><button class="ui button play-btn">Following</button></div>
                <div class="four wide column"><button class="ui button play-btn">Following</button></div>
                <div class="four wide column"> <button class="ui button play-btn">Following</button></div>
                <div class="four wide column"> <button class="ui button play-btn">Following</button></div>
                <div class="four wide column"> <button class="ui button play-btn">Following</button></div>
                <div class="four wide column"> <button class="ui button play-btn">Following</button></div>
                <div class="four wide column"> <button class="ui button play-btn">Following</button></div>
                <div class="four wide column"> <button class="ui button play-btn">Following</button></div>
            </div>
        </div>
        <!--页面描述-->
        <div class="ui teal attached segment">
            <div class="typo content"></div>
        </div>
        <!-- 评论 -->
        <!-- <div class="ui bottom teal attached segment threaded comments">
			<CommentList :page="2" :blogId="null" v-if="info.commentEnabled"/>
			<h3 class="ui header" v-else>评论已关闭</h3>
		</div> -->
    </div>
</template>

<script setup>
// import CommentList from "@/components/comment/CommentList";
import { ref } from 'vue';

// 音频元素的引用
const audioPlayer = ref(null);

// 播放音频的方法
const playAudio = (audioUrl) => {
    if (audioPlayer.value) {
        audioPlayer.value.src = audioUrl;
        audioPlayer.value.play();
    }
};

</script>

<style scoped>
.play {
    margin: 10px !important;
}

.play-btn {
    width: 100%;
    height: 60px;
    margin: 0 !important;
    padding: 5px;
    border: 1px solid #c2c2c2;
    border-radius: 0;
}

.play .column {
    margin: 0 !important;
    padding: 0 !important;
}
</style>