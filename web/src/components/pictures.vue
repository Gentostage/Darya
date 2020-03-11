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
            v-for="(item, index) in Picture"
            v-bind:key="index"
            class="col s12 m4 l3 img_box"
          >
            <a @click="omModal(item.id)">
              <div class="card">
                <div class="col s12 center-align">
                  <h6>{{item.title}}</h6>
                </div>
                <div class="">
                  <div class="card-image">
                    <img :src="item.mainPic">
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
    <div v-if="showModal" >
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'pictures',
  data () {
    return {
      showModal: false,
      Picture: []
    }
  },
  watch: {
    $route: {
      immediate: true,
      handler: function (newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal
      }
    }
  },
  created () {
    var t = this
    this.$http.get('/api/works/')
      .then(function (response) {
        const works = response.data.data.works
        works.forEach((data) => {
          t.Picture.push({
            title: data.name,
            id: data.id,
            mainPic: process.env.VUE_APP_BASE_URL + data.mainPic
          })
        })
      })
  },
  methods: {
    omModal (id) {
      console.log(id)
      this.$router.push('/picture/' + id)
    }
  }

}
</script>

<style scoped>

</style>
