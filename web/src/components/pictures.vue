<template>
  <div>
    <div class="row">
      <div class="col s12 center-align">
        <h3>
          <span class="white-text"><br><br><br></span>
        </h3>
      </div>
      <div class="content">
        <div class="row">
          <div
            v-for="item in 10"
            v-bind:key="item"
            class="col s12 m4 l3 img_box"
          >
            <a @click="omModal(item)">
              <div class="card">
                <div class="col s12 center-align">
                  <h6>Заголовок</h6>
                </div>
                <div class="">
                  <div class="card-image">
                    <img :src="`https://picsum.photos/id/10${item}/800/800`">
                    <!--                    <span class="card-title">Краткое описание </span>-->
                  </div>
                  <div class="card-content">
                    <span class="card"></span>
                  </div>
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'pictures',
  data () {
    return {

    }
  },
  mounted () {

  },
  methods: {
    omModal (id) {
      this.$router.push('/picture/' + id)
    }
  }

}
</script>

<style scoped>
.modal{
  max-height: 85%;
}
</style>
