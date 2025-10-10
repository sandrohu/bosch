<template>
  <div class="events-container">

    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div> <!-- 为logo留出空间 -->
      <img src="../assets/images/rainbow.png" alt="Rainbow strip" class="rainbow-strip" />
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- 博世推荐 Section -->
      <section class="recommendation-section">
        <div class="section-header">
          <h2 class="section-title">博世推荐</h2>
          <a href="#" class="view-all-link">查看全部 →</a>
        </div>

        <!-- Hero Image Card -->
        <div class="hero-card">
          <img :src="slides[currentSlide].image" :alt="slides[currentSlide].title" class="hero-image" />
          <div class="hero-overlay">
            <div class="hero-content">
              <div class="hero-info">
                <h3 class="hero-title">{{ slides[currentSlide].title }}</h3>
                <p class="hero-date">{{ slides[currentSlide].date }}</p>
              </div>
              <a href="#" class="view-details-link">查看详情 →</a>
            </div>
            <p class="hero-description">
              {{ slides[currentSlide].description }}
            </p>
            <div class="engagement-stats">
              <span class="stat-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path d="M1 21h22L12 2 1 21z" stroke-width="2"/>
                </svg>
                1.5w
              </span>
              <span class="stat-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3" stroke-width="2"/>
                </svg>
                1.5w
              </span>
              <span class="stat-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" stroke-width="2"/>
                </svg>
                1.5w
              </span>
            </div>
          </div>
        </div>

        <!-- Carousel Dots -->
        <div class="carousel-dots">
          <span v-for="(slide, index) in slides"
                :key="slide.id"
                :class="['dot', { active: currentSlide === index }]"
                @click="goToSlide(index)"></span>
        </div>
      </section>

      <!-- Activity Cards -->
      <section class="activity-cards-section">
        <div class="activity-card">
          <img src="../assets/images/activity-1.png" alt="活动1" class="activity-image" />
        </div>
        <div class="activity-card">
          <img src="../assets/images/activity-2.png" alt="活动2" class="activity-image" />
        </div>
        <div class="activity-card">
          <img src="../assets/images/activity-3.png" alt="活动3" class="activity-image" />
        </div>
      </section>

      <!-- Bottom Navigation -->
      <nav class="bottom-nav">
        <button class="nav-item" @click="navigateToHome">
          <div class="nav-icon-wrapper">
            <img src="../assets/images/daohang-1-click.png" alt="首页" class="nav-icon-active" />
            <img src="../assets/images/daohang-1.png" alt="首页" class="nav-icon-default" />
          </div>
          <span>首页</span>
        </button>
        <button class="nav-item active">
          <div class="nav-icon-wrapper">
            <img src="../assets/images/daohang-2-click.png" alt="博世活动" class="nav-icon-active" />
            <img src="../assets/images/daohang-2.png" alt="博世活动" class="nav-icon-default" />
          </div>
          <span>博世活动</span>
        </button>
        <button class="nav-item" @click="navigateToCareers">
          <div class="nav-icon-wrapper">
            <img src="../assets/images/daohang-3-click.png" alt="职通博世" class="nav-icon-active" />
            <img src="../assets/images/daohang-3.png" alt="职通博世" class="nav-icon-default" />
          </div>
          <span>职通博世</span>
        </button>
      </nav>
    </main>
  </div>
</template>

<script>
import xunhuiImage from '../assets/images/xunhuixuanjiang.jpg'
import boschHeadquarterImage from '../assets/images/bosch-cn-headquarter_res_1600x900.webp'

export default {
  name: 'EventsPage',
  data() {
    return {
      currentSlide: 0,
      slides: [
        {
          id: 1,
          title: '博士生论坛',
          date: '07-09-2025',
          image: xunhuiImage,
          description: '人工智能领域的突破开启了技术发展的新篇章，加速创新及其商业转化。博世集团董事会主席哈通博士表示...'
        },
        {
          id: 2,
          title: '校园巡回宣讲会',
          date: '15-09-2025',
          image: xunhuiImage,
          description: '博世2025秋季校园巡回宣讲会即将开启，走进全国重点高校，为同学们带来最新的职业发展机会和行业前沿资讯...'
        },
        {
          id: 3,
          title: '运动嘉年华',
          date: '20-10-2025',
          image: boschHeadquarterImage,
          description: '博世运动嘉年华活动，汇聚各类体育项目，展现博世员工的活力与激情，促进团队协作与健康生活方式...'
        }
      ],
      autoPlayTimer: null
    }
  },
  mounted() {
    // 启动自动轮播
    this.startAutoPlay()
  },
  beforeUnmount() {
    // 清理定时器
    if (this.autoPlayTimer) {
      clearInterval(this.autoPlayTimer)
    }
  },
  methods: {
    viewDetails(type) {
      console.log('View details for:', type)
    },
    navigateToHome() {
      this.$router.push('/home')
    },
    navigateToCareers() {
      this.$router.push('/careers')
    },
    // 切换到指定轮播图
    goToSlide(index) {
      this.currentSlide = index
      // 重置自动播放
      this.resetAutoPlay()
    },
    // 切换到下一张
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length
    },
    // 切换到上一张
    prevSlide() {
      this.currentSlide = (this.currentSlide - 1 + this.slides.length) % this.slides.length
    },
    // 启动自动播放
    startAutoPlay() {
      this.autoPlayTimer = setInterval(() => {
        this.nextSlide()
      }, 5000) // 每5秒切换一次
    },
    // 重置自动播放
    resetAutoPlay() {
      if (this.autoPlayTimer) {
        clearInterval(this.autoPlayTimer)
      }
      this.startAutoPlay()
    }
  }
}
</script>

<style scoped>
.events-container {
  min-height: 100vh;
  background-color: #f5f5f5;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
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
  padding-bottom: 72px; /* 56px + some margin */
}

/* Recommendation Section */
.recommendation-section {
  margin-bottom: 30px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.section-title {
  font-size: 20px;
  font-weight: 600;
  color: #333;
  margin: 0;
}

.view-all-link {
  color: #666;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s;
}

.view-all-link:hover {
  color: #DA291C;
}

/* Hero Card */
.hero-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  margin-bottom: 15px;
}

.hero-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.hero-overlay {
  padding: 20px;
}

.hero-content {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}

.hero-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin: 0 0 5px 0;
}

.hero-date {
  color: #999;
  font-size: 14px;
  margin: 0;
}

.view-details-link {
  color: #DA291C;
  text-decoration: none;
  font-size: 14px;
  white-space: nowrap;
}

.hero-description {
  color: #666;
  font-size: 14px;
  line-height: 1.5;
  margin-bottom: 15px;
}

.engagement-stats {
  display: flex;
  gap: 20px;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 5px;
  color: #999;
  font-size: 14px;
}

.stat-item svg {
  width: 16px;
  height: 16px;
}

/* Carousel Dots */
.carousel-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 15px;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ddd;
  cursor: pointer;
  transition: background 0.3s;
}

.dot.active {
  background: #DA291C;
}

/* Activity Cards */
.activity-cards-section {
  display: flex;
  gap: 12px;
  margin-bottom: 30px;
  margin-top: 20px;
  width: 100%;
}

.activity-card {
  flex: 1;
  min-width: 0; /* 允许flex子项缩小到内容以下 */
  background: transparent; /* 去掉白色背景 */
  border-radius: 0; /* 去掉圆角边框 */
  overflow: visible; /* 允许内容完整显示 */
  box-shadow: none; /* 去掉阴影边框 */
  transition: all 0.3s ease;
  cursor: pointer;
  /* 移除 aspect-ratio 以允许图片自适应 */
}

.activity-card:hover {
  transform: translateY(-4px);
  /* 保持hover效果但不添加阴影 */
}

.activity-image {
  width: 100%;
  height: auto; /* 改为auto让高度自适应 */
  object-fit: contain; /* 确保图片完整显示 */
  display: block;
  /* 去掉白色背景 */
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
  text-decoration: none;
  color: #B0B0B0;
}

.nav-item.active {
  color: #4A90E2;
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

.nav-item span {
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

.nav-item.active span {
  color: #4A90E2;
  font-weight: 500;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .main-content {
    padding: 15px;
  }

  .activity-cards-section {
    display: flex;
    flex-direction: row;
    gap: 8px;
    width: 100%;
  }

  .activity-card {
    flex: 1;
    width: auto;
    height: auto;
  }
}

/* Extra small screens */
@media (max-width: 480px) {
  .activity-cards-section {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .activity-card {
    width: 100%;
    height: auto;
  }
}

/* Desktop Responsive */
@media (min-width: 769px) {
  .status-bar.mobile-only {
    display: none;
  }

  .header {
    position: sticky;
    top: 0;
  }

  .spacer {
    height: 60px; /* 桌面端为logo留更多空间 */
  }

  .main-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px;
  }

  .hero-image {
    height: 300px;
  }

  .activity-cards-section {
    gap: 20px;
  }

  .activity-card {
    height: auto; /* 改为auto让高度自适应 */
  }

  .bottom-nav {
    display: none;
  }
}
</style>