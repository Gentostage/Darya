<template>
  <div>
    <headline></headline>
    <pictures></pictures>
    <slot></slot>
  </div>
</template>

<script>
import Headline from '@/components/headline'
import Pictures from '@/components/pictures'

export default {
  name: 'mainpage',
  components: {Headline, Pictures}
}
</script>

<style scoped>

</style>
