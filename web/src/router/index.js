import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store.js'

import MainPage from '../views/MainPage'
import ModalPicture from '../components/ModalPicture'
import Profile from '../views/Profile.vue'
import Login from '../components/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainpage',
    component: MainPage,
    meta: { title: 'Усова Дарья' },
    children: [
      {
        meta: {
          showModal: true,
          title: 'Усова Дарья'
        },
        path: 'picture/:id',
        component: ModalPicture,
        props: true
      }
    ]
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login')
  } else {
    next()
  }
  next()
})

export default router
