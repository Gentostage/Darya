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
            v-for="(item, index) in works"
            v-bind:key="index"
            class="col s12 m6 l6 xl3 img_box"
          >
            <a @click="omModal(item.id)">
              <div class="card">
                <div class="col s12 center-align">
                  <h6>{{item.title}}</h6>
                </div>
                <div class="">
                  <div class="card-image">
                    <picture>
                      <source :srcset="item.webCompPic" >
                      <source :srcset="item.mCompPic" >
                      <img :srcset="item.mainPic" alt=""/>
                    </picture>
<!--                    <img :src="item.mainPic">-->
                    <!--                    <span class="card-title">Краткое описание </span>-->
                  </div>
<!--                  <div class="card-content">-->
<!--                    <span class="card"></span>-->
<!--                  </div>-->
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div>
    </div>
    <div v-if="showModal" >
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'Pictures',
  data () {
    return {
      showModal: false
    }
  },
  computed: {
    ...mapState([
      'works'
    ])
  },
  watch: {
    $route: {
      immediate: true,
      handler: function (newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal
      }
    }
  },
  created () {
    this.getWorks()
  },
  methods: {
    ...mapActions([
      'getWorks'
    ]),
    omModal (id) {
      this.$router.push('/picture/' + id)
    }
  }

}
</script>

<style scoped>
  .content {
    margin-right: 7%;
    margin-left: 7%;
  }

  .card-image img {
    object-fit: cover;
  }

  .card {
    border-radius: .25rem;
    box-shadow: 0 13px 27px -5px hsla(240, 30.1%, 28%, 0.25), 0 8px 16px -8px hsla(0, 0%, 0%, 0.3), 0 -6px 16px -6px hsla(0, 0%, 0%, 0.03);
  }

  @media (min-width: 992px) and (max-width: 1199px) {
    .content {
        margin-right: 10px !important;
        margin-left: 10px !important;
    }
  }
  @media (min-width: 768px) and (max-width: 991px) {
    .content {
        margin-right: 10px !important;
        margin-left: 10px !important;
    }
  }
  @media (max-width: 767px) {
    .content {
      margin-right: 0 !important;
      margin-left: 0 !important;
    }

  }
</style>
