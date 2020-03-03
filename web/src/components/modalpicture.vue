<template>
  <MainSlot>
      <div id="modal1" class="modal">
        <div class="modal-content">
          <div class="row">

            <div class="col s12 m6">
              <h4>{{activePicture.title}}</h4>
              <p>{{activePicture.decryption}}</p>
            </div>
            <div class="col s12 m6">
              <img class="materialboxed" width="100%" src="https://picsum.photos/id/10/400/400">
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
  </MainSlot>
</template>

<script>
import MainSlot from '../views/mainpage'
export default {
  name: 'modalpicture',
  components: { MainSlot },
  data () {
    return {
      instance: null,
      activePicture: [],
      hover: 'blur'
    }
  },
  mounted () {
    const Modalelem = document.querySelector('.modal')
    const t = this
    // eslint-disable-next-line no-undef
    this.instance = M.Modal.init(Modalelem, {
      onCloseEnd () {
        t.$router.push('/')
      }
    })

    this.instance.open()
  },
  created () {
    const id = this.$route.params.id
    this.$http.get('/' + id)
    this.activePicture = {
      title: 'Заголовок',
      decryption: 'Описание',
      content: id,
      listimage: []
    }
    for (var i = 0; i < 9; i++) {
      this.activePicture.listimage.push({
        src: 'https://picsum.photos/id/1' + id + i + '/800/800'
      })
    }
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
