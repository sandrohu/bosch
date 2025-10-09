<template>
  <div class="news-list-container">
    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div>
      <img src="../assets/images/rainbow.png" alt="Rainbow strip" class="rainbow-strip" />
      <div class="header-content">
        <button class="back-button" @click="goBack">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
          </svg>
          <span>返回</span>
        </button>
        <div class="header-spacer"></div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- News List Banner Image -->
      <div class="banner-image-container">
        <img src="../assets/images/news-list.png" alt="热文追踪" class="banner-image" />
      </div>

      <!-- News List -->
      <div class="news-list">
        <article
          v-for="(news, index) in newsList"
          :key="index"
          class="news-item"
          @click="goToDetail(index)"
        >
          <div class="news-image">
            <img :src="news.image" :alt="news.title" />
          </div>
          <div class="news-content">
            <div class="news-meta">
              <span class="news-category">{{ news.category }}</span>
              <span class="news-date">{{ news.date }}</span>
            </div>
            <h2 class="news-title">{{ news.title }}</h2>
            <p class="news-excerpt">{{ news.content }}</p>
          </div>
        </article>
      </div>
    </main>

    <!-- Bottom Navigation (Mobile Only) -->
    <nav class="bottom-nav mobile-only">
      <a href="/home" class="nav-item">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-1-click.png" alt="首页" class="nav-icon-active" />
          <img src="../assets/images/daohang-1.png" alt="首页" class="nav-icon-default" />
        </div>
        <span>首页</span>
      </a>
      <a href="/events" class="nav-item">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-2-click.png" alt="博世活动" class="nav-icon-active" />
          <img src="../assets/images/daohang-2.png" alt="博世活动" class="nav-icon-default" />
        </div>
        <span>博世活动</span>
      </a>
      <a href="/careers" class="nav-item">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-3-click.png" alt="职通博世" class="nav-icon-active" />
          <img src="../assets/images/daohang-3.png" alt="职通博世" class="nav-icon-default" />
        </div>
        <span>职通博世</span>
      </a>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const newsList = ref([
  {
    image: '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._0.png',
    category: '企业荣誉',
    date: '2025-09-28',
    title: '2025福布斯中国最佳雇主，我们上榜啦！',
    content: '博世荣获福布斯2025「中国年度最佳雇主」及「年度最佳ESG实践雇主」，这份荣誉属于每一位敢拼敢闯的博世人。'
  },
  {
    image: '/src/assets/file/article2/image_博世投入25亿欧元发力AI，事关..._0.png',
    category: '技术创新',
    date: '2025-09-25',
    title: '博世投入25亿欧元发力AI，事关你我未来生活',
    content: '博世投入25亿欧元发力AI，1500+欧洲专利加持，让自动驾驶更安全、制造质量更可靠、日常生活更便利。'
  },
  {
    image: '/src/assets/images/bosch-cn-headquarter_res_1600x900.webp',
    category: '可持续发展',
    date: '2025-09-20',
    title: '博世中国区实现碳中和目标，引领行业绿色转型',
    content: '博世在中国的所有工厂已全面实现碳中和，成为行业绿色转型的典范，推动可持续发展。'
  },
  {
    image: '/src/assets/images/mobility-solutions-web-portal_res_1280x720.webp',
    category: '产品发布',
    date: '2025-09-15',
    title: '博世推出新一代智能驾驶辅助系统',
    content: '全新智能驾驶辅助系统搭载先进传感器技术，为用户提供更安全、更智能的驾驶体验。'
  },
  {
    image: '/src/assets/images/jump.jpg',
    category: '校园招聘',
    date: '2025-09-10',
    title: '2025博世中国秋季校园招聘全面启动',
    content: '博世中国2025秋季校园招聘正式开启，诚邀优秀学子加入，共创美好未来。'
  }
])

const goBack = () => {
  router.back()
}

const goToDetail = (index) => {
  router.push(`/news-detail/${index}`)
}
</script>

<style scoped>
.news-list-container {
  min-height: 100vh;
  background-color: #f5f5f5;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
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
  height: 60px;
}

.rainbow-strip {
  height: 4px;
  margin: 0;
  width: 100%;
  display: block;
  object-fit: cover;
}

/* Header Content */
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

.header-spacer {
  width: 80px;
}

/* Main Content */
.main-content {
  padding: 16px;
  padding-bottom: 72px;
}

/* Banner Image */
.banner-image-container {
  width: 100%;
  margin-bottom: 20px;
}

.banner-image {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}

/* News List */
.news-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.news-item {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.news-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

.news-item:active {
  transform: scale(0.98);
}

.news-image {
  width: 100%;
  height: 160px; /* 降低高度 */
  overflow: hidden;
}

.news-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.news-content {
  padding: 16px;
}

.news-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
}

.news-category {
  background: #5AA397;
  color: white;
  padding: 3px 10px;
  border-radius: 10px;
  font-size: 11px;
  font-weight: 500;
}

.news-date {
  color: #999;
  font-size: 11px;
}

.news-title {
  font-size: 16px;
  font-weight: 600;
  color: #333;
  line-height: 1.3;
  margin-bottom: 8px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.news-excerpt {
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
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
  text-decoration: none;
  color: #B0B0B0;
}

.nav-item.active {
  color: #4A90E2;
}

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

.nav-item span {
  font-size: 10px;
  transition: color 0.2s ease;
  margin-top: 2px;
  font-weight: 400;
}

.nav-item.active span {
  color: #4A90E2;
  font-weight: 500;
}

/* Tablet Styles */
@media (min-width: 768px) {
  .main-content {
    padding: 24px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .header-content {
    height: 70px;
    padding: 0 24px;
  }

  .back-button {
    padding: 10px 16px;
    font-size: 15px;
  }

  .banner-image-container {
    margin-bottom: 30px;
  }

  .news-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 24px;
  }

  .news-image {
    height: 180px;
  }

  .news-content {
    padding: 20px;
  }

  .news-title {
    font-size: 18px;
  }

  .news-excerpt {
    font-size: 14px;
  }
}

/* Desktop Styles */
@media (min-width: 1024px) {
  .mobile-only {
    display: none !important;
  }

  .header-content {
    height: 80px;
    padding: 0 40px;
  }

  .main-content {
    padding: 40px;
    padding-bottom: 40px;
    max-width: 1400px;
  }

  .banner-image-container {
    margin-bottom: 40px;
  }

  .news-list {
    gap: 30px;
  }

  .news-image {
    height: 200px;
  }

  .news-item {
    border-radius: 16px;
  }

  .news-title {
    font-size: 20px;
    margin-bottom: 10px;
  }

  .news-excerpt {
    font-size: 15px;
    -webkit-line-clamp: 3;
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
    max-width: 1600px;
  }

  .news-list {
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
    gap: 40px;
  }
}
</style>