<template>
  <div class="job-detail-container">
    <h1>职位详情</h1>
    <p>职位ID: {{ jobId }}</p>
    <p>职位详情页面，功能待开发</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { jobAPI } from '../api/job'

const route = useRoute()
const jobId = ref(route.params.id)
const jobDetail = ref(null)

onMounted(async () => {
  // TODO: 获取职位详情
  console.log('获取职位详情，ID:', jobId.value)
})
</script>

<style scoped>
.job-detail-container {
  padding: 20px;
}
</style>