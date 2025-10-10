<template>
  <div class="container">
    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div> <!-- 为logo留出空间 -->
      <img src="../assets/images/rainbow.png" alt="Rainbow strip" class="rainbow-strip" />
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Hero Banner with Fixed Image and Overlay -->
      <div class="hero-banner">
        <div class="image-wrapper">
          <img
            :src="slides[0].image"
            :alt="slides[0].alt"
            class="hero-image"
          />
        </div>
      </div>
    </main>

    <!-- White Overlay Section that extends to bottom nav -->
    <div class="white-overlay-section">
      <!-- Zhitongweilai Logo -->
      <div class="logo-container">
        <img
          src="../assets/images/zhitongweilai.png"
          alt="职通未来"
          class="overlay-logo"
        />
      </div>

      <!-- Career Images Section -->
      <div class="career-images">
        <div class="career-image-item" @click="viewDetails('campus')">
          <img src="../assets/images/zhitong-1.png" alt="校园招聘" />
        </div>
        <div class="career-image-item" @click="viewDetails('social')">
          <img src="../assets/images/zhitong-2.png" alt="社会招聘" />
        </div>
        <div class="career-image-item" @click="viewDetails('intern')">
          <img src="../assets/images/zhitong-3.png" alt="日常实习生" />
        </div>
      </div>
    </div>

    <!-- Bottom Navigation (only shown on mobile) -->
    <nav class="bottom-nav mobile-only">
      <button class="nav-item" @click="goHome">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-1-click.png" alt="首页" class="nav-icon-active" />
          <img src="../assets/images/daohang-1.png" alt="首页" class="nav-icon-default" />
        </div>
        <span class="nav-label">首页</span>
      </button>

      <button class="nav-item" @click="goEvents">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-2-click.png" alt="博世活动" class="nav-icon-active" />
          <img src="../assets/images/daohang-2.png" alt="博世活动" class="nav-icon-default" />
        </div>
        <span class="nav-label">博世活动</span>
      </button>

      <button class="nav-item active">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-3-click.png" alt="职通博世" class="nav-icon-active" />
          <img src="../assets/images/daohang-3.png" alt="职通博世" class="nav-icon-default" />
        </div>
        <span class="nav-label">职通博世</span>
      </button>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 导入轮播图图片
import lunbo1 from '../assets/images/lunbo1.jpg'

// 只使用第一张图片
const slides = ref([
  {
    image: lunbo1,
    alt: 'BOSCH 招聘 - 科技成就生活之美'
  }
])

const goHome = () => {
  router.push('/home')
}

const goEvents = () => {
  router.push('/events')
}

const viewDetails = (type) => {
  // 根据不同类型跳转到不同的详情页或外部链接
  switch(type) {
    case 'campus':
      // 校园招聘详情
      window.open('https://app.mokahr.com/campus-recruitment/bosch/73873#/', '_blank')
      break
    case 'social':
      // 社会招聘详情
      window.open('https://www.bosch.com.cn/careers/job-offers/professionals-recruitment/', '_blank')
      break
    case 'intern':
      // 实习生招聘详情
      window.open('https://www.bosch.com.cn/careers/job-offers/internship/', '_blank')
      break
  }
}
</script>

<style scoped>
.container {
  width: 100%;
  min-height: 100vh;
  background: #EDEDED;
  position: relative;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', sans-serif;
}

/* Mobile only elements */
.mobile-only {
  display: block;
}

/* Header */
.header {
  background: white;
  position: sticky;
  top: 0;
  z-index: 50;
}

.spacer {
  height: 60px; /* 增加顶部留白高度，为logo留出更多空间 */
}

.rainbow-strip {
  height: 4px;
  margin: 0;
  width: 100%;
  display: block;
  object-fit: cover;
}

/* Main Content */
.main-content {
  padding: 16px;
  padding-bottom: 0; /* Remove bottom padding as white overlay extends to bottom */
}

/* Hero Banner */
.hero-banner {
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 0; /* Remove margin as white overlay connects directly */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: relative;
}

.image-wrapper {
  position: relative;
  height: 351px;
  overflow: hidden;
  background: #f5f5f5;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* White Overlay Section that covers 1/4 of image and extends to bottom */
.white-overlay-section {
  position: relative;
  background: white;
  margin-top: -88px; /* 351px * 0.25 = ~88px to overlap 1/4 of image */
  padding-top: 20px;
  padding-bottom: 72px; /* Account for bottom nav */
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  z-index: 10;
}

.logo-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  margin-bottom: 20px;
}

.overlay-logo {
  max-width: 200px;
  height: auto;
  object-fit: contain;
}

/* Career Images Section */
.career-images {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 0 16px;
}

/* Career Image Items */
.career-image-item {
  width: 100%;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  cursor: pointer;
  background: white;
}

.career-image-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.career-image-item img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain;
}

/* Bottom Navigation */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 56px;
  background: white;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 0;
  padding-bottom: env(safe-area-inset-bottom);
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
  z-index: 100;
}

/* 中间按钮上方的梯形 - 使用SVG创建更圆润的效果 */
.bottom-nav::before {
  content: '';
  position: absolute;
  bottom: calc(100% - 1px);
  left: 50%;
  transform: translateX(-50%);
  width: 85px;
  height: 12px;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 85 12'%3E%3Cpath d='M 0 12 C 0 12 8 2 20 0 L 65 0 C 77 2 85 12 85 12 Z' fill='white'/%3E%3C/svg%3E");
  background-size: 100% 100%;
  background-repeat: no-repeat;
  filter: drop-shadow(0 -1px 3px rgba(0, 0, 0, 0.02));
}

.nav-item {
  flex: 1;
  background: none;
  border: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  padding: 8px 0;
  height: 100%;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}

/* Active indicator */
.nav-item.active::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 30px;
  height: 2px;
  background: #4A90E2;
  border-radius: 0 0 2px 2px;
}

.nav-icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  position: relative;
}

.nav-icon-default,
.nav-icon-active {
  width: 28px;
  height: 28px;
  object-fit: contain;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: opacity 0.2s ease;
}

.nav-icon-active {
  opacity: 0;
}

.nav-icon-default {
  opacity: 1;
}

.nav-label {
  font-size: 10px;
  color: #B0B0B0;
  transition: color 0.2s ease;
  margin-top: 2px;
  font-weight: 400;
}

.nav-item.active .nav-icon-active {
  opacity: 1;
}

.nav-item.active .nav-icon-default {
  opacity: 0;
}

.nav-item.active .nav-label {
  color: #4A90E2;
  font-weight: 500;
}

.nav-item:active {
  opacity: 0.7;
}

/* Tablet Styles */
@media (min-width: 768px) {
  .spacer {
    height: 60px;
  }

  .main-content {
    padding: 24px;
    padding-bottom: 72px;
    max-width: 900px;
    margin: 0 auto;
  }

  .image-wrapper {
    height: 400px;
  }

  .hero-banner {
    margin-bottom: 0;
  }

  .white-overlay-section {
    margin-top: -100px; /* 400px * 0.25 = 100px */
  }

  .career-images {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 0 24px;
  }
}

/* Desktop Styles */
@media (min-width: 1024px) {
  .mobile-only {
    display: none !important;
  }

  .spacer {
    height: 60px;
  }

  .main-content {
    padding: 40px;
    padding-bottom: 40px;
    max-width: 1200px;
  }

  .image-wrapper {
    height: 450px;
  }

  .hero-banner {
    margin-bottom: 0;
    border-radius: 20px;
  }

  .white-overlay-section {
    margin-top: -112px; /* 450px * 0.25 = ~112px */
    padding-bottom: 40px; /* No bottom nav on desktop */
  }

  .career-images {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    padding: 0 40px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .overlay-logo {
    max-width: 300px;
  }
}
</style>