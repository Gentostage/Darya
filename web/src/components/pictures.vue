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
            class="col s3 img_box"
          >
            <a @click="omModal(item)"  class="modal-trigger" data-target="modal1">
              <div class="card">
                <div class="col s12 center-align">
                  <h6>Заголовок</h6>
                </div>
                <div class="">
                  <div class="card-image">
                    <img :src="`https://picsum.photos/id/10${item}/800/800`">
                    <span class="card-title">Краткое описание </span>
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
      <div id="modal1" class="modal">
        <div class="modal-content">
          <div class="row">

            <div class="col s12 m6">
              <h4>{{activePicture.title}}</h4>
              <p>{{activePicture.decryption}}</p>
            </div>
            <div class="col s12 m6">
              <img class="materialboxed" width="475" src="https://picsum.photos/id/10/400/400">
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
  </div>
</template>

<script>
export default {
  name: 'pictures',
  data () {
    return {
      hover: 'blur',
      instance: true,
      activePicture: []
    }
  },
  mounted () {
    // eslint-disable-next-line no-unused-vars
    var l = {
      t: this
    }
    var Modalelem = document.querySelector('.modal')
    // eslint-disable-next-line no-undef
    this.instance = M.Modal.init(Modalelem, {
      onOpenStart: function () {
      },
      onCloseEnd: function () {
      }
    })
  },
  methods: {
    routPath (path) {
      this.$router.push(path)
    },
    omModal (id) {
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
    setImnage (id) {
      console.log(id)
    }
  }

}
</script>

<style scoped>
.modal{
  max-height: 85%;
}
</style>
