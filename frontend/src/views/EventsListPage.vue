<template>
  <div class="events-list-container">
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
      <!-- Tab Navigation -->
      <div class="tab-navigation">
        <button
          v-for="tab in tabs"
          :key="tab.key"
          :class="['tab-item', { active: activeTab === tab.key }]"
          @click="switchTab(tab.key)"
        >
          {{ tab.label }}
        </button>
      </div>

      <!-- Events List -->
      <div class="events-list">
        <article
          v-for="(event, index) in filteredEvents"
          :key="index"
          class="event-card"
          @click="goToDetail(event)"
        >
          <div class="event-image">
            <img :src="event.image" :alt="event.title" />
          </div>
          <div class="event-content">
            <h3 class="event-title">{{ event.title }}</h3>
            <div class="event-meta">
              <div class="event-location">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                <span>{{ event.location }}</span>
              </div>
              <div class="event-time">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/>
                  <polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>{{ event.time }}</span>
              </div>
            </div>
            <div class="event-date-tag">
              <span class="date-day">{{ event.dateDay }}</span>
              <span class="date-month">{{ event.dateMonth }}</span>
            </div>
            <button class="event-register-btn" @click.stop="registerEvent(event)">
              查看详情
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="9 18 15 12 9 6"/>
              </svg>
            </button>
          </div>
        </article>

        <!-- Empty State -->
        <div v-if="filteredEvents.length === 0" class="empty-state">
          <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="1.5">
            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
            <line x1="9" y1="9" x2="15" y2="9"/>
            <line x1="9" y1="13" x2="15" y2="13"/>
            <line x1="9" y1="17" x2="13" y2="17"/>
          </svg>
          <p>暂无相关活动</p>
        </div>
      </div>
    </main>

    <!-- Bottom Navigation (Mobile Only) -->
    <nav class="bottom-nav mobile-only">
      <button class="nav-item" @click="navigateToHome">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-1-click.png" alt="首页" class="nav-icon-active" />
          <img src="../assets/images/daohang-1.png" alt="首页" class="nav-icon-default" />
        </div>
        <span>首页</span>
      </button>
      <button class="nav-item active" @click="navigateToEvents">
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
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import boschHeadquarterImage from '../assets/images/bosch-cn-headquarter_res_1600x900.webp'

const router = useRouter()

// Tab配置
const tabs = ref([
  { key: 'all', label: '全部' },
  { key: 'lecture', label: '校园宣讲会' },
  { key: 'forum', label: '博士生论坛' }
])

// 当前激活的tab
const activeTab = ref('all')

// 所有活动数据
const events = ref([
  {
    id: 1,
    type: 'lecture',
    title: '中国科学技术大学 宣讲会',
    location: '西区学生活动中心一楼报告厅',
    time: '09:00-12:00',
    dateDay: '08',
    dateMonth: '12-2025',
    image: boschHeadquarterImage,
    description: '博世中国2025秋季校园招聘宣讲会，诚邀优秀学子参加。'
  },
  {
    id: 2,
    type: 'lecture',
    title: '清华大学 宣讲会',
    location: '经管学院伟伦楼报告厅',
    time: '14:00-17:00',
    dateDay: '10',
    dateMonth: '12-2025',
    image: boschHeadquarterImage,
    description: '博世集团清华大学专场宣讲会，期待与你相遇。'
  },
  {
    id: 3,
    type: 'forum',
    title: '博士生论坛 - AI与未来',
    location: '博世中国研发中心',
    time: '09:00-17:00',
    dateDay: '15',
    dateMonth: '12-2025',
    image: boschHeadquarterImage,
    description: '探讨人工智能在工业4.0中的应用与发展前景。'
  },
  {
    id: 4,
    type: 'lecture',
    title: '上海交通大学 宣讲会',
    location: '闵行校区陈瑞球楼100号',
    time: '13:30-16:30',
    dateDay: '18',
    dateMonth: '12-2025',
    image: boschHeadquarterImage,
    description: '博世集团上海交通大学校园宣讲会。'
  },
  {
    id: 5,
    type: 'forum',
    title: '博士生论坛 - 智能制造',
    location: '博世苏州工厂',
    time: '10:00-16:00',
    dateDay: '20',
    dateMonth: '12-2025',
    image: boschHeadquarterImage,
    description: '智能制造技术创新与实践分享。'
  },
  {
    id: 6,
    type: 'lecture',
    title: '浙江大学 宣讲会',
    location: '紫金港校区国际会议中心',
    time: '14:00-17:00',
    dateDay: '22',
    dateMonth: '12-2025',
    image: boschHeadquarterImage,
    description: '博世集团浙江大学专场招聘宣讲会。'
  },
  {
    id: 7,
    type: 'forum',
    title: '博士生论坛 - 新能源技术',
    location: '博世中国创新中心',
    time: '09:30-16:30',
    dateDay: '25',
    dateMonth: '12-2025',
    image: boschHeadquarterImage,
    description: '新能源汽车技术发展趋势与挑战。'
  },
  {
    id: 8,
    type: 'lecture',
    title: '北京大学 宣讲会',
    location: '英杰交流中心阳光大厅',
    time: '15:00-18:00',
    dateDay: '28',
    dateMonth: '12-2025',
    image: boschHeadquarterImage,
    description: '博世集团北京大学校园招聘宣讲会。'
  }
])

// 根据tab筛选活动
const filteredEvents = computed(() => {
  if (activeTab.value === 'all') {
    return events.value
  }
  return events.value.filter(event => event.type === activeTab.value)
})

// 切换tab
const switchTab = (tabKey) => {
  activeTab.value = tabKey
}

// 返回上一页
const goBack = () => {
  router.back()
}

// 跳转到活动详情
const goToDetail = (event) => {
  console.log('Go to event detail:', event)
  // 这里可以跳转到活动详情页
  // router.push(`/event-detail/${event.id}`)
}

// 注册活动
const registerEvent = (event) => {
  console.log('Register for event:', event)
  // 这里可以处理活动注册逻辑
}

// 导航功能
const navigateToHome = () => {
  router.push('/home')
}

const navigateToEvents = () => {
  router.push('/events')
}

const navigateToCareers = () => {
  router.push('/careers')
}
</script>

<style scoped>
.events-list-container {
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

/* Tab Navigation */
.tab-navigation {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  background: white;
  padding: 12px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.tab-item {
  flex: 1;
  padding: 10px 16px;
  background: transparent;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  color: #666;
  cursor: pointer;
  transition: all 0.3s ease;
}

.tab-item:hover {
  background: #f5f5f5;
}

.tab-item.active {
  background: #DA291C;
  color: white;
}

/* Events List */
.events-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.event-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  position: relative;
}

.event-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

.event-image {
  width: 100%;
  height: 180px;
  overflow: hidden;
}

.event-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.event-content {
  padding: 16px;
  position: relative;
}

.event-title {
  font-size: 16px;
  font-weight: 600;
  color: #333;
  margin-bottom: 12px;
  line-height: 1.4;
}

.event-meta {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}

.event-location,
.event-time {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #666;
  font-size: 13px;
}

.event-location svg,
.event-time svg {
  color: #999;
  flex-shrink: 0;
}

/* 日期标签 */
.event-date-tag {
  position: absolute;
  top: 16px;
  right: 16px;
  background: white;
  border-radius: 8px;
  padding: 8px 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  min-width: 60px;
}

.date-day {
  display: block;
  font-size: 20px;
  font-weight: bold;
  color: #DA291C;
  line-height: 1;
}

.date-month {
  display: block;
  font-size: 11px;
  color: #666;
  margin-top: 4px;
}

/* 注册按钮 */
.event-register-btn {
  width: 100%;
  padding: 10px 16px;
  background: #DA291C;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.event-register-btn:hover {
  background: #c02318;
  transform: translateY(-1px);
}

.event-register-btn:active {
  transform: translateY(0);
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
}

.empty-state p {
  margin-top: 16px;
  color: #999;
  font-size: 14px;
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

  .tab-navigation {
    padding: 16px;
  }

  .tab-item {
    font-size: 15px;
    padding: 12px 20px;
  }

  .events-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 24px;
  }

  .event-image {
    height: 200px;
  }

  .event-content {
    padding: 20px;
  }

  .event-title {
    font-size: 18px;
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

  .events-list {
    gap: 30px;
  }

  .event-image {
    height: 220px;
  }

  .event-card {
    border-radius: 16px;
  }

  .event-title {
    font-size: 20px;
    margin-bottom: 16px;
  }

  .event-register-btn {
    font-size: 15px;
    padding: 12px 20px;
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

  .events-list {
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
    gap: 40px;
  }
}
</style>