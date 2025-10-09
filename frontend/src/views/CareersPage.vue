<template>
  <div class="container">
    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div> <!-- 为logo留出空间 -->
      <img src="../assets/images/rainbow.png" alt="Rainbow strip" class="rainbow-strip" />
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Hero Banner with Carousel -->
      <div class="hero-banner">
        <div class="carousel-wrapper">
          <transition-group name="slide-fade" tag="div">
            <div
              class="carousel-slide"
              v-for="(slide, index) in slides"
              :key="index"
              v-show="currentSlide === index"
            >
              <img
                :src="slide.image"
                :alt="slide.alt"
                class="carousel-image"
              />
            </div>
          </transition-group>
          <!-- Navigation Arrows -->
          <button class="carousel-prev" @click="prevSlide" aria-label="Previous slide">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
              <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
            </svg>
          </button>
          <button class="carousel-next" @click="nextSlide" aria-label="Next slide">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
              <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
            </svg>
          </button>
        </div>

        <!-- Carousel Dots -->
        <div class="carousel-dots">
          <span
            v-for="(slide, index) in slides"
            :key="index"
            :class="['dot', { active: currentSlide === index }]"
            @click="currentSlide = index"
          ></span>
        </div>
      </div>

      <!-- Career Cards Section -->
      <div class="career-cards">
        <!-- 校园招聘 Card -->
        <div class="career-card campus-card">
          <div class="card-header">
            <h2 class="card-title">校园招聘</h2>
            <h3 class="card-subtitle">2026应届生招聘</h3>
          </div>
          <div class="card-content">
            <p class="card-description">
              毕业时间在2025年1月-2026年12月<br>
              期间的同学
            </p>
          </div>
          <button class="card-button" @click="viewDetails('campus')">
            查看详情
          </button>
        </div>

        <!-- 社会招聘 Card -->
        <div class="career-card social-card">
          <div class="card-header">
            <h2 class="card-title">社会招聘</h2>
          </div>
          <div class="card-content">
            <p class="card-description">
              主要面向有一定工作经验的优秀人才
            </p>
          </div>
          <button class="card-button" @click="viewDetails('social')">
            查看详情
          </button>
        </div>

        <!-- 日常实习生 Card -->
        <div class="career-card intern-card">
          <div class="card-header">
            <h2 class="card-title">日常实习生</h2>
          </div>
          <div class="card-content">
            <p class="card-description">
              全部在校大学生
            </p>
          </div>
          <button class="card-button" @click="viewDetails('intern')">
            查看详情
          </button>
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

      <button class="nav-item" @click="goEvents">
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

      <button class="nav-item active">
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
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const currentSlide = ref(0)

// 导入轮播图图片
import lunbo1 from '../assets/images/lunbo1.jpg'
import lunbo2 from '../assets/images/lunbo2.jpg'
import lunbo3 from '../assets/images/lunbo3.jpg'

// 轮播图数据 - 使用与首页相同的图片
const slides = ref([
  {
    image: lunbo1,
    alt: 'BOSCH 招聘 - 科技成就生活之美'
  },
  {
    image: lunbo2,
    alt: 'BOSCH 招聘 - 创新引领未来'
  },
  {
    image: lunbo3,
    alt: 'BOSCH 招聘 - 加入我们'
  }
])

let intervalId = null

// Navigation functions
const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % slides.value.length
}

const prevSlide = () => {
  currentSlide.value = currentSlide.value === 0
    ? slides.value.length - 1
    : currentSlide.value - 1
}

// Auto-play carousel
onMounted(() => {
  intervalId = setInterval(nextSlide, 5000)
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
})

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
      window.open('https://www.bosch.com.cn/careers/students-and-graduates/', '_blank')
      break
    case 'social':
      // 社会招聘详情
      window.open('https://www.bosch.com.cn/careers/professionals/', '_blank')
      break
    case 'intern':
      // 实习生招聘详情
      window.open('https://www.bosch.com.cn/careers/students-and-graduates/internships/', '_blank')
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
  height: 45px; /* 为logo留出空间 */
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

/* Hero Banner */
.hero-banner {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.carousel-wrapper {
  height: 351px;
  position: relative;
  overflow: hidden;
  background: #f5f5f5;
}

.carousel-slide {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.carousel-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Carousel Navigation Arrows */
.carousel-prev,
.carousel-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 2;
}

.carousel-prev:hover,
.carousel-next:hover {
  background: rgba(0, 0, 0, 0.7);
}

.carousel-prev {
  left: 10px;
}

.carousel-next {
  right: 10px;
}

/* Slide transition */
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: opacity 0.5s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
}

.carousel-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 12px;
  background: white;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #D0D0D0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  width: 20px;
  border-radius: 4px;
  background: #333;
}

/* Career Cards */
.career-cards {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.career-card {
  background: white;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  min-height: 160px;
}

.career-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

/* Campus Card - Blue Theme */
.campus-card {
  background: linear-gradient(135deg, #7FA8D8 0%, #A5C4E7 100%);
}

.campus-card .card-title,
.campus-card .card-subtitle,
.campus-card .card-description {
  color: white;
}

.campus-card .card-button {
  background: rgba(255, 255, 255, 0.9);
  color: #7FA8D8;
}

/* Social Card - Purple Theme */
.social-card {
  background: linear-gradient(135deg, #B799D9 0%, #D4B9EC 100%);
}

.social-card .card-title,
.social-card .card-description {
  color: white;
}

.social-card .card-button {
  background: rgba(255, 255, 255, 0.9);
  color: #B799D9;
}

/* Intern Card - Teal Theme */
.intern-card {
  background: linear-gradient(135deg, #7ABDB3 0%, #A5D5CE 100%);
}

.intern-card .card-title,
.intern-card .card-description {
  color: white;
}

.intern-card .card-button {
  background: rgba(255, 255, 255, 0.9);
  color: #7ABDB3;
}

/* Card Content */
.card-header {
  margin-bottom: 12px;
}

.card-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 6px;
}

.card-subtitle {
  font-size: 16px;
  font-weight: 500;
  opacity: 0.95;
}

.card-content {
  margin-bottom: 16px;
}

.card-description {
  font-size: 14px;
  line-height: 1.6;
  opacity: 0.9;
}

.card-button {
  padding: 10px 24px;
  border: none;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  float: right;
}

.card-button:hover {
  transform: scale(1.05);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.card-button:active {
  transform: scale(0.98);
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

.nav-item.active .nav-icon {
  color: #4A90E2;
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

  .carousel-wrapper {
    height: 400px;
  }

  .carousel-prev,
  .carousel-next {
    width: 48px;
    height: 48px;
  }

  .hero-banner {
    margin-bottom: 24px;
  }

  .career-cards {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }

  .career-card {
    padding: 24px;
    min-height: 180px;
  }

  .card-title {
    font-size: 24px;
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

  .carousel-wrapper {
    height: 450px;
  }

  .carousel-prev,
  .carousel-next {
    width: 56px;
    height: 56px;
  }

  .carousel-prev {
    left: 20px;
  }

  .carousel-next {
    right: 20px;
  }

  .hero-banner {
    margin-bottom: 40px;
    border-radius: 20px;
  }

  .career-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
  }

  .career-card {
    padding: 28px;
    min-height: 200px;
  }

  .card-title {
    font-size: 26px;
  }

  .card-subtitle {
    font-size: 20px;
  }

  .card-description {
    font-size: 16px;
  }

  .card-button {
    padding: 14px 32px;
    font-size: 16px;
  }
}
</style>