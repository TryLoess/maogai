import axios from 'axios';
import * as cheerio from 'cheerio';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import config from './config.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/**
 * 网页爬虫主类
 */
class WebSpider {
  constructor(options = {}) {
    this.baseUrl = options.baseUrl || config.baseUrl;
    this.timeout = options.timeout || config.timeout;
    this.headers = {
      'User-Agent': config.userAgent,
      ...options.headers
    };
  }

  /**
   * 获取网页内容
   * @param {string} url - 目标 URL
   * @returns {Promise<string>} HTML 内容
   */
  async fetchPage(url) {
    try {
      console.log(`正在获取: ${url}`);
      const response = await axios.get(url, {
        headers: this.headers,
        timeout: this.timeout
      });
      return response.data;
    } catch (error) {
      console.error(`获取页面失败: ${error.message}`);
      throw error;
    }
  }

  /**
   * 解析 HTML 内容
   * @param {string} html - HTML 内容
   * @returns {Array} 解析后的数据
   */
  parseContent(html) {
    const $ = cheerio.load(html);
    const results = [];

    // 示例：爬取所有文章标题和链接
    $('article, .post, .item').each((index, element) => {
      const title = $(element).find('h2, h3, .title').text().trim();
      const link = $(element).find('a').attr('href');
      const description = $(element).find('p, .description').first().text().trim();

      if (title) {
        results.push({
          id: index + 1,
          title,
          link: link ? new URL(link, this.baseUrl).href : null,
          description,
          crawledAt: new Date().toISOString()
        });
      }
    });

    return results;
  }

  /**
   * 保存数据到文件
   * @param {Array} data - 要保存的数据
   * @param {string} filename - 文件名
   */
  async saveData(data, filename = 'spider-data.json') {
    const outputPath = path.join(__dirname, '../../data', filename);
    
    // 确保目录存在
    await fs.mkdir(path.dirname(outputPath), { recursive: true });
    
    await fs.writeFile(
      outputPath,
      JSON.stringify(data, null, 2),
      'utf-8'
    );
    
    console.log(`数据已保存到: ${outputPath}`);
    console.log(`共爬取 ${data.length} 条记录`);
  }

  /**
   * 执行爬虫任务
   * @param {string} url - 目标 URL
   * @returns {Promise<Array>} 爬取的数据
   */
  async run(url = this.baseUrl) {
    try {
      console.log('开始爬取数据...');
      const html = await this.fetchPage(url);
      const data = this.parseContent(html);
      await this.saveData(data);
      console.log('爬取完成！');
      return data;
    } catch (error) {
      console.error(`爬虫执行失败: ${error.message}`);
      throw error;
    }
  }
}

// 如果直接运行此文件，执行爬虫
if (import.meta.url === `file://${process.argv[1]}`) {
  const spider = new WebSpider();
  spider.run().catch(console.error);
}

export default WebSpider;
