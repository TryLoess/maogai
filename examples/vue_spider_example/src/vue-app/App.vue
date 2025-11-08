<template>
  <div id="app">
    <header class="app-header">
      <h1>🕷️ Vue Spider Example</h1>
      <p>网页爬虫数据展示</p>
    </header>

    <main class="app-main">
      <div class="controls">
        <button @click="loadData" class="btn btn-primary">
          {{ loading ? '加载中...' : '加载数据' }}
        </button>
        <button @click="refreshData" class="btn btn-secondary">
          刷新
        </button>
      </div>

      <div v-if="error" class="error-message">
        ⚠️ {{ error }}
      </div>

      <DataDisplay :items="data" :loading="loading" />

      <div v-if="data.length > 0" class="stats">
        <p>共加载 <strong>{{ data.length }}</strong> 条数据</p>
      </div>
    </main>

    <footer class="app-footer">
      <p>Vue Spider Example © 2024</p>
    </footer>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import DataDisplay from './components/DataDisplay.vue';
import { loadSpiderData } from '../utils/helpers.js';

export default {
  name: 'App',
  components: {
    DataDisplay
  },
  setup() {
    const data = ref([]);
    const loading = ref(false);
    const error = ref(null);

    const loadData = async () => {
      loading.value = true;
      error.value = null;
      
      try {
        const result = await loadSpiderData();
        data.value = result;
      } catch (err) {
        error.value = err.message || '加载数据失败';
        console.error('Error loading data:', err);
      } finally {
        loading.value = false;
      }
    };

    const refreshData = () => {
      data.value = [];
      loadData();
    };

    onMounted(() => {
      loadData();
    });

    return {
      data,
      loading,
      error,
      loadData,
      refreshData
    };
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.app-header {
  background: rgba(255, 255, 255, 0.95);
  padding: 2rem;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.app-header h1 {
  color: #333;
  margin-bottom: 0.5rem;
}

.app-header p {
  color: #666;
}

.app-main {
  flex: 1;
  max-width: 1200px;
  width: 100%;
  margin: 2rem auto;
  padding: 0 1rem;
}

.controls {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  justify-content: center;
}

.btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
}

.btn-primary {
  background: #667eea;
  color: white;
}

.btn-primary:hover {
  background: #5568d3;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
}

.btn-secondary:hover {
  background: #f8f9ff;
  transform: translateY(-2px);
}

.error-message {
  background: #fee;
  color: #c33;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  text-align: center;
}

.stats {
  text-align: center;
  margin-top: 2rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
}

.app-footer {
  background: rgba(0, 0, 0, 0.7);
  color: white;
  text-align: center;
  padding: 1rem;
  margin-top: 2rem;
}
</style>
