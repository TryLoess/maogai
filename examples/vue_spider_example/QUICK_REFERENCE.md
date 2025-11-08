# Vue Spider Example 快速参考

## 📋 目录结构

```
vue_spider_example/
├── README.md                    # 项目说明
├── package.json                 # 项目配置
├── .gitignore                  # Git 忽略文件
├── vite.config.js              # Vite 配置
├── index.html                  # HTML 入口
├── start.sh                    # 快速启动脚本
├── src/
│   ├── spider/                 # 爬虫代码
│   │   ├── index.js           # 爬虫主文件
│   │   └── config.js          # 爬虫配置
│   ├── vue-app/               # Vue 应用
│   │   ├── App.vue            # 主组件
│   │   ├── main.js            # 入口文件
│   │   └── components/
│   │       └── DataDisplay.vue # 数据展示组件
│   └── utils/                 # 工具函数
│       └── helpers.js
└── examples/                  # 示例代码
    └── basic-example.js
```

## 🚀 快速开始

### 方法一：使用快速启动脚本（推荐）

```bash
# 在项目目录下运行
./start.sh
```

### 方法二：手动命令

```bash
# 1. 安装依赖
npm install

# 2. 运行爬虫
npm run spider

# 3. 运行前端
npm run dev

# 4. 查看示例
npm run spider:example
```

## 📝 常用命令

| 命令 | 说明 |
|------|------|
| `npm install` | 安装项目依赖 |
| `npm run dev` | 启动开发服务器 |
| `npm run build` | 构建生产版本 |
| `npm run preview` | 预览生产版本 |
| `npm run spider` | 运行爬虫 |
| `npm run spider:example` | 运行示例代码 |

## 🔧 自定义配置

### 修改爬虫目标

编辑 `src/spider/config.js`:

```javascript
export default {
  baseUrl: 'https://your-target-site.com',  // 修改为目标网站
  timeout: 10000,
  // ...
};
```

### 自定义数据解析

编辑 `src/spider/index.js` 中的 `parseContent` 方法:

```javascript
parseContent(html) {
  const $ = cheerio.load(html);
  const results = [];
  
  // 自定义你的选择器
  $('.your-selector').each((index, element) => {
    // 提取数据
  });
  
  return results;
}
```

## 🎨 自定义前端样式

修改 `src/vue-app/App.vue` 中的 `<style>` 部分来自定义样式。

## 📦 添加新功能

### 添加新的 Vue 组件

1. 在 `src/vue-app/components/` 创建新组件
2. 在 `App.vue` 中引入并使用

### 添加新的爬虫功能

1. 在 `src/spider/` 中创建新模块
2. 在 `index.js` 中导入并使用

## 🔍 常见问题

### Q: 爬虫返回空数据？

**A**: 检查以下几点：
- 目标网站的 HTML 结构是否变化
- 选择器是否正确
- 网站是否需要登录或验证
- 是否被反爬虫机制阻止

### Q: 前端无法加载数据？

**A**: 确保：
- 爬虫已成功运行并生成数据文件
- 数据文件位于正确的位置
- 检查浏览器控制台错误信息

### Q: npm install 失败？

**A**: 尝试：
```bash
# 清除缓存
npm cache clean --force

# 删除 node_modules 和 package-lock.json
rm -rf node_modules package-lock.json

# 重新安装
npm install
```

## 📚 学习资源

- Vue.js 官方文档: https://vuejs.org/
- Axios 文档: https://axios-http.com/
- Cheerio 文档: https://cheerio.js.org/
- Vite 文档: https://vitejs.dev/

## ⚠️ 注意事项

1. **遵守法律法规**: 爬取数据请遵守相关法律法规
2. **尊重 robots.txt**: 遵守网站的爬虫协议
3. **控制频率**: 不要过于频繁地请求目标网站
4. **数据使用**: 爬取的数据仅供学习使用
5. **隐私保护**: 不要爬取和传播个人隐私信息

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License
