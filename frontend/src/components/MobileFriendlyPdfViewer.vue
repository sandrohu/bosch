<template>
  <div class="mobile-pdf-viewer">
    <!-- 桌面端：使用iframe直接显示 -->
    <iframe
      v-if="!isMobile"
      :src="src"
      class="pdf-frame"
      title="PDF Document"
    />

    <!-- 移动端：提供预览和下载选项 -->
    <div v-else class="mobile-view">
      <!-- 使用object标签尝试显示 -->
      <object
        :data="src"
        type="application/pdf"
        class="pdf-object"
      >
        <!-- Fallback内容 -->
        <div class="pdf-fallback">
          <div class="fallback-content">
            <svg class="pdf-icon" width="80" height="80" viewBox="0 0 24 24" fill="#007BC0">
              <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20M10,19L12,15H13L15,19H13.5L13.1,18H11.9L11.5,19H10M12.3,16.5L11.9,17.5H13.1L12.7,16.5H12.3Z" />
            </svg>
            <h3>博世2024整体介绍</h3>
            <p class="file-info">PDF文档 · 约13MB</p>

            <div class="action-buttons">
              <a
                :href="src"
                target="_blank"
                class="primary-btn"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="white">
                  <path d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"/>
                </svg>
                在新窗口打开
              </a>

              <a
                :href="src"
                download="bosch2024.pdf"
                class="secondary-btn"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="#007BC0">
                  <path d="M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z"/>
                </svg>
                下载PDF
              </a>
            </div>

            <div class="tips">
              <p>💡 提示：点击"在新窗口打开"可使用系统默认PDF阅读器查看</p>
            </div>
          </div>
        </div>
      </object>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  src: {
    type: String,
    required: true
  }
})

const isMobile = ref(false)

// 检测是否为移动设备
const checkIsMobile = () => {
  const userAgent = navigator.userAgent.toLowerCase()
  const mobileKeywords = ['android', 'iphone', 'ipad', 'ipod', 'windows phone', 'mobile']
  const isSmallScreen = window.innerWidth <= 768

  isMobile.value = mobileKeywords.some(keyword => userAgent.includes(keyword)) || isSmallScreen
}

onMounted(() => {
  checkIsMobile()
  window.addEventListener('resize', checkIsMobile)
})
</script>

<style scoped>
.mobile-pdf-viewer {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

/* 桌面端iframe */
.pdf-frame {
  width: 100%;
  height: 100%;
  border: none;
  background: white;
}

/* 移动端视图 */
.mobile-view {
  width: 100%;
  height: 100%;
  position: relative;
}

.pdf-object {
  width: 100%;
  height: 100%;
}

/* Fallback内容 */
.pdf-fallback {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
}

.fallback-content {
  text-align: center;
  padding: 40px 20px;
  max-width: 400px;
}

.pdf-icon {
  margin-bottom: 20px;
}

.fallback-content h3 {
  font-size: 20px;
  color: #333;
  margin-bottom: 8px;
  font-weight: 600;
}

.file-info {
  color: #666;
  font-size: 14px;
  margin-bottom: 30px;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 30px;
}

.primary-btn, .secondary-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  font-size: 16px;
  transition: all 0.2s ease;
}

.primary-btn {
  background: #007BC0;
  color: white;
  border: 2px solid #007BC0;
}

.primary-btn:hover {
  background: #005a90;
  border-color: #005a90;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 123, 192, 0.3);
}

.secondary-btn {
  background: white;
  color: #007BC0;
  border: 2px solid #007BC0;
}

.secondary-btn:hover {
  background: #f0f7ff;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 123, 192, 0.15);
}

.tips {
  background: #f0f7ff;
  border-radius: 8px;
  padding: 12px 16px;
}

.tips p {
  color: #555;
  font-size: 13px;
  margin: 0;
  line-height: 1.5;
}

/* 平板优化 */
@media (min-width: 768px) and (max-width: 1024px) {
  .fallback-content {
    max-width: 500px;
  }

  .action-buttons {
    flex-direction: row;
    justify-content: center;
  }

  .primary-btn, .secondary-btn {
    flex: 1;
    max-width: 200px;
  }
}
</style>