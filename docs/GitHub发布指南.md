# ChangoConverter GitHub发布指南

## 📋 发布信息

- **项目名称**: ChangoConverter
- **版本**: v1.4.1
- **GitHub用户**: wyg5208
- **仓库建议名称**: ChangoConverter
- **项目描述**: 基于Pandoc的全功能文档转换器，支持批量转换、字体定制、智能UI

---

## 🚀 第一步：创建GitHub仓库

### 1.1 登录GitHub
访问 https://github.com 并登录 wyg5208 账号

### 1.2 创建新仓库
1. 点击右上角 `+` → `New repository`
2. 填写仓库信息：
   - **Repository name**: `ChangoConverter`
   - **Description**: `🔄 基于Pandoc的全功能文档转换器 | 支持批量转换、字体定制、智能UI | Full-Featured Document Converter`
   - **Visibility**: `Public` (公开) 或 `Private` (私有)
   - **✓** Initialize this repository with a README (不勾选，我们有自己的README)
   - **Add .gitignore**: `Python`
   - **Choose a license**: `MIT License` (推荐)

3. 点击 `Create repository`

---

## 📦 第二步：准备发布文件

### 2.1 创建.gitignore文件

在项目根目录创建 `.gitignore`：

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
temp_content.md
*.log
test_output/
```

### 2.2 确保必要文件存在

确认以下文件已准备好：
- ✅ README.md (项目主文档)
- ✅ LICENSE (如果选择了MIT)
- ✅ requirements_build.txt (依赖清单)
- ✅ app_all_function.py (主程序)
- ✅ version.py (版本信息)
- ✅ docs/ 目录 (所有文档)
- ✅ resources/ 目录 (图标、资源)

---

## 🔧 第三步：本地Git初始化

### 3.1 打开PowerShell/命令提示符

```powershell
cd D:\python_projects\markdown_2_docx_pandoc
```

### 3.2 初始化Git仓库

```bash
# 初始化Git仓库
git init

# 配置用户信息（如果还没配置）
git config user.name "wyg5208"
git config user.email "wyg5208@126.com"  # 替换为你的邮箱
```

### 3.3 添加远程仓库

```bash
# 添加远程仓库（替换为你的实际仓库URL）
git remote add origin https://github.com/wyg5208/ChangoConverter.git
```

### 3.4 添加文件到Git

```bash
# 添加所有文件
git add .

# 查看状态
git status

# 提交
git commit -m "🎉 Initial commit: ChangoConverter v1.4.1

- ✨ 完整的文档转换功能
- 🎨 专业图标设计
- 📚 完善的文档系统
- 🔄 批量转换支持
- 📝 DOCX字体定制
- 📄 PDF转换优化
- 🎯 智能UI设计"
```

### 3.5 推送到GitHub

```bash
# 推送到GitHub主分支
git push -u origin main

# 如果提示使用master分支，使用：
# git branch -M main
# git push -u origin main
```

---

## 🏷️ 第四步：创建Release发布

### 4.1 打包可执行文件（可选）

```bash
# 运行打包脚本
.\快速打包.bat

# 打包完成后，在 dist/ 目录会生成 ChangoConverter.exe
```

### 4.2 准备Release资源

创建一个发布文件夹：
```
ChangoConverter_v1.4.1_Release/
├── ChangoConverter.exe              # 可执行文件
├── README.md                        # 使用说明
├── 快速使用指南.pdf                 # (可选)转换的PDF指南
└── resources/                       # 资源文件
    └── icon.ico
```

### 4.3 创建压缩包

```powershell
# 使用PowerShell压缩
Compress-Archive -Path "dist\*" -DestinationPath "ChangoConverter_v1.4.1_Windows_x64.zip"
```

### 4.4 在GitHub上创建Release

1. 访问仓库页面：`https://github.com/wyg5208/ChangoConverter`
2. 点击右侧 `Releases` → `Create a new release`
3. 填写Release信息：

**Tag version**: `v1.4.1`

**Release title**: `ChangoConverter v1.4.1 - 专业图标 + 目录优化`

**Description**:

```markdown
## 🎉 ChangoConverter v1.4.1 发布

### ✨ 主要特性

#### 🎨 全新功能
- ✅ **专业应用图标**: 深绿色CC标识，多尺寸支持
- ✅ **目录结构优化**: 根目录精简40%，文档集中管理
- ✅ **完善文档系统**: 包含完整README和详细说明

#### 🔄 核心功能
- ✅ **批量转换**: 自动遍历文件夹和子文件夹
- ✅ **多格式支持**: Markdown、HTML、Word、PDF、PowerPoint等12+种格式
- ✅ **字体定制**: 支持设置DOCX文件的字体和字号
- ✅ **智能UI**: 左右布局，TAB页面，高度优化
- ✅ **PDF优化**: XeLaTeX引擎，自动处理Emoji

#### 📊 界面优化
- ✅ 主窗体高度减少20%，更紧凑
- ✅ 左右布局，日志在右侧1/3区域
- ✅ 深绿色转换按钮，视觉突出
- ✅ 深色按钮文字，对比度更好

### 📦 下载

- **Windows 64位**: `ChangoConverter_v1.4.1_Windows_x64.zip`
- **源代码**: Source code (zip/tar.gz)

### 📋 系统要求

- **操作系统**: Windows 7/10/11 (64位)
- **Python**: 3.8+ (如果运行源代码)
- **Pandoc**: 2.0+ (必需)
- **LaTeX**: MiKTeX (PDF转换可选)
- **显示器**: 最低 1280x768

### 🚀 快速开始

#### 使用可执行文件
1. 下载 `ChangoConverter_v1.4.1_Windows_x64.zip`
2. 解压到任意目录
3. 双击 `ChangoConverter.exe` 运行

#### 使用源代码
```bash
# 克隆仓库
git clone https://github.com/wyg5208/ChangoConverter.git
cd ChangoConverter

# 安装依赖
pip install -r requirements_build.txt

# 运行程序
python app_all_function.py
```

### 📚 文档

- [快速使用指南](docs/快速使用指南_v1.1.0.txt)
- [批量转换指南](docs/批量转换快速开始.txt)
- [PDF转换指南](docs/PDF转换问题快速解决.txt)
- [目录结构说明](docs/目录结构说明.md)

### 🔧 完整更新日志

#### v1.4.1 (2024-10-24)
- ✨ 设计并应用专业应用图标（深绿色CC标识）
- ✨ 使用Python PIL自动生成多尺寸ICO图标（256-16px）
- ✨ 完成目录结构清理优化（根目录从30+精简到18个文件）
- ✨ 创建docs/目录集中管理所有文档（20+个MD和TXT）
- ✨ 创建test_scripts/目录管理测试脚本
- ✨ 创建resources/目录存放资源文件（图标、Lua脚本）
- ✨ 创建完整的README.md项目文档
- ✨ 创建目录结构说明.md详细文档
- 📝 窗口高度优化：600px → 480px（再减少20%）
- 📝 开始转换按钮文字改为深色（#1a1a1a），对比度更好
- 🐛 修复PDF转换Emoji字体缺失问题
- 🐛 增强时间类Emoji映射（⏱⏲等）

### ⭐ 版本亮点

- ⭐⭐⭐ **专业图标设计**，提升品牌识别度
- ⭐⭐⭐ **目录结构清理**，易于维护和管理
- ⭐⭐⭐ **界面更紧凑**，高度减少20%
- ⭐⭐⭐ **PDF转换优化**，自动处理Emoji
- ⭐⭐ **完善的文档系统**，包含完整README

### 🐛 已知问题

- PDF转换需要安装MiKTeX和LaTeX包
- 部分Unicode字符可能在PDF中显示为空（LaTeX限制）
- 建议不要以管理员身份运行程序

### 🤝 贡献

欢迎提交Issue和Pull Request！

### 📄 许可证

MIT License

---

**ChangoConverter** - 让文档转换更简单、更专业、更高效！ 🚀
```

4. 上传附件：
   - 拖拽 `ChangoConverter_v1.4.1_Windows_x64.zip` 到附件区域

5. 点击 `Publish release`

---

## 🎨 第五步：美化GitHub仓库

### 5.1 添加Shields徽章

编辑README.md，在顶部添加：

```markdown
# ChangoConverter 全功能文档转换器

![Version](https://img.shields.io/badge/version-1.4.1-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Pandoc](https://img.shields.io/badge/pandoc-required-orange.svg)

🔄 基于Pandoc的强大文档格式转换工具，支持批量转换、字体设置、智能UI等功能。
```

### 5.2 添加截图

在README.md中添加程序截图：

```markdown
## 📸 界面预览

![主界面](docs/screenshots/main_interface.png)
*左右布局，日志在右侧，界面简洁美观*

![批量转换](docs/screenshots/batch_convert.png)
*批量转换，自动遍历文件夹*
```

建议截取几张程序界面截图，保存到 `docs/screenshots/` 目录。

### 5.3 创建GitHub Pages（可选）

在仓库设置中：
1. Settings → Pages
2. Source: Deploy from a branch
3. Branch: main, /docs
4. 访问 `https://wyg5208.github.io/ChangoConverter/`

---

## 📊 第六步：维护和更新

### 6.1 日常提交

```bash
# 修改文件后
git add .
git commit -m "🐛 修复某个问题"
git push
```

### 6.2 发布新版本

```bash
# 更新版本号（在version.py中）
# 提交更改
git add .
git commit -m "🔖 Release v1.4.2"
git push

# 创建新的tag
git tag -a v1.4.2 -m "Release v1.4.2"
git push origin v1.4.2

# 在GitHub上创建新的Release
```

### 6.3 处理Issues

- 及时回复用户问题
- 使用标签分类：bug, enhancement, documentation
- 关闭已解决的Issues

---

## 📝 第七步：编写优秀的README

### 7.1 README结构建议

```markdown
# 项目标题
简短描述 + 徽章

## 特性
核心功能列表

## 快速开始
安装和使用步骤

## 截图
界面预览

## 文档
详细文档链接

## 贡献
如何参与贡献

## 许可证
MIT License

## 联系方式
作者信息
```

### 7.2 多语言支持（可选）

```markdown
[English](README.md) | [简体中文](README_CN.md)
```

---

## 🔐 第八步：安全和权限

### 8.1 创建.gitattributes

```gitattributes
# Auto detect text files and perform LF normalization
* text=auto

# Python files
*.py text eol=lf

# Windows batch files
*.bat text eol=crlf

# Binary files
*.exe binary
*.ico binary
*.png binary
```

### 8.2 保护分支（可选）

Settings → Branches → Add rule:
- Branch name pattern: `main`
- ✓ Require pull request reviews before merging
- ✓ Require status checks to pass before merging

---

## 🎯 发布检查清单

发布前确认：

### 代码和文档
- [ ] 代码已测试，无明显bug
- [ ] README.md完整详细
- [ ] 版本号已更新（version.py）
- [ ] 更新日志已完成
- [ ] LICENSE文件存在
- [ ] .gitignore配置正确

### Git和GitHub
- [ ] 本地仓库已初始化
- [ ] 远程仓库已创建
- [ ] 所有文件已提交
- [ ] 已推送到GitHub
- [ ] Release已创建
- [ ] 可执行文件已上传

### 项目质量
- [ ] 图标显示正常
- [ ] 目录结构清晰
- [ ] 文档完整准确
- [ ] 依赖清单正确
- [ ] 打包脚本可用

### 用户体验
- [ ] README易于理解
- [ ] 快速开始步骤清晰
- [ ] 截图美观专业
- [ ] 问题和贡献指南明确

---

## 🚀 快速命令参考

```bash
# 初始化和推送
git init
git remote add origin https://github.com/wyg5208/ChangoConverter.git
git add .
git commit -m "🎉 Initial commit: ChangoConverter v1.4.1"
git branch -M main
git push -u origin main

# 创建标签
git tag -a v1.4.1 -m "Release v1.4.1"
git push origin v1.4.1

# 更新推送
git add .
git commit -m "更新说明"
git push

# 查看状态
git status
git log --oneline

# 撤销操作
git reset HEAD~1          # 撤销上次提交（保留更改）
git checkout -- 文件名     # 丢弃本地更改
```

---

## 📞 遇到问题？

### 常见问题

**Q: 推送时要求输入用户名密码**
A: 使用Personal Access Token代替密码，在GitHub Settings → Developer settings → Personal access tokens创建

**Q: 推送被拒绝**
A: 先拉取远程更改：`git pull origin main --rebase`，然后再推送

**Q: 文件太大无法上传**
A: GitHub单文件限制100MB，使用Git LFS或不提交大文件

**Q: 如何删除已提交的敏感文件**
A: 使用 `git filter-branch` 或 `BFG Repo-Cleaner`

### 获取帮助

- GitHub文档: https://docs.github.com/
- Git文档: https://git-scm.com/doc
- Stack Overflow: https://stackoverflow.com/questions/tagged/git

---

## 🎉 发布完成！

完成以上步骤后，你的ChangoConverter项目将：

✅ 在GitHub上公开可访问  
✅ 拥有专业的README文档  
✅ 提供可下载的Release版本  
✅ 具备完整的版本管理  
✅ 方便用户和贡献者参与  

**仓库地址**: https://github.com/wyg5208/ChangoConverter

祝你的项目获得更多star！⭐⭐⭐

---

**注意**: 请替换文中所有的占位符为你的实际信息（如邮箱地址等）。

