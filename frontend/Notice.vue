<template>
  <div :class="['notice', type]" v-if="message">
    <h4 v-if="title">{{ title }}</h4>
    <p>{{ message }}</p>
    <button v-if="dismissible" @click="dismiss" class="dismiss-btn">×</button>
  </div>
</template>

<script>
export default {
  name: 'Notice',
  props: {
    type: {
      type: String,
      default: 'info', // 'info', 'warning', 'error', 'success'
      validator: (value) => ['info', 'warning', 'error', 'success'].includes(value)
    },
    title: {
      type: String,
      default: ''
    },
    message: {
      type: String,
      required: true
    },
    dismissible: {
      type: Boolean,
      default: false
    }
  },
  emits: ['dismiss'],
  methods: {
    dismiss() {
      this.$emit('dismiss')
    }
  }
}
</script>

<style scoped>
.notice {
  position: relative;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1rem;
}

.notice.info {
  background: #dbeafe;
  border: 1px solid #3b82f6;
  color: #1e40af;
}

.notice.warning {
  background: #fef3c7;
  border: 1px solid #f59e0b;
  color: #d97706;
}

.notice.error {
  background: #fef2f2;
  border: 1px solid #ef4444;
  color: #dc2626;
}

.notice.success {
  background: #f0fdf4;
  border: 1px solid #10b981;
  color: #059669;
}

.notice h4 {
  margin: 0 0 0.5rem 0;
  font-weight: 600;
}

.notice p {
  margin: 0;
  line-height: 1.5;
}

.dismiss-btn {
  position: absolute;
  top: 0.5rem;
  right: 0.75rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: currentColor;
  opacity: 0.7;
  transition: opacity 0.2s;
}

.dismiss-btn:hover {
  opacity: 1;
}</style>