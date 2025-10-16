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

        <!-- 跳过提示 -->
        <div class="skip-hint">点击跳过</div>

        <!-- 进度条 -->
        <div class="progress-bar">
          <div class="progress-fill"></div>
        </div>
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
  animation: imageEntrance 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards,
             imagePulse 2s ease-in-out 1.2s infinite;
}

/* 跳过提示 */
.skip-hint {
  position: absolute;
  bottom: 100px;
  right: 30px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  padding: 8px 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.1);
  z-index: 3;
  animation: fadeInUp 0.8s ease-out 0.5s both;
  transition: all 0.3s ease;
}

.skip-hint:hover {
  background: rgba(255, 255, 255, 0.2);
  color: rgba(255, 255, 255, 0.9);
}

/* 进度条 */
.progress-bar {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 3px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
  overflow: hidden;
  z-index: 3;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #fff 0%, #fff 100%);
  border-radius: 3px;
  animation: progressAnimation 3s linear forwards;
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
    transform: scale(0.8) translateY(20px);
  }
  60% {
    opacity: 1;
    transform: scale(1.05) translateY(-5px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

@keyframes imagePulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.02);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg);
  }
  33% {
    transform: translate(30px, -30px) rotate(120deg);
  }
  66% {
    transform: translate(-20px, 20px) rotate(240deg);
  }
}

@keyframes progressAnimation {
  from {
    width: 0%;
  }
  to {
    width: 100%;
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