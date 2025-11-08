# 如何使用本仓库中的 vue_spider_example 项目模板

## 📖 概述

本仓库现在包含了一个完整的 `vue_spider_example` 项目模板和详细的使用指南，帮助你：

1. 创建自己的私有 GitHub 仓库
2. 在本地关联和上传代码
3. 快速启动一个 Vue.js + 网页爬虫的项目

## 📁 文件说明

### 主要文件

- **VUE_SPIDER_EXAMPLE_GUIDE.md** - 完整的创建仓库和上传代码指南
- **examples/vue_spider_example/** - 可直接使用的完整项目模板

## 🚀 使用步骤

### 步骤 1: 阅读指南

首先阅读 `VUE_SPIDER_EXAMPLE_GUIDE.md` 文件，了解如何：
- 在 GitHub 上创建私有仓库
- 初始化本地 Git 仓库
- 关联远程仓库并上传代码

### 步骤 2: 复制项目模板

将 `examples/vue_spider_example/` 目录复制到你想要的位置：

```bash
# 复制整个项目模板到新位置
cp -r examples/vue_spider_example ~/my-projects/vue_spider_example

# 进入项目目录
cd ~/my-projects/vue_spider_example
```

### 步骤 3: 初始化 Git

```bash
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "初始提交：Vue Spider Example 项目"
```

### 步骤 4: 创建 GitHub 仓库

按照 `VUE_SPIDER_EXAMPLE_GUIDE.md` 中的说明：
1. 在 GitHub 上创建名为 `vue_spider_example` 的私有仓库
2. 不要勾选 "Initialize this repository with a README"

### 步骤 5: 关联并推送

```bash
# 关联远程仓库（替换为你的 GitHub 用户名）
git remote add origin https://github.com/你的用户名/vue_spider_example.git

# 推送到远程仓库
git branch -M main
git push -u origin main
```

### 步骤 6: 开始开发

```bash
# 安装依赖
npm install

# 使用快速启动脚本（推荐）
./start.sh

# 或手动运行命令
npm run dev      # 启动前端
npm run spider   # 运行爬虫
```

## 📚 文档资源

项目模板包含以下文档：

1. **README.md** - 项目说明和技术栈介绍
2. **QUICK_REFERENCE.md** - 快速参考和常见问题
3. **VUE_SPIDER_EXAMPLE_GUIDE.md** - 完整的仓库创建和代码上传指南

## 🎯 项目特点

这个模板项目包含：

✅ **前端部分** (Vue.js 3)
- 现代化的 UI 界面
- 响应式设计
- 数据展示组件

✅ **爬虫部分** (Node.js)
- 使用 Axios 获取网页
- 使用 Cheerio 解析 HTML
- 可配置的爬虫设置

✅ **开发工具**
- Vite 构建工具
- 快速启动脚本
- 完整的项目结构

## 💡 下一步

1. 自定义爬虫目标网站 (`src/spider/config.js`)
2. 修改数据解析逻辑 (`src/spider/index.js`)
3. 自定义前端样式 (`src/vue-app/App.vue`)
4. 添加新功能和组件

## ⚠️ 重要提示

- 爬虫使用请遵守法律法规和网站的 robots.txt
- 不要过于频繁地请求目标网站
- 爬取的数据仅供学习使用
- 敏感信息（API key、密码等）不要提交到仓库

## 🤝 需要帮助？

如果遇到问题，可以：
1. 查看 `QUICK_REFERENCE.md` 中的常见问题部分
2. 检查项目的 README.md
3. 参考官方文档链接

---

祝你使用愉快！🎉
