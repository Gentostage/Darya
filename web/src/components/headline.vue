<template>
  <div>
    <div class="row head">
      <div class="col s12 center-align">
        <h3>Портфолио</h3>
        <h4>Усова Дарья</h4>
      </div>
      <div class="col s12">
        <div class="">
          <img src="https://pp.userapi.com/c848532/v848532019/17fd38/QphjfSlwC3I.jpg?ava=1" alt="" class="circle responsive-img center-block">
        </div>
      </div>
    </div>
    <div class="parallax-container">
      <div class="parallax"><img :src="'/static/img/par.jpg'"></div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'headline',
  data () {
    return {
      msg: 'headline',
      activeItem: 0,
      search: '',
      instances: null
    }
  },
  mounted () {
    document.addEventListener('DOMContentLoaded', function () {
      var elems = document.querySelectorAll('.parallax')
      this.instances = M.Parallax.init(elems)
    })
  }
}
</script>

<style scoped>
  .head{
    height: 400px;
    background: #ffffff;
    margin: 0px;
  }
</style>
