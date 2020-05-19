import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

const axios = Axios.create({
  baseURL: process.env.VUE_APP_BASE_URL
})

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    errorMassage: ''
  },
  mutations: {
    auth_request (state) {
      state.status = 'loading'
    },
    auth_success (state, token) {
      state.status = 'success'
      state.token = token
    },
    auth_error (state, errorMassage) {
      state.status = 'error'
      state.errorMassage = errorMassage
    },
    logout (state) {
      state.status = ''
      state.token = ''
    }
  },
  actions: {
    login ({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: '/auth/token/login', data: user, method: 'POST' })
          .then(resp => {
            const token = resp.data.auth_token
            console.log(token)
            localStorage.setItem('token', 'Token ' + token)
            axios.defaults.headers.common.Authorization = token
            commit('auth_success', token)
            resolve(resp)
          })
          .catch((err) => {
            commit('auth_error', err.response.data.non_field_errors[0])
            localStorage.removeItem('token')
            reject(err.response.data)
          })
      })
    },
    register ({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: '/register', data: user, method: 'POST' })
          .then(resp => {
            const token = resp.data.token
            const user = resp.data.user
            localStorage.setItem('token', token)
            axios.defaults.headers.common.Authorization = token
            commit('auth_success', token, user)
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error', err)
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    logout ({ commit }) {
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common.Authorization
        resolve()
      })
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    errorMassage: state => state.errorMassage
  }
})
