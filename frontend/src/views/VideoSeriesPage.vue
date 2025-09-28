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
        <h1 class="page-title">博世系列视频</h1>
        <div class="header-spacer"></div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Hero Video Section -->
      <div class="hero-section">
        <div class="hero-video-container">
          <video
            ref="heroVideo"
            :src="heroVideoData.src"
            :poster="heroVideoData.poster"
            controls
            class="hero-video"
          >
            您的浏览器不支持视频播放
          </video>
          <div class="video-overlay" v-if="!isPlaying" @click="playVideo">
            <svg class="play-icon" width="60" height="60" viewBox="0 0 60 60" fill="white">
              <circle cx="30" cy="30" r="30" fill="rgba(0,0,0,0.5)"/>
              <path d="M24 20L40 30L24 40V20Z" fill="white"/>
            </svg>
          </div>
        </div>

        <div class="hero-info">
          <div class="hero-tags">
            <span class="tag">Why Bosch ?</span>
            <span class="subtitle">你的工作可以多有意义</span>
            <span class="subtitle">过往视频汇总</span>
          </div>
        </div>
      </div>

      <!-- Video List Section -->
      <div class="video-list">
        <div
          v-for="video in videoList"
          :key="video.id"
          class="video-card"
          @click="selectVideo(video)"
        >
          <div class="video-thumbnail-container">
            <img :src="video.thumbnail" :alt="video.title" class="video-thumbnail" />
            <div class="video-play-overlay">
              <svg class="play-icon-small" width="40" height="40" viewBox="0 0 40 40" fill="white">
                <circle cx="20" cy="20" r="20" fill="rgba(255,255,255,0.9)"/>
                <path d="M16 13L28 20L16 27V13Z" fill="#007BC0"/>
              </svg>
            </div>
            <span class="video-duration">{{ video.duration }}</span>
            <span class="video-views">{{ video.views }}次播放</span>
          </div>

          <div class="video-info">
            <h3 class="video-title">{{ video.title }}</h3>
            <p class="video-description">{{ video.description }}</p>
            <div class="video-meta">
              <span class="video-date">时间：{{ video.date }}</span>
            </div>
          </div>
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
const heroVideo = ref(null)
const isPlaying = ref(false)

// 主视频数据
const heroVideoData = ref({
  src: '/videos/bosch-intro.mp4',
  poster: '/src/assets/images/video-poster.jpg',
  title: '博世系列视频'
})

// 视频列表数据
const videoList = ref([
  {
    id: 1,
    title: '国际技术交流会上海站',
    description: '博世集团董事会主席史蒂凡·哈通凡博世："中国是博世创新的重要市场和创新的关键驱动..."',
    thumbnail: '/src/assets/images/video-thumb-1.jpg',
    duration: '00:16',
    views: '51',
    date: '2025/06/12 09:00-17:00',
    src: '/videos/video1.mp4'
  },
  {
    id: 2,
    title: '博世中国创新日',
    description: '探索博世在中国的创新成果，了解最新的技术发展和未来战略...',
    thumbnail: '/src/assets/images/video-thumb-2.jpg',
    duration: '02:35',
    views: '128',
    date: '2025/05/20 14:00-16:00',
    src: '/videos/video2.mp4'
  }
])

// 播放视频
const playVideo = () => {
  if (heroVideo.value) {
    heroVideo.value.play()
    isPlaying.value = true
  }
}

// 选择视频
const selectVideo = (video) => {
  heroVideoData.value = {
    src: video.src,
    poster: video.thumbnail,
    title: video.title
  }
  isPlaying.value = false

  // 滚动到顶部
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

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

.header-content {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  background: white;
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
  padding-bottom: 90px;
}

/* Hero Section */
.hero-section {
  background: white;
  margin-bottom: 16px;
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
  object-fit: contain;
}

.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background: rgba(0, 0, 0, 0.3);
}

.play-icon {
  transition: transform 0.2s;
}

.video-overlay:hover .play-icon {
  transform: scale(1.1);
}

.hero-info {
  padding: 16px;
}

.hero-tags {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.tag {
  display: inline-block;
  padding: 4px 12px;
  background: #007BC0;
  color: white;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
}

.subtitle {
  color: #666;
  font-size: 14px;
}

/* Video List */
.video-list {
  padding: 0 16px;
}

.video-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.video-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.video-thumbnail-container {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  overflow: hidden;
}

.video-thumbnail {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.video-play-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: all 0.3s ease;
}

.video-card:hover .video-play-overlay {
  transform: translate(-50%, -50%) scale(1.1);
}

.play-icon-small {
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}

.video-duration {
  position: absolute;
  bottom: 8px;
  left: 8px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
}

.video-views {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
}

.video-info {
  padding: 12px 16px;
}

.video-title {
  font-size: 16px;
  font-weight: 600;
  color: #333;
  margin: 0 0 8px 0;
  line-height: 1.4;
}

.video-description {
  font-size: 14px;
  color: #666;
  margin: 0 0 8px 0;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.video-meta {
  font-size: 12px;
  color: #999;
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
}

.nav-label {
  font-size: 10px;
  color: #B0B0B0;
  margin-top: 2px;
  font-weight: 400;
}

/* Desktop Styles */
@media (min-width: 1024px) {
  .mobile-only {
    display: none !important;
  }

  .main-content {
    padding-bottom: 40px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .video-list {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
    padding: 0 24px;
  }

  .header-content {
    height: 80px;
    padding: 0 40px;
  }

  .page-title {
    font-size: 22px;
  }
}
</style>