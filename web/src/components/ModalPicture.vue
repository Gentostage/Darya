<template>
  <div>
    <div id="modal1" class="modal modal-fixed-footer">
      <div class="modal-content">
        <div class="row">

          <div class="col s12 m6">
            <h4>{{work.name}}</h4>
            <p>{{work.descriptions}}</p>
          </div>
        </div>
        <div class="row">
          <div class="col s12 card-img-modal"
               v-for="(image, index) in work.picture"
               :key="index">
            <picture >
              <source :srcset="url + image.mWebPic" media="(max-width: 1199px)">
              <source :srcset="url + image.webPic" media="(min-width: 1199px)">
              <source :srcset="url + image.mPic" media="(max-width: 1199px)" >
              <source :srcset="url + image.compPic" media="(min-width: 1199px)">
              <img :srcset="url + image.pic" alt="" class="img-modal"
                   />
            </picture>
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
import { mapActions, mapState } from 'vuex'
export default {
  name: 'ModalPicture',
  data () {
    return {
      instance: null,
      activePicture: [],
      url: process.env.VUE_APP_BASE_URL
    }
  },
  async mounted () {
    const Modalelem = document.querySelector('.modal')
    const router = this.$router
    // eslint-disable-next-line no-undef
    this.instance = M.Modal.init(Modalelem, {
      onCloseEnd () {
        router.push('../')
      }
    })

    this.instance.open()

    const id = this.$route.params.id
    this.getWorkById(id)
  },
  methods: {
    ...mapActions([
      'getWorkById'
    ])
  },
  computed: {
    ...mapState([
      'work'
    ])
  },
  beforeRouteLeave (to, from, next) {
    console.log(this.instance.isOpen)
    if (this.instance.isOpen) {
      this.instance.close()
    } else {
      next()
    }
  }
}
</script>

<style scoped>
@import "../assets/css/modalpicture.css";
</style>
