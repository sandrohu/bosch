<template>
  <transition name="splash-fade">
    <div v-if="showSplash" class="splash-screen" @click="skipToHome">
      <div class="splash-container">
        <!-- 背景装饰元素 -->
        <div class="bg-decoration">
          <div class="circle circle-1"></div>
          <div class="circle circle-2"></div>
          <div class="circle circle-3"></div>
        </div>

        <!-- 主图片 -->
        <img src="../assets/images/kaiping.png" alt="Bosch Career" class="splash-image" />
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const showSplash = ref(true)

// 3秒后自动跳转到首页
onMounted(() => {
  const timer = setTimeout(() => {
    handleNavigate()
  }, 3000)

  // 组件卸载时清理定时器
  return () => clearTimeout(timer)
})

// 处理导航，添加淡出效果
const handleNavigate = () => {
  showSplash.value = false
  setTimeout(() => {
    router.push('/home')
  }, 300)
}

// Skip to home page when clicked
const skipToHome = () => {
  handleNavigate()
}
</script>

<style scoped>
.splash-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #007BC0 0%, #9E2896 50%, #37B19D 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  overflow: hidden;
  z-index: 9999;
}

.splash-container {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

/* 背景装饰元素 */
.bg-decoration {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
}

.circle {
  position: absolute;
  border-radius: 50%;
  opacity: 0.1;
  animation: float 15s infinite ease-in-out;
}

.circle-1 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.8) 0%, transparent 70%);
  top: -100px;
  left: -100px;
  animation-delay: 0s;
}

.circle-2 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.6) 0%, transparent 70%);
  bottom: -150px;
  right: -150px;
  animation-delay: 5s;
}

.circle-3 {
  width: 250px;
  height: 250px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.7) 0%, transparent 70%);
  top: 50%;
  left: 70%;
  animation-delay: 10s;
}

/* 主图片动画 */
.splash-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  z-index: 2;
  animation: imageEntrance 1.5s ease-out forwards,
             imagePulse 3s ease-in-out 1.5s infinite;
}

/* 淡出过渡 */
.splash-fade-enter-active,
.splash-fade-leave-active {
  transition: opacity 0.3s ease-out;
}

.splash-fade-leave-to {
  opacity: 0;
}

/* 动画定义 */
@keyframes imageEntrance {
  0% {
    opacity: 0;
    transform: scale(0.95);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes imagePulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.01);
  }
}

@keyframes float {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg);
  }
  33% {
    transform: translate(20px, -20px) rotate(120deg);
  }
  66% {
    transform: translate(-15px, 15px) rotate(240deg);
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