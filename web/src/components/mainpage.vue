<template>
  <div>
    <div id="scroll-area">
      <smooth-scrollbar>
        <div class="example-content">
          <router-view name="head"/>
          <router-view name="pic"/>
          <router-view name="mod"/>
        </div>
      </smooth-scrollbar>
    </div>
  </div>
</template>

<script>
export default {
  name: 'mainpage'
}
</script>

<style scoped>

</style>
