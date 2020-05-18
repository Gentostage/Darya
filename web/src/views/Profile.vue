<template>
  <div class="content">
  <div class="col s12 profile-head"><h4 class="center white">Мои работы</h4></div>
    <div class="row">
      <div class="col s12">
        <div class="profile-image-list">
          <div v-for="(item, index) in workList" :key="index" class='col s12 xl4 card-profile-image white'>
            <div class="col s4 profile-image">
              <picrute>
                <source :srcset="item.webCompPic">
                <source :srcset="item.mCompPic">
                <img :srcset="item.mainPic" alt=""/>
              </picrute>
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
</template>

<script>
export default {
  name: 'Profile',
  data () {
    return {
      workList: []
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

<style scoped>
  .profile-image-list{

  }
  .profile-image-list .profile-image{
    padding: 2px;
  }
  .profile-image-list .card-profile-image{
    padding: 2px;
  }
  .card-profile-image {
    margin-bottom: 5px;
    border-radius: 5px;
  }
  .card-profile-image h5 {
    margin: 5px;
  }

  .profile-image {
    height: 100px;
  }

  .profile-image img {
    object-fit: cover;
    width: 100%;
    height: 100%;
  }

  .profile-head {
    width: 100%;
  }

  .profile-head h4 {
    margin: 0 0 15px 0;
    padding: 10px 0 10px 0;
  }
</style>
