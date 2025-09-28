<template>
  <transition name="modal-fade">
    <div v-if="show" class="pdf-modal" @click="handleBackdropClick">
      <div class="pdf-container" @click.stop>
        <!-- Header -->
        <div class="pdf-header">
          <button class="back-button" @click="$emit('close')">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
            </svg>
            <span>返回</span>
          </button>
          <h2 class="pdf-title">博世整体介绍</h2>
        </div>

        <!-- PDF Viewer -->
        <div class="pdf-viewer">
          <iframe
            :src="pdfUrl"
            class="pdf-iframe"
            title="博世整体介绍PDF"
          />
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  show: {
    type: Boolean,
    default: false
  },
  pdfPath: {
    type: String,
    default: '/pdf/bosch2024.pdf'
  }
})

const emit = defineEmits(['close'])

const pdfUrl = computed(() => props.pdfPath)

const handleBackdropClick = (event) => {
  if (event.target === event.currentTarget) {
    emit('close')
  }
}
</script>

<style scoped>
.pdf-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.pdf-container {
  width: 100%;
  max-width: 900px;
  height: 90vh;
  background: white;
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

.pdf-header {
  background: linear-gradient(135deg, #007BC0 0%, #8FB7F9 100%);
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  flex-shrink: 0;
}

.back-button {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 8px;
  padding: 8px 12px;
  color: white;
  font-size: 14px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.3);
}

.pdf-title {
  flex: 1;
  color: white;
  font-size: 18px;
  font-weight: 600;
  margin: 0;
}

.pdf-viewer {
  flex: 1;
  overflow: hidden;
  background: #f5f5f5;
}

.pdf-iframe {
  width: 100%;
  height: 100%;
  border: none;
}

/* Transition animations */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.3s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

.modal-fade-enter-active .pdf-container,
.modal-fade-leave-active .pdf-container {
  transition: transform 0.3s ease;
}

.modal-fade-enter-from .pdf-container {
  transform: scale(0.9) translateY(20px);
}

.modal-fade-leave-to .pdf-container {
  transform: scale(0.9) translateY(20px);
}

/* Mobile adjustments */
@media (max-width: 768px) {
  .pdf-modal {
    padding: 0;
  }

  .pdf-container {
    max-width: 100%;
    width: 100%;
    height: 100vh;
    border-radius: 0;
  }

  .pdf-header {
    padding: 12px 16px;
    padding-top: max(12px, env(safe-area-inset-top));
  }
}
</style>