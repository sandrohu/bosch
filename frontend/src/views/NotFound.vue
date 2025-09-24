<template>
  <div class="not-found-container">
    <h1>404</h1>
    <p>页面不存在</p>
    <router-link to="/">返回首页</router-link>
  </div>
</template>

<script setup>
</script>

<style scoped>
.not-found-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

h1 {
  font-size: 72px;
  color: #409eff;
  margin-bottom: 20px;
}

p {
  font-size: 20px;
  color: #666;
  margin-bottom: 30px;
}

a {
  color: #409eff;
  text-decoration: none;
  font-size: 16px;
}

a:hover {
  text-decoration: underline;
}
</style>