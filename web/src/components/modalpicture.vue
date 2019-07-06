<template>
  <div>
    <div id="modal1" class="modal">
      <div class="modal-content">
        <h4>{{id}}</h4>
        <p>A bunch of text</p>
      </div>
      <div class="modal-footer">
        <a href="/" class="modal-close waves-effect waves-green btn-flat">Agree</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['id'],
  name: 'modalpicture',
  data () {
    return {
      instance: null
    }
  },
  created () {

  }
}
</script>

<style scoped>

</style>
