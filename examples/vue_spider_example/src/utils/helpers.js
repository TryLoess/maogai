/**
 * 工具函数集合
 */

/**
 * 从文件或 API 加载爬虫数据
 * @returns {Promise<Array>} 爬虫数据
 */
export async function loadSpiderData() {
  try {
    // 尝试从本地文件加载数据
    const response = await fetch('/data/spider-data.json');
    
    if (!response.ok) {
      // 如果文件不存在，返回模拟数据
      console.warn('未找到爬虫数据文件，使用模拟数据');
      return getMockData();
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('加载数据失败:', error);
    // 发生错误时返回模拟数据
    return getMockData();
  }
}

/**
 * 获取模拟数据（用于演示）
 * @returns {Array} 模拟数据
 */
export function getMockData() {
  return [
    {
      id: 1,
      title: '示例文章标题 1',
      link: 'https://example.com/article/1',
      description: '这是一个示例文章的描述内容，展示爬虫如何提取网页信息。',
      crawledAt: new Date().toISOString()
    },
    {
      id: 2,
      title: '示例文章标题 2',
      link: 'https://example.com/article/2',
      description: 'Vue.js 和爬虫技术的结合可以创建强大的数据采集和展示应用。',
      crawledAt: new Date().toISOString()
    },
    {
      id: 3,
      title: '示例文章标题 3',
      link: 'https://example.com/article/3',
      description: '使用 Cheerio 可以像 jQuery 一样方便地解析 HTML 内容。',
      crawledAt: new Date().toISOString()
    },
    {
      id: 4,
      title: '示例文章标题 4',
      link: 'https://example.com/article/4',
      description: 'Axios 是一个基于 Promise 的 HTTP 客户端，非常适合用于网页爬虫。',
      crawledAt: new Date().toISOString()
    }
  ];
}

/**
 * 格式化日期
 * @param {string} dateString - ISO 日期字符串
 * @returns {string} 格式化后的日期
 */
export function formatDate(dateString) {
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

/**
 * 延迟函数（用于控制请求频率）
 * @param {number} ms - 延迟毫秒数
 * @returns {Promise}
 */
export function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * 验证 URL 是否有效
 * @param {string} urlString - URL 字符串
 * @returns {boolean} 是否有效
 */
export function isValidUrl(urlString) {
  try {
    new URL(urlString);
    return true;
  } catch (error) {
    return false;
  }
}
