<template>
  <div class="content">
    <div class="col s12 profile-head"><h4 class="center white">Мои работы</h4></div>
    <div class="row">
      <div class="col s12">
        <div class="profile-image-list">
          <div v-for="(item, index) in workList" :key="index" class='col s12 m6 xl4' @click="openCard(item.id)">
            <div class="profile-card-image white">
              <div class="col s4 profile-image">
                <picture>
                  <source :srcset="item.webCompPic">
                  <source :srcset="item.mCompPic">
                  <img :srcset="item.mainPic" alt=""/>
                </picture>
              </div>
              <div class="col s8">
                <h5 class="center blue-text">{{item.title}}</h5>
                <div class="col s12">{{item.description}}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data () {
    return {
      workList: []
    }
  },
  methods: {
    openCard (id) {
      this.$router.push({ path: `/profile/card/${id}` })
    }
  },
  created () {
    this.$http.get('/api/works/')
      .then((res) => {
        const response = res.data.data.works
        const works = []
        response.forEach((data) => {
          works.push({
            title: data.name,
            id: data.id,
            mainPic: process.env.VUE_APP_BASE_URL + data.mainPic,
            mCompPic: process.env.VUE_APP_BASE_URL + data.mCompPic,
            webCompPic: process.env.VUE_APP_BASE_URL + data.webCompPic,
            description: data.descriptions
          })
        })
        this.workList = works
      })
  }
}
</script>

<style lang="scss" scoped>
  .profile-head {
    width: 100%;

    h4 {
      margin: 0 0 15px 0;
      padding: 10px 0 10px 0;
    }
  }

  .profile-image-list {
    .profile-image {
      padding: 2px;
      height: 50%;
      img {
        object-fit: cover;
        width: 100%;
        height: 100%;
      }
    }

    .profile-card-image {
      display: flex;
      padding: 2px;
      margin-bottom: 5px;
      border-radius: 5px;

      h5 {
        margin: 5px;
      }
    }
    .profile-card-image:hover{
      cursor: pointer;
    }
  }
</style>
