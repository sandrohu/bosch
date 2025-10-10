<template>
  <div class="news-detail-container">
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
        <div class="action-buttons">
          <button :class="['action-button', 'like-button', { 'liked': isLiked }]" @click="handleLike">
            <svg width="20" height="20" viewBox="0 0 24 24" :fill="isLiked ? '#FF6B6B' : 'none'" :stroke="isLiked ? '#FF6B6B' : 'currentColor'">
              <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span v-if="likeCount > 0" class="like-count">{{ likeCount }}</span>
          </button>
          <button class="action-button" @click="handleShare">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/>
            </svg>
          </button>
        </div>
      </div>
    </header>

    <!-- Copy Success Toast -->
    <transition name="toast">
      <div v-if="showToast" class="toast">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
          <path d="M20 6L9 17l-5-5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>链接已复制到剪贴板</span>
      </div>
    </transition>

    <!-- News Detail -->
    <main class="news-detail" v-if="currentNews">
      <!-- Hero Image -->
      <div class="hero-image">
        <img :src="currentNews.image" :alt="currentNews.title" />
      </div>

      <!-- Article Content -->
      <article class="article-content">
        <!-- Meta Info -->
        <div class="meta-info">
          <span class="category">{{ currentNews.category }}</span>
          <span class="date">{{ currentNews.date }}</span>
        </div>

        <!-- Title -->
        <h1 class="article-title">{{ currentNews.title }}</h1>

        <!-- Full Content -->
        <div class="article-body">
          <p class="lead">{{ currentNews.content }}</p>

          <!-- Article 1 - Forbes Content -->
          <div v-if="newsId === '0'" class="article-special">
            <div class="highlight-box">
              <p>🎉 博世荣获福布斯2025「中国年度最佳雇主」及「年度最佳ESG实践雇主」</p>
            </div>

            <p>这份荣誉，属于每一位敢拼敢闯的博世人</p>

            <p>✊ 我们相信：真正的进步，源自对员工的充分信任，以及对创新的执着坚守。</p>

            <p>在这里，技术不止于想象，成长不设边界。</p>

            <!-- Additional Images -->
            <div class="image-gallery" v-if="currentNews.detailImages">
              <img
                v-for="(img, index) in currentNews.detailImages"
                :key="index"
                :src="img"
                :alt="`详情图片${index + 1}`"
                class="gallery-image"
              />
            </div>

            <div class="recruitment-section">
              <h3>✅ 2025博世中国秋招进行中</h3>
              <h3>✅ 博世中国海外招聘·美国专场即将开启</h3>

              <p>如果你也期待：</p>
              <ul>
                <li>🌟 与卓越团队共同成就</li>
                <li>🌟 在职场中快速成长</li>
                <li>🌟 用专业能力创造价值</li>
              </ul>

              <p class="cta">诚邀您加入博世，与2025福布斯中国最佳雇主一起<br/>
              探索职场意义，创造更多可能！</p>

              <p class="question">👀 也期待您与我们聊一聊：什么是您心中"有意义的职场"？</p>
            </div>
          </div>

          <!-- Article 2 - AI Investment Content -->
          <div v-else-if="newsId === '1'" class="article-special">
            <div class="highlight-box">
              <p>💰 博世投入25亿欧元发力AI，1500+欧洲专利加持，改变你我生活！</p>
            </div>

            <!-- Additional Images -->
            <div class="image-gallery" v-if="currentNews.detailImages">
              <img
                v-for="(img, index) in currentNews.detailImages"
                :key="index"
                :src="img"
                :alt="`详情图片${index + 1}`"
                class="gallery-image"
              />
            </div>

            <div class="ai-benefits">
              <h3>AI赋能未来生活</h3>
              <div class="benefit-item">
                <span class="icon">🚗</span>
                <div>
                  <h4>自动驾驶更安全</h4>
                  <p>先进的AI算法让驾驶辅助系统更智能，提升道路安全性</p>
                </div>
              </div>

              <div class="benefit-item">
                <span class="icon">🏭</span>
                <div>
                  <h4>制造质量更可靠</h4>
                  <p>AI质检系统大幅提升产品质量，降低缺陷率</p>
                </div>
              </div>

              <div class="benefit-item">
                <span class="icon">🏠</span>
                <div>
                  <h4>日常生活更便利</h4>
                  <p>智能家居解决方案让生活更加舒适便捷</p>
                </div>
              </div>

              <div class="benefit-item">
                <span class="icon">🧠</span>
                <div>
                  <h4>人工智能人才已就位</h4>
                  <p>全球顶尖AI专家团队，推动技术创新</p>
                </div>
              </div>
            </div>

            <p class="conclusion">人工智能时代将至？你我都是受益者！</p>
          </div>

          <!-- Default Content for Other Articles -->
          <div v-else class="article-default">
            <p>{{ currentNews.fullContent || currentNews.content }}</p>

            <!-- Additional Images -->
            <div class="image-gallery" v-if="currentNews.detailImages">
              <img
                v-for="(img, index) in currentNews.detailImages"
                :key="index"
                :src="img"
                :alt="`详情图片${index + 1}`"
                class="gallery-image"
              />
            </div>
          </div>
        </div>

      </article>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

// Article 1 images
import article1Image0 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._0.png'
import article1Image1 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._1.png'
import article1Image2 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._2.png'
import article1Image3 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._3.png'
import article1Image4 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._4.png'
import article1Image5 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._5.png'
import article1Image6 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._6.png'
import article1Image7 from '../assets/file/article1/image_2025福布斯中国最佳雇主，我们..._7.png'

// Article 2 images
import article2Image0 from '../assets/file/article2/image_博世投入25亿欧元发力AI，事关..._0.png'
import article2Image1 from '../assets/file/article2/image_博世投入25亿欧元发力AI，事关..._1.png'
import article2Image2 from '../assets/file/article2/image_博世投入25亿欧元发力AI，事关..._2.png'
import article2Image3 from '../assets/file/article2/image_博世投入25亿欧元发力AI，事关..._3.png'
import article2Image4 from '../assets/file/article2/image_博世投入25亿欧元发力AI，事关..._4.png'

// Other images
import boschHeadquarterImage from '../assets/images/bosch-cn-headquarter_res_1600x900.webp'
import mobilityImage from '../assets/images/mobility-solutions-web-portal_res_1280x720.webp'
import jumpImage from '../assets/images/jump.jpg'

const route = useRoute()
const router = useRouter()

const newsId = computed(() => route.params.id)
const showToast = ref(false)
const isLiked = ref(false)
const likeCount = ref(0)

const newsData = ref([
  {
    image: article1Image0,
    category: '企业荣誉',
    date: '2025-09-28',
    title: '2025福布斯中国最佳雇主，我们上榜啦！',
    content: '博世荣获福布斯2025「中国年度最佳雇主」及「年度最佳ESG实践雇主」',
    detailImages: [
      article1Image1,
      article1Image2,
      article1Image3,
      article1Image4,
      article1Image5,
      article1Image6,
      article1Image7
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
      article2Image2,
      article2Image3,
      article2Image4
    ]
  },
  {
    image: boschHeadquarterImage,
    category: '可持续发展',
    date: '2025-09-20',
    title: '博世中国区实现碳中和目标，引领行业绿色转型',
    content: '博世在中国的所有工厂已全面实现碳中和，成为行业绿色转型的典范',
    fullContent: '博世集团在中国的所有工厂已经全面实现碳中和目标，这标志着博世在可持续发展道路上迈出了重要一步。通过采用可再生能源、提高能源效率、实施创新的环保技术，博世不仅减少了自身的碳足迹，还为整个行业树立了绿色转型的典范。这一成就体现了博世"科技成就生活之美"的理念，以及对环境保护的坚定承诺。'
  },
  {
    image: mobilityImage,
    category: '产品发布',
    date: '2025-09-15',
    title: '博世推出新一代智能驾驶辅助系统',
    content: '全新智能驾驶辅助系统搭载先进传感器技术，为用户提供更安全、更智能的驾驶体验',
    fullContent: '博世最新推出的智能驾驶辅助系统集成了毫米波雷达、摄像头和超声波传感器等多种先进技术，能够实现L2+级别的自动驾驶功能。系统包括自适应巡航控制、车道保持辅助、自动紧急制动、盲点监测等多项功能，大大提升了驾驶的安全性和舒适性。这套系统已经在多家主流汽车制造商的新车型上得到应用。'
  },
  {
    image: jumpImage,
    category: '校园招聘',
    date: '2025-09-10',
    title: '2025博世中国秋季校园招聘全面启动',
    content: '博世中国2025秋季校园招聘正式开启，诚邀优秀学子加入，共创美好未来',
    fullContent: '博世中国2025年秋季校园招聘已经全面启动，面向应届毕业生开放研发、制造、销售、管理等多个领域的职位。我们提供完善的培训体系、广阔的发展平台和具有竞争力的薪酬福利。加入博世，你将有机会参与前沿技术的研发，与全球顶尖团队合作，在这里实现个人价值，共同创造美好未来。'
  }
])

const currentNews = computed(() => {
  const index = parseInt(newsId.value)
  return newsData.value[index] || null
})

const goBack = () => {
  router.back()
}

const handleLike = () => {
  // 切换点赞状态
  isLiked.value = !isLiked.value

  // 更新点赞数
  if (isLiked.value) {
    likeCount.value++
  } else {
    likeCount.value = Math.max(0, likeCount.value - 1)
  }

  // 这里可以添加发送到服务器的逻辑
  console.log(isLiked.value ? '已点赞' : '取消点赞')
}

const handleShare = async () => {
  try {
    // 获取当前页面的完整URL
    const currentUrl = window.location.href

    // 尝试使用现代的 Clipboard API
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(currentUrl)
    } else {
      // 降级方案：使用传统的方法
      const textArea = document.createElement('textarea')
      textArea.value = currentUrl
      textArea.style.position = 'fixed'
      textArea.style.left = '-999999px'
      textArea.style.top = '-999999px'
      document.body.appendChild(textArea)
      textArea.focus()
      textArea.select()
      document.execCommand('copy')
      document.body.removeChild(textArea)
    }

    // 显示提示
    showToast.value = true

    // 3秒后自动隐藏提示
    setTimeout(() => {
      showToast.value = false
    }, 3000)
  } catch (error) {
    console.error('复制失败:', error)
    alert('复制链接失败，请手动复制')
  }
}
</script>

<style scoped>
.news-detail-container {
  min-height: 100vh;
  background: #f5f5f5;
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

/* Action Buttons */
.action-buttons {
  display: flex;
  gap: 8px;
}

.action-button {
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

.action-button:hover {
  background: #f5f5f5;
  border-radius: 8px;
}

.action-button:active {
  background: #ececec;
  border-radius: 8px;
}

.action-button svg {
  width: 18px;
  height: 18px;
}

/* Like Button Styles */
.like-button {
  position: relative;
  transition: all 0.3s ease;
}

.like-button.liked {
  background: #FFE5E5;
  color: #FF6B6B;
}

.like-button.liked:hover {
  background: #FFD5D5;
}

.like-button.liked:active {
  background: #FFC5C5;
}

.like-count {
  background: #FF6B6B;
  color: white;
  padding: 2px 6px;
  border-radius: 10px;
  font-size: 11px;
  font-weight: 600;
  margin-left: 2px;
  animation: countBounce 0.3s ease;
}

@keyframes countBounce {
  0% {
    transform: scale(0.8);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

/* Like button animation when clicked */
.like-button:active svg {
  animation: likeAnimation 0.4s ease;
}

@keyframes likeAnimation {
  0% {
    transform: scale(1);
  }
  25% {
    transform: scale(1.2) rotate(-5deg);
  }
  50% {
    transform: scale(1.1) rotate(5deg);
  }
  75% {
    transform: scale(1.15) rotate(-2deg);
  }
  100% {
    transform: scale(1);
  }
}

/* Hero Image */
.hero-image {
  width: 100%;
  height: 240px;
  overflow: hidden;
}

.hero-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Article Content */
.article-content {
  background: white;
  padding: 20px;
  margin-top: -20px;
  border-radius: 20px 20px 0 0;
  position: relative;
}

.meta-info {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.category {
  background: #5AA397;
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

.date {
  color: #999;
  font-size: 12px;
}

.article-title {
  font-size: 24px;
  font-weight: 700;
  color: #333;
  line-height: 1.4;
  margin-bottom: 20px;
}

.article-body {
  font-size: 16px;
  line-height: 1.8;
  color: #333;
}

.lead {
  font-size: 18px;
  font-weight: 500;
  color: #555;
  margin-bottom: 24px;
  line-height: 1.6;
}

/* Special Content Styles */
.highlight-box {
  background: linear-gradient(135deg, #5AA397 0%, #8BCFC5 100%);
  color: white;
  padding: 16px;
  border-radius: 12px;
  margin: 20px 0;
  font-size: 16px;
  font-weight: 500;
}

.recruitment-section {
  margin-top: 32px;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 12px;
}

.recruitment-section h3 {
  color: #5AA397;
  margin-bottom: 12px;
  font-size: 18px;
}

.recruitment-section ul {
  list-style: none;
  padding: 0;
  margin: 16px 0;
}

.recruitment-section li {
  margin-bottom: 8px;
}

.cta {
  font-weight: 600;
  color: #333;
  margin-top: 20px;
  text-align: center;
}

.question {
  color: #5AA397;
  font-weight: 500;
  margin-top: 16px;
  text-align: center;
}

/* AI Benefits */
.ai-benefits {
  margin: 32px 0;
}

.ai-benefits h3 {
  font-size: 20px;
  color: #333;
  margin-bottom: 20px;
}

.benefit-item {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
  padding: 16px;
  background: #f9f9f9;
  border-radius: 12px;
}

.benefit-item .icon {
  font-size: 32px;
  flex-shrink: 0;
}

.benefit-item h4 {
  font-size: 16px;
  color: #333;
  margin-bottom: 8px;
}

.benefit-item p {
  font-size: 14px;
  color: #666;
  line-height: 1.5;
}

.conclusion {
  font-size: 18px;
  font-weight: 600;
  color: #5AA397;
  text-align: center;
  margin: 32px 0;
}

/* Image Gallery */
.image-gallery {
  margin: 24px 0;
}

.gallery-image {
  width: 100%;
  margin-bottom: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}


/* Toast Notification */
.toast {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.85);
  color: white;
  padding: 16px 24px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 15px;
  z-index: 1000;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.toast svg {
  flex-shrink: 0;
}

/* Toast transition animation */
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  opacity: 0;
  transform: translate(-50%, -50%) scale(0.8);
}

.toast-leave-to {
  opacity: 0;
  transform: translate(-50%, -50%) scale(0.8);
}

/* Responsive Design */
@media (min-width: 768px) {
  .header-content {
    height: 70px;
    padding: 0 24px;
  }

  .back-button,
  .action-button {
    padding: 10px 16px;
    font-size: 15px;
  }

  .hero-image {
    height: 400px;
  }

  .article-content {
    max-width: 800px;
    margin: -40px auto 0;
    padding: 32px;
  }

  .article-title {
    font-size: 32px;
  }

  .article-body {
    font-size: 17px;
  }
}

@media (min-width: 1024px) {
  .header-content {
    height: 80px;
    padding: 0 40px;
  }

  .hero-image {
    height: 500px;
  }

  .article-content {
    padding: 40px;
  }
}
</style>