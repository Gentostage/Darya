<template>
  <div class="content">
    <div class="col s12 profile-head"><h4 class="center white">Мои работы</h4></div>
    <div class="row">
      <div class="col s12">
        <div class="profile-image-list">
          <div  class='col s12 m6 xl4'>
            <div class="profile-card-image-new white center" @click="createNew">
              <h3 class="blue-text">Создать</h3>
            </div>
          </div>
          <div v-for="(item, index) in works" :key="index" class='col s12 m6 xl4' @click="openCard(item.id)">
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
import { mapActions, mapState } from 'vuex'
export default {
  name: 'Profile',
  data () {
    return {
    }
  },
  computed: {
    ...mapState([
      'works'
    ])
  },
  methods: {
    ...mapActions([
      'getWorks',
      'createWork'
    ]),
    openCard (id) {
      this.$router.push({ path: `/profile/card/${id}` })
    },
    createNew () {
      this.createWork()
        .then(response => {
          this.$router.push(`/profile/card/${response}`)
        })
    }
  },
  created () {
    this.getWorks()
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
    .profile-card-image-new{
      padding: 2px 2px 20px;
      border-radius: 5px;
      margin-bottom: 5px;
      h5 {
        margin: 5px;
      }
    }
    .profile-card-image-new:hover{
      cursor: pointer;
    }

  }
</style>
