<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn: function () { return this.$store.getters.isLoggedIn }
  },
  methods: {

  },
  created: function () {
    this.$http.interceptors.response.use(undefined, function (err) {
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch('logout')
        }
        throw err
      })
    })
  }
}
</script>

<style>
body {
    margin: 0 auto;
    background-image: url('assets/img/bg.webp');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: 100% auto;
    z-index: -1;
    scroll-behavior: smooth !important;

}

::-webkit-scrollbar {
    width: 5px;
    height: 5px;
    display: block;
}

::-webkit-scrollbar-track {
    /*-webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);*/
    border-radius: 2px;
    background: #00e43d00;
}

::-webkit-scrollbar-thumb {
    border-radius: 10px;
    /*-webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.5);*/
    background: #9ba5ff;
}

@media (min-width: 1200px) {}
@media (min-width: 992px) and (max-width: 1199px) {
    body {
        background-size: auto 100%;
    }
}
@media (min-width: 768px) and (max-width: 991px) {
    body {
        background-size: auto 100%;
    }
}
@media (max-width: 767px) {
    body {
        background-size: auto 100%;
    }
}
@media (max-width: 480px) {}
@media (max-width: 650px) {}
</style>
