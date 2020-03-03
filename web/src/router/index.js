import Vue from 'vue'
import VueRouter from 'vue-router'
import mainpage from '../views/mainpage'
import modalpicture from '../components/modalpicture'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainpage',
    component: mainpage,
    meta: { title: 'Усова Дарья' }
  },
  {
    path: '/picture/:id',
    component: modalpicture,
    meta: { title: 'Усова Дарья' }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

export default router
