<template>
  <div class="splash-container">
    <!-- Background Image -->
    <div class="background-image"></div>

    <!-- Rainbow Divider Line -->
    <div class="rainbow-divider"></div>

    <!-- Mobile Status Bar -->
    <div class="status-bar mobile-only">
      <span class="time">9:41</span>
      <div class="status-icons">
        <svg width="17" height="12" viewBox="0 0 17 12" fill="none">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M1 0H0V1H1V0Z" fill="white"/>
        </svg>
        <svg width="15" height="11" viewBox="0 0 15 11" fill="none">
          <path d="M0 0H15V11H0V0Z" fill="white" fill-opacity="0.8"/>
        </svg>
        <svg width="25" height="12" viewBox="0 0 25 12" fill="none">
          <rect opacity="0.35" x="0.5" y="0.5" width="21" height="11" rx="2.5" stroke="white"/>
          <path opacity="0.4" d="M22 4V8C22.8 7.66 23.5 6.5 23.5 6C23.5 5.5 22.8 4.34 22 4Z" fill="white"/>
          <rect x="2" y="2" width="18" height="8" rx="1" fill="white"/>
        </svg>
      </div>
    </div>

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

/* Mobile Status Bar */
.mobile-only {
  display: block;
}

.status-bar {
  height: 44px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 21px;
  position: relative;
  z-index: 10;
}

.time {
  font-size: 15px;
  font-weight: 600;
  color: white;
  letter-spacing: -0.3px;
}

.status-icons {
  display: flex;
  gap: 5px;
  align-items: center;
}

/* Splash Logo - same position as GlobalLogo */
.splash-logo {
  position: fixed;
  top: 3.25rem;  /* 状态栏高度 + 一些间距 */
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

/* Rainbow Divider Line */
.rainbow-divider {
  position: absolute;
  /* 背景图高度是42.94rem，精确定位在背景图底部 */
  top: calc(42.94rem - 4px);  /* 减去线条本身的高度 */
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg,
    #E60012 0%,
    #F39800 14.28%,
    #FFF100 28.57%,
    #8FC31F 42.86%,
    #00A0E9 57.14%,
    #0068B7 71.43%,
    #920783 85.71%,
    #E4007F 100%
  );
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
    top: 2.75rem;  /* 44px状态栏 + 间距 */
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

  .rainbow-divider {
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

  .rainbow-divider {
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
  .mobile-only {
    display: none;
  }

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