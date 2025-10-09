<template>
  <div class="container">

    <!-- Header with Rainbow Strip -->
    <header class="header">
      <div class="spacer"></div> <!-- 为logo留出空间 -->
      <img src="../assets/images/rainbow.png" alt="Rainbow strip" class="rainbow-strip" />
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <div class="content-wrapper">
        <!-- Hero Banner with Carousel -->
        <div class="hero-banner" v-show="!showExploreDetail && !showGravityDetail && !showNewsDetail">
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

        <!-- Feature Cards -->
        <div class="feature-cards" v-show="!showExploreDetail && !showGravityDetail && !showNewsDetail">
          <!-- Card 1: 全景探索 -->
          <div class="feature-card card-explore" @click="toggleExploreDetail">
            <div class="card-content">
              <h3 class="card-title">全景探索，来个博世</h3>
              <p class="card-subtitle">博世全景 了解博士</p>
            </div>
            <button class="card-button">
              查看详情
              <img src="../assets/images/click.png" alt="" class="card-click-icon" />
            </button>
          </div>

          <!-- Card 2: 引力解码 -->
          <div class="feature-card card-gravity" @click="toggleGravityDetail">
            <div class="card-content">
              <h3 class="card-title">引力解码，来个博世</h3>
              <p class="card-subtitle">博世引力场 雇主价值主张</p>
            </div>
            <button class="card-button">
              查看详情
              <img src="../assets/images/click.png" alt="" class="card-click-icon" />
            </button>
          </div>

          <!-- Card 3: 热文追踪 -->
          <div class="feature-card card-news" @click="toggleNewsDetail">
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

        <!-- Full Page Expanded Explore Card -->
        <div v-if="showExploreDetail" class="full-page-expanded">
          <div class="expanded-card card-explore-expanded">
            <div class="expanded-header">
              <h2 class="expanded-title">全景探索，来个博世</h2>
              <div class="header-right">
                <img src="../assets/images/zhedie-logo-1.png" alt="BOSCH" class="bosch-logo" />
                <button class="collapse-button" @click="toggleExploreDetail">
                  <span>收回</span>
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="white">
                    <path d="M4 6L8 10L12 6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>

            <div class="expanded-image">
              <img src="../assets/images/bosch-cn-headquarter_res_1600x900.webp" alt="博世园区" />
            </div>

            <div class="expanded-content">
              <p class="description">
                博世集团于1909年首次进入中国市场，开设了第一家贸易办事处。1926年，博世在上海创建了首家汽车售后服务车间。在过去的112年里，博世见证了中国社会日新月异的变化——尤其是改革开放以来经济的迅速崛起。博世集团秉承"根植本土、服务本土"的理念，深度融入了中国经济的发展，与中国市场共同成长。现在，博世为中国市场和用户提供汽车与智能交通、工业、消费品以及能源与建筑技术领域先进的技术和解决方案，在各个业务领域深刻地践行并诠释"科技成就生活之美"的理念。截至2020年12月31日，博世在中国经营着56家公司，销售额达1173亿人民币，中国市场首次成为博世集团最大的单一市场，也是博世除德国以外拥有员工人数最多的国家。
              </p>
            </div>

            <div class="expanded-footer">
              <div class="button-wrapper" @click="navigateToPdfViewer">
                <img src="../assets/images/boshizhengtijieshao.png" alt="博世整体介绍" class="button-image" />
              </div>
              <div class="button-wrapper" @click="navigateToVideoSeries">
                <img src="../assets/images/boshixilieshipin.png" alt="博世系列视频" class="button-image" />
              </div>
            </div>
          </div>

          <!-- Other feature cards shown below expanded view -->
          <div class="other-cards">
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
        </div>

        <!-- Full Page Expanded Gravity Card -->
        <div v-if="showGravityDetail" class="full-page-expanded">
          <div class="expanded-card card-gravity-expanded">
            <div class="expanded-header">
              <h2 class="expanded-title">引力解码，来个博世</h2>
              <div class="header-right">
                <img src="../assets/images/zhedie-logo-2.png" alt="BOSCH" class="bosch-logo" />
                <button class="collapse-button" @click="toggleGravityDetail">
                  <span>收回</span>
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="white">
                    <path d="M4 6L8 10L12 6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>

            <!-- Gravity Content Section -->
            <div class="gravity-content-wrapper">
              <!-- 100 Reasons Auto Scrolling Section -->
              <div class="reasons-section">
                <h3 class="section-title">爱上博世的100个理由</h3>

                <!-- First Row -->
                <div class="auto-scroll-container">
                  <div class="scroll-track scroll-track-1" :style="{ transform: `translateX(${scrollPosition1}px)` }">
                    <!-- First set of items -->
                    <div class="scroll-item" v-for="(item, index) in scrollItemsRow1" :key="`first-${index}`">
                      <img src="../assets/images/juxing-17399.png" class="item-bg" alt="" />
                      <img src="../assets/images/yinhao.png" class="quote-icon" alt="" />
                      <div class="item-number">爱上博世的100个理由 #{{ String(index + 1).padStart(3, '0') }}</div>
                      <div class="item-content">
                        <div class="item-logo">
                          <img :src="item.logo" :alt="item.title" />
                        </div>
                        <span class="item-text">{{ item.title }}</span>
                      </div>
                    </div>
                    <!-- Duplicate set for infinite scroll -->
                    <div class="scroll-item" v-for="(item, index) in scrollItemsRow1" :key="`second-${index}`">
                      <img src="../assets/images/juxing-17399.png" class="item-bg" alt="" />
                      <img src="../assets/images/yinhao.png" class="quote-icon" alt="" />
                      <div class="item-number">爱上博世的100个理由 #{{ String(index + 1).padStart(3, '0') }}</div>
                      <div class="item-content">
                        <div class="item-logo">
                          <img :src="item.logo" :alt="item.title" />
                        </div>
                        <span class="item-text">{{ item.title }}</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Second Row -->
                <div class="auto-scroll-container">
                  <div class="scroll-track scroll-track-2" :style="{ transform: `translateX(${scrollPosition2}px)` }">
                    <!-- First set of items -->
                    <div class="scroll-item" v-for="(item, index) in scrollItemsRow2" :key="`first-${index}`">
                      <img src="../assets/images/juxing-17399.png" class="item-bg" alt="" />
                      <img src="../assets/images/yinhao.png" class="quote-icon" alt="" />
                      <div class="item-number">爱上博世的100个理由 #{{ String(index + 7).padStart(3, '0') }}</div>
                      <div class="item-content">
                        <div class="item-logo">
                          <img :src="item.logo" :alt="item.title" />
                        </div>
                        <span class="item-text">{{ item.title }}</span>
                      </div>
                    </div>
                    <!-- Duplicate set for infinite scroll -->
                    <div class="scroll-item" v-for="(item, index) in scrollItemsRow2" :key="`second-${index}`">
                      <img src="../assets/images/juxing-17399.png" class="item-bg" alt="" />
                      <img src="../assets/images/yinhao.png" class="quote-icon" alt="" />
                      <div class="item-number">爱上博世的100个理由 #{{ String(index + 7).padStart(3, '0') }}</div>
                      <div class="item-content">
                        <div class="item-logo">
                          <img :src="item.logo" :alt="item.title" />
                        </div>
                        <span class="item-text">{{ item.title }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Carousel Image Section -->
              <div class="gravity-carousel">
                <div class="carousel-container">
                  <img v-if="gravitySlide === 0"
                       src="../assets/images/mobility-solutions-web-portal_res_1280x720.webp"
                       alt="爱上博世的100个理由"
                       class="carousel-image" />
                  <img v-else
                       src="../assets/images/jump.jpg"
                       alt="跳一跳"
                       class="carousel-image" />

                  <div class="carousel-overlay">
                    <h3 class="carousel-title">{{ gravitySlide === 0 ? '爱上博世的100个理由' : '跳一跳' }}</h3>
                  </div>

                  <!-- Carousel Controls -->
                  <button class="carousel-prev" @click="prevGravitySlide">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
                      <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
                    </svg>
                  </button>
                  <button class="carousel-next" @click="nextGravitySlide">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
                      <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
                    </svg>
                  </button>
                </div>

                <!-- Carousel Dots -->
                <div class="carousel-dots">
                  <span
                    class="dot"
                    :class="{ active: gravitySlide === 0 }"
                    @click="gravitySlide = 0"
                  ></span>
                  <span
                    class="dot"
                    :class="{ active: gravitySlide === 1 }"
                    @click="gravitySlide = 1"
                  ></span>
                </div>
              </div>
            </div>
          </div>

          <!-- Other feature cards shown below expanded view -->
          <div class="other-cards">
            <div class="feature-card card-explore">
              <div class="card-content">
                <h3 class="card-title">全景探索，来个博世</h3>
                <p class="card-subtitle">博世全景 了解博士</p>
              </div>
              <button class="card-button">
                查看详情
                <img src="../assets/images/click.png" alt="" class="card-click-icon" />
              </button>
            </div>

            <div class="feature-card card-news" @click="toggleNewsDetail">
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
        </div>

        <!-- Full Page Expanded News Card -->
        <div v-if="showNewsDetail" class="full-page-expanded">
          <div class="expanded-card card-news-expanded">
            <div class="expanded-header">
              <h2 class="expanded-title">热文追踪，来个博世</h2>
              <div class="header-right">
                <img src="../assets/images/zhedie-logo-3.png" alt="BOSCH" class="bosch-logo" />
                <button class="collapse-button" @click="toggleNewsDetail">
                  <span>收回</span>
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="white">
                    <path d="M4 6L8 10L12 6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>

            <!-- News Content Section -->
            <div class="news-content-wrapper">
              <!-- News Carousel -->
              <div class="news-carousel">
                <transition name="slide-fade" mode="out-in">
                  <div class="news-slide" :key="currentNewsSlide">
                    <div class="news-image-container">
                      <img :src="newsSlides[currentNewsSlide].image" :alt="newsSlides[currentNewsSlide].title" class="news-image" />
                    </div>
                    <div class="news-info">
                      <div class="news-meta">
                        <span class="news-category">{{ newsSlides[currentNewsSlide].category }}</span>
                        <span class="news-date">{{ newsSlides[currentNewsSlide].date }}</span>
                      </div>
                      <h3 class="news-title">{{ newsSlides[currentNewsSlide].title }}</h3>
                      <p class="news-description" v-if="newsSlides[currentNewsSlide].content">{{ newsSlides[currentNewsSlide].content }}</p>
                      <button class="read-more-btn" @click="readNewsDetail(currentNewsSlide)">
                        了解详情
                        <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
                          <path d="M6 12l4-4-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </button>
                    </div>
                  </div>
                </transition>

                <!-- Carousel Dots -->
                <div class="news-carousel-dots">
                  <span
                    v-for="(slide, index) in newsSlides"
                    :key="index"
                    :class="['dot', { active: currentNewsSlide === index }]"
                    @click="currentNewsSlide = index"
                  ></span>
                </div>
              </div>

              <!-- More News Button -->
              <div class="more-news-section">
                <button class="more-news-btn" @click="viewMoreNews">
                  查看更多新闻
                </button>
              </div>
            </div>
          </div>

          <!-- Other feature cards shown below expanded view -->
          <div class="other-cards">
            <div class="feature-card card-explore" @click="toggleExploreDetail">
              <div class="card-content">
                <h3 class="card-title">全景探索，来个博世</h3>
                <p class="card-subtitle">博世全景 了解博士</p>
              </div>
              <button class="card-button">
                查看详情
                <img src="../assets/images/click.png" alt="" class="card-click-icon" />
              </button>
            </div>

            <div class="feature-card card-gravity" @click="toggleGravityDetail">
              <div class="card-content">
                <h3 class="card-title">引力解码，来个博世</h3>
                <p class="card-subtitle">博世引力场 雇主价值主张</p>
              </div>
              <button class="card-button">
                查看详情
                <img src="../assets/images/click.png" alt="" class="card-click-icon" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Bottom Navigation (only shown on mobile) -->
    <nav class="bottom-nav mobile-only">
      <button class="nav-item active">
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
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const currentSlide = ref(0)
const showExploreDetail = ref(false)
const showGravityDetail = ref(false)
const showNewsDetail = ref(false)
const gravitySlide = ref(0)
const scrollPosition1 = ref(0)
const scrollPosition2 = ref(0)
const currentNewsSlide = ref(0)
const newsSlides = ref([
  {
    image: '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._0.png',
    category: '企业荣誉',
    date: '2025-09-28',
    title: '2025福布斯中国最佳雇主，我们上榜啦！',
    content: '博世荣获福布斯2025「中国年度最佳雇主」及「年度最佳ESG实践雇主」',
    detailImages: [
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._1.png',
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._2.png',
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._3.png'
    ]
  },
  {
    image: '/src/assets/file/article2/image_博世投入25亿欧元发力AI，事关..._0.png',
    category: '技术创新',
    date: '2025-09-25',
    title: '博世投入25亿欧元发力AI，事关你我未来生活',
    content: '博世投入25亿欧元发力AI，1500+欧洲专利加持，改变你我生活！',
    detailImages: [
      '/src/assets/file/article2/image_博世投入25亿欧元发力AI，事关..._1.png',
      '/src/assets/file/article2/image_博世投入25亿欧元发力AI，事关..._2.png'
    ]
  },
  {
    image: '/src/assets/images/bosch-cn-headquarter_res_1600x900.webp',
    category: '可持续发展',
    date: '2025-09-20',
    title: '博世中国区实现碳中和目标，引领行业绿色转型',
    content: '博世在中国的所有工厂已全面实现碳中和，成为行业绿色转型的典范'
  }
])
const scrollItemsRow1 = ref([
  { title: '居家办公', logo: '/src/assets/images/100-reasons/logo1.png' },
  { title: '博世内部福利', logo: '/src/assets/images/100-reasons/logo2.png' },
  { title: '黑客马拉松大赛', logo: '/src/assets/images/100-reasons/logo3.png' },
  { title: '博世多元日', logo: '/src/assets/images/100-reasons/logo1.png' },
  { title: '海外轮岗计划', logo: '/src/assets/images/100-reasons/logo2.png' },
  { title: '技术创新', logo: '/src/assets/images/100-reasons/logo3.png' }
])
const scrollItemsRow2 = ref([
  { title: '碳中和企业', logo: '/src/assets/images/100-reasons/logo1.png' },
  { title: '认可激励', logo: '/src/assets/images/100-reasons/logo2.png' },
  { title: '职业发展', logo: '/src/assets/images/100-reasons/logo3.png' },
  { title: '团队协作', logo: '/src/assets/images/100-reasons/logo1.png' },
  { title: '弹性工作', logo: '/src/assets/images/100-reasons/logo2.png' },
  { title: '创新文化', logo: '/src/assets/images/100-reasons/logo3.png' }
])
// 导入轮播图图片
import lunbo1 from '../assets/images/lunbo1.jpg'
import lunbo2 from '../assets/images/lunbo2.jpg'
import lunbo3 from '../assets/images/lunbo3.jpg'

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
let scrollIntervalId = null

// Navigation functions
const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % slides.value.length
}

const prevSlide = () => {
  currentSlide.value = currentSlide.value === 0
    ? slides.value.length - 1
    : currentSlide.value - 1
}

// Toggle explore detail
const toggleExploreDetail = () => {
  showExploreDetail.value = !showExploreDetail.value
  if (showExploreDetail.value) {
    showGravityDetail.value = false
    showNewsDetail.value = false
  }
}

// Toggle gravity detail
const toggleGravityDetail = () => {
  showGravityDetail.value = !showGravityDetail.value
  if (showGravityDetail.value) {
    showExploreDetail.value = false
    showNewsDetail.value = false
  }
}

// Toggle news detail
const toggleNewsDetail = () => {
  showNewsDetail.value = !showNewsDetail.value
  if (showNewsDetail.value) {
    showExploreDetail.value = false
    showGravityDetail.value = false
  }
}

// Read news detail
const readNewsDetail = (index) => {
  router.push(`/news-detail/${index}`)
}

// View more news
const viewMoreNews = () => {
  router.push('/news-list')
}

// Gravity carousel navigation
const nextGravitySlide = () => {
  gravitySlide.value = (gravitySlide.value + 1) % 2
}

const prevGravitySlide = () => {
  gravitySlide.value = gravitySlide.value === 0 ? 1 : 0
}

// Navigate to PDF viewer page
const navigateToPdfViewer = () => {
  router.push('/pdf-viewer')
}

// Navigate to video series page
const navigateToVideoSeries = () => {
  router.push('/video-series')
}

// Navigate to events page
const navigateToEvents = () => {
  router.push('/events')
}

// Navigate to careers page
const navigateToCareers = () => {
  router.push('/careers')
}

// Auto-scroll animation
const startAutoScroll = () => {
  const itemWidth = 280 // width of each item + gap
  const totalWidth1 = scrollItemsRow1.value.length * itemWidth
  const totalWidth2 = scrollItemsRow2.value.length * itemWidth

  scrollIntervalId = setInterval(() => {
    // Row 1 scrolls left
    scrollPosition1.value -= 1
    // Row 2 scrolls left too (same direction but slightly different speed)
    scrollPosition2.value -= 1.2

    // Reset positions when first set is completely scrolled
    if (Math.abs(scrollPosition1.value) >= totalWidth1) {
      scrollPosition1.value = 0
    }
    if (Math.abs(scrollPosition2.value) >= totalWidth2) {
      scrollPosition2.value = 0
    }
  }, 30)
}

// Auto-play carousel
onMounted(() => {
  intervalId = setInterval(nextSlide, 5000)
  startAutoScroll()
  // Auto-play news carousel
  setInterval(() => {
    currentNewsSlide.value = (currentNewsSlide.value + 1) % newsSlides.value.length
  }, 4000)
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
  if (scrollIntervalId) {
    clearInterval(scrollIntervalId)
  }
})
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
  height: 45px; /* 为logo留出空间 */
}

.rainbow-strip {
  height: 4px;
  margin: 0;
  width: 100%;
  display: block;
  object-fit: cover;
}

/* 移除桌面导航相关样式，因为不再需要 */

/* Main Content */
.main-content {
  padding: 16px;
  padding-bottom: 72px; /* 56px + some margin */
}

.content-wrapper {
  max-width: 100%;
  margin: 0 auto;
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

/* 第一个卡片正常圆角 */
.feature-card:first-child {
  border-radius: 16px;
  margin-bottom: -8px;
  z-index: 3;
}

/* 中间卡片 */
.feature-card:nth-child(2) {
  border-radius: 16px;
  padding-top: 32px;
  margin-bottom: -8px;
  z-index: 2;
}

/* 最后一个卡片 */
.feature-card:last-child {
  border-radius: 16px;
  padding-top: 32px;
  z-index: 1;
}

.feature-card:hover {
  transform: translateY(-2px);
  z-index: 10 !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.feature-card:active {
  transform: scale(0.99);
}

.card-explore {
  background: linear-gradient(135deg, #007BC0 0%, #8FB7F9 100%);
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

/* Full Page Expanded View */
.full-page-expanded {
  position: relative;
  animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
  from {
    transform: translateY(100px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Expanded Card Styles */
.expanded-card {
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  margin-bottom: 16px;
}

@keyframes expandCard {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.card-explore-expanded {
  background: linear-gradient(135deg, #5E9FD8 0%, #91C2F2 100%);
}

.expanded-header {
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.expanded-title {
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

.expanded-image {
  margin: 0 20px;
  border-radius: 12px;
  overflow: hidden;
  height: 200px;
  background: #f0f0f0;
}

.expanded-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.expanded-content {
  padding: 20px;
}

.expanded-content .description {
  font-size: 14px;
  line-height: 1.8;
  color: white;
  position: relative;
  text-align: justify;
}

.expand-icon {
  display: inline-block;
  margin-left: 4px;
  vertical-align: middle;
}

.expanded-footer {
  padding: 0 20px 20px;
  display: flex;
  gap: 12px;
}

.button-wrapper {
  flex: 1;
  cursor: pointer;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.button-wrapper:hover {
  transform: scale(1.02);
  opacity: 0.9;
}

.button-wrapper:active {
  transform: scale(0.98);
}

.button-image {
  width: 100%;
  height: auto;
  border-radius: 12px;
  display: block;
}

/* Other cards below expanded view */
.other-cards {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.other-cards .feature-card {
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

.other-cards .feature-card:first-child {
  margin-bottom: -8px;
  z-index: 2;
}

.other-cards .feature-card:last-child {
  padding-top: 32px;
  z-index: 1;
}

/* Gravity Expanded Card Styles */
.card-gravity-expanded {
  background: linear-gradient(135deg, #B97FC4 0%, #D4B5E6 100%);
}

.gravity-content-wrapper {
  padding: 20px;
}

.reasons-section {
  margin-bottom: 20px;
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  color: white;
  margin-bottom: 16px;
}

/* Auto Scroll Container Styles */
.auto-scroll-container {
  position: relative;
  overflow: hidden;
  margin-bottom: 8px;
  padding: 8px 0;
}

.auto-scroll-container:last-of-type {
  margin-bottom: 20px;
}

.scroll-track {
  display: flex;
  gap: 15px;
  transition: transform 0.03s linear;
  will-change: transform;
}

.scroll-item {
  position: relative;
  white-space: nowrap;
  flex-shrink: 0;
  min-width: 220px;
  height: 60px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.scroll-item:hover {
  transform: scale(1.05);
}

/* 背景图片 */
.item-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: fill;
  z-index: 0;
}

/* 引号图标 */
.quote-icon {
  position: absolute;
  left: 17px;
  top: 0;
  width: 18px;
  height: 18px;
  object-fit: contain;
  z-index: 2;
}

/* 内容容器 */
.item-content {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: flex-end;
  gap: 10px;
  height: 100%;
  padding: 10px 20px 5px 8px;
}

.item-logo {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
  background: white;
  margin-bottom: -3px;
}

.item-logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.item-text {
  font-size: 17px;
  font-weight: 500;
  color: #333;
  padding-bottom: 5px;
  padding-left: 5px;
}

/* 编号样式 */
.item-number {
  position: absolute;
  top: 8px;
  left: 55px;
  font-size: 10px;
  color: #666;
  z-index: 1;
  font-weight: 400;
  letter-spacing: 0.5px;
}

/* Gravity Carousel */
.gravity-carousel {
  margin-bottom: 20px;
}

.carousel-container {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  height: 200px;
  background: #f0f0f0;
}

.carousel-container .carousel-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 16px;
  background: linear-gradient(to top, rgba(0,0,0,0.7), transparent);
}

.carousel-title {
  font-size: 16px;
  font-weight: 600;
  color: white;
}

.gravity-carousel .carousel-prev,
.gravity-carousel .carousel-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  border: none;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 2;
}

.gravity-carousel .carousel-prev {
  left: 10px;
}

.gravity-carousel .carousel-next {
  right: 10px;
}

.gravity-carousel .carousel-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 12px;
}

/* News Expanded Card Styles */
.card-news-expanded {
  background: linear-gradient(135deg, #5AA397 0%, #8BCFC5 100%);
}

.news-content-wrapper {
  padding: 20px;
}

.news-carousel {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 20px;
}

.news-slide {
  position: relative;
}

.news-image-container {
  height: 240px;
  overflow: hidden;
  position: relative;
}

.news-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.news-info {
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.news-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.news-category {
  background: #F0F5F4;
  color: #5AA397;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

.news-date {
  color: #999;
  font-size: 12px;
}

.news-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  line-height: 1.4;
  margin-bottom: 12px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.news-description {
  font-size: 14px;
  color: #666;
  line-height: 1.5;
  margin-bottom: 16px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.read-more-btn {
  background: transparent;
  border: 1px solid #5AA397;
  color: #5AA397;
  padding: 10px 24px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  align-self: center;
  margin-top: auto;
}

.read-more-btn:hover {
  background: #5AA397;
  color: white;
}

.read-more-btn svg {
  width: 12px;
  height: 12px;
  fill: none;
}

.news-carousel-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 12px;
  background: white;
}

.more-news-section {
  text-align: center;
}

.more-news-btn {
  background: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 24px;
  padding: 14px 32px;
  color: #5AA397;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  max-width: 300px;
}

.more-news-btn:hover {
  background: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Responsive adjustments for news module */
@media (min-width: 768px) {
  .news-image-container {
    height: 280px;
  }

  .news-title {
    font-size: 20px;
  }

  .news-info {
    padding: 24px;
  }
}

@media (min-width: 1024px) {
  .news-content-wrapper {
    padding: 30px;
  }

  .news-image-container {
    height: 320px;
  }

  .news-title {
    font-size: 22px;
    -webkit-line-clamp: 3;
  }

  .news-carousel {
    margin-bottom: 30px;
  }

  .more-news-btn {
    max-width: 400px;
  }
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
  justify-content: center;
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
  .main-content {
    padding: 24px;
    padding-bottom: 72px; /* Account for mobile nav */
  }

  .content-wrapper {
    max-width: 900px;
  }

  .feature-cards {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
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

  .card-title {
    font-size: 20px;
  }

  .card-subtitle {
    font-size: 15px;
  }
}

/* Desktop Styles */
@media (min-width: 1024px) {
  /* Hide mobile elements */
  .mobile-only {
    display: none !important;
  }

  .desktop-only {
    display: flex !important;
  }

  /* Header adjustments */
  .header {
    position: sticky;
    top: 0;
  }

  .spacer {
    height: 60px; /* 桌面端为logo留更多空间 */
  }

  /* Main content adjustments */
  .main-content {
    padding: 40px;
    padding-bottom: 40px;
  }

  .content-wrapper {
    max-width: 1400px;
  }

  /* Hero banner adjustments */
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

  /* Feature cards grid layout */
  .feature-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
  }

  .feature-card {
    padding: 30px;
    border-radius: 20px;
    flex-direction: column;
    align-items: flex-start;
    min-height: 180px;
    height: auto;
  }

  .card-content {
    margin-bottom: 20px;
  }

  .card-title {
    font-size: 22px;
    margin-bottom: 12px;
  }

  .card-subtitle {
    font-size: 16px;
  }

  .card-button {
    padding: 10px 20px;
    font-size: 15px;
  }
}

/* Large Desktop */
@media (min-width: 1440px) {
  .spacer {
    height: 70px; /* 大屏幕更多空间 */
  }

  .main-content {
    padding: 50px 60px;
  }

  .content-wrapper {
    max-width: 1600px;
  }

  .carousel-wrapper {
    height: 500px;
  }

  .feature-card {
    padding: 35px;
  }

  .card-title {
    font-size: 24px;
  }
}
</style>