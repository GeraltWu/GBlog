import { fileURLToPath, URL } from 'node:url'
import { defineConfig, loadEnv } from 'vite'
import { prismjsPlugin } from 'vite-plugin-prismjs'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  // 根据当前模式加载相应的环境变量
  const env = loadEnv(mode, process.cwd(), '');

  return {
    plugins: [
      vue(),
      prismjsPlugin({
        languages: 'all', // 语言
        plugins: ['line-numbers', 'show-language', 'copy-to-clipboard', 'inline-color'],
        theme: 'okaidia',// 主题
        css: true,
      }),
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      },
      //import 时省略 .vue 后缀
      extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.vue']
    },

    // 解决跨域问题，使用代理将域名换为目标api的域名，这下就同域了
    server: { // byd我花了半小时时间排查出server单词拼错的问题
      proxy: {
        '/api': {
          // apifox的接口地址好像不跨域，不知道为什么
          // target: 'http://127.0.0.1:4523/m1/4911720-0-default/',
          target: env.VITE_API_BASE_URL,
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '')
        }
      }
    }
  }
});
