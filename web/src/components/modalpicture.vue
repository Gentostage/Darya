<template>
  <div>
    <div id="modal1" class="modal modal-fixed-footer">
      <div class="modal-content">
        <div class="row">

          <div class="col s12 m6">
            <h4>{{activePicture.name}}</h4>
            <p>{{activePicture.descriptions}}</p>
          </div>
        </div>
        <div class="row">
          <div class="col s12 card-img-modal"
               v-for="(image, index) in activePicture.picture"
               :key="index">
            <img alt="" class="img-modal"
                 :src="url + image.pic"
                 />
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <a class="modal-close waves-effect waves-green btn-flat">Закрыть</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'modalpicture',
  data () {
    return {
      instance: null,
      activePicture: [],
      url: process.env.VUE_APP_BASE_URL
    }
  },
  async mounted () {
    const Modalelem = document.querySelector('.modal')
    const t = this
    // eslint-disable-next-line no-undef
    this.instance = M.Modal.init(Modalelem, {
      onCloseEnd () {
        t.$router.push('../')
      }
    })

    this.instance.open()

    const id = this.$route.params.id
    await this.fetchPict(id)
  },
  methods: {
    async fetchPict (id) {
      const response = await this.$http.get('/api/works/' + id)
      console.log(response.data.data.work[0])
      this.activePicture = response.data.data.work[0]
    }
  }
}
</script>

<style scoped>
@import "../assets/css/modalpicture.css";
</style>
