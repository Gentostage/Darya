<template>
  <div class="container">
    <div class="row ">
      <div class="col s12 m6 offset-m3   xl4 offset-xl4 card-panel white login-box">
        <form class="login" @submit.prevent="login">
          <h1>Вход</h1>
          <div class="row">
            <div class="input-field col s12">
              <input id="login" type="text"  class="validate" v-model="username">
              <label for="login">Логин</label>
            </div>
            <div class="input-field col s12">
              <input id="password" type="password"  class="validate" v-model="password">
              <label for="password">Логин</label>
            </div>
            <div class="class s12 center" v-if="errorMassage">
              <h6 class="red-text">{{errorMassage}}</h6>
            </div>
            <div class="col s12">
              <button class="btn waves-effect waves-light" :class="{disabled:validUserData}" type="submit"
                      name="action">
                Войти
              </button>
              <a class="waves-effect waves-light btn right" @click="logout">Выход</a>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: '',
      errorMassage: ''
    }
  },
  methods: {
    login () {
      const username = this.username
      const password = this.password
      this.$store.dispatch('login', { username, password })
        .then(() => this.$router.push('/profile'))
        .catch((err) => { this.errorMassage = err.non_field_errors[0] })
    },
    logout () {
      this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
    },
    ValidLogin () {
      return this.username.length
    },
    ValidPassword () {
      return this.password.length
    }
  },
  computed: {
    validUserData () {
      return !this.ValidLogin() || !this.ValidPassword()
    }
  }
}
</script>

<style scoped>
.login-box{
  -webkit-box-shadow: 5px 5px 20px 1px #000000;
  box-shadow: 5px 5px 20px 1px #000000;
  border-radius: 5px;
}
</style>
