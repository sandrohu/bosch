<template>
  <div class="container">
    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div> <!-- 为logo留出空间 -->
      <img src="../assets/images/rainbow.png" alt="Rainbow strip" class="rainbow-strip" />
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Bosch Headquarter Banner with Back Button -->
      <div class="headquarter-banner">
        <img src="../assets/images/bosch-cn-headquarter_res_1600x900.webp" alt="博世中国总部" class="headquarter-image" />

        <!-- 博世系列视频标题图片叠加在总部图片上 -->
        <div class="video-title-overlay">
          <img src="../assets/images/xilieshipin.png" alt="博世系列视频" class="video-title-image" />
        </div>

        <button class="back-button-overlay" @click="goBack">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
          </svg>
          <span>返回</span>
        </button>
      </div>

      <!-- Category Navigation Bar -->
      <div class="category-nav">
        <div class="nav-tabs">
          <button
            :class="['nav-tab', { active: activeTab === 'why' }]"
            @click="activeTab = 'why'"
          >
            Why Bosch ?
          </button>
          <button
            :class="['nav-tab', { active: activeTab === 'meaning' }]"
            @click="activeTab = 'meaning'"
          >
            你的工作可以多有意义
          </button>
          <button
            :class="['nav-tab', { active: activeTab === 'history' }]"
            @click="activeTab = 'history'"
          >
            过往视频汇总
          </button>
        </div>
      </div>

      <!-- Hero Video Section -->
      <div class="hero-section">
        <!-- Why Bosch 视频 -->
        <div v-show="activeTab === 'why'" class="hero-video-container">
          <video
            controls
            class="hero-video"
            preload="metadata"
            controlsList="nodownload"
          >
            <source src="/videos/whybosch.mp4" type="video/mp4">
            <p>您的浏览器不支持HTML5视频。</p>
          </video>
        </div>

        <!-- 你的工作可以多有意义 视频 -->
        <div v-show="activeTab === 'meaning'" class="hero-video-container">
          <video
            controls
            class="hero-video"
            preload="metadata"
            controlsList="nodownload"
          >
            <source src="/videos/whybosch.mp4" type="video/mp4">
            <p>您的浏览器不支持HTML5视频。</p>
          </video>
              <div class="video-info-overlay">
                <span class="video-count">89次播放</span>
                <span class="video-duration">00:16</span>
              </div>
            </div>
            <div class="video-info">
              <h3 class="video-title">博世创新与可持续发展</h3>
              <p class="video-description">
                探索博世如何通过创新技术改变世界，让每一份工作都充满意义，创造可持续的未来...
              </p>
              <div class="video-meta">
                <span class="video-date">时间：2025/05/20 14:00-16:00</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 过往视频汇总 -->
        <div v-show="activeTab === 'history'" class="hero-video-container">
          <video
            controls
            class="hero-video"
            preload="metadata"
            controlsList="nodownload"
          >
            <source src="/videos/whybosch.mp4" type="video/mp4">
            <p>您的浏览器不支持HTML5视频。</p>
          </video>
        </div>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeTab = ref('why')

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


/* Header */
.header {
  background: white;
  position: sticky;
  top: 0;
  z-index: 50;
}

.spacer {
  height: 45px;
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
  flex: 1;
  padding-bottom: 72px;
  padding-top: 0;
}

/* Headquarter Banner */
.headquarter-banner {
  width: 100%;
  margin-bottom: 0;
  position: relative;
  border-radius: 8px 8px 0 0; /* 上圆角，下直角 */
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.headquarter-image {
  width: 100%;
  height: auto;
  display: block;
}

/* Back Button Overlay */
.back-button-overlay {
  position: absolute;
  top: 16px;
  left: 16px;
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
  z-index: 10;
}

.back-button-overlay:hover {
  background: rgba(245, 245, 245, 0.9);
  border-radius: 8px;
}

/* Category Navigation Bar */
.category-nav {
  background: white;
  border-radius: 16px 16px 0 0;
  margin-top: -30px; /* 重叠高度约为导航栏高度的一半 */
  position: relative;
  z-index: 3;
  padding: 0;
  box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.08);
  min-height: 60px;
}

.nav-tabs {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 0;
  height: 60px;
}

.nav-tab {
  flex: 1;
  background: transparent;
  border: none;
  color: #666;
  font-size: 14px;
  font-weight: 400;
  padding: 20px 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  white-space: nowrap;
}

.nav-tab:hover {
  color: #333;
}

.nav-tab.active {
  color: #333;
  font-size: 16px;
  font-weight: 600;
}

/* 添加底部指示条 */
.nav-tab.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 20%;
  right: 20%;
  height: 3px;
  background: #007BC0;
  border-radius: 2px 2px 0 0;
}

/* Hero Section */
.hero-section {
  background: white;
  margin-bottom: 16px;
  margin-top: 0;
  border-radius: 0 0 16px 16px;
}

/* 视频标题叠加层 */
.video-title-overlay {
  position: absolute;
  top: 25%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 5;
  width: 80%;
  max-width: 400px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.video-title-image {
  width: 100%;
  height: auto;
  display: block;
  filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.3));
}

.hero-video-container {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  background: #000;
}

.hero-video {
  width: 100%;
  height: 100%;
  border: none;
}

/* Bottom Navigation (Mobile) */
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
    height: 60px;
  }

  .main-content {
    padding: 24px;
    max-width: 900px;
    margin: 0 auto;
  }

  .category-nav {
    border-radius: 12px 12px 0 0;
    margin-top: -35px;
    min-height: 70px;
  }

  .nav-tabs {
    height: 70px;
  }

  .nav-tab {
    font-size: 15px;
  }

  .nav-tab.active {
    font-size: 17px;
  }

  .hero-section {
    border-radius: 0 0 12px 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .video-title-overlay {
    max-width: 500px;
  }

  .headquarter-banner {
    border-radius: 12px 12px 0 0;
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

  .category-nav {
    border-radius: 16px 16px 0 0;
    margin-top: -40px;
    min-height: 80px;
  }

  .nav-tabs {
    height: 80px;
  }

  .nav-tab {
    font-size: 16px;
    padding: 25px 20px;
  }

  .nav-tab.active {
    font-size: 18px;
  }

  .hero-section {
    border-radius: 0 0 16px 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  .video-title-overlay {
    max-width: 600px;
  }

  .headquarter-banner {
    border-radius: 16px 16px 0 0;
    margin-bottom: 0;
  }

  .back-button-overlay {
    top: 24px;
    left: 24px;
    padding: 10px 16px;
    font-size: 16px;
  }
}
</style>