<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  created () {
  }
}
</script>

<style>

body{
  margin:0 auto;
  /*background-image:url('/static/img/bg.webp');*/
  background-repeat:no-repeat;
  background-attachment:fixed;
  background-size: 100%;
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

@media only screen and (max-width: 600px)  {
  body{
    /*background-image:url('/static/img/bg_rew.webp');*/
    background-size: 100% 100%;

  }
}
</style>
