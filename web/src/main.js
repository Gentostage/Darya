import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Axios from 'axios'
import store from './store'

import 'material-icons/iconfont/material-icons.css'
import 'materialize-css'
import 'materialize-css/dist/css/materialize.min.css'

Vue.prototype.$http = Axios.create({
  baseURL: process.env.VUE_APP_BASE_URL
})
const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common.Authorization = token
}

Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
