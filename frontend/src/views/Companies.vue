<template>
  <div class="companies-container">
    <h1>公司列表</h1>
    <p>公司列表页面，功能待开发</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const companies = ref([])

onMounted(async () => {
  // TODO: 获取公司列表
  console.log('公司列表页面加载')
})
</script>

<style scoped>
.companies-container {
  padding: 20px;
}
</style>