<template>
  <div class="container">
    <div class="row white">
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
      <div v-for="(item, index) in work.picture" :key="index" class="col s12 ">
        <img :src="url+item.mPic" alt="" width="100%">
      </div>
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
      'updateMainPucture'
    ]),
    uploadMainPiture (e) {
      const form = new FormData()
      form.append('mainPic', e.target.files[0])
      const id = this.$route.params.id
      this.updateMainPucture({ form: form, id: id })
        .then(data => { this.work.mainPic = data })
        .catch(data => console.log(data))
    }
  }
}
</script>

<style scoped>
.image-upload>input {
  display: none;
}
</style>
