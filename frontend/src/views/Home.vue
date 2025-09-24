<template>
  <div class="home-container">
    <h1>欢迎来到招聘网站</h1>
    <p>这是首页，功能待开发</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

onMounted(() => {
  console.log('首页加载完成')
})
</script>

<style scoped>
.home-container {
  padding: 20px;
  text-align: center;
}

h1 {
  color: #2c3e50;
  margin-bottom: 20px;
}
</style>