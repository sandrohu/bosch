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
        <div class="carousel-section" v-show="!showExploreDetail && !showGravityDetail && !showNewsDetail">
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
          </div>

          <!-- Carousel Dots - 独立在轮播图下方 -->
          <div class="carousel-dots-wrapper">
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

            <div class="feature-card card-news" @click="toggleNewsDetail">
              <div class="card-content">
                <h3 class="card-title">热文追踪，来个博世</h3>
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
                    <div class="scroll-item" v-for="(item, index) in scrollItemsRow1" :key="`first-${index}`" @click="goToReasonsDetail">
                      <img src="../assets/images/juxing-17399.png" class="item-bg" alt="" />
                      <img src="../assets/images/yinhao.png" class="quote-icon" alt="" />
                      <div class="item-number">爱上博世的100个理由 #{{ String(item.id).padStart(3, '0') }}</div>
                      <div class="item-content">
                        <div class="item-logo">
                          <img :src="item.logo" :alt="item.title" />
                        </div>
                        <span class="item-text">{{ item.title }}</span>
                      </div>
                      <div class="item-description">{{ item.description }}</div>
                    </div>
                    <!-- Duplicate set for infinite scroll -->
                    <div class="scroll-item" v-for="(item, index) in scrollItemsRow1" :key="`second-${index}`" @click="goToReasonsDetail">
                      <img src="../assets/images/juxing-17399.png" class="item-bg" alt="" />
                      <img src="../assets/images/yinhao.png" class="quote-icon" alt="" />
                      <div class="item-number">爱上博世的100个理由 #{{ String(item.id).padStart(3, '0') }}</div>
                      <div class="item-content">
                        <div class="item-logo">
                          <img :src="item.logo" :alt="item.title" />
                        </div>
                        <span class="item-text">{{ item.title }}</span>
                      </div>
                      <div class="item-description">{{ item.description }}</div>
                    </div>
                  </div>
                </div>

                <!-- Second Row -->
                <div class="auto-scroll-container">
                  <div class="scroll-track scroll-track-2" :style="{ transform: `translateX(${scrollPosition2}px)` }">
                    <!-- First set of items -->
                    <div class="scroll-item" v-for="(item, index) in scrollItemsRow2" :key="`first-${index}`" @click="goToReasonsDetail">
                      <img src="../assets/images/juxing-17399.png" class="item-bg" alt="" />
                      <img src="../assets/images/yinhao.png" class="quote-icon" alt="" />
                      <div class="item-number">爱上博世的100个理由 #{{ String(item.id).padStart(3, '0') }}</div>
                      <div class="item-content">
                        <div class="item-logo">
                          <img :src="item.logo" :alt="item.title" />
                        </div>
                        <span class="item-text">{{ item.title }}</span>
                      </div>
                      <div class="item-description">{{ item.description }}</div>
                    </div>
                    <!-- Duplicate set for infinite scroll -->
                    <div class="scroll-item" v-for="(item, index) in scrollItemsRow2" :key="`second-${index}`" @click="goToReasonsDetail">
                      <img src="../assets/images/juxing-17399.png" class="item-bg" alt="" />
                      <img src="../assets/images/yinhao.png" class="quote-icon" alt="" />
                      <div class="item-number">爱上博世的100个理由 #{{ String(item.id).padStart(3, '0') }}</div>
                      <div class="item-content">
                        <div class="item-logo">
                          <img :src="item.logo" :alt="item.title" />
                        </div>
                        <span class="item-text">{{ item.title }}</span>
                      </div>
                      <div class="item-description">{{ item.description }}</div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Carousel Image Section -->
              <div class="gravity-carousel">
                <div class="carousel-container" @click="gravitySlide === 0 ? goToReasonsDetail() : null">
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

            <div class="feature-card card-news" @click="toggleNewsDetail">
              <div class="card-content">
                <h3 class="card-title">热文追踪，来个博世</h3>
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
    image: article1Image0,
    category: '企业荣誉',
    date: '2025-09-28',
    title: '2025福布斯中国最佳雇主，我们上榜啦！',
    content: '博世荣获福布斯2025「中国年度最佳雇主」及「年度最佳ESG实践雇主」',
    detailImages: [
      article1Image1,
      article1Image2,
      article1Image3
    ]
  },
  {
    image: article2Image0,
    category: '技术创新',
    date: '2025-09-25',
    title: '博世投入25亿欧元发力AI，事关你我未来生活',
    content: '博世投入25亿欧元发力AI，1500+欧洲专利加持，改变你我生活！',
    detailImages: [
      article2Image1,
      article2Image2
    ]
  },
  {
    image: boschHeadquarter,
    category: '可持续发展',
    date: '2025-09-20',
    title: '博世中国区实现碳中和目标，引领行业绿色转型',
    content: '博世在中国的所有工厂已全面实现碳中和，成为行业绿色转型的典范'
  }
])
// 所有100个理由数据
const allReasons = ref([
  { id: 1, title: '"为生活而发明"理念', description: '博世始终秉持 "Invented for life" 的品牌主张，为人类创造更美好的生活。', logo: logo1 },
  { id: 2, title: '全球化布局', description: '博世业务覆盖 60 多个国家，是真正的全球化公司。', logo: logo2 },
  { id: 3, title: '中国深耕力度', description: '博世在中国有多年历史，深耕本地市场，致力于本土化发展。', logo: logo3 },
  { id: 4, title: '多元业务领域', description: '博世涵盖汽车技术、工业技术、消费品与能源技术等多个业务板块。', logo: logo1 },
  { id: 5, title: '可持续发展承诺', description: '博世致力于以可持续科技为核心，推动环保与社会责任。', logo: logo2 },
  { id: 6, title: '责任与伦理', description: '在商业决策中坚持责任与伦理，是博世企业文化的基石。', logo: logo3 },
  { id: 7, title: '公正与尊重', description: '公正对待员工与合作方，倡导尊重，是博世内在的价值观。', logo: logo1 },
  { id: 8, title: '开放与信任', description: '博世鼓励在组织内部建立开放沟通与相互信任的氛围。', logo: logo2 },
  { id: 9, title: '主动与担当', description: '每个人都被鼓励主动承担责任、追求目标。', logo: logo3 },
  { id: 10, title: '结果导向', description: '博世重视实效，追求行动带来结果与价值。', logo: logo1 },
  { id: 11, title: '多样性与包容性', description: '博世重视员工多样性，倡导包容互补的团队文化。', logo: logo2 },
  { id: 12, title: '企业传承基因', description: '博世的价值观可追溯至创始人罗伯特·博世的初心。', logo: logo3 },
  { id: 13, title: '强大的研发实力', description: '博世在全球拥有大量研发机构，不断投入技术创新。', logo: logo1 },
  { id: 14, title: '技术驱动企业', description: '博世的产品与方案背后，都是先进的技术驱动。', logo: logo2 },
  { id: 15, title: '智能互联解决方案', description: '博世在物联网、智能互联产品上不断深耕。', logo: logo3 },
  { id: 16, title: '汽车事业的核心角色', description: '博世在全球汽车技术领域是关键供应商。', logo: logo1 },
  { id: 17, title: '移动出行未来愿景', description: '博世致力于安全、可持续、智能的未来出行解决方案。', logo: logo2 },
  { id: 18, title: '工业自动化领先者', description: '博世（例如力士乐部门）在传动与控制技术具领先地位。', logo: logo3 },
  { id: 19, title: '家电与消费品链条', description: '博世在家电、厨房、热能设备等消费品领域拥有较高影响力。', logo: logo1 },
  { id: 20, title: '节能与环境科技', description: '博世在能源利用、热泵、节能系统等领域持续投入。', logo: logo2 },
  { id: 21, title: '智能传感器技术', description: '博世子公司 Sensortec 在 MEMS 传感器方面具影响力。', logo: logo3 },
  { id: 22, title: '跨界整合能力', description: '博世能够整合硬件、软件、云服务等跨领域能力。', logo: logo1 },
  { id: 23, title: '强大的产业链掌控', description: '从元器件到系统方案，博世在产业链上具备控制能力。', logo: logo2 },
  { id: 24, title: '长期视野与投资', description: '博世注重中长期发展而不仅短期利益。', logo: logo3 },
  { id: 25, title: '本地化策略', description: '在中国市场，博世注重本地化设计与服务。', logo: logo1 },
  { id: 26, title: '创投与未来投入', description: '博世设立创投基金，不断探索未来技术。', logo: logo2 },
  { id: 27, title: '科技与社会责任融合', description: '博世强调科技创新必须兼顾社会责任。', logo: logo3 },
  { id: 28, title: '慈善实践根植中国', description: '博世在中国有自己的慈善中心，积极参与教育扶贫项目。', logo: logo1 },
  { id: 29, title: '员工志愿者文化', description: '博世鼓励员工以志愿者身份参与社会公益。', logo: logo2 },
  { id: 30, title: '高度透明的公益机制', description: '在中国的慈善中心强调项目透明性与可持续性。', logo: logo3 },
  { id: 31, title: '持续教育投入', description: '博世在教育、人才培养方面持续投入。', logo: logo1 },
  { id: 32, title: '因地制宜的公益方案', description: '博世的公益项目结合当地实际需求设计。', logo: logo2 },
  { id: 33, title: '本地员工成长机会', description: '本地团队能获得参与全球项目的机会。', logo: logo3 },
  { id: 34, title: '跨国导师机制', description: '博世内部可能设有跨国导师或技能传承机制。', logo: logo1 },
  { id: 35, title: '技术交流平台', description: '员工可参与跨区域、跨业务的技术交流与分享。', logo: logo2 },
  { id: 36, title: '内部创新孵化', description: '博世鼓励内部创新、创业项目孵化。', logo: logo3 },
  { id: 37, title: '国际派遣计划', description: '博世提供海外派遣、轮岗机会，让人国际化成长。', logo: logo1 },
  { id: 38, title: '多元职业路径', description: '在博世，无论你是技术、管理、市场方向，都有路径。', logo: logo2 },
  { id: 39, title: '跨部门协作体验', description: '不同业务线之间协作，为员工提供跨界视角。', logo: logo3 },
  { id: 40, title: '系统培训体系', description: '博世通常会提供系统化的入职与在职培训体系。', logo: logo1 },
  { id: 41, title: '学习型组织氛围', description: '员工被鼓励不断学习、挑战自我、拥抱新知识。', logo: logo2 },
  { id: 42, title: '成果认可机制', description: '优秀成果能得到公司或团队认可、奖励。', logo: logo3 },
  { id: 43, title: '创意表达机会', description: '在项目中有机会提出创意、进行实践。', logo: logo1 },
  { id: 44, title: '职能轮岗制度', description: '轮岗制度帮助员工拓展视野与能力。', logo: logo2 },
  { id: 45, title: '透明的绩效考核', description: '公正、透明的绩效体系让员工清楚自己的定位。', logo: logo3 },
  { id: 46, title: '灵活工作机制', description: '在不同岗位可能享有一定的弹性工作制度。', logo: logo1 },
  { id: 47, title: '国际文化交流', description: '与来自不同国家同事合作，拓展文化视野。', logo: logo2 },
  { id: 48, title: '丰富的内部活动', description: '团队建设、年度活动、兴趣小组丰富员工生活。', logo: logo3 },
  { id: 49, title: '健康与福利保障', description: '员工可以享受系统的健康、保险等福利机制。', logo: logo1 },
  { id: 50, title: '家庭友好政策', description: '对有家庭责任的员工可能提供亲子支持或弹性安排。', logo: logo2 },
  { id: 51, title: '工作环境优越', description: '办公场地、设备通常现代化、舒适。', logo: logo3 },
  { id: 52, title: '安全第一思维', description: '在工业、制造、实验环境，博世强调安全标准。', logo: logo1 },
  { id: 53, title: '标准化流程', description: '规范流程与制度帮助效率与质量保障。', logo: logo2 },
  { id: 54, title: '品牌背书加分', description: '来自博世这个品牌对个人简历也有加分效应。', logo: logo3 },
  { id: 55, title: '高质量合作伙伴', description: '与一流高校、企业、研究机构合作，从项目中受益。', logo: logo1 },
  { id: 56, title: '参与未来前沿领域', description: '博世在 AI、自动驾驶、能源科技等前沿领域布局。', logo: logo2 },
  { id: 57, title: '积极响应全球趋势', description: '博世紧跟工业4.0、绿色发展、数字化趋势。', logo: logo3 },
  { id: 58, title: '强大的品牌认知度', description: '博世是公众熟知、值得信赖的高科技品牌。', logo: logo1 },
  { id: 59, title: '产品覆盖日常生活', description: '博世产品涉及日常家庭、出行、生活多数场景。', logo: logo2 },
  { id: 60, title: '科技与人性结合', description: '博世强调科技应服务于人的幸福，而非冷冰工具。', logo: logo3 },
  { id: 61, title: '客户导向文化', description: '博世重视客户反馈，将其视为产品优化关键。', logo: logo1 },
  { id: 62, title: '高标准质量管理', description: '在产品和服务上保持高标准的质量认证和控制。', logo: logo2 },
  { id: 63, title: '快速响应机制', description: '在市场、客户或技术变化中，博世具备快速响应能力。', logo: logo3 },
  { id: 64, title: '持续改进文化', description: '不断反思、优化、精进，是博世文化的一部分。', logo: logo1 },
  { id: 65, title: '跨文化团队合作', description: '国际团队协作让你习得跨文化沟通能力。', logo: logo2 },
  { id: 66, title: '职业稳定性', description: '在大企业体系下，具有相对稳定的职业保障。', logo: logo3 },
  { id: 67, title: '与行业顶尖竞争', description: '博世经常参与或引领行业技术标准与竞争。', logo: logo1 },
  { id: 68, title: '可见的社会影响力', description: '博世的很多产品与项目直接影响社会发展。', logo: logo2 },
  { id: 69, title: '实践可持续技术项目', description: '你可能参与减碳、能源效率提升等项目。', logo: logo3 },
  { id: 70, title: '长寿命产品价值观', description: '博世的产品设计注重耐用性与可维护性。', logo: logo1 },
  { id: 71, title: '本地化制造能力', description: '在中国设有生产基地，更贴近市场与用户。', logo: logo2 },
  { id: 72, title: '全球采购网络', description: '博世具备全球采购与供应链能力，资源整合强。', logo: logo3 },
  { id: 73, title: '绿色制造推进', description: '制造过程中推行节能减排与绿色标准。', logo: logo1 },
  { id: 74, title: '智能制造与自动化', description: '博世内部也在使用智能制造技术进行自我升级。', logo: logo2 },
  { id: 75, title: '工业 4.0 实践者', description: '在智能工厂、数字化车间上有真实落地经验。', logo: logo3 },
  { id: 76, title: '精益生产理念', description: '博世推行精益、六西格玛等管理理念以提升效率。', logo: logo1 },
  { id: 77, title: '客户定制化能力', description: '能为客户提供定制化方案，而非一刀切产品。', logo: logo2 },
  { id: 78, title: '开放平台生态', description: '在 IoT、平台生态上愿与合作伙伴共建。', logo: logo3 },
  { id: 79, title: '强调知识产权', description: '在专利、技术保护方面严格，尊重创新。', logo: logo1 },
  { id: 80, title: '国际项目经验积累', description: '能参与跨国项目，获得国际视野。', logo: logo2 },
  { id: 81, title: '员工荣誉传承', description: '博世内部有优秀员工、团队表彰机制。', logo: logo3 },
  { id: 82, title: '成就感可视化', description: '项目成果直观可见，可以看到"自己做的东西在世界上被用到"。', logo: logo1 },
  { id: 83, title: '参与标准制定', description: '在行业标准、技术标准制定中有代表性声音。', logo: logo2 },
  { id: 84, title: '行业先锋角色', description: '在许多业务领域，博世都是技术与市场的先锋。', logo: logo3 },
  { id: 85, title: '自主决策空间', description: '虽在大公司架构中，仍赋予项目或团队一定自主权。', logo: logo1 },
  { id: 86, title: '透明晋升通道', description: '晋升、发展路径在公司内部较为透明。', logo: logo2 },
  { id: 87, title: '国际交流机会', description: '有机会到德国或其他国家交流、学习。', logo: logo3 },
  { id: 88, title: '多语种环境', description: '英语、德语或其他语种成为工作环境的一部分。', logo: logo1 },
  { id: 89, title: '高标准安全保障', description: '企业对员工的安全保护制度严格，减少风险。', logo: logo2 },
  { id: 90, title: '品牌自豪感', description: '身为博世人，背后有强大品牌支持与认同感。', logo: logo3 },
  { id: 91, title: '公信力企业形象', description: '博世在大众、行业中具有良好口碑与信任度。', logo: logo1 },
  { id: 92, title: '营造创新文化', description: '鼓励试错、创新，让员工敢于挑战。', logo: logo2 },
  { id: 93, title: '多学科交叉机会', description: '你可能跨机械、电子、软件、控制等多个学科协作。', logo: logo3 },
  { id: 94, title: '国际化视野塑造', description: '在博世工作自然塑造你具备国际化思维。', logo: logo1 },
  { id: 95, title: '全球客户互动', description: '与全球客户、合作伙伴互动交流经验。', logo: logo2 },
  { id: 96, title: '卓越科技影响力', description: '博世的科技、解决方案在世界许多地方落地。', logo: logo3 },
  { id: 97, title: '面向未来的业务布局', description: '博世在新能源、自动驾驶、智慧家居等未来方向持续投入。', logo: logo1 },
  { id: 98, title: '长期信任背后资本结构', description: '博世大部分股份由基金会持有，以社会责任为导向。', logo: logo2 },
  { id: 99, title: '历史底蕴与品牌传承', description: '博世有悠久历史，从 1886 年创业至今，是百年科技公司。', logo: logo3 },
  { id: 100, title: '与优秀人为伍', description: '在博世，你将与国内外顶尖人才合作、成长、成就未来。', logo: logo1 }
])

// 随机选择显示在滚动条中的项目
const getRandomReasons = (count) => {
  const shuffled = [...allReasons.value].sort(() => 0.5 - Math.random())
  return shuffled.slice(0, count)
}

const scrollItemsRow1 = ref(getRandomReasons(6))
const scrollItemsRow2 = ref(getRandomReasons(6))
// 导入轮播图图片
import lunbo1 from '../assets/images/lunbo1.jpg'
import lunbo2 from '../assets/images/lunbo2.jpg'
import lunbo3 from '../assets/images/lunbo3.jpg'

// 导入100个理由的logo图片
import logo1 from '../assets/images/100-reasons/logo1.png'
import logo2 from '../assets/images/100-reasons/logo2.png'
import logo3 from '../assets/images/100-reasons/logo3.png'

// 导入新闻文章图片
import article1Image0 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._0.png'
import article1Image1 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._1.png'
import article1Image2 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._2.png'
import article1Image3 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._3.png'
import article2Image0 from '../assets/file/article2/image_博世投入25亿欧元发力AI，事关..._0.png'
import article2Image1 from '../assets/file/article2/image_博世投入25亿欧元发力AI，事关..._1.png'
import article2Image2 from '../assets/file/article2/image_博世投入25亿欧元发力AI，事关..._2.png'
import boschHeadquarter from '../assets/images/bosch-cn-headquarter_res_1600x900.webp'

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

// Navigate to reasons detail page
const goToReasonsDetail = () => {
  router.push('/reasons-detail')
}

// Auto-scroll animation
const startAutoScroll = () => {
  const itemWidth = 265 // width of each item + gap (250 + 15)
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
  height: 60px; /* 增加顶部留白高度，为logo留出更多空间 */
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
  min-height: calc(100vh - 64px); /* 确保内容区域填满屏幕(60px spacer + 4px rainbow) */
  display: flex;
  flex-direction: column;
}

.content-wrapper {
  max-width: 100%;
  margin: 0 auto;
  width: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: calc(100vh - 64px - 88px); /* 减去header、padding和底部导航 */
}

/* Carousel Section Container */
.carousel-section {
  margin-top: 20px; /* 往下移动轮播图 */
  margin-bottom: 20px;
  flex-shrink: 0; /* 防止被压缩 */
}

/* Hero Banner */
.hero-banner {
  background: white;
  border-radius: 16px;
  overflow: hidden;
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

/* Carousel Dots - 独立在轮播图下方 */
.carousel-dots-wrapper {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 12px 0;
  margin-top: 12px; /* 与轮播图保持间距 */
  background: transparent; /* 透明背景 */
}

.carousel-dots-wrapper .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #D0D0D0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.carousel-dots-wrapper .dot.active {
  width: 20px;
  border-radius: 4px;
  background: #333;
}

/* Feature Cards */
.feature-cards {
  display: flex;
  flex-direction: column;
  gap: 0;
  margin-top: auto; /* 使用margin-top:auto推到底部 */
  margin-bottom: 10px; /* 与底部保持小间距 */
  width: 100%;
  z-index: 9;
}

.feature-cards .feature-card {
  width: 100%; /* 确保卡片占满容器宽度 */
}

.feature-card {
  border-radius: 16px;
  padding: 28px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s ease;
  cursor: pointer;
  height: 120px; /* 增加高度 */
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
  padding-top: 36px; /* 适当增加padding */
  margin-bottom: -8px;
  z-index: 2;
}

/* 最后一个卡片 */
.feature-card:last-child {
  border-radius: 16px;
  padding-top: 36px; /* 适当增加padding */
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
  padding: 28px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s ease;
  cursor: pointer;
  height: 120px; /* 增加高度 */
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
  margin-bottom: 4px;
  padding: 4px 0;
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
  min-width: 250px;
  height: 90px;
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

/* 引号图标 - 放在左上角缺角位置 */
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
  align-items: center;
  gap: 10px;
  height: 50px;
  padding: 0 12px;
  margin-top: 20px;
}

.item-logo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
  background: white;
  padding: 3px;
}

.item-logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.item-text {
  font-size: 16px;
  font-weight: 500;
  color: #333;
  text-align: left;
  flex: 1;
  line-height: 1.3;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* 编号样式 - 与标题左对齐 */
.item-number {
  position: absolute;
  top: 8px;
  left: 62px;
  font-size: 10px;
  color: #666;
  z-index: 1;
  font-weight: 400;
  letter-spacing: 0.5px;
}

/* 描述样式 */
.item-description {
  position: absolute;
  bottom: 10px;
  left: 12px;
  right: 12px;
  font-size: 11px;
  color: #888;
  line-height: 1.3;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  line-clamp: 1;
  -webkit-box-orient: vertical;
  white-space: normal;
  text-align: left;
  z-index: 1;
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
  background: white;
}

.gravity-carousel .carousel-dots .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #D0D0D0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.gravity-carousel .carousel-dots .dot.active {
  width: 20px;
  border-radius: 4px;
  background: #333;
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
  line-clamp: 2;
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
  line-clamp: 2;
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

.news-carousel-dots .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #D0D0D0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.news-carousel-dots .dot.active {
  width: 20px;
  border-radius: 4px;
  background: #333;
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
    line-clamp: 3;
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

/* 小屏幕高度设备特殊处理 (iPhone 12 Pro等) */
@media (max-height: 850px) {
  .carousel-section {
    margin-top: 10px; /* 减少顶部间距 */
    margin-bottom: 10px;
  }

  .carousel-wrapper {
    height: 280px; /* 减少轮播图高度 */
  }

  .feature-card {
    height: 100px; /* 减少卡片高度 */
    padding: 20px 16px;
  }

  .feature-card:nth-child(2),
  .feature-card:last-child {
    padding-top: 28px; /* 减少层叠间距 */
  }

  .card-title {
    font-size: 18px;
  }

  .card-subtitle {
    font-size: 14px;
  }
}

/* 超小屏幕高度设备 */
@media (max-height: 700px) {
  .spacer {
    height: 45px; /* 减少顶部留白 */
  }

  .carousel-wrapper {
    height: 240px; /* 进一步减少轮播图高度 */
  }

  .feature-card {
    height: 90px; /* 进一步减少卡片高度 */
    padding: 18px 16px;
  }

  .carousel-dots-wrapper {
    padding: 8px 0;
    margin-top: 8px;
  }
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
    position: relative; /* 改回相对定位 */
    margin-top: 20px; /* 正常的顶部间距 */
    margin-bottom: 0;
    width: 100%;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }

  .feature-cards .feature-card {
    width: auto; /* 恢复自动宽度 */
    height: auto; /* 恢复自动高度 */
    margin-bottom: 0; /* 移除层叠效果 */
    padding-top: 24px !important; /* 统一padding */
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