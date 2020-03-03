import Vue from 'vue'
import Router from 'vue-router'
import modalpicture from '@/components/modalpicture'
import mainpage from '@/components/mainpage'

import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'

import 'material-icons/iconfont/material-icons.css'
import 'materialize-css'
import 'materialize-css/dist/css/materialize.min.css'
import '@/assets/css/picture.css'

Vue.use(Router)
Vue.use(Vuesax)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'mainpage',
      component: mainpage
    },
    {
      path: '/picture/:id',
      component: modalpicture
    }

  ]
})
