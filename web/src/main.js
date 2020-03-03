import Vue from 'vue'
import App from './App.vue'
import router from './router'

import 'material-icons/iconfont/material-icons.css'
import 'materialize-css'
import 'materialize-css/dist/css/materialize.min.css'
import './assets/css/picture.css'

import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'

import Axios from 'axios'

const client = Axios.create({
  baseURL: process.env.VUE_APP_BASEURL
})

Vue.prototype.$http = client

Vue.use(Vuesax)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
