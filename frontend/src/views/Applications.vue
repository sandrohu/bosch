<template>
  <div class="applications-container">
    <h1>我的投递</h1>
    <p>投递记录页面，功能待开发</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const applications = ref([])

onMounted(async () => {
  // TODO: 获取投递记录
  console.log('投递记录页面加载')
})
</script>

<style scoped>
.applications-container {
  padding: 20px;
}
</style>