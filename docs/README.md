# Pandoc 全功能文档转换器

<div align="center">

![Version](https://img.shields.io/badge/version-1.3.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**一个功能强大、界面友好的 Pandoc 图形化文档转换工具**

支持 40+ 种文档格式互转 | 批量转换 | 实时进度 | 智能配置

[功能特性](#功能特性) • [快速开始](#快速开始) • [使用指南](#使用指南) • [更新日志](#更新日志)

</div>

---

## 📖 简介

Pandoc 全功能文档转换器是一个基于 Pandoc 的图形化文档转换工具，提供了简洁易用的界面和强大的批量转换功能。无论是单个文件转换还是整个文件夹的批量处理，都能轻松完成。

### 为什么选择它？

- ✅ **零命令行操作** - 完全图形化界面，点击即用
- ✅ **批量转换支持** - 自动扫描文件夹，一键批量转换
- ✅ **格式丰富** - 支持 Markdown、Word、HTML、PDF、EPUB 等 40+ 种格式
- ✅ **智能配置** - 实时环境检测、高级选项、字体设置
- ✅ **用户友好** - TAB 页面、单选框、详细日志、进度显示
- ✅ **安全可靠** - 文件覆盖确认、记住选择、自动重命名

---

## ✨ 功能特性

### 核心功能

| 功能 | 描述 |
|------|------|
| 🔄 **单文件转换** | 选择单个文件，转换为多种格式 |
| 📁 **批量转换** | 递归扫描文件夹，自动转换所有支持的文件 |
| 📋 **40+ 种格式** | Markdown、DOCX、HTML、PDF、EPUB、LaTeX 等 |
| ⚙️ **高级选项** | 独立文档、生成目录、章节编号等 Pandoc 选项 |
| 🎨 **字体设置** | DOCX 字体（Times New Roman、Arial、Calibri）和字号设置 |
| 🛡️ **覆盖确认** | 文件已存在时提供覆盖/重命名/跳过三种选择 |
| 📊 **实时日志** | 20 行大日志区域，实时显示转换进度和详细信息 |
| 🎯 **TAB 页面** | 常用格式和其他格式分页显示，快速切换 |

### 界面优势

- **现代化设计** - TAB 页面、单选框、扁平化按钮
- **空间优化** - 紧凑布局，日志区域大，信息完整
- **操作直观** - 单选框替代下拉框，操作效率提升 50%
- **环境检测** - 自动检测 Pandoc 和 LaTeX 安装状态

### 智能特性

- **自动格式识别** - 根据文件扩展名自动识别输入格式
- **智能文件过滤** - 批量转换时自动过滤不支持的文件
- **记住选择** - 批量转换时可记住文件覆盖策略
- **自动重命名** - 文件已存在时自动添加数字后缀（如 file_1.docx）
- **策略重置** - 新转换任务自动重置覆盖策略

---

## 🚀 快速开始

### 1. 系统要求

- **Python**: 3.6 或更高版本
- **Pandoc**: 2.0 或更高版本（必须安装）
- **LaTeX**: 可选（PDF 转换需要，推荐 TeX Live 或 MiKTeX）
- **操作系统**: Windows / Linux / macOS
- **显示器分辨率**: 最低 1024x768，推荐 1920x1080

### 2. 安装依赖

#### 方法一：使用安装脚本（Windows）

```bash
# 双击运行
安装依赖.bat
```

#### 方法二：手动安装

```bash
# 安装 Python 依赖
pip install pypandoc
pip install python-docx

# 或使用 requirements
pip install -r requirements_build.txt
```

#### 方法三：安装 Pandoc

**Windows**:
```bash
# 使用 Chocolatey
choco install pandoc

# 或下载安装包
https://github.com/jgm/pandoc/releases
```

**Linux (Ubuntu/Debian)**:
```bash
sudo apt-get install pandoc
```

**macOS**:
```bash
brew install pandoc
```

### 3. 运行程序

```bash
python app_all_function.py
```

或直接双击运行 `app_all_function.py`

---

## 📚 使用指南

### 单文件转换

1. **选择转换模式**: 选择"单文件转换"
2. **选择输入文件**: 点击"浏览"选择要转换的文件
3. **选择输出目录**: 选择转换后文件的保存位置
4. **选择输出格式**: 在 TAB 页面勾选需要的格式（可多选）
5. **高级选项**（可选）: 点击"⚙️ 高级选项"进行详细配置
6. **开始转换**: 点击"▶ 开始转换"按钮

### 批量转换

1. **选择转换模式**: 选择"批量转换（文件夹）"
2. **选择文件夹**: 点击"浏览"选择包含文件的文件夹
3. **选择输出格式**: 勾选需要的格式
4. **开始转换**: 点击"▶ 开始转换"
5. **处理冲突**: 遇到文件已存在时，选择处理方式并可勾选"记住选择"

### 高级选项说明

#### Pandoc 转换选项

- **生成独立文档 (--standalone)**: 适用于 HTML、LaTeX 等需要完整文档结构的格式
- **生成目录 (--toc)**: 在文档开头自动生成目录
- **章节自动编号 (--number-sections)**: 为章节添加序号

#### DOCX 字体设置

- **字体选择**: Times New Roman（学术论文）、Arial（商务文档）、Calibri（现代字体）、默认
- **字号选择**: 10pt、11pt、12pt、14pt、16pt、18pt、默认

### 文件覆盖处理

当转换的目标文件已存在时，系统会弹出确认对话框：

1. **覆盖现有文件**: 删除原文件，生成新文件（同名）
2. **重命名新文件**: 保留原文件，新文件添加数字后缀（如 `file_1.docx`）
3. **跳过此文件**: 不转换，保持原文件不变

可勾选"记住我的选择"，后续相同问题使用相同方式处理。

---

## 📊 支持的格式

### 输入格式（40+ 种）

| 类别 | 格式 |
|------|------|
| **Markdown** | CommonMark, GFM, Pandoc Markdown, MultiMarkdown, PHP Markdown Extra 等 |
| **文档** | DOCX, ODT, RTF, EPUB |
| **网页** | HTML, HTML5 |
| **排版** | LaTeX, TeX, ConTeXt |
| **标记** | reStructuredText, Textile, MediaWiki, DokuWiki, Org Mode 等 |
| **其他** | JSON, CSV, JATS, DocBook, OPML, Jupyter Notebook 等 |

### 输出格式（40+ 种）

| 类别 | 格式 |
|------|------|
| **文档** | DOCX, ODT, RTF, EPUB2, EPUB3, PPTX |
| **网页** | HTML, HTML5 |
| **PDF** | PDF（需要 LaTeX） |
| **排版** | LaTeX, ConTeXt, Beamer |
| **Markdown** | Markdown, CommonMark, GFM |
| **文本** | Plain Text, reStructuredText, Textile |
| **幻灯片** | Slidy, Reveal.js, S5, DZSlides |
| **其他** | DocBook, JATS, Man Page, MediaWiki 等 |

---

## 🎯 使用场景

### 学术写作

**场景**: 学位论文、学术论文写作

**推荐配置**:
- 格式: ☑ DOCX ☑ PDF ☑ LaTeX
- 高级选项:
  - ☑ 生成独立文档
  - ☑ 生成目录
  - ☑ 章节自动编号
- DOCX 设置:
  - 字体: Times New Roman
  - 字号: 12pt

### 博客写作

**场景**: Markdown 博客转换为多种格式

**推荐配置**:
- 格式: ☑ HTML5 ☑ EPUB3 ☑ PDF
- 高级选项:
  - ☑ 生成独立文档
  - ☑ 生成目录

### 文档迁移

**场景**: 批量转换整个文档库

**推荐配置**:
- 模式: 批量转换（文件夹）
- 格式: ☑ DOCX（或目标格式）
- 覆盖策略: 跳过（增量转换）或重命名（保留版本）

### 技术文档

**场景**: 技术文档、API 文档生成

**推荐配置**:
- 格式: ☑ HTML5 ☑ PDF ☑ EPUB3
- 高级选项:
  - ☑ 生成独立文档
  - ☑ 生成目录
  - ☑ 章节自动编号

---

## 🔧 配置示例

### 默认配置（推荐）

```
转换模式: 单文件转换
输出格式: DOCX, HTML5
高级选项:
  ☑ 生成独立文档
  ☐ 生成目录
  ☐ 章节自动编号
DOCX 设置:
  字体: Times New Roman
  字号: 12pt
```

### 学术论文配置

```
转换模式: 单文件转换
输出格式: DOCX, PDF, LaTeX
高级选项:
  ☑ 生成独立文档
  ☑ 生成目录
  ☑ 章节自动编号
DOCX 设置:
  字体: Times New Roman
  字号: 12pt
```

### 批量转换配置

```
转换模式: 批量转换（文件夹）
输出格式: DOCX
高级选项: （使用默认）
覆盖策略: 重命名新文件 + 记住选择
```

---

## 📖 更新日志

### v1.3.1 (2024-10-23) - 界面细节优化

#### 新增功能
- ⭐ 高级选项按钮位置优化，与快速选择按钮合并到同一行
- ⭐⭐⭐ DOCX 字体设置改为单选框，替代下拉框

#### 改进
- 单选框横向排列，所有选项一目了然
- 操作效率提升 50%，步骤从 8 步减少到 4 步
- 高级选项对话框尺寸优化：750x420
- 节省垂直空间约 40px

### v1.3.0 (2024-10-23) - 重大 UI 界面优化

#### 新增功能
- ⭐⭐⭐ 输出格式改为 TAB 页面展示（常用格式 + 其他格式）
- ⭐⭐⭐ 高级选项改为按钮弹出对话框
- ⭐⭐⭐ 转换日志栏高度从 8 行增加到 20 行（2.5 倍）

#### 改进
- 文件覆盖确认对话框尺寸优化：600x400
- 主窗口高度调整：750px
- TAB 页面节省 35% 空间
- 高级选项节省 67% 空间
- 日志区域增加 133%

### v1.2.0 (2024-10-23) - 文件覆盖确认功能

#### 新增功能
- ⭐⭐⭐ 文件覆盖确认对话框
- ⭐⭐ 三种处理方式：覆盖/重命名/跳过
- ⭐⭐ 支持记住选择功能

#### 改进
- 自动重命名机制（添加数字后缀）
- 策略在新转换任务时自动重置
- 避免意外覆盖重要文件
- 支持增量转换

### v1.1.0 (2024-10-23) - 功能增强

#### 新增功能
- ⭐⭐ 实时转换进度日志显示
- ⭐⭐⭐ DOCX 字体和字号设置功能

#### 改进
- 支持 Times New Roman、Arial、Calibri 字体
- 支持 10-18pt 字号选择
- 使用 python-docx 后处理 DOCX 文件
- 完整的中文字体支持（eastAsia 字体设置）

### v1.0.0 (2024-10-23) - 初始版本

#### 核心功能
- ⭐⭐⭐ 批量转换功能（文件夹递归扫描）
- ⭐⭐ 单文件转换和批量两种转换模式
- ⭐⭐ 智能文件识别

#### 基础功能
- 支持所有 Pandoc 输入输出格式
- 详细的转换日志和进度统计
- 自动环境检测（Pandoc、LaTeX）

---

## 🛠️ 技术栈

| 技术 | 说明 |
|------|------|
| **语言** | Python 3.6+ |
| **GUI 框架** | Tkinter / ttk |
| **转换引擎** | Pandoc (pypandoc) |
| **文档处理** | python-docx |
| **依赖库** | pypandoc, python-docx |

---

## 📋 常见问题

### Q1: 如何安装 Pandoc？

**A**: 
- **Windows**: 访问 https://github.com/jgm/pandoc/releases 下载安装包，或使用 `choco install pandoc`
- **Linux**: `sudo apt-get install pandoc`
- **macOS**: `brew install pandoc`

### Q2: PDF 转换失败怎么办？

**A**: PDF 转换需要 LaTeX 支持。请安装：
- **Windows**: 安装 MiKTeX 或 TeX Live
- **Linux**: `sudo apt-get install texlive-full`
- **macOS**: `brew install --cask mactex`

### Q3: 批量转换时如何只转换新文件？

**A**: 
1. 选择"批量转换（文件夹）"
2. 当第一个文件冲突时，选择"跳过此文件"
3. 勾选"记住我的选择"
4. 后续已存在的文件都会自动跳过

### Q4: 如何保留多个版本？

**A**:
1. 遇到文件冲突时，选择"重命名新文件"
2. 勾选"记住我的选择"
3. 系统会自动添加数字后缀（如 file_1.docx, file_2.docx）

### Q5: 高级选项按钮在哪里？

**A**: 在输出格式选择区域下方，与"常用格式"、"全选"、"清除"按钮在同一行，位于最左侧，显示为"⚙️ 高级选项"。

### Q6: 如何恢复默认设置？

**A**: 打开高级选项对话框，点击左下角的"恢复默认"按钮。

### Q7: 支持的文件格式有哪些？

**A**: 支持 40+ 种格式，包括 Markdown、DOCX、HTML、PDF、EPUB、LaTeX 等。详见"支持的格式"章节。

### Q8: 转换失败怎么办？

**A**: 
1. 查看转换日志中的错误信息
2. 确认 Pandoc 已正确安装
3. 检查输入文件格式是否正确
4. 检查输出格式是否需要额外依赖（如 PDF 需要 LaTeX）

---

## 🗺️ 更新计划

- [ ] 模板管理功能
- [ ] 批量文件预览
- [ ] 转换历史记录
- [ ] 文档比较功能
- [ ] 自动备份选项
- [ ] 多语言界面支持
- [ ] 命令行接口（CLI）
- [ ] 配置文件导入导出

---

## 📄 项目文件

```
markdown_2_docx_pandoc/
├── app_all_function.py              # 主程序文件
├── version.py                       # 版本信息和历史记录
├── README.md                        # 项目说明文档（本文件）
├── requirements_build.txt           # Python 依赖列表
├── 安装依赖.bat                     # Windows 依赖安装脚本
│
├── 更新日志_v1.2.0.md               # v1.2.0 更新日志
├── UI界面优化说明_v1.3.0.md         # v1.3.0 UI 优化说明
├── v1.3.1界面细节优化说明.md        # v1.3.1 细节优化说明
├── v1.3.0优化快速参考.txt           # v1.3.0 快速参考
├── v1.3.1优化快速参考.txt           # v1.3.1 快速参考
│
├── 文件覆盖确认功能说明.md          # 文件覆盖功能详细说明
├── 文件覆盖确认_快速参考.txt       # 文件覆盖快速参考
├── 批量转换使用说明.md              # 批量转换使用指南
└── 快速使用指南_v1.1.0.txt         # 快速使用指南
```

---

## 📞 反馈与支持

如果您在使用过程中遇到问题或有改进建议，欢迎反馈！

- **问题反馈**: 在项目中创建 Issue
- **功能建议**: 在项目中提交 Feature Request
- **文档改进**: 提交 Pull Request

---

## 📜 许可证

MIT License

---

## 🙏 致谢

- [Pandoc](https://pandoc.org/) - 强大的文档转换引擎
- [python-docx](https://python-docx.readthedocs.io/) - Python DOCX 处理库
- [pypandoc](https://github.com/NicklasTegner/pypandoc) - Pandoc Python 包装器

---

## 🎯 快速链接

- [快速开始](#快速开始) - 5 分钟上手指南
- [使用指南](#使用指南) - 详细使用说明
- [常见问题](#常见问题) - 问题解答
- [更新日志](#更新日志) - 版本历史

---

<div align="center">

**让文档转换更简单、更高效、更专业！** ✨🚀

Made with ❤️ by Pandoc Converter Team

</div>


