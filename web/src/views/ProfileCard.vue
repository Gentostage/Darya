<template>
  <div class="container">
    <div class="row white">
      <div class="col s12"><h3>Редактирование</h3></div>
      <div class="input-field col s12">
        <input id="name" type="text" class="validate" v-model="Work.name" placeholder="Моя первая работа ...">
        <label for="name">Название</label>
      </div>
      <hr>
      <div class="input-field col s12">
          <textarea id="descriptions" class="materialize-textarea" placeholder="Описание моей первой работы ..."
                    v-model="Work.descriptions"></textarea>
        <label for="descriptions">Описание</label>
      </div>
      <h4 class="center">Главная картинка</h4>
      <div class="col s12 image-upload">
        <label for="file-input">
            <img :srcset="url + Work.mainPic" width="100%" alt=""/>
        </label>
        <input id="file-input" type="file" @change="updateMainPucture"/>
      </div>
      <h4 class="center">Работы</h4>
      <div v-for="(item, index) in Work.picture" :key="index" class="col s12 ">
        <img :src="url+item.mPic" alt="" width="100%">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileCard',
  data () {
    return {
      Work: [],
      url: process.env.VUE_APP_BASE_URL
    }
  },
  created () {
    const id = this.$route.params.id
    this.fetchPict(id)
  },
  methods: {
    fetchPict (id) {
      this.$http.get('/api/works/' + id)
        .then(res => {
          this.Work = res.data.data.work[0]
        })
        .catch(err => console.log(err))
    },
    updateMainPucture (e) {
      const form = new FormData()
      form.append('mainPic', e.target.files[0])
      this.$http.put(`/api/works/image/${this.Work.id}`, form)
        .then(res => console.log(this.Work.mainPic = res.data.data.attributes.picture_url))
    }
  }
}
</script>

<style scoped>
.image-upload>input {
  display: none;
}
</style>
