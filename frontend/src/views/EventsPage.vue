<template>
  <div class="events-container">

    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div> <!-- 为logo留出空间 -->
      <div class="rainbow-strip"></div>
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
          <img src="../assets/images/bosch-cn-headquarter_res_1600x900.webp" alt="博世园区" class="hero-image" />
          <div class="hero-overlay">
            <div class="hero-content">
              <div class="hero-info">
                <h3 class="hero-title">博士生论坛</h3>
                <p class="hero-date">07-09-2025</p>
              </div>
              <a href="#" class="view-details-link">查看详情 →</a>
            </div>
            <p class="hero-description">
              人工智能领域的突破开启了技术发展的新篇章，加速创新及其商业转化。博世集团董事会主席哈通博士表示...
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
          <span class="dot active"></span>
          <span class="dot"></span>
          <span class="dot"></span>
        </div>
      </section>

      <!-- Event Categories -->
      <section class="categories-section">
        <!-- 校园巡回宣讲会 -->
        <div class="category-card campus-tour">
          <div class="card-header">
            <h3 class="card-title">校园巡回宣讲会</h3>
            <p class="card-subtitle">即将开启 3 场宣讲会</p>
          </div>
          <div class="card-illustration">
            <svg class="presenter-icon" width="120" height="120" viewBox="0 0 120 120">
              <circle cx="60" cy="40" r="20" fill="#E0E7FF"/>
              <path d="M30 70 Q30 60 60 60 Q90 60 90 70 L90 100 L30 100 Z" fill="#6B7FCC"/>
              <rect x="55" y="60" width="10" height="30" fill="#4B5CC4"/>
              <circle cx="58" cy="75" r="3" fill="#fff"/>
            </svg>
          </div>
          <button class="view-details-btn">查看详情</button>
        </div>

        <!-- 运动嘉年华 -->
        <div class="category-card sports-carnival">
          <div class="card-header">
            <h3 class="card-title">运动嘉年华</h3>
            <p class="card-subtitle">同济大学 ｜ 上海交通大学</p>
          </div>
          <div class="card-illustration">
            <svg class="sports-icon" width="120" height="120" viewBox="0 0 120 120">
              <circle cx="40" cy="60" r="25" fill="#FFE0F0" opacity="0.8"/>
              <circle cx="80" cy="60" r="25" fill="#E8D5FF" opacity="0.8"/>
              <path d="M30 85 Q60 70 90 85" stroke="#9B59B6" stroke-width="3" fill="none"/>
            </svg>
          </div>
          <button class="view-details-btn">查看详情</button>
        </div>
      </section>

      <!-- Bottom Navigation -->
      <nav class="bottom-nav">
        <a href="/" class="nav-item">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z" stroke-width="2"/>
          </svg>
          <span>首页</span>
        </a>
        <a href="/events" class="nav-item active">
          <div class="nav-icon-wrapper">
            <svg class="nav-icon" width="24" height="24" viewBox="0 0 28 28" fill="currentColor">
              <rect x="4" y="6" width="20" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/>
              <rect x="7" y="3" width="3" height="6" rx="1" fill="currentColor"/>
              <rect x="18" y="3" width="3" height="6" rx="1" fill="currentColor"/>
              <line x1="8" y1="11" x2="20" y2="11" stroke="currentColor" stroke-width="1.5"/>
              <line x1="8" y1="15" x2="20" y2="15" stroke="currentColor" stroke-width="1.5"/>
              <line x1="8" y1="19" x2="16" y2="19" stroke="currentColor" stroke-width="1.5"/>
            </svg>
          </div>
          <span>博世活动</span>
        </a>
        <a href="/careers" class="nav-item">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2" stroke-width="2"/>
            <path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16" stroke-width="2"/>
          </svg>
          <span>职通博世</span>
        </a>
      </nav>
    </main>
  </div>
</template>

<script>
export default {
  name: 'EventsPage',
  data() {
    return {
      currentSlide: 0,
      slides: [
        { id: 1, title: '博士生论坛' },
        { id: 2, title: '技术创新大会' },
        { id: 3, title: '校园招聘会' }
      ]
    }
  },
  methods: {
    viewDetails(type) {
      console.log('View details for:', type)
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
  height: 45px; /* 为logo留出空间 */
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
  margin: 0;
  width: 100%;
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

/* Category Cards */
.categories-section {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
}

.category-card {
  flex: 1;
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.campus-tour {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.sports-carnival {
  background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
}

.card-header {
  margin-bottom: 20px;
}

.card-title {
  font-size: 16px;
  font-weight: 600;
  margin: 0 0 8px 0;
}

.campus-tour .card-title {
  color: white;
}

.sports-carnival .card-title {
  color: #333;
}

.card-subtitle {
  font-size: 13px;
  margin: 0;
  opacity: 0.9;
}

.campus-tour .card-subtitle {
  color: rgba(255, 255, 255, 0.9);
}

.sports-carnival .card-subtitle {
  color: #666;
}

.card-illustration {
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.view-details-btn {
  background: white;
  color: #333;
  border: none;
  padding: 10px 24px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.campus-tour .view-details-btn {
  background: white;
  color: #667eea;
}

.sports-carnival .view-details-btn {
  background: white;
  color: #fc8c69;
}

.view-details-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
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
  box-shadow: 0 -1px 0 0 rgba(0, 0, 0, 0.08);
  z-index: 100;
}

.nav-item {
  background: none;
  border: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  padding: 8px 24px;
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

.nav-item svg {
  width: 28px;
  height: 28px;
  color: #B0B0B0;
  transition: color 0.2s ease;
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

.nav-item span {
  font-size: 10px;
  color: #B0B0B0;
  transition: color 0.2s ease;
  margin-top: 2px;
  font-weight: 400;
}

.nav-item.active svg,
.nav-item.active .nav-icon {
  color: #4A90E2;
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

  .categories-section {
    flex-direction: column;
  }

  .category-card {
    width: 100%;
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

  .categories-section {
    gap: 30px;
  }

  .bottom-nav {
    display: none;
  }
}
</style>