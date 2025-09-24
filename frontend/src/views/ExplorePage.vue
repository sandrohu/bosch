<template>
  <div class="explore-container">
    <!-- Mobile Status Bar -->
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
      <div class="spacer"></div>
      <div class="rainbow-strip"></div>
    </header>

    <!-- Page Title -->
    <div class="page-title">
      <button @click="goBack" class="back-button">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M15 18L9 12L15 6" stroke="#333" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <h1>全景探索</h1>
      <div class="title-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="#4A90E2">
          <path d="M19 3H5C3.89 3 3 3.89 3 5V19C3 20.11 3.89 21 5 21H19C20.11 21 21 20.11 21 19V5C21 3.89 20.11 3 19 3M19 19H5V5H19V19Z"/>
        </svg>
      </div>
    </div>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Hero Section -->
      <div class="hero-section">
        <div class="hero-card">
          <div class="hero-header">
            <h2 class="hero-title">全景探索，来个博世</h2>
            <div class="header-right">
              <img src="../assets/images/zhedie-logo-1.png" alt="BOSCH" class="bosch-logo" />
              <button class="collapse-button" @click="toggleCollapse">
                <span>{{ isCollapsed ? '展开' : '收回' }}</span>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="white">
                  <path :d="isCollapsed ? 'M4 10L8 6L12 10' : 'M4 6L8 10L12 6'" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </div>

          <div class="hero-image" v-show="!isCollapsed">
            <img src="../assets/images/bosch-campus.jpg" alt="博世园区" />
          </div>

          <div class="hero-content" v-show="!isCollapsed">
            <p class="description">
              博世集团于1909年首次进入中国市场，开设了第一家贸易办事处。1926年，博世在上海创建了首家汽车售后服务车间。在过去的112年里，博世见证了中国社会日新月异的变化——无其是改革开放以来经济的迅速崛起。博世集团秉承"根植本土、服务本土"的理念，深度融入了中国经济的发展。与中国市场共同成长。现在，博世为中国市场和用户提供...
              <span class="expand-icon">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="#4A90E2">
                  <path d="M4 5L8 9L12 5" stroke="#4A90E2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
            </p>
          </div>

          <div class="hero-footer" v-show="!isCollapsed">
            <button class="intro-button">
              <span>博世整体介绍</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="white">
                <path d="M12 10L8 6L8 14L12 10Z" transform="rotate(-90 10 10)" fill="white"/>
              </svg>
            </button>
            <button class="video-button">
              <span>博世系列视频</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="#4A90E2">
                <path d="M8 5V15L15 10L8 5Z" fill="#4A90E2"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Feature Cards -->
      <div class="feature-cards">
        <!-- Card 1: 引力解码 -->
        <div class="feature-card card-gravity">
          <div class="card-content">
            <h3 class="card-title">引力解码，来个博世</h3>
            <p class="card-subtitle">博世引力场 雇主价值主张</p>
          </div>
          <button class="card-button">
            查看详情
            <img src="../assets/images/click.png" alt="" class="card-click-icon" />
          </button>
        </div>

        <!-- Card 2: 热文追踪 -->
        <div class="feature-card card-news">
          <div class="card-content">
            <h3 class="card-title">热文追踪，来个博世</h3>
            <p class="card-subtitle">博世新闻事件</p>
          </div>
          <button class="card-button">
            查看详情
            <img src="../assets/images/click.png" alt="" class="card-click-icon" />
          </button>
        </div>
      </div>
    </main>

    <!-- Bottom Navigation -->
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
const isCollapsed = ref(false)

const toggleCollapse = () => {
  isCollapsed.value = !isCollapsed.value
}

const goBack = () => {
  router.back()
}

const goHome = () => {
  router.push('/home')
}
</script>

<style scoped>
.explore-container {
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

/* Status Bar */
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
  z-index: 50;
}

.spacer {
  height: 60px;
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

/* Page Title */
.page-title {
  background: white;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #E5E5E5;
}

.back-button {
  background: none;
  border: none;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.page-title h1 {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  flex: 1;
  text-align: center;
}

.title-icon {
  width: 24px;
  height: 24px;
}

/* Main Content */
.main-content {
  padding: 16px;
  padding-bottom: 90px;
}

/* Hero Section */
.hero-section {
  margin-bottom: 16px;
}

.hero-card {
  background: linear-gradient(135deg, #5E9FD8 0%, #91C2F2 100%);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.hero-header {
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.hero-title {
  font-size: 22px;
  font-weight: 600;
  color: white;
}

.header-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
}

.bosch-logo {
  width: 105px;
  height: 22px;
  object-fit: contain;
}

.collapse-button {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 16px;
  padding: 6px 12px;
  color: white;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.collapse-button:hover {
  background: rgba(255, 255, 255, 0.3);
}

.hero-image {
  margin: 0 20px;
  border-radius: 12px;
  overflow: hidden;
  height: 200px;
  background: #f0f0f0;
}

.hero-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-content {
  padding: 20px;
}

.description {
  font-size: 14px;
  line-height: 1.6;
  color: white;
  position: relative;
}

.expand-icon {
  display: inline-block;
  margin-left: 4px;
  vertical-align: middle;
}

.hero-footer {
  padding: 0 20px 20px;
  display: flex;
  gap: 12px;
}

.intro-button,
.video-button {
  flex: 1;
  background: rgba(255, 255, 255, 0.25);
  border: none;
  border-radius: 20px;
  padding: 10px 16px;
  font-size: 14px;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.intro-button {
  color: white;
}

.video-button {
  background: white;
  color: #4A90E2;
}

/* Feature Cards */
.feature-cards {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.feature-card {
  border-radius: 16px;
  padding: 24px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s ease;
  cursor: pointer;
  height: 102px;
  position: relative;
  overflow: visible;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

.feature-card:first-child {
  margin-bottom: -8px;
  z-index: 2;
}

.feature-card:last-child {
  padding-top: 32px;
  z-index: 1;
}

.feature-card:hover {
  transform: translateY(-2px);
  z-index: 10 !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.card-gravity {
  background: linear-gradient(135deg, #9E2896 0%, #C29FFF 100%);
}

.card-news {
  background: linear-gradient(135deg, #37B19D 0%, #7AE3D1 100%);
}

.card-content {
  flex: 1;
}

.card-title {
  font-size: 20px;
  font-weight: 600;
  color: white;
  margin-bottom: 8px;
  line-height: 1.3;
}

.card-subtitle {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.4;
}

.card-button {
  background: rgba(255, 255, 255, 0.25);
  border: none;
  border-radius: 20px;
  padding: 10px 18px;
  color: white;
  font-size: 16px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: background 0.2s ease;
  position: relative;
}

.card-click-icon {
  position: absolute;
  bottom: -10px;
  right: -10px;
  width: 33px;
  height: 32px;
  object-fit: contain;
  z-index: 2;
  pointer-events: none;
}

.card-button:hover {
  background: rgba(255, 255, 255, 0.35);
}

/* Bottom Navigation */
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

/* Tablet and Desktop styles */
@media (min-width: 768px) {
  .main-content {
    padding: 24px;
    max-width: 900px;
    margin: 0 auto;
  }

  .hero-image {
    height: 300px;
  }

  .hero-title {
    font-size: 26px;
  }

  .description {
    font-size: 16px;
  }
}

@media (min-width: 1024px) {
  .mobile-only {
    display: none !important;
  }

  .header {
    position: sticky;
    top: 0;
  }

  .spacer {
    height: 80px;
  }

  .main-content {
    padding: 40px;
    padding-bottom: 40px;
    max-width: 1200px;
  }

  .hero-image {
    height: 400px;
  }

  .page-title {
    padding: 16px 40px;
  }

  .page-title h1 {
    font-size: 22px;
  }
}
</style>