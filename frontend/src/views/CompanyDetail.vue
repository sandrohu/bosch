<template>
  <div class="company-detail-container">
    <h1>公司详情</h1>
    <p>公司ID: {{ companyId }}</p>
    <p>公司详情页面，功能待开发</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const companyId = ref(route.params.id)
const companyDetail = ref(null)

onMounted(async () => {
  // TODO: 获取公司详情
  console.log('获取公司详情，ID:', companyId.value)
})
</script>

<style scoped>
.company-detail-container {
  padding: 20px;
}
</style>