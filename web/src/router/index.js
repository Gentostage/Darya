import Vue from 'vue'
import Router from 'vue-router'
import modalpicture from '@/components/modalpicture'
import headline from '@/components/headline'
import pictures from '@/components/pictures'

import {vsPopup, vsButton, vsIcon, vsImages} from 'vuesax'
import 'vuesax/dist/vuesax.css'

import 'material-icons/iconfont/material-icons.css'
import 'materialize-css'
import 'materialize-css/dist/css/materialize.min.css'
import '@/assets/css/picture.css'

Vue.use(Router)
Vue.use(vsPopup)
Vue.use(vsButton)
Vue.use(vsIcon)
Vue.use(vsImages)

const MainPage = {
  template: `
  <div>

        <router-view/>
        <headline/>
        <pictures/>
  </div>

`,
  components: {headline, pictures}
}
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'mainpage',
      component: MainPage,
      children: [{
        path: 'picture/:id',
        component: modalpicture,
        props: true
      }]
    }

  ]
})
