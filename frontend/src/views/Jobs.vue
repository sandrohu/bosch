<template>
  <div class="jobs-container">
    <h1>职位列表</h1>
    <p>职位列表页面，功能待开发</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { jobAPI } from '../api/job'

const jobs = ref([])

onMounted(async () => {
  // TODO: 获取职位列表
  console.log('职位列表页面加载')
})
</script>

<style scoped>
.jobs-container {
  padding: 20px;
}
</style>