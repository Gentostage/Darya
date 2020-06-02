import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

const axios = Axios.create({
  baseURL: process.env.VUE_APP_BASE_URL
})

const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common.Authorization = token
}
axios.interceptors.response.use(undefined, (err) => {
  return new Promise((resolve, reject) => {
    if (err.response.status === 401 && err.config && !err.config.__isRetryRequest) {
      this.$store.dispatch('logout')
    }
    throw err
  })
})

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    errorMassage: '',
    works: [],
    work: []
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
    },
    set_works (state, works) {
      state.works = works
    },
    set_work (state, work) {
      state.work = work
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
    },
    getWorks ({ commit }) {
      axios.get('/api/works/')
        .then((res) => {
          const response = res.data
          const works = []
          response.forEach((data) => {
            works.push({
              title: data.name,
              id: data.id,
              mainPic: process.env.VUE_APP_BASE_URL + data.mainPic,
              mCompPic: process.env.VUE_APP_BASE_URL + data.mCompPic,
              webCompPic: process.env.VUE_APP_BASE_URL + data.webCompPic,
              description: data.descriptions
            })
          })
          commit('set_works', works)
        })
    },
    getWorkById ({ commit }, id) {
      axios.get('/api/works/' + id)
        .then((response) => { commit('set_work', response.data) })
        .catch((response) => console.log(response))
    },
    createWork ({ commit }) {
      return new Promise((resolve, reject) => {
        axios.post('/api/works/', { name: 'Новая работа', descriptions: 'Описание новой работы....' })
          .then(res => {
            commit('set_work', res.data)
            resolve(res.data.id)
          })
          .catch(res => console.log(res))
      })
    },
    updateMainPucture ({ commit }, data) {
      return new Promise((resolve, reject) => {
        axios.put(`/api/works/image/${data.id}`, data.form)
          .then(res => { resolve(res.data.picture_url) })
          .catch(res => { reject(res) })
      })
    },
    deleteImage ({ commit }, id) {
      axios.delete(`/api/picture/${id}`)
        .catch(resp => { console.log(resp) })
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    errorMassage: state => state.errorMassage
  }
})
