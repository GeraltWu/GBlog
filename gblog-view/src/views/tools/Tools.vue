<template>
    <div>
        <div class="ui top attached segment" style="text-align: center">
            <h2 class="m-text-500">好玩的小组件</h2>
        </div>
        <div class="ui attached segment">
            <div class="ui link two doubling cards">
                <router-link :to="{ name: 'heishou' }" custom v-slot="{ navigate, isActive }">
                    <div class="tool card m-grey1-bg" @click="navigate" :class="{'active': isActive, 'tool card': true}">
                        <div class="image">
                            <img src="/img/heishou.jpg">
                        </div>
                        <div class="content">
                            <div class="header">神鹰语音包</div>
                            <div class="meta">
                                <span class="date">阿弥诺斯</span>
                            </div>
                            <div class="description">
                                哈哈，你也想动手点一点就能享受极致的ASMR吗
                            </div>
                        </div>
                        <!-- <div class="extra content"></div> -->
                    </div>
                </router-link>

                <div class="tool card m-grey1-bg">
                    <div class="image">

                    </div>
                    <div class="content">
                        <div class="header">Molly</div>
                        <div class="meta">
                            <span class="date">Coworker</span>
                        </div>
                        <div class="description">
                            Molly is a personal assistant living in Paris.
                        </div>
                    </div>
                    <!-- <div class="extra content"> </div> -->
                </div>
                <div class="tool card m-grey1-bg">
                    <div class="image">

                    </div>
                    <div class="content">
                        <div class="header">Elyse</div>
                        <div class="meta">
                            <a>Coworker</a>
                        </div>
                        <div class="description">
                            Elyse is a copywriter working in New York.
                        </div>
                    </div>
                    <!-- <div class="extra content"></div> -->
                </div>
            </div>
        </div>
        <!--页面描述-->
        <div class="ui teal attached segment">
            <div class="typo content" v-viewer></div>
        </div>
        <!--评论-->
        <!-- <div class="ui bottom teal attached segment threaded comments">
            <CommentList :page="2" :blogId="null" v-if="info.commentEnabled" />
            <h3 class="ui header" v-else>评论已关闭</h3>
        </div> -->
    </div>
</template>

<script>
import { getData, addViewsByNickname } from "@/api/friend";
import CommentList from "@/components/comment/CommentList";

export default {
    name: "Tools",
    components: { CommentList },
    data() {
        return {
        }
    },
    created() {

    },
    methods: {

    }
}
</script>

<style scoped>


.tool.card {
    display: flex !important;
    flex-direction: row !important;
    align-items: flex-start;
}

.tool.card .image {
    flex: 0 0 auto !important;
    width: 120px;
    height: 100%;
}

.tool.card .image img {
    height: 100% !important;
    object-fit: cover !important;
    /* 保持图片比例并裁剪 */
}

.tool.card .content {
    flex: 1 1 auto !important;
}

.tool.card .content .header {
    margin-top: 0.5em;
    margin-bottom: 0.5em;
}

.tool.card .content .description {
    max-height: 3em;
    /* 假设每行高度为1.5em，两行就是3em */
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    /* 显示两行 */
    -webkit-box-orient: vertical;
}
</style>