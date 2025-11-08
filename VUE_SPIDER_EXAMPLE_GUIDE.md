# Vue Spider Example 项目创建指南

本指南将帮助你创建一个名为 `vue_spider_example` 的私有仓库，并提供本地关联和上传代码的完整步骤。

## 第一步：在 GitHub 上创建私有仓库

### 方式一：通过 GitHub 网页界面创建

1. 登录 GitHub (https://github.com)
2. 点击右上角的 `+` 号，选择 `New repository`
3. 填写仓库信息：
   - **Repository name**: `vue_spider_example`
   - **Description**: "Vue.js 爬虫示例项目"
   - **Visibility**: 选择 `Private` （私有仓库）
   - 不要勾选 "Initialize this repository with a README"
4. 点击 `Create repository`

### 方式二：使用 GitHub CLI 创建（如果已安装 gh 命令）

```bash
gh repo create vue_spider_example --private --description "Vue.js 爬虫示例项目"
```

## 第二步：本地项目初始化

### 1. 创建项目目录

```bash
# 创建项目目录
mkdir vue_spider_example
cd vue_spider_example
```

### 2. 初始化 Git 仓库

```bash
# 初始化 git
git init

# 配置用户信息（如果还没配置）
git config user.name "你的名字"
git config user.email "你的邮箱@example.com"
```

### 3. 创建项目文件结构

参考下面的项目结构创建文件：

```
vue_spider_example/
├── README.md
├── package.json
├── .gitignore
├── src/
│   ├── spider/
│   │   ├── index.js
│   │   └── config.js
│   ├── vue-app/
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── components/
│   └── utils/
│       └── helpers.js
└── examples/
    └── basic-example.js
```

## 第三步：关联远程仓库并上传

### 1. 关联远程仓库

```bash
# 将你的 GitHub 用户名替换到下面的命令中
git remote add origin https://github.com/你的用户名/vue_spider_example.git

# 或者使用 SSH（如果配置了 SSH key）
git remote add origin git@github.com:你的用户名/vue_spider_example.git
```

### 2. 添加文件到暂存区

```bash
# 添加所有文件
git add .

# 或者逐个添加
git add README.md
git add package.json
git add src/
# ... 等等
```

### 3. 提交更改

```bash
git commit -m "初始提交：Vue Spider Example 项目"
```

### 4. 推送到远程仓库

```bash
# 推送到 main 分支（GitHub 新仓库默认分支）
git branch -M main
git push -u origin main
```

## 第四步：后续更新代码

当你修改代码后，使用以下命令上传更新：

```bash
# 查看修改状态
git status

# 添加修改的文件
git add .

# 提交修改
git commit -m "描述你的修改内容"

# 推送到远程仓库
git push
```

## 常用 Git 命令

```bash
# 查看仓库状态
git status

# 查看提交历史
git log

# 查看远程仓库信息
git remote -v

# 拉取远程更新
git pull

# 创建新分支
git checkout -b feature-branch-name

# 切换分支
git checkout main

# 查看所有分支
git branch -a
```

## 注意事项

1. **私有仓库权限**：私有仓库只有你和你授权的用户可以访问
2. **敏感信息**：不要将密码、API key 等敏感信息提交到仓库
3. **.gitignore**：使用 .gitignore 文件排除不需要版本控制的文件（如 node_modules）
4. **定期提交**：养成经常提交代码的习惯，便于版本管理和回滚

## 获取帮助

- GitHub 官方文档：https://docs.github.com
- Git 官方文档：https://git-scm.com/doc
- 如果遇到问题，可以使用 `git --help` 或 `git <command> --help` 查看帮助

---

## 项目示例代码

参考本仓库中的以下示例文件：
- `examples/vue_spider_example/` - 完整的项目示例
