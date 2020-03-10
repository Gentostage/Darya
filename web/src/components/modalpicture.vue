<template>
  <div>
    <div id="modal1" class="modal">
      <div class="modal-content">
        <div class="row">

          <div class="col s12 m6">
            <h4>{{activePicture.title}}</h4>
            <p>{{activePicture.decryption}}</p>
          </div>
          <div class="col s12 m6" v-if="sizePict">
            <img class="materialboxed" width="100%" :src="sizePict">
          </div>
        </div>
        <div>
          <div class="con-example-images">
            <vs-images :hover="hover">
              <vs-image @click="setImnage(index)"
                        :key="index"
                        :src="image.src"
                        v-for="(image, index) in activePicture.listimage
              "/>
            </vs-images>
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
      hover: 'blur',
      sizePict: ''
    }
  },
  mounted () {
    const Modalelem = document.querySelector('.modal')
    const t = this
    // eslint-disable-next-line no-undef
    this.instance = M.Modal.init(Modalelem, {
      onCloseEnd () {
        t.$router.push('../')
      }
    })

    this.instance.open()
  },
  created () {
    const id = this.$route.params.id
    console.log(id)
    var t = this
    this.$http.get('/api/works/' + id)
      .then(function (response) {
        const work = response.data.data.work
        t.activePicture = {
          title: work[0].name,
          decryption: work[0].descriptions,
          content: work[0].id,
          listimage: []
        }
        t.sizePict = process.env.VUE_APP_BASE_URL + work[0].picture[0].pic
        work[0].picture.forEach((data) => {
          t.activePicture.listimage.push({
            src: process.env.VUE_APP_BASE_URL + data.pic
          })
        })
      })
  },
  methods: {
    setImnage (id) {
      console.log(id)
    },
    getImage (id) {
      this.$http.get('/' + id)
    }
  }
}
</script>

<style scoped>

</style>
