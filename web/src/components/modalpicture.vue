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
import MainSlot from './mainpage'
export default {
  name: 'modalpicture',
  components: {MainSlot},
  data () {
    return {
      instance: null,
      activePicture: [],
      hover: 'blur'
    }
  },
  mounted () {
    var Modalelem = document.querySelector('.modal')
    // eslint-disable-next-line no-undef
    this.instance = M.Modal.init(Modalelem, {})
    this.instance.open()
  },
  created () {
    let id = this.$route.params.id
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
    }
  }
}
</script>

<style scoped>

</style>
