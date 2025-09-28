<template>
  <div class="simple-pdf-viewer">
    <!-- 控制栏 -->
    <div class="pdf-controls">
      <button @click="previousPage" :disabled="pageNum <= 1" class="control-btn">
        上一页
      </button>
      <span class="page-info">
        {{ pageNum }} / {{ pageCount || '...' }}
      </span>
      <button @click="nextPage" :disabled="pageNum >= pageCount" class="control-btn">
        下一页
      </button>
      <button @click="zoomIn" class="control-btn">放大</button>
      <button @click="zoomOut" class="control-btn">缩小</button>
    </div>

    <!-- PDF渲染区域 -->
    <div class="pdf-canvas-container" ref="pdfContainer">
      <canvas ref="pdfCanvas"></canvas>
      <div v-if="loading" class="loading">加载中...</div>
      <div v-if="error" class="error">{{ error }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import * as pdfjsLib from 'pdfjs-dist'

// 使用本地的worker文件
pdfjsLib.GlobalWorkerOptions.workerSrc = '/lib/pdf.worker.min.js'

const props = defineProps({
  src: {
    type: String,
    required: true
  }
})

const pdfCanvas = ref(null)
const pdfContainer = ref(null)
const pageNum = ref(1)
const pageCount = ref(0)
const pdfDoc = ref(null)
const pageRendering = ref(false)
const pageNumPending = ref(null)
const scale = ref(1.0)
const loading = ref(true)
const error = ref('')

// 渲染页面
const renderPage = (num) => {
  if (!pdfDoc.value) return

  pageRendering.value = true

  pdfDoc.value.getPage(num).then((page) => {
    const viewport = page.getViewport({ scale: scale.value })
    const canvas = pdfCanvas.value
    const context = canvas.getContext('2d')

    // 根据容器宽度自动缩放
    const containerWidth = pdfContainer.value.clientWidth
    const desiredWidth = containerWidth - 20 // 留出一些边距
    const actualScale = desiredWidth / viewport.width * scale.value
    const scaledViewport = page.getViewport({ scale: actualScale })

    canvas.height = scaledViewport.height
    canvas.width = scaledViewport.width

    const renderContext = {
      canvasContext: context,
      viewport: scaledViewport
    }

    const renderTask = page.render(renderContext)

    renderTask.promise.then(() => {
      pageRendering.value = false

      if (pageNumPending.value !== null) {
        renderPage(pageNumPending.value)
        pageNumPending.value = null
      }
    })
  }).catch((err) => {
    error.value = '渲染页面失败: ' + err.message
    pageRendering.value = false
  })

  pageNum.value = num
}

// 排队渲染
const queueRenderPage = (num) => {
  if (pageRendering.value) {
    pageNumPending.value = num
  } else {
    renderPage(num)
  }
}

// 上一页
const previousPage = () => {
  if (pageNum.value <= 1) return
  pageNum.value--
  queueRenderPage(pageNum.value)
}

// 下一页
const nextPage = () => {
  if (pageNum.value >= pageCount.value) return
  pageNum.value++
  queueRenderPage(pageNum.value)
}

// 放大
const zoomIn = () => {
  scale.value *= 1.2
  queueRenderPage(pageNum.value)
}

// 缩小
const zoomOut = () => {
  scale.value *= 0.8
  queueRenderPage(pageNum.value)
}

// 加载PDF
const loadPdf = async () => {
  loading.value = true
  error.value = ''

  try {
    console.log('Loading PDF from:', props.src)
    const loadingTask = pdfjsLib.getDocument(props.src)
    pdfDoc.value = await loadingTask.promise
    pageCount.value = pdfDoc.value.numPages

    // 渲染第一页
    renderPage(1)
    loading.value = false
  } catch (err) {
    console.error('Failed to load PDF:', err)
    error.value = '加载PDF失败: ' + err.message
    loading.value = false
  }
}

onMounted(() => {
  loadPdf()
})

watch(() => props.src, () => {
  loadPdf()
})
</script>

<style scoped>
.simple-pdf-viewer {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: white;
}

.pdf-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 10px;
  background: #f5f5f5;
  border-bottom: 1px solid #ddd;
  flex-shrink: 0;
}

.control-btn {
  padding: 6px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.control-btn:hover:not(:disabled) {
  background: #007BC0;
  color: white;
  border-color: #007BC0;
}

.control-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  padding: 0 10px;
  font-size: 14px;
  font-weight: 500;
}

.pdf-canvas-container {
  flex: 1;
  overflow: auto;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 20px;
  position: relative;
  background: #f9f9f9;
}

canvas {
  max-width: 100%;
  height: auto;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.loading, .error {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 16px;
  color: #666;
}

.error {
  color: #e60012;
}

/* 移动端优化 */
@media (max-width: 768px) {
  .pdf-controls {
    padding: 8px;
    gap: 5px;
  }

  .control-btn {
    padding: 5px 8px;
    font-size: 12px;
  }

  .page-info {
    font-size: 12px;
    padding: 0 5px;
  }

  .pdf-canvas-container {
    padding: 10px;
  }
}
</style>