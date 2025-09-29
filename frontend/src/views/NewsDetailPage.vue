<template>
  <div class="news-detail-container">
    <!-- Header -->
    <header class="header">
      <button class="back-btn" @click="goBack">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="#333">
          <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/>
        </svg>
      </button>
      <h1 class="page-title">新闻详情</h1>
      <div class="header-right"></div>
    </header>

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

        <!-- Share Section -->
        <div class="share-section">
          <button class="share-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/>
            </svg>
            分享
          </button>
        </div>
      </article>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const newsId = computed(() => route.params.id)

const newsData = ref([
  {
    image: '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._0.png',
    category: '企业荣誉',
    date: '2025-09-28',
    title: '2025福布斯中国最佳雇主，我们上榜啦！',
    content: '博世荣获福布斯2025「中国年度最佳雇主」及「年度最佳ESG实践雇主」',
    detailImages: [
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._1.png',
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._2.png',
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._3.png',
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._4.png',
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._5.png',
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._6.png',
      '/src/assets/file/article1/image_2025福布斯中国最佳雇主，我们..._7.png'
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
      '/src/assets/file/article2/image_博世投入25亿欧元发力AI，事关..._2.png',
      '/src/assets/file/article2/image_博世投入25亿欧元发力AI，事关..._3.png',
      '/src/assets/file/article2/image_博世投入25亿欧元发力AI，事关..._4.png'
    ]
  },
  {
    image: '/src/assets/images/bosch-cn-headquarter_res_1600x900.webp',
    category: '可持续发展',
    date: '2025-09-20',
    title: '博世中国区实现碳中和目标，引领行业绿色转型',
    content: '博世在中国的所有工厂已全面实现碳中和，成为行业绿色转型的典范',
    fullContent: '博世集团在中国的所有工厂已经全面实现碳中和目标，这标志着博世在可持续发展道路上迈出了重要一步。通过采用可再生能源、提高能源效率、实施创新的环保技术，博世不仅减少了自身的碳足迹，还为整个行业树立了绿色转型的典范。这一成就体现了博世"科技成就生活之美"的理念，以及对环境保护的坚定承诺。'
  },
  {
    image: '/src/assets/images/mobility-solutions-web-portal_res_1280x720.webp',
    category: '产品发布',
    date: '2025-09-15',
    title: '博世推出新一代智能驾驶辅助系统',
    content: '全新智能驾驶辅助系统搭载先进传感器技术，为用户提供更安全、更智能的驾驶体验',
    fullContent: '博世最新推出的智能驾驶辅助系统集成了毫米波雷达、摄像头和超声波传感器等多种先进技术，能够实现L2+级别的自动驾驶功能。系统包括自适应巡航控制、车道保持辅助、自动紧急制动、盲点监测等多项功能，大大提升了驾驶的安全性和舒适性。这套系统已经在多家主流汽车制造商的新车型上得到应用。'
  },
  {
    image: '/src/assets/images/jump.jpg',
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
</script>

<style scoped>
.news-detail-container {
  min-height: 100vh;
  background: #f5f5f5;
}

/* Header */
.header {
  position: sticky;
  top: 0;
  background: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.back-btn {
  background: none;
  border: none;
  padding: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.page-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  flex: 1;
  text-align: center;
}

.header-right {
  width: 40px;
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

/* Share Section */
.share-section {
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid #e0e0e0;
  text-align: center;
}

.share-btn {
  background: #5AA397;
  color: white;
  border: none;
  padding: 12px 32px;
  border-radius: 24px;
  font-size: 16px;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.share-btn:hover {
  background: #4A8A7D;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Responsive Design */
@media (min-width: 768px) {
  .header {
    padding: 20px 40px;
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
  .hero-image {
    height: 500px;
  }

  .article-content {
    padding: 40px;
  }
}
</style>