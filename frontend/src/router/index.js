import { createRouter, createWebHistory } from 'vue-router'
import SplashScreen from '../views/SplashScreen.vue'
import HomePage from '../views/HomePage.vue'
import ExplorePage from '../views/ExplorePage.vue'
import PdfViewerPage from '../views/PdfViewerPage.vue'
import VideoSeriesPage from '../views/VideoSeriesPage.vue'
import NewsListPage from '../views/NewsListPage.vue'
import NewsDetailPage from '../views/NewsDetailPage.vue'
import EventsPage from '../views/EventsPage.vue'

const routes = [
  {
    path: '/',
    name: 'Splash',
    component: SplashScreen,
    meta: { title: 'BOSCH 招聘' }
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage,
    meta: { title: '首页 - BOSCH 招聘' }
  },
  {
    path: '/explore',
    name: 'Explore',
    component: ExplorePage,
    meta: { title: '全景探索 - BOSCH 招聘' }
  },
  {
    path: '/pdf-viewer',
    name: 'PdfViewer',
    component: PdfViewerPage,
    meta: { title: '博世整体介绍 - BOSCH 招聘' }
  },
  {
    path: '/video-series',
    name: 'VideoSeries',
    component: VideoSeriesPage,
    meta: { title: '博世系列视频 - BOSCH 招聘' }
  },
  {
    path: '/news-list',
    name: 'NewsList',
    component: NewsListPage,
    meta: { title: '热文追踪 - BOSCH 招聘' }
  },
  {
    path: '/news-detail/:id',
    name: 'NewsDetail',
    component: NewsDetailPage,
    meta: { title: '新闻详情 - BOSCH 招聘' }
  },
  {
    path: '/events',
    name: 'Events',
    component: EventsPage,
    meta: { title: '博世活动 - BOSCH 招聘' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫 - 设置页面标题
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'BOSCH 招聘'
  next()
})

export default router