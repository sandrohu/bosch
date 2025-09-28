<template>
  <div class="direct-pdf-viewer">
    <!-- 直接使用iframe显示PDF -->
    <iframe
      :src="src"
      class="pdf-iframe"
      title="PDF Document"
      frameborder="0"
      allowfullscreen
    />
  </div>
</template>

<script setup>
defineProps({
  src: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.direct-pdf-viewer {
  width: 100%;
  height: 100%;
  min-height: 500px;
}

.pdf-iframe {
  width: 100%;
  height: 100%;
  min-height: calc(100vh - 250px);
  border: none;
  background: white;
}

/* 移动端优化 */
@media (max-width: 768px) {
  .pdf-iframe {
    min-height: calc(100vh - 280px);
  }
}
</style>