/**
 * 爬虫配置文件
 */
export default {
  // 目标网站 URL（示例，请替换为实际要爬取的网站）
  baseUrl: 'https://example.com',
  
  // 请求超时时间（毫秒）
  timeout: 10000,
  
  // User-Agent 设置
  userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  
  // 请求间隔时间（毫秒），避免过于频繁请求
  requestDelay: 1000,
  
  // 最大重试次数
  maxRetries: 3,
  
  // 数据保存路径
  outputDir: './data'
};
