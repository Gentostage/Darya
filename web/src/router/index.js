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
    meta: { title: 'Усова Дарья' },
    children: [
      {
        meta: {
          showModal: true
        },
        path: 'picture/:id',
        component: modalpicture,
        props: true
      }
    ]
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
