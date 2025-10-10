<template>
  <div class="reasons-detail-container">
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
      <!-- Top Images Section -->
      <section class="top-images-section">
        <!-- Title Image -->
        <div class="title-image-container">
          <img src="../assets/images/bosche-reason-title.png" alt="爱上博世的100个理由" class="title-image" />
        </div>

        <!-- Images Row with Letters -->
        <div class="images-row">
          <div class="image-container">
            <img src="../assets/images/rd-1.png" alt="理由图片1" class="reason-image" />
            <img src="../assets/images/rdl-1.png" alt="GROW" class="letter-overlay" />
          </div>
          <div class="image-container">
            <img src="../assets/images/rd-2.png" alt="理由图片2" class="reason-image" />
            <img src="../assets/images/rdl-2.png" alt="INSPIRE" class="letter-overlay" />
          </div>
          <div class="image-container">
            <img src="../assets/images/rd-3.png" alt="理由图片3" class="reason-image" />
            <img src="../assets/images/rdl-3.png" alt="ENJOY" class="letter-overlay" />
          </div>
        </div>
      </section>

      <!-- 100 Reasons Section -->
      <section class="reasons-section">

        <!-- Reasons Grid -->
        <div class="reasons-grid">
          <div class="reason-card" v-for="reason in allReasons" :key="reason.id">
            <!-- Card Number in Corner Notch -->
            <div class="corner-notch">
              <span class="notch-number">#{{ String(reason.id).padStart(3, '0') }}</span>
            </div>

            <div class="reason-content">
              <div class="reason-logo">
                <img :src="reason.logo" :alt="reason.title" />
              </div>
              <div class="reason-text">
                <h3 class="reason-title">{{ reason.title }}</h3>
                <p class="reason-description">{{ reason.description }}</p>
              </div>
            </div>

            <div class="reason-footer">
              <span class="source-tag">{{ reason.tag }}</span>
              <div class="likes-section">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3" stroke-width="2"/>
                </svg>
                <span class="likes-count">1.5w</span>
              </div>
            </div>
          </div>
        </div>
      </section>
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
      <button class="nav-item active">
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Navigation functions
const goBack = () => {
  router.back()
}

const navigateToHome = () => {
  router.push('/home')
}

const navigateToCareers = () => {
  router.push('/careers')
}

// Import logo images
import logo1 from '../assets/images/100-reasons/rdl-logo-1.png'
import logo2 from '../assets/images/100-reasons/rdl-logo-2.png'
import logo3 from '../assets/images/100-reasons/rdl-logo-3.png'

// Logo and tag options
const logos = [
  logo1,
  logo2,
  logo3
]

const tags = ['GROW', 'INSPIRE', 'ENJOY']

// Function to get random logo
const getRandomLogo = () => logos[Math.floor(Math.random() * logos.length)]

// Function to get random tag
const getRandomTag = () => tags[Math.floor(Math.random() * tags.length)]

// All 100 reasons data
const allReasons = ref([
  { id: 1, title: '"为生活而发明"理念', description: '博世始终秉持 "Invented for life" 的品牌主张，为人类创造更美好的生活。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 2, title: '全球化布局', description: '博世业务覆盖 60 多个国家，是真正的全球化公司。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 3, title: '中国深耕力度', description: '博世在中国有多年历史，深耕本地市场，致力于本土化发展。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 4, title: '多元业务领域', description: '博世涵盖汽车技术、工业技术、消费品与能源技术等多个业务板块。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 5, title: '可持续发展承诺', description: '博世致力于以可持续科技为核心，推动环保与社会责任。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 6, title: '责任与伦理', description: '在商业决策中坚持责任与伦理，是博世企业文化的基石。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 7, title: '公正与尊重', description: '公正对待员工与合作方，倡导尊重，是博世内在的价值观。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 8, title: '开放与信任', description: '博世鼓励在组织内部建立开放沟通与相互信任的氛围。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 9, title: '主动与担当', description: '每个人都被鼓励主动承担责任、追求目标。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 10, title: '结果导向', description: '博世重视实效，追求行动带来结果与价值。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 11, title: '多样性与包容性', description: '博世重视员工多样性，倡导包容互补的团队文化。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 12, title: '企业传承基因', description: '博世的价值观可追溯至创始人罗伯特·博世的初心。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 13, title: '强大的研发实力', description: '博世在全球拥有大量研发机构，不断投入技术创新。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 14, title: '技术驱动企业', description: '博世的产品与方案背后，都是先进的技术驱动。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 15, title: '智能互联解决方案', description: '博世在物联网、智能互联产品上不断深耕。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 16, title: '汽车事业的核心角色', description: '博世在全球汽车技术领域是关键供应商。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 17, title: '移动出行未来愿景', description: '博世致力于安全、可持续、智能的未来出行解决方案。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 18, title: '工业自动化领先者', description: '博世（例如力士乐部门）在传动与控制技术具领先地位。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 19, title: '家电与消费品链条', description: '博世在家电、厨房、热能设备等消费品领域拥有较高影响力。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 20, title: '节能与环境科技', description: '博世在能源利用、热泵、节能系统等领域持续投入。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 21, title: '智能传感器技术', description: '博世子公司 Sensortec 在 MEMS 传感器方面具影响力。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 22, title: '跨界整合能力', description: '博世能够整合硬件、软件、云服务等跨领域能力。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 23, title: '强大的产业链掌控', description: '从元器件到系统方案，博世在产业链上具备控制能力。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 24, title: '长期视野与投资', description: '博世注重中长期发展而不仅短期利益。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 25, title: '本地化策略', description: '在中国市场，博世注重本地化设计与服务。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 26, title: '创投与未来投入', description: '博世设立创投基金，不断探索未来技术。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 27, title: '科技与社会责任融合', description: '博世强调科技创新必须兼顾社会责任。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 28, title: '慈善实践根植中国', description: '博世在中国有自己的慈善中心，积极参与教育扶贫项目。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 29, title: '员工志愿者文化', description: '博世鼓励员工以志愿者身份参与社会公益。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 30, title: '高度透明的公益机制', description: '在中国的慈善中心强调项目透明性与可持续性。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 31, title: '持续教育投入', description: '博世在教育、人才培养方面持续投入。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 32, title: '因地制宜的公益方案', description: '博世的公益项目结合当地实际需求设计。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 33, title: '本地员工成长机会', description: '本地团队能获得参与全球项目的机会。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 34, title: '跨国导师机制', description: '博世内部可能设有跨国导师或技能传承机制。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 35, title: '技术交流平台', description: '员工可参与跨区域、跨业务的技术交流与分享。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 36, title: '内部创新孵化', description: '博世鼓励内部创新、创业项目孵化。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 37, title: '国际派遣计划', description: '博世提供海外派遣、轮岗机会，让人国际化成长。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 38, title: '多元职业路径', description: '在博世，无论你是技术、管理、市场方向，都有路径。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 39, title: '跨部门协作体验', description: '不同业务线之间协作，为员工提供跨界视角。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 40, title: '系统培训体系', description: '博世通常会提供系统化的入职与在职培训体系。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 41, title: '学习型组织氛围', description: '员工被鼓励不断学习、挑战自我、拥抱新知识。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 42, title: '成果认可机制', description: '优秀成果能得到公司或团队认可、奖励。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 43, title: '创意表达机会', description: '在项目中有机会提出创意、进行实践。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 44, title: '职能轮岗制度', description: '轮岗制度帮助员工拓展视野与能力。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 45, title: '透明的绩效考核', description: '公正、透明的绩效体系让员工清楚自己的定位。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 46, title: '灵活工作机制', description: '在不同岗位可能享有一定的弹性工作制度。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 47, title: '国际文化交流', description: '与来自不同国家同事合作，拓展文化视野。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 48, title: '丰富的内部活动', description: '团队建设、年度活动、兴趣小组丰富员工生活。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 49, title: '健康与福利保障', description: '员工可以享受系统的健康、保险等福利机制。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 50, title: '家庭友好政策', description: '对有家庭责任的员工可能提供亲子支持或弹性安排。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 51, title: '工作环境优越', description: '办公场地、设备通常现代化、舒适。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 52, title: '安全第一思维', description: '在工业、制造、实验环境，博世强调安全标准。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 53, title: '标准化流程', description: '规范流程与制度帮助效率与质量保障。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 54, title: '品牌背书加分', description: '来自博世这个品牌对个人简历也有加分效应。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 55, title: '高质量合作伙伴', description: '与一流高校、企业、研究机构合作，从项目中受益。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 56, title: '参与未来前沿领域', description: '博世在 AI、自动驾驶、能源科技等前沿领域布局。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 57, title: '积极响应全球趋势', description: '博世紧跟工业4.0、绿色发展、数字化趋势。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 58, title: '强大的品牌认知度', description: '博世是公众熟知、值得信赖的高科技品牌。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 59, title: '产品覆盖日常生活', description: '博世产品涉及日常家庭、出行、生活多数场景。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 60, title: '科技与人性结合', description: '博世强调科技应服务于人的幸福，而非冷冰工具。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 61, title: '客户导向文化', description: '博世重视客户反馈，将其视为产品优化关键。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 62, title: '高标准质量管理', description: '在产品和服务上保持高标准的质量认证和控制。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 63, title: '快速响应机制', description: '在市场、客户或技术变化中，博世具备快速响应能力。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 64, title: '持续改进文化', description: '不断反思、优化、精进，是博世文化的一部分。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 65, title: '跨文化团队合作', description: '国际团队协作让你习得跨文化沟通能力。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 66, title: '职业稳定性', description: '在大企业体系下，具有相对稳定的职业保障。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 67, title: '与行业顶尖竞争', description: '博世经常参与或引领行业技术标准与竞争。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 68, title: '可见的社会影响力', description: '博世的很多产品与项目直接影响社会发展。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 69, title: '实践可持续技术项目', description: '你可能参与减碳、能源效率提升等项目。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 70, title: '长寿命产品价值观', description: '博世的产品设计注重耐用性与可维护性。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 71, title: '本地化制造能力', description: '在中国设有生产基地，更贴近市场与用户。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 72, title: '全球采购网络', description: '博世具备全球采购与供应链能力，资源整合强。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 73, title: '绿色制造推进', description: '制造过程中推行节能减排与绿色标准。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 74, title: '智能制造与自动化', description: '博世内部也在使用智能制造技术进行自我升级。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 75, title: '工业 4.0 实践者', description: '在智能工厂、数字化车间上有真实落地经验。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 76, title: '精益生产理念', description: '博世推行精益、六西格玛等管理理念以提升效率。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 77, title: '客户定制化能力', description: '能为客户提供定制化方案，而非一刀切产品。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 78, title: '开放平台生态', description: '在 IoT、平台生态上愿与合作伙伴共建。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 79, title: '强调知识产权', description: '在专利、技术保护方面严格，尊重创新。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 80, title: '国际项目经验积累', description: '能参与跨国项目，获得国际视野。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 81, title: '员工荣誉传承', description: '博世内部有优秀员工、团队表彰机制。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 82, title: '成就感可视化', description: '项目成果直观可见，可以看到"自己做的东西在世界上被用到"。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 83, title: '参与标准制定', description: '在行业标准、技术标准制定中有代表性声音。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 84, title: '行业先锋角色', description: '在许多业务领域，博世都是技术与市场的先锋。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 85, title: '自主决策空间', description: '虽在大公司架构中，仍赋予项目或团队一定自主权。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 86, title: '透明晋升通道', description: '晋升、发展路径在公司内部较为透明。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 87, title: '国际交流机会', description: '有机会到德国或其他国家交流、学习。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 88, title: '多语种环境', description: '英语、德语或其他语种成为工作环境的一部分。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 89, title: '高标准安全保障', description: '企业对员工的安全保护制度严格，减少风险。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 90, title: '品牌自豪感', description: '身为博世人，背后有强大品牌支持与认同感。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 91, title: '公信力企业形象', description: '博世在大众、行业中具有良好口碑与信任度。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 92, title: '营造创新文化', description: '鼓励试错、创新，让员工敢于挑战。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 93, title: '多学科交叉机会', description: '你可能跨机械、电子、软件、控制等多个学科协作。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 94, title: '国际化视野塑造', description: '在博世工作自然塑造你具备国际化思维。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 95, title: '全球客户互动', description: '与全球客户、合作伙伴互动交流经验。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 96, title: '卓越科技影响力', description: '博世的科技、解决方案在世界许多地方落地。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 97, title: '面向未来的业务布局', description: '博世在新能源、自动驾驶、智慧家居等未来方向持续投入。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 98, title: '长期信任背后资本结构', description: '博世大部分股份由基金会持有，以社会责任为导向。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 99, title: '历史底蕴与品牌传承', description: '博世有悠久历史，从 1886 年创业至今，是百年科技公司。', logo: getRandomLogo(), tag: getRandomTag() },
  { id: 100, title: '与优秀人为伍', description: '在博世，你将与国内外顶尖人才合作、成长、成就未来。', logo: getRandomLogo(), tag: getRandomTag() }
])
</script>

<style scoped>
.reasons-detail-container {
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

.page-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin: 0;
}

.header-spacer {
  width: 80px;
}

/* Main Content */
.main-content {
  padding: 16px;
  padding-bottom: 72px;
}

/* Top Images Section */
.top-images-section {
  margin-bottom: 20px;
}

/* Title Image Container */
.title-image-container {
  width: 100%;
  margin-bottom: 16px;
  text-align: center;
}

.title-image {
  width: 100%;
  max-width: 400px;
  height: auto;
  object-fit: contain;
}

/* Images Row */
.images-row {
  display: flex;
  gap: 8px;
  width: 100%;
}

/* Individual Image Container */
.image-container {
  flex: 1;
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.reason-image {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}

/* Letter Overlay */
.letter-overlay {
  position: absolute;
  bottom: 8px;
  left: 8px;
  width: 65%;
  max-width: 130px;
  height: auto;
  object-fit: contain;
  z-index: 2;
}

/* 100 Reasons Section */
.reasons-section {
  margin-top: 30px;
}

.reasons-main-title {
  font-size: 24px;
  font-weight: 600;
  color: #333;
  text-align: center;
  margin-bottom: 30px;
}

/* Reasons Grid */
.reasons-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

.reason-card {
  background: white;
  border-radius: 16px;
  padding: 25px 20px 15px 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  position: relative;
  min-height: 150px;
  overflow: visible;
}

.reason-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

/* Corner Notch - 右上角缺口 */
.reason-card::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 46px 20px 0;
  border-color: transparent #f5f5f5 transparent transparent;
}

.corner-notch {
  position: absolute;
  top: 0;
  right: 0;
  width: 46px;
  height: 20px;
  background: rgba(162, 169, 183, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}

.notch-number {
  font-size: 11px;
  font-weight: 600;
  color: white;
  letter-spacing: 0.5px;
  text-align: center;
}

.reason-content {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  margin-bottom: 15px;
  margin-top: 5px;
}

.reason-logo {
  width: 72px;
  height: 72px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.reason-logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.reason-text {
  flex: 1;
  padding-top: 5px;
}

.reason-title {
  font-size: 18px;
  font-weight: 700;
  color: #000;
  margin: 0 0 8px 0;
  line-height: 1.2;
  font-family: 'PingFang SC', 'Helvetica Neue', Arial, sans-serif;
}

.reason-description {
  font-size: 13px;
  color: #666;
  line-height: 1.5;
  margin: 0;
}

.reason-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid #f0f0f0;
}

.source-tag {
  font-size: 12px;
  color: #999;
  background: #f5f5f5;
  padding: 4px 10px;
  border-radius: 12px;
}

.likes-section {
  display: flex;
  align-items: center;
  gap: 6px;
}

.likes-section svg {
  width: 18px;
  height: 18px;
  stroke: #999;
}

.likes-count {
  font-size: 14px;
  color: #666;
  font-weight: 500;
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

  .page-title {
    font-size: 20px;
  }

  .back-button {
    padding: 10px 16px;
    font-size: 15px;
  }

  .title-image-container {
    margin-bottom: 20px;
  }

  .title-image {
    max-width: 500px;
  }

  .images-row {
    gap: 12px;
  }

  .image-container {
    border-radius: 12px;
  }

  .letter-overlay {
    bottom: 12px;
    left: 12px;
    max-width: 160px;
  }

  .reasons-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }

  .reasons-main-title {
    font-size: 28px;
    margin-bottom: 40px;
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

  .page-title {
    font-size: 22px;
  }

  .main-content {
    padding: 40px;
    padding-bottom: 40px;
    max-width: 1400px;
  }

  .title-image-container {
    margin-bottom: 24px;
  }

  .title-image {
    max-width: 600px;
  }

  .images-row {
    gap: 16px;
    margin-bottom: 30px;
  }

  .image-container {
    border-radius: 16px;
  }

  .letter-overlay {
    bottom: 16px;
    left: 16px;
    max-width: 200px;
  }

  .reasons-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
  }

  .reasons-main-title {
    font-size: 32px;
  }

  .reason-card {
    padding: 35px 24px 24px 24px;
  }

  .reason-logo {
    width: 85px;
    height: 85px;
  }

  .reason-title {
    font-size: 22px;
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

  .title-image-container {
    margin-bottom: 30px;
  }

  .title-image {
    max-width: 700px;
  }

  .images-row {
    gap: 20px;
  }

  .letter-overlay {
    bottom: 20px;
    left: 20px;
    max-width: 240px;
  }

  .reasons-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>