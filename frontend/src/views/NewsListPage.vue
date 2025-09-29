<template>
  <div class="news-list-container">
    <!-- Header -->
    <header class="header">
      <button class="back-btn" @click="goBack">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="#333">
          <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/>
        </svg>
      </button>
      <h1 class="page-title">热文追踪</h1>
      <div class="header-right"></div>
    </header>

    <!-- News List -->
    <main class="news-list">
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
    </main>
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

/* News List */
.news-list {
  padding: 16px;
}

.news-item {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 16px;
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
  height: 200px;
  overflow: hidden;
}

.news-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.news-content {
  padding: 20px;
}

.news-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.news-category {
  background: #5AA397;
  color: white;
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
}

.news-excerpt {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Tablet and Desktop */
@media (min-width: 768px) {
  .header {
    padding: 20px 40px;
  }

  .page-title {
    font-size: 20px;
  }

  .news-list {
    padding: 24px;
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 24px;
  }

  .news-item {
    margin-bottom: 0;
  }

  .news-image {
    height: 240px;
  }
}

@media (min-width: 1024px) {
  .news-list {
    padding: 32px;
    gap: 32px;
  }
}
</style>