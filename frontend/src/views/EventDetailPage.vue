<template>
  <div class="container">
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
      <!-- Hero Banner -->
      <div class="hero-banner">
        <div class="image-wrapper">
          <img :src="eventDetail.image" :alt="eventDetail.title" class="hero-image" />
        </div>
      </div>
    </main>

    <!-- White Overlay Section -->
    <div class="white-overlay-section">
      <!-- Event Header -->
      <div class="event-header">
        <h1 class="event-title">{{ eventDetail.title }}</h1>
        <div class="event-meta">
          <div class="meta-item">
            <span class="meta-date">{{ eventDetail.date }}</span>
            <span class="meta-time">{{ eventDetail.time }}</span>
          </div>
          <!-- Register/Replay Button (only for certain events) -->
          <button v-if="eventDetail.id === 6 || eventDetail.id === 7" class="register-button" @click="handleReplayClick">
            <span>查看回放</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"/>
            </svg>
          </button>
          <button v-else-if="eventDetail.registrationUrl" class="register-button" @click="handleRegistrationClick">
            <span>立即报名</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"/>
            </svg>
          </button>
          <button v-else-if="eventDetail.type === 'lecture' && eventDetail.id > 7" class="register-button" @click="showQRCode = true">
            <span>立即报名</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"/>
            </svg>
          </button>
        </div>
        <div class="event-location">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
            <circle cx="12" cy="10" r="3"/>
          </svg>
          <span>{{ eventDetail.location }}</span>
        </div>
      </div>

      <!-- Activity Details Section -->
      <div class="activity-details">
        <h2 class="section-title">活动详情</h2>
        <div class="activity-content">
          <p>{{ eventDetail.description }}</p>
          <div class="highlights" v-if="eventDetail.highlights">
            <p v-for="(highlight, index) in eventDetail.highlights" :key="index">
              {{ highlight }}
            </p>
          </div>
        </div>
      </div>

    </div>

    <!-- QR Code Modal -->
    <div v-if="showQRCode" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <button class="close-button" @click="closeModal">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"/>
            <line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>

        <!-- QR Code with Event Info Overlay -->
        <div class="qr-code-wrapper">
          <!-- Event Info Overlay on Image -->
          <div class="event-info-overlay">
            <h3>{{ eventDetail.title }}</h3>
            <p class="overlay-date">{{ eventDetail.date }} {{ eventDetail.time }}</p>
            <p class="overlay-location">{{ eventDetail.location }}</p>
          </div>
          <!-- QR Code Image -->
          <img src="../assets/images/erweima.png" alt="报名二维码" class="qr-code-full-image" />
        </div>
      </div>
    </div>

    <!-- Bottom Navigation (only shown on mobile) -->
    <nav class="bottom-nav mobile-only">
      <button class="nav-item" @click="goHome">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-1-click.png" alt="首页" class="nav-icon-active" />
          <img src="../assets/images/daohang-1.png" alt="首页" class="nav-icon-default" />
        </div>
        <span class="nav-label">首页</span>
      </button>

      <button class="nav-item active" @click="goEvents">
        <div class="nav-icon-wrapper">
          <img src="../assets/images/daohang-2-click.png" alt="博世活动" class="nav-icon-active" />
          <img src="../assets/images/daohang-2.png" alt="博世活动" class="nav-icon-default" />
        </div>
        <span class="nav-label">博世活动</span>
      </button>

      <button class="nav-item" @click="goCareers">
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
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import boschHeadquarterImage from '../assets/images/bosch-cn-headquarter_res_1600x900.webp'
import boshishengluntanImage from '../assets/images/boshishengluntan.jpg'
import xunhuiImage from '../assets/images/xunhuixuanjiang.jpg'
import kongxuan1Image from '../assets/images/kongxuan-1.jpg'
import kongxuan2Image from '../assets/images/kongxuan-2.jpg'
import tongjiImage from '../assets/images/tongji.jpg'
import formulaStudentImage from '../assets/images/formula-student.jpg'

const router = useRouter()
const route = useRoute()

// 显示二维码弹窗
const showQRCode = ref(false)

// 活动详情数据
const eventDetail = ref({
  id: 1,
  title: '中国科学技术大学 宣讲会',
  date: '08-12-2025',
  time: '09:00-12:00',
  location: '中国科学技术大学·西区学生活动中心一楼报告厅',
  image: boshishengluntanImage,
  description: '博世携手同济大学，共同打造了一场充满青春与活力的运动嘉年华。活动面向全体在校学生开放，旨在通过轻松有趣的体育项目，传递"健康生活、团队合作、激情挑战"的理念，展现博世年轻化、多元化的企业形象。',
  highlights: [
    '博世集团将详细介绍公司的发展历程、业务领域和企业文化',
    '分享最新的技术创新成果和行业发展趋势',
    '提供丰富的职业发展机会和校园招聘信息',
    '现场答疑环节，解答同学们关心的问题'
  ]
})

// 所有活动数据（模拟数据库）
const allEvents = [
  {
    id: 1,
    type: 'lecture',
    title: '第三届中国博士生学术论坛',
    date: '2025年7月5日-6日',
    time: '10:00-16:30',
    location: '中国上海',
    image: boshishengluntanImage,
    description: '本次论坛将围绕整车、能源动力、底盘、车身、智能化技术、电动化技术、轻量化技术、网联化技术、新材料与新工艺、智能制造等研究方向，邀请海内外相关领域博士生就博士生学位论文及阶段性研究成果展开交流汇报。',
    highlights: [
      '本次论坛有50余位汽车领域顶尖高校及企业的院士、院长、专家出席。150多位全国有论文发表的PHD来参加。博世共出席20多位专家参与论文答辩，并在现场设立了博世智能驾驶技术展位。与院长及10位业务匹配的教授建立深度链接，展位超150位博士及20位教授体验了解。',
      '活动详情：（1）论坛4个技术方向共计64场博士论文报告会 （2）车辆系统动力学与控制技术（底盘相关等） （3）智能网联汽车技术（所有智驾话题） （4）车用电源技术（电力电子话题） （5）车用动力系统技术（能源类）',
    ]
  },
  {
    id: 2,
    type: 'sports',
    title: '博世 X 同济大学',
    date: '2025年10月17日',
    time: '14:00-17:00',
    location: '同济大学汽车学院',
    image: xunhuiImage,
    description: '博世 X 同济大学',
    highlights: [
      '博世集团将详细介绍公司的发展历程、业务领域和企业文化',
      '分享最新的技术创新成果和行业发展趋势',
      '提供丰富的职业发展机会和校园招聘信息',
      '现场答疑环节，解答同学们关心的问题'
    ]
  },
  {
    id: 3,
    type: 'sports',
    title: '博世 X 上海交通大学',
    date: '2025年11月15日',
    time: '13:00-17:00',
    location: '上海交通大学自动化与感知学院',
    image: xunhuiImage,
    description: '博世 X 上海交通大学',
    highlights: [
      '博世集团将详细介绍公司的发展历程、业务领域和企业文化',
      '分享最新的技术创新成果和行业发展趋势',
      '提供丰富的职业发展机会和校园招聘信息',
      '现场答疑环节，解答同学们关心的问题'
    ]
  },
  {
    id: 4,
    type: 'sports',
    title: '博世 X 南京大学',
    date: '2025年10月20日',
    time: '14:00-17:00',
    location: '南京大学人工智能学院',
    image: xunhuiImage,
    description: '博世 X 南京大学',
    highlights: [
      '博世集团将详细介绍公司的发展历程、业务领域和企业文化',
      '分享最新的技术创新成果和行业发展趋势',
      '提供丰富的职业发展机会和校园招聘信息',
      '现场答疑环节，解答同学们关心的问题'
    ]
  },
  {
    id: 5,
    type: 'sports',
    title: '博世 X 东南大学',
    date: '2025年10月25日',
    time: '10:00-17:00',
    location: '东南大学计软智学院',
    image: xunhuiImage,
    description: '博世 X 东南大学',
    highlights: [
      '博世集团将详细介绍公司的发展历程、业务领域和企业文化',
      '分享最新的技术创新成果和行业发展趋势',
      '提供丰富的职业发展机会和校园招聘信息',
      '现场答疑环节，解答同学们关心的问题'
    ]
  },
  {
    id: 6,
    type: 'lecture',
    title: '看直播，拿世界500强校招offer',
    date: '2025年9月25日',
    time: '18:00-19:00',
    location: '小红书-博世中国招聘',
    image: kongxuan1Image,
    description: '相约@博世中国招聘 直播间，为你带来精彩内容！',
    replayUrl: 'https://www.xiaohongshu.com/fe/live-h5/page/live_replay/569939621870932425?share_source=live_dynamic&share_source_id=137594152571704932&host_id=60c37ff40000000001005f41&xhsshare=WeixinSession&appuid=68b7ae6800000000190194be&apptime=1760167753&share_id=14a9937c91614d32b5afa5006fdd18bc&share_channel=wechat',
    highlights: [
      '多元视角：不同背景、不同岗位的同事，分享他们眼中的博世',
      '趣闻分享：揭秘不同行业的"好玩"日常，打破你的认知壁垒',
      '在线答疑：关于求职、面试、职业发展的任何问题，现场为你解答',
      '初见故事：分享他们"第一次听说博世"和最终选择博世的暖心故事',
      '直播多轮抽奖，博世好礼送不停！更有直通面试机会等你来拿！'
    ]
  },
  {
    id: 7,
    type: 'lecture',
    title: '博世秋招秘籍即将上线，速来',
    date: '2025年9月9日',
    time: '18:00-19:00',
    location: '小红书-博世中国招聘',
    image: kongxuan2Image,
    description: '还在准备秋招的宝子们，博世中国秋招直播来啦！',
    replayUrl: 'https://www.xiaohongshu.com/fe/live-h5/page/live_replay/569916433896234740?share_source=live_dynamic&share_source_id=137570961291913841&host_id=60c37ff40000000001005f41&xhsshare=WeixinSession&appuid=68b7ae6800000000190194be&apptime=1760167768&share_id=c4a9ecadc37b46a5928e8528a3505982&share_channel=wechat',
    highlights: [
      '✔️博世员工解析面试技巧',
      '✔️2026博世校招岗位揭秘',
      '✔️在线答疑，聊聊职场那些事',
      '✔️三轮抽奖，博世喊你接好运',
      '一边冲浪一边拿offer，治好你的求职迷茫！'
    ]
  },
  {
    id: 8,
    type: 'sports',
    title: '博世 X 浙江大学',
    date: '2025年10月26日',
    time: '09:00-17:00',
    location: '浙江大学',
    image: xunhuiImage,
    description: '博世 X 浙江大学',
    highlights: [
      '博世集团将详细介绍公司的发展历程、业务领域和企业文化',
      '分享最新的技术创新成果和行业发展趋势',
      '提供丰富的职业发展机会和校园招聘信息',
      '现场答疑环节，解答同学们关心的问题'
    ]
  },
  {
    id: 9,
    type: 'forum',
    title: '博士·2025大学生方程式大赛',
    date: '2025年11月19日',
    time: '全天',
    location: '全国',
    image: formulaStudentImage,
    description: '博士·2025大学生方程式大赛正式启动！这是一场汇集全国高校精英的工程技术竞赛，旨在培养大学生的创新设计能力、工程实践能力和团队协作精神。参赛队伍将设计、制造并驾驶赛车，在赛道上展现技术与速度的完美结合。',
    registrationUrl: 'https://v.wjx.cn/vm/t64DL8q.aspx',
    highlights: [
      '🏎️ 培养大学生的创新设计能力、工程实践能力和团队协作精神',
      '🏁 参赛队伍将设计、制造并驾驶自己的方程式赛车',
      '🏆 在赛道上展现技术与速度的完美结合',
      '💡 提供与行业专家交流学习的机会',
      '🎯 优秀团队将获得博世实习和就业机会'
    ]
  }
]

// 页面加载时获取活动详情
onMounted(() => {
  const eventId = parseInt(route.params.id)
  const event = allEvents.find(e => e.id === eventId)
  if (event) {
    eventDetail.value = event
  }
})

// 返回上一页
const goBack = () => {
  router.back()
}

// 导航方法
const goHome = () => {
  router.push('/home')
}

const goEvents = () => {
  router.push('/events')
}

const goCareers = () => {
  router.push('/careers')
}

// 关闭弹窗
const closeModal = () => {
  showQRCode.value = false
}

// 处理查看回放按钮点击
const handleReplayClick = () => {
  if (eventDetail.value.replayUrl) {
    window.open(eventDetail.value.replayUrl, '_blank')
  }
}

// 处理报名按钮点击
const handleRegistrationClick = () => {
  if (eventDetail.value.registrationUrl) {
    window.open(eventDetail.value.registrationUrl, '_blank')
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

.header-spacer {
  width: 80px;
}

/* Main Content */
.main-content {
  padding: 16px;
  padding-bottom: 0;
}

/* Hero Banner */
.hero-banner {
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: relative;
}

.image-wrapper {
  position: relative;
  height: 250px;
  overflow: hidden;
  background: #f5f5f5;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* White Overlay Section */
.white-overlay-section {
  position: relative;
  background: white;
  margin-top: -62px; /* 250px * 0.25 = ~62px */
  padding: 20px 16px;
  padding-bottom: 72px; /* Account for bottom nav */
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  z-index: 10;
}

/* Event Header */
.event-header {
  margin-bottom: 30px;
  padding-top: 10px;
}

.event-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin: 0 0 12px 0;
  line-height: 1.3;
}

.event-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 12px;
}

.meta-date {
  font-size: 16px;
  font-weight: 600;
  color: #333;
}

.meta-time {
  font-size: 16px;
  color: #666;
}

.event-location {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #666;
  font-size: 14px;
}

.event-location svg {
  flex-shrink: 0;
}

/* Activity Details */
.activity-details {
  margin-bottom: 40px;
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
}

.activity-content {
  color: #666;
  font-size: 14px;
  line-height: 1.8;
}

.activity-content p {
  margin-bottom: 12px;
}

.highlights {
  margin-top: 16px;
  padding-left: 20px;
}

.highlights p {
  position: relative;
  margin-bottom: 8px;
}

.highlights p::before {
  content: '•';
  position: absolute;
  left: -15px;
  color: #4A90E2;
}

/* Register Button - Inline with time */
.event-meta .register-button {
  padding: 6px 14px;
  background: #4A90E2;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 4px;
  flex-shrink: 0;
}

.event-meta .register-button:hover {
  background: #3a7bc8;
  transform: translateY(-1px);
}

.event-meta .register-button:active {
  transform: translateY(0);
}

.event-meta .register-button svg {
  width: 14px;
  height: 14px;
}

/* Modal Overlay */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background: white;
  border-radius: 20px;
  padding: 15px;
  max-width: 400px;
  width: 100%;
  position: relative;
  animation: slideUp 0.3s ease;
  text-align: center;
}

@keyframes slideUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.5);
  border: none;
  padding: 8px;
  cursor: pointer;
  color: white;
  transition: all 0.2s;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 20;
}

.close-button:hover {
  background: rgba(0, 0, 0, 0.7);
  transform: scale(1.1);
}

.close-button svg {
  width: 18px;
  height: 18px;
}

/* QR Code Wrapper */
.qr-code-wrapper {
  position: relative;
  display: inline-block;
}

/* Event Info Overlay on Image */
.event-info-overlay {
  position: absolute;
  top: 20px;
  left: 30px;
  text-align: left;
  z-index: 10;
  width: calc(100% - 60px);
  color: #333;
}

.event-info-overlay h3 {
  font-size: 16px;
  font-weight: 600;
  margin: 0 0 8px 0;
  color: #333;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
  text-align: left;
}

.overlay-date {
  font-size: 13px;
  color: #555;
  margin: 0 0 6px 0;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
  text-align: left;
}

.overlay-location {
  font-size: 12px;
  color: #666;
  margin: 0;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
  text-align: left;
}

/* QR Code Full Image */
.qr-code-full-image {
  width: 100%;
  max-width: 350px;
  height: auto;
  display: block;
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

.nav-label {
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

.nav-item.active .nav-label {
  color: #4A90E2;
  font-weight: 500;
}

/* Tablet & Desktop Styles */
@media (min-width: 768px) {
  .main-content {
    padding: 24px;
    max-width: 900px;
    margin: 0 auto;
  }

  .image-wrapper {
    height: 350px;
  }

  .white-overlay-section {
    margin-top: -88px;
    padding: 30px;
  }

  .event-title {
    font-size: 28px;
  }
}

@media (min-width: 1024px) {
  .mobile-only {
    display: none !important;
  }

  .main-content {
    padding: 40px;
    max-width: 1200px;
  }

  .image-wrapper {
    height: 400px;
  }

  .white-overlay-section {
    margin-top: -100px;
    padding: 40px;
    padding-bottom: 60px;
  }

  .hero-banner {
    border-radius: 20px;
  }
}
</style>