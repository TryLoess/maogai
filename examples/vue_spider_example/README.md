# Vue Spider Example

这是一个结合 Vue.js 和网页爬虫的示例项目。

## 项目简介

本项目演示如何：
- 使用 Node.js 编写网页爬虫
- 使用 Vue.js 构建前端界面展示爬取的数据
- 整合爬虫后端和 Vue 前端

## 技术栈

- **前端**: Vue.js 3
- **爬虫**: Node.js + Axios + Cheerio
- **构建工具**: Vite
- **包管理**: npm

## 安装依赖

```bash
npm install
```

## 运行爬虫

```bash
node src/spider/index.js
```

## 运行前端应用

```bash
npm run dev
```

## 项目结构

```
vue_spider_example/
├── README.md                 # 项目说明
├── package.json              # 项目配置和依赖
├── .gitignore               # Git 忽略文件
├── vite.config.js           # Vite 配置
├── index.html               # HTML 入口文件
├── src/
│   ├── spider/              # 爬虫相关代码
│   │   ├── index.js         # 爬虫主文件
│   │   └── config.js        # 爬虫配置
│   ├── vue-app/             # Vue 应用
│   │   ├── App.vue          # Vue 主组件
│   │   ├── main.js          # Vue 入口文件
│   │   └── components/      # Vue 组件
│   │       └── DataDisplay.vue
│   └── utils/               # 工具函数
│       └── helpers.js
└── examples/                # 使用示例
    └── basic-example.js
```

## 功能特性

1. **数据爬取**: 从指定网站爬取数据
2. **数据存储**: 将爬取的数据保存为 JSON 文件
3. **数据展示**: 使用 Vue.js 展示爬取的数据
4. **响应式设计**: 支持移动端和桌面端

## 注意事项

1. 请遵守网站的 robots.txt 规则
2. 不要过于频繁地请求目标网站
3. 爬取数据仅供学习使用
4. 尊重网站的版权和服务条款

## 许可证

MIT License
