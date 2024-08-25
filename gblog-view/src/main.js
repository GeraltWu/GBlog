import {createApp} from 'vue'
import App from './App.vue'

import router from './router'

import { createPinia } from 'pinia'
import directives from './util/directive'; // 导入自定义指令

//自定义css
import './assets/css/base.css'
//阿里icon
import './assets/css/icon/iconfont.css'
//typo.css
import "./assets/css/typo.css";
//semantic-ui
import 'semantic-ui-css/semantic.min.css'
//element-plus
import Element from 'element-plus'
import 'element-plus/theme-chalk/index.css'
//moment
import './util/dateTimeFormatUtils.js'
//v-viewer
import 'viewerjs/dist/viewer.css'
import Viewer from 'v-viewer'
//directive
import './util/directive'

console.log(
    '%c 原作者 %c Naccl %c https://github.com/Naccl/NBlog',
    'background:#35495e ; padding: 1px; border-radius: 3px 0 0 3px;  color: #fff',
    'background:#41b883 ; padding: 1px; border-radius: 0 3px 3px 0;  color: #000',
    'background:transparent'
)

const app = createApp(App,
    {
    render(){
        return h => h(App)
    }
});

const cubic = value => Math.pow(value, 3);
const easeInOutCubic = value => value < 0.5 ? cubic(value * 2) / 2 : 1 - cubic((1 - value) * 2) / 2;

//滚动至页面顶部，使用 Element-ui 回到顶部 组件中的算法
app.config.globalProperties.scrollToTop = function () {
    const el = document.documentElement
    const beginTime = Date.now()
    const beginValue = el.scrollTop
    const rAF = window.requestAnimationFrame || (func => setTimeout(func, 16))
    const frameFunc = () => {
        const progress = (Date.now() - beginTime) / 500;
        if (progress < 1) {
            el.scrollTop = beginValue * (1 - easeInOutCubic(progress))
            rAF(frameFunc)
        } else {
            el.scrollTop = 0
        }
    }
    rAF(frameFunc)
}

app.config.productionTip = false

const pinia = createPinia()
// 注册自定义指令
app.use(directives) //全局注册

app.use(Element);
app.use(Viewer);
app.use(pinia)
app.use(router);

app.mount('#app')
