<template>
  <div class="global-logo" v-if="!hideLogo">
    <img src="../assets/images/logo.png" alt="BOSCH" class="logo-image" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// 在开屏页不显示全局logo（因为开屏页有自己的logo）
const hideLogo = computed(() => {
  return route.name === 'Splash'
})
</script>

<style scoped>
.global-logo {
  position: fixed;
  top: 1rem;  /* 调整到彩虹线上方 */
  left: 1rem;
  width: 7.25rem;  /* 116px */
  height: 1.63rem; /* 26px */
  z-index: 100;
  display: flex;
  align-items: center;
}

.logo-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* 移动端适配 */
@media (max-width: 375px) {
  .global-logo {
    top: 0.75rem;  /* 调整到彩虹线上方 */
    left: 1rem;
    width: 7.25rem;
    height: 1.63rem;
  }
}

/* 平板端 */
@media (min-width: 768px) {
  .global-logo {
    top: 1.5rem;
    left: 1.5rem;
    width: 8rem;
    height: 1.8rem;
  }
}

/* 桌面端 */
@media (min-width: 1024px) {
  .global-logo {
    top: 1.5rem;
    left: 2.5rem;
    width: 9rem;
    height: 2rem;
  }
}
</style>