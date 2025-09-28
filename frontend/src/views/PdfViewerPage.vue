<template>
  <div class="container">
    <!-- Mobile Status Bar (only shown on mobile) -->
    <div class="status-bar mobile-only">
      <span class="time">9:41</span>
      <div class="status-icons">
        <svg width="17" height="12" viewBox="0 0 17 12" fill="none">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M1 0H0V1H1V0Z" fill="black"/>
        </svg>
        <svg width="15" height="11" viewBox="0 0 15 11" fill="none">
          <path d="M0 0H15V11H0V0Z" fill="black" fill-opacity="0.35"/>
        </svg>
        <svg width="25" height="12" viewBox="0 0 25 12" fill="none">
          <rect opacity="0.35" x="0.5" y="0.5" width="21" height="11" rx="2.5" stroke="black"/>
          <path opacity="0.4" d="M22 4V8C22.8 7.66 23.5 6.5 23.5 6C23.5 5.5 22.8 4.34 22 4Z" fill="black"/>
          <rect x="2" y="2" width="18" height="8" rx="1" fill="black"/>
        </svg>
      </div>
    </div>

    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div> <!-- 为logo留出空间 -->
      <div class="rainbow-strip"></div>
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
      <button class="nav-item" @click="goHome">
        <div class="nav-icon-wrapper">
          <svg class="nav-icon" width="28" height="28" viewBox="0 0 28 28" fill="currentColor">
            <path d="M11.5 23v-7h5v7h6.25v-9.5H26L14 2.5 2 13.5h3.25v9.5z"/>
          </svg>
        </div>
        <span class="nav-label">首页</span>
      </button>

      <button class="nav-item">
        <div class="nav-icon-wrapper">
          <svg class="nav-icon" width="28" height="28" viewBox="0 0 28 28" fill="currentColor">
            <rect x="4" y="6" width="20" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/>
            <rect x="7" y="3" width="3" height="6" rx="1" fill="currentColor"/>
            <rect x="18" y="3" width="3" height="6" rx="1" fill="currentColor"/>
            <line x1="8" y1="11" x2="20" y2="11" stroke="currentColor" stroke-width="1.5"/>
            <line x1="8" y1="15" x2="20" y2="15" stroke="currentColor" stroke-width="1.5"/>
            <line x1="8" y1="19" x2="16" y2="19" stroke="currentColor" stroke-width="1.5"/>
          </svg>
        </div>
        <span class="nav-label">博世活动</span>
      </button>

      <button class="nav-item">
        <div class="nav-icon-wrapper">
          <svg class="nav-icon" width="28" height="28" viewBox="0 0 28 28" fill="currentColor">
            <rect x="5" y="8" width="18" height="14" rx="1" fill="none" stroke="currentColor" stroke-width="2"/>
            <path d="M9 8V6a5 5 0 0 1 10 0v2" fill="none" stroke="currentColor" stroke-width="2"/>
            <circle cx="14" cy="15" r="2" fill="currentColor"/>
            <path d="M14 17v3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
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

const goHome = () => {
  router.push('/home')
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

/* Status Bar (Mobile) */
.status-bar {
  height: 44px;
  background: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 21px;
}

.time {
  font-size: 15px;
  font-weight: 600;
  color: #000;
  letter-spacing: -0.3px;
}

.status-icons {
  display: flex;
  gap: 5px;
  align-items: center;
}

/* Header */
.header {
  background: white;
  position: sticky;
  top: 0;
  z-index: 50; /* 低于logo的z-index */
}

.spacer {
  height: 60px; /* 为logo留出空间 */
}

.rainbow-strip {
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
  width: 100%;
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
  padding-bottom: 90px;
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

/* Bottom Navigation (Mobile) */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 73px;
  background: white;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 0;
  padding-bottom: env(safe-area-inset-bottom);
  box-shadow: 0 -1px 0 0 rgba(0, 0, 0, 0.08);
  z-index: 100;
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

.nav-icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
}

.nav-icon {
  width: 28px;
  height: 28px;
  color: #B0B0B0;
  transition: color 0.2s ease;
}

.nav-label {
  font-size: 10px;
  color: #B0B0B0;
  transition: color 0.2s ease;
  margin-top: 2px;
  font-weight: 400;
}

.nav-item:active {
  opacity: 0.7;
}

/* Tablet Styles */
@media (min-width: 768px) {
  .spacer {
    height: 70px; /* 平板端为logo留更多空间 */
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
    height: 80px; /* 桌面端为logo留更多空间 */
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