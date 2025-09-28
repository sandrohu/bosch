<template>
  <div class="image-viewer">
    <!-- 连续滚动的图片容器 -->
    <div class="image-scroll-container">
      <img
        v-for="page in totalPages"
        :key="page"
        :src="`/src/assets/boshijieshao/boshijieshao_Page${page}.png`"
        :alt="`第${page}页`"
        class="page-image"
        loading="lazy"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const totalPages = ref(34)
</script>

<style scoped>
.image-viewer {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.image-scroll-container {
  width: 100%;
  height: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  background: #f5f5f5;
  padding: 20px 0;

  /* 平滑滚动 */
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
}

.page-image {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
  margin: 0 auto 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background: white;
}

/* 移动端优化 */
@media (max-width: 768px) {
  .image-scroll-container {
    padding: 10px 0;
  }

  .page-image {
    margin-bottom: 10px;
  }
}

/* 平板优化 */
@media (min-width: 768px) and (max-width: 1024px) {
  .image-scroll-container {
    padding: 15px 0;
  }

  .page-image {
    margin-bottom: 15px;
  }
}

/* 桌面端优化 - 限制最大宽度 */
@media (min-width: 1024px) {
  .image-scroll-container {
    padding: 30px;
  }

  .page-image {
    max-width: 900px;
    margin-bottom: 30px;
  }
}
</style>