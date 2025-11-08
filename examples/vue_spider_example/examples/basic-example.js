/**
 * 基础使用示例
 * 演示如何使用 WebSpider 类爬取数据
 */

import WebSpider from '../src/spider/index.js';

async function basicExample() {
  console.log('=== Vue Spider Example - 基础示例 ===\n');

  // 创建爬虫实例
  const spider = new WebSpider({
    baseUrl: 'https://example.com',
    timeout: 10000,
    headers: {
      'User-Agent': 'Mozilla/5.0 (compatible; VueSpiderExample/1.0)'
    }
  });

  try {
    // 执行爬虫任务
    console.log('开始爬取数据...\n');
    const data = await spider.run();
    
    // 显示结果
    console.log('\n爬取结果:');
    console.log('━'.repeat(50));
    data.forEach(item => {
      console.log(`\n标题: ${item.title}`);
      console.log(`链接: ${item.link || '无'}`);
      console.log(`描述: ${item.description || '无'}`);
      console.log(`时间: ${item.crawledAt}`);
    });
    console.log('\n' + '━'.repeat(50));
    console.log(`\n✅ 成功爬取 ${data.length} 条数据`);
    
  } catch (error) {
    console.error('\n❌ 爬取失败:', error.message);
  }
}

// 运行示例
basicExample();
