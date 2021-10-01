import Vue from 'vue'
import Router from "vue-router";
import Floor from '@/components/Floor.vue'

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'django-elevator',
    components: {
      default: Floor,
    }
  }
]

const router = new Router({
  mode: "history",
  routes
})

export default router