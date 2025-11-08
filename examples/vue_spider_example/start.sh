#!/bin/bash

# Vue Spider Example 快速启动脚本

echo "==================================="
echo "  Vue Spider Example 快速启动"
echo "==================================="
echo ""

# 检查是否在正确的目录
if [ ! -f "package.json" ]; then
    echo "❌ 错误: 请在项目根目录运行此脚本"
    exit 1
fi

# 检查 Node.js 是否安装
if ! command -v node &> /dev/null; then
    echo "❌ 错误: 未检测到 Node.js，请先安装 Node.js"
    echo "   下载地址: https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js 版本: $(node --version)"
echo "✅ npm 版本: $(npm --version)"
echo ""

# 检查依赖是否已安装
if [ ! -d "node_modules" ]; then
    echo "📦 正在安装依赖..."
    npm install
    if [ $? -ne 0 ]; then
        echo "❌ 依赖安装失败"
        exit 1
    fi
    echo "✅ 依赖安装完成"
    echo ""
fi

# 显示菜单
echo "请选择要执行的操作:"
echo "1) 运行爬虫"
echo "2) 运行 Vue 前端应用"
echo "3) 运行示例代码"
echo "4) 构建生产版本"
echo "5) 退出"
echo ""

read -p "请输入选项 (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🕷️  正在运行爬虫..."
        npm run spider
        ;;
    2)
        echo ""
        echo "🚀 正在启动 Vue 应用..."
        echo "   浏览器将自动打开 http://localhost:3000"
        npm run dev
        ;;
    3)
        echo ""
        echo "📝 正在运行示例代码..."
        npm run spider:example
        ;;
    4)
        echo ""
        echo "🔨 正在构建生产版本..."
        npm run build
        echo "✅ 构建完成！文件位于 dist/ 目录"
        ;;
    5)
        echo "👋 再见！"
        exit 0
        ;;
    *)
        echo "❌ 无效的选项"
        exit 1
        ;;
esac
