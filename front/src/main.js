import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

const app = createApp(App).use(store).use(router)

// fetchを定義
app.config.globalProperties.$http = (url, opts) => fetch(url, opts)
// DRFのURL（API用）
app.config.globalProperties.$httpFloor = 'http://127.0.0.1:8000/api/floor/'

app.mount('#app')