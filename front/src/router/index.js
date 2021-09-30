import { createRouter, createWebHistory } from 'vue-router'
import Floor from '@/components/Floor.vue'

const routes = [
  {
    path: '/',
    name: 'django-elevator',
    components: {
      default: Floor,
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router