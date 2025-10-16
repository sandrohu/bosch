<template>
  <div class="splash-screen" @click="skipToHome">
    <img src="../assets/images/kaiping.png" alt="Bosch Career" class="splash-image" />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 3秒后自动跳转到首页
onMounted(() => {
  const timer = setTimeout(() => {
    router.push('/home')
  }, 3000)

  // 组件卸载时清理定时器
  return () => clearTimeout(timer)
})

// Skip to home page when clicked
const skipToHome = () => {
  router.push('/home')
}
</script>

<style scoped>
.splash-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  overflow: hidden;
  z-index: 9999;
}

.splash-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* 手机屏幕优化 - 竖屏 */
@media (max-width: 768px) and (orientation: portrait) {
  .splash-screen {
    background: linear-gradient(135deg, #007BC0 0%, #9E2896 50%, #37B19D 100%);
  }

  .splash-image {
    width: 100%;
    height: 100%;
    object-fit: contain;
    object-position: center;
  }
}

/* 手机屏幕优化 - 横屏 */
@media (max-width: 768px) and (orientation: landscape) {
  .splash-screen {
    background: linear-gradient(135deg, #007BC0 0%, #9E2896 50%, #37B19D 100%);
  }

  .splash-image {
    width: auto;
    height: 100%;
    object-fit: contain;
    object-position: center;
  }
}

/* 平板优化 */
@media (min-width: 769px) and (max-width: 1023px) {
  .splash-screen {
    background: linear-gradient(135deg, #007BC0 0%, #9E2896 50%, #37B19D 100%);
  }

  .splash-image {
    max-width: 90%;
    max-height: 90%;
    object-fit: contain;
  }
}

/* 桌面优化 */
@media (min-width: 1024px) {
  .splash-screen {
    background: linear-gradient(135deg, #007BC0 0%, #9E2896 50%, #37B19D 100%);
  }

  .splash-image {
    max-width: 1200px;
    max-height: 90vh;
    object-fit: contain;
  }
}
</style>