<template>
  <div class="data-display">
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>正在加载数据...</p>
    </div>

    <div v-else-if="items.length === 0" class="empty-state">
      <p>📭 暂无数据</p>
      <p class="hint">点击"加载数据"按钮开始</p>
    </div>

    <div v-else class="items-grid">
      <div 
        v-for="item in items" 
        :key="item.id" 
        class="item-card"
      >
        <div class="item-header">
          <span class="item-id">#{{ item.id }}</span>
          <span class="item-date">{{ formatDate(item.crawledAt) }}</span>
        </div>
        
        <h3 class="item-title">{{ item.title }}</h3>
        
        <p v-if="item.description" class="item-description">
          {{ item.description }}
        </p>
        
        <a 
          v-if="item.link" 
          :href="item.link" 
          target="_blank" 
          rel="noopener noreferrer"
          class="item-link"
        >
          查看详情 →
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DataDisplay',
  props: {
    items: {
      type: Array,
      default: () => []
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      });
    }
  }
};
</script>

<style scoped>
.data-display {
  min-height: 300px;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  color: white;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 12px;
  color: #666;
}

.empty-state p:first-child {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hint {
  color: #999;
  font-size: 0.9rem;
}

.items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.item-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.item-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  font-size: 0.85rem;
}

.item-id {
  background: #667eea;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-weight: 600;
}

.item-date {
  color: #999;
}

.item-title {
  color: #333;
  margin-bottom: 1rem;
  font-size: 1.25rem;
  line-height: 1.4;
}

.item-description {
  color: #666;
  line-height: 1.6;
  margin-bottom: 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.item-link {
  display: inline-block;
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
}

.item-link:hover {
  color: #5568d3;
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .items-grid {
    grid-template-columns: 1fr;
  }
}
</style>
