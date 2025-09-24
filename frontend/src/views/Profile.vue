<template>
  <div class="profile-container">
    <h1>个人中心</h1>
    <p>个人中心页面，功能待开发</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const userInfo = ref(null)

onMounted(async () => {
  // TODO: 获取用户信息
  console.log('个人中心页面加载')
})
</script>

<style scoped>
.profile-container {
  padding: 20px;
}
</style>