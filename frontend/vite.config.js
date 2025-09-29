import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    port: 80,
    allowedHosts: 'all'  // 允许所有主机访问
  },
  assetsInclude: ['**/*.m4v']  // 让 Vite 将 .m4v 文件作为静态资源处理
})
