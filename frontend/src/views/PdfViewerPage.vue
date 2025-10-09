<template>
  <div class="container">

    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div> <!-- 为logo留出空间 -->
      <img src="../assets/images/rainbow.png" alt="Rainbow strip" class="rainbow-strip" />
      <div class="header-content">
        <button class="back-button" @click="goBack">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
          </svg>
          <span>返回</span>
        </button>
        <h1 class="page-title">博世整体介绍</h1>
        <div class="header-spacer"></div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <div class="pdf-container">
        <!-- 使用ImageViewer组件显示图片 -->
        <ImageViewer />
      </div>
    </main>

    <!-- Bottom Navigation (only shown on mobile) -->
    <nav class="bottom-nav mobile-only">
      <button class="nav-item" @click="navigateToHome">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-1-click.png" alt="首页" class="nav-icon-active" />
          <img src="../assets/images/daohang-1.png" alt="首页" class="nav-icon-default" />
        </div>
        <span class="nav-label">首页</span>
      </button>

      <button class="nav-item" @click="navigateToEvents">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-2-click.png" alt="博世活动" class="nav-icon-active" />
          <img src="../assets/images/daohang-2.png" alt="博世活动" class="nav-icon-default" />
        </div>
        <span class="nav-label">博世活动</span>
      </button>

      <button class="nav-item" @click="navigateToCareers">
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
import { useRouter } from 'vue-router'
import ImageViewer from '../components/ImageViewer.vue'

const router = useRouter()


const goBack = () => {
  router.back()
}

const navigateToHome = () => {
  router.push('/home')
}

const navigateToEvents = () => {
  router.push('/events')
}

const navigateToCareers = () => {
  router.push('/careers')
}
</script>

<style scoped>
.container {
  width: 100%;
  min-height: 100vh;
  background: #EDEDED;
  position: relative;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', sans-serif;
  display: flex;
  flex-direction: column;
}

/* Mobile only elements */
.mobile-only {
  display: block;
}

.desktop-only {
  display: none;
}


/* Header */
.header {
  background: white;
  position: sticky;
  top: 0;
  z-index: 50; /* 低于logo的z-index */
}

.spacer {
  height: 60px; /* 统一为logo留出空间，与首页保持一致 */
}

.rainbow-strip {
  height: 4px;
  margin: 0;
  width: 100%;
  display: block;
  object-fit: cover;
}

.header-content {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
}

.back-button {
  background: transparent;
  border: none;
  padding: 8px 12px;
  color: #333;
  font-size: 14px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.back-button:hover {
  background: #f5f5f5;
  border-radius: 8px;
}

.back-button:active {
  background: #ececec;
  border-radius: 8px;
}

.page-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin: 0;
}

.header-spacer {
  width: 80px;
}


/* Main Content */
.main-content {
  flex: 1;
  padding: 16px;
  padding-bottom: 72px;
  display: flex;
  flex-direction: column;
}

.pdf-container {
  flex: 1;
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
}

/* Bottom Navigation (Mobile) - 与首页完全一致 */
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

.nav-item.active .nav-icon-active {
  opacity: 1;
}

.nav-item.active .nav-icon-default {
  opacity: 0;
}

.nav-label {
  font-size: 10px;
  color: #B0B0B0;
  transition: color 0.2s ease;
  margin-top: 2px;
  font-weight: 400;
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
    height: 60px; /* 统一高度 */
  }

  .main-content {
    padding: 24px;
    padding-bottom: 90px;
  }

  .header-content {
    height: 70px;
    padding: 0 24px;
  }

  .page-title {
    font-size: 20px;
  }

  .back-button {
    padding: 10px 16px;
    font-size: 15px;
  }

  .pdf-container {
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
  }

  .pdf-iframe {
    min-height: calc(100vh - 220px);
  }
}

/* Desktop Styles */
@media (min-width: 1024px) {
  .spacer {
    height: 60px; /* 统一高度 */
  }

  /* Hide mobile elements */
  .mobile-only {
    display: none !important;
  }

  .desktop-only {
    display: flex !important;
  }

  .header-content {
    height: 80px;
    padding: 0 40px;
  }

  .page-title {
    font-size: 22px;
  }

  .main-content {
    padding: 40px;
    padding-bottom: 40px;
  }

  .pdf-container {
    max-width: 1400px;
  }

  .pdf-iframe {
    min-height: calc(100vh - 180px);
  }
}

/* Large Desktop */
@media (min-width: 1440px) {
  .header-content {
    height: 90px;
    padding: 0 60px;
  }

  .main-content {
    padding: 50px 60px;
  }

  .pdf-container {
    max-width: 1600px;
  }
}
</style>