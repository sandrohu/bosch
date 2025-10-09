<template>
  <div class="splash-container">
    <!-- Background Image -->
    <div class="background-image"></div>

    <!-- Rainbow Divider Line -->
    <img src="../assets/images/rainbow.png" alt="Rainbow strip" class="rainbow-strip" />

    <!-- Logo positioned same as other pages -->
    <div class="splash-logo">
      <img src="../assets/images/splash-logo.png" alt="BOSCH" class="logo-image" />
    </div>


    <!-- Main Content -->
    <div class="splash-content">
      <!-- Chinese Title -->
      <div class="title-section">
        <h1 class="chinese-title">
          嗨～<br>
          来个博世，让精彩开始<br>
          Work #LikeABosch
        </h1>
      </div>

      <!-- Bottom Section -->
      <div class="bottom-section">
        <img src="../assets/images/tagline.png" alt="来个博世，没有难事" class="tagline-image" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
  // Auto redirect to home after 3 seconds
  setTimeout(() => {
    router.push('/home')
  }, 3000)
})
</script>

<style scoped>
.splash-container {
  width: 100%;
  height: 100vh;
  position: relative;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', sans-serif;
}

/* Background Image - 根据设计稿参数设置 */
.background-image {
  position: absolute;
  top: 0;
  left: -5.44rem;
  width: 34.25rem;
  height: 42.94rem;
  background-image: url('../assets/images/splash-bg.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 1;
  z-index: 1;
}

/* Add dark overlay for better text contrast */
.splash-container::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(180deg,
    rgba(0, 0, 0, 0.4) 0%,
    rgba(0, 0, 0, 0.2) 50%,
    rgba(0, 0, 0, 0.6) 100%
  );
  z-index: 2;
}

/* Splash Logo - same position as GlobalLogo */
.splash-logo {
  position: fixed;
  top: 1.5rem;  /* 直接从顶部开始，不需要考虑状态栏 */
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

/* Main Content */
.splash-content {
  position: relative;
  z-index: 3;
  height: calc(100vh - 120px);
  margin-top: 80px; /* 只需要避开logo区域 */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 40px 20px;
  color: white;
}

/* Title Section */
.title-section {
  margin-top: 15vh;
  animation: fadeInUp 1.2s ease-out;
}

.chinese-title {
  font-size: 32px;
  font-weight: 700;
  line-height: 1.4;
  color: white;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  letter-spacing: 1px;
}

/* Rainbow Strip - same as other pages */
.rainbow-strip {
  position: absolute;
  /* 背景图高度是42.94rem，精确定位在背景图底部 */
  top: calc(42.94rem - 4px);  /* 减去线条本身的高度 */
  left: 0;
  right: 0;
  height: 4px;
  width: 100%;
  display: block;
  object-fit: cover;
  z-index: 15;
}

/* Bottom Section */
.bottom-section {
  position: fixed;
  bottom: 95px;  /* 往上调整15px */
  left: 50%;
  transform: translateX(-50%);
  z-index: 20;
}

.tagline-image {
  width: 15.75rem;  /* 宽度 */
  height: 3.06rem;  /* 高度 */
  display: block;
  object-fit: contain;
  opacity: 0;  /* 初始透明 */
  animation: fadeInOnly 1.4s ease-out forwards;  /* 只有淡入效果 */
  animation-delay: 0.5s;  /* 延迟显示 */
}

/* Animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInOnly {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideRight {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(5px);
  }
}

/* Responsive - convert rem to responsive units */
@media (max-width: 375px) {
  .splash-logo {
    top: 1.5rem;  /* 直接从顶部开始 */
    left: 1rem;
    width: 7.25rem;
    height: 1.63rem;
  }

  .background-image {
    /* Convert rem to vw for mobile responsiveness */
    width: 91.33vw;  /* 34.25rem * 16 / 375 * 100 */
    height: 114.51vw; /* 42.94rem * 16 / 375 * 100 */
    left: -14.51vw;   /* -5.44rem * 16 / 375 * 100 */
  }

  .chinese-title {
    font-size: 28px;
  }

  .rainbow-strip {
    /* 移动端：背景图高度114.51vw */
    top: calc(114.51vw - 4px);  /* 精确对齐背景图底部 */
  }

  .bottom-section {
    /* Mobile positioning - 简单固定定位 */
    position: fixed;
    bottom: 75px;  /* 往上调整15px */
    left: 50%;
    transform: translateX(-50%);
  }

  .tagline-image {
    width: calc(15.75 * 16 / 375 * 100vw);  /* 15.75rem converted */
    height: calc(3.06 * 16 / 375 * 100vw);   /* 3.06rem converted */
  }
}

/* Tablet and Desktop */
@media (min-width: 768px) {
  .splash-logo {
    top: 1.5rem;
    left: 1.5rem;
    width: 8rem;
    height: 1.8rem;
  }

  .background-image {
    width: 548px;  /* 34.25rem * 16 */
    height: 687px; /* 42.94rem * 16 */
    left: -87px;   /* -5.44rem * 16 */
  }

  .spacer {
    height: 120px; /* 平板端彩虹线低一点 */
  }

  .splash-content {
    margin-top: 124px; /* 120px spacer + 4px rainbow */
    height: calc(100vh - 124px);
    padding: 60px 40px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  .chinese-title {
    font-size: 42px;
  }

  .rainbow-strip {
    /* 桌面端：背景图高度687px */
    top: calc(687px - 4px);  /* 精确对齐背景图底部 */
  }

  .bottom-section {
    /* 桌面端 - 固定在底部 */
    position: fixed;
    bottom: 120px;  /* 往上调整20px */
    left: 50%;
    transform: translateX(-50%);
  }

  .tagline-image {
    width: 252px;   /* 15.75rem * 16 */
    height: 49px;   /* 3.06rem * 16 */
  }
}

@media (min-width: 1024px) {
  .splash-logo {
    top: 1.5rem;
    left: 2.5rem;
    width: 9rem;
    height: 2rem;
  }

  .spacer {
    height: 140px; /* 桌面端彩虹线低一点 */
  }

  .splash-content {
    margin-top: 144px; /* 140px spacer + 4px rainbow */
    height: calc(100vh - 144px);
  }

  .background-image {
    /* Center the image on larger screens */
    left: 50%;
    transform: translateX(-50%);
    width: 548px;
    height: 687px;
  }

  .splash-content {
    max-width: 800px;
  }

  .chinese-title {
    font-size: 48px;
  }
}
</style>