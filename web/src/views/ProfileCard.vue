<template>
  <div class="container">
    <div class="row white card">
      <div class="col s12"><h3>Редактирование</h3></div>
      <div class="input-field col s12">
        <input id="name" type="text" v-model="work.name" placeholder="Моя первая работа ...">
        <label for="name">Название</label>
      </div>
      <hr>
      <div class="input-field col s12">
          <textarea id="descriptions" class="materialize-textarea" placeholder="Описание моей первой работы ..."
                    v-model="work.descriptions"></textarea>
        <label for="descriptions">Описание</label>
      </div>
      <h4 class="center">Главная картинка</h4>
      <div class="col s12 image-upload">
        <label for="file-input">
            <img :srcset="url + work.mainPic" width="100%" alt=""/>
        </label>
        <input id="file-input" type="file" @change="uploadMainPiture"/>
      </div>
      <h4 class="center">Работы</h4>
      <div class="image-upload image-upload-card center">
        <label for="file-input-card">
            <div><h5 class="blue-text">Загрузить фотографию</h5></div>
        </label>
      <input id="file-input-card" type="file" @change="uploadPiture"/>
      </div>
      <div v-for="(item, index) in work.picture" :key="index" class="col s12 ">
        <div class="card-image">
          <img :src="url+item.mPic" alt="" width="100%">
          <div class="card-image-button" @click="deleteImageCard(index)">
            <h5>Удалить</h5>
          </div>
        </div>
      </div>
    </div>
    <div class="card-button">
      <a class="waves-effect waves-light btn right" @click="saveWorkCard">Сохранить</a>
      <a class="waves-effect waves-light btn left red" @click="deleteWorkCard">Удалить</a>
    </div>
  </div>
</template>

<script>

import { mapActions, mapState } from 'vuex'
export default {
  name: 'ProfileCard',
  data () {
    return {
      Work: [],
      url: process.env.VUE_APP_BASE_URL
    }
  },
  mounted () {
    // eslint-disable-next-line no-undef
    M.updateTextFields()
    const id = this.$route.params.id
    this.getWorkById(id)
  },
  computed: {
    ...mapState([
      'work'
    ])
  },
  methods: {
    ...mapActions([
      'getWorkById',
      'updateMainPucture',
      'deleteImage',
      'createPucture',
      'deleteWork',
      'updateWork'
    ]),
    uploadMainPiture (e) {
      const form = new FormData()
      form.append('mainPic', e.target.files[0])
      const id = this.$route.params.id
      this.updateMainPucture({ form: form, id: id })
        .then(data => { this.work.mainPic = data })
        .catch(data => console.log(data))
    },
    deleteImageCard (id) {
      const imageId = this.work.picture[id].id
      this.deleteImage(imageId)
      this.work.picture.splice(id, 1)
    },
    uploadPiture (e) {
      const id = this.$route.params.id
      const form = new FormData()
      form.append('pic', e.target.files[0])
      form.append('work', id)
      this.createPucture(form)
    },
    deleteWorkCard () {
      const id = this.$route.params.id
      this.deleteWork(id)
        .then(() => this.$router.push('../'))
        .catch((res) => console.log(res))
    },
    saveWorkCard () {
      const id = this.$route.params.id
      this.updateWork({ id: id, form: { name: this.work.name, descriptions: this.work.descriptions } })
    }
  }
}
</script>

<style  lang="scss" scoped>
.card{
  margin-bottom: 50px;
}
.card-image{
  position: relative;
  margin-bottom: 5px;
  &-button {
    position: absolute;
    bottom: 5px;
    right: 0px;
    background-color: #ffffff9e;
    h5{
      margin: 5px;
    }
  }
  &-button:hover{
    cursor: pointer;
  }
}
.image-upload>input {
  display: none;
}
.image-upload-card{
  margin:  25px 15px 25px 15px;
  border-radius: 10px;
  border: gray solid 1px;
  h5{
      margin: 5px;
  }
}
.card-button{
  width: 100%;
  position: fixed;
  bottom: 0px;
  left: 0;
  right: 0;
  z-index: 10;
  padding: 5px;
  background-color: rgba(255, 255, 255, 0.5);
}
</style>
