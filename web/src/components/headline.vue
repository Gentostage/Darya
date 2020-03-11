<template>
  <div>
    <div class="row head">
      <div class="col s12 center-align">
        <h3>Портфолио</h3>
        <hr>
        <div class="col s12 l5">
          <div class="col s6 el_head">
            <a target="_blank" rel="noopener noreferrer" href="https://vk.com/dashkausova">
              <img  src="../assets/ico/vk.svg"  width="120" height="120" >
            </a>
          </div>
          <div class="col s6 el_head">
            <a target="_blank" rel="noopener noreferrer" href="https://www.instagram.com/daryausova_alex/">
                <img src="../assets/ico/instagram.svg" width="120" height="120" >
             </a>
          </div>
        </div>
        <div class="col s12 l2">
          <h3>Усова Дарья</h3>
          <br>
          <div class="col s12">
            <div class="">
              <img src="https://pp.userapi.com/c848532/v848532019/17fd38/QphjfSlwC3I.jpg?ava=1" alt=""
                   class="circle responsive-img center-block">
            </div>
          </div>
        </div>
        <div class="col s12 l2">
          <div class="col s12 el_head">
            <h3>Обо мне</h3>
          </div>
        </div>
        <div class="col s12 l3">
<!--             <img :src="`/static/img/dopey-pug-prints.webp`" width="300" height="300">-->
        </div>
      </div>

    </div>
    <div class="parallax-container">
      <div class="parallax"><img src="../assets/img/par.webp"></div>
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
    const elems = document.querySelectorAll('.parallax')
    // eslint-disable-next-line no-undef
    this.instances = M.Parallax.init(elems)
  }
}
</script>

<style scoped>
@import "../assets/css/headline.css";

</style>
