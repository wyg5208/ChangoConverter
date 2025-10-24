# Pandoc 全功能文档转换器 v1.0.0

一个基于 Pandoc 的图形化文档格式转换工具，支持 30+ 种输入格式和 40+ 种输出格式的互相转换。

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Pandoc Required](https://img.shields.io/badge/pandoc-required-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ 主要特性

### 🚀 核心功能
- **全格式支持**：支持 30+ 输入格式，40+ 输出格式
- **智能识别**：自动识别输入文件格式
- **批量转换**：一次性输出多个格式
- **实时日志**：转换过程实时显示
- **友好界面**：直观的图形用户界面

### 📋 支持的格式

#### 📥 输入格式（30+）
- **Markdown 系列**：markdown, commonmark, gfm, markdown_mmd, markdown_phpextra, markdown_strict
- **文档格式**：docx, odt, rtf, epub, pdf
- **标记语言**：html, latex, rst, org, textile, mediawiki
- **其他格式**：docbook, jats, csv, ipynb 等

#### 📤 输出格式（40+）
- **常用格式**：markdown, html5, docx, pdf, plain text, pptx
- **电子书**：epub, epub3, fb2
- **幻灯片**：beamer, reveal.js, slidy, s5, dzslides
- **专业排版**：latex, context, texinfo, icml
- **其他格式**：asciidoc, rst, org, mediawiki, dokuwiki 等

## 📦 安装说明

### 1️⃣ 安装 Python
需要 Python 3.7 或更高版本

### 2️⃣ 安装 Pandoc
从官网下载并安装：https://pandoc.org/installing.html

### 3️⃣ 安装 pypandoc
```bash
pip install pypandoc
```

### 4️⃣ 安装 LaTeX（可选，PDF 转换必需）

#### Windows 系统 - MiKTeX（推荐）
1. 下载：https://miktex.org/download
2. 选择 Basic MiKTeX Installer（约 200MB）
3. 安装时选择"Install missing packages on-the-fly"为"Yes"
4. 验证安装：
   ```bash
   pdflatex --version
   ```

#### macOS 系统 - MacTeX
1. 下载：https://www.tug.org/mactex/
2. 安装 MacTeX.pkg（约 4GB）
3. 验证安装：
   ```bash
   pdflatex --version
   ```

#### Linux 系统 - TeX Live
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# Fedora/CentOS
sudo dnf install texlive-scheme-full

# Arch Linux
sudo pacman -S texlive-most
```

#### 轻量级选择 - TinyTeX
适合只需要 PDF 转换的用户（约 100MB）
官网：https://yihui.org/tinytex/

## 🎯 使用方法

### 启动程序
```bash
python app_all_function.py
```

### 基本步骤
1. **选择输入文件** - 点击"浏览"选择要转换的文件
2. **选择输出目录** - 默认为输入文件所在目录
3. **选择输出格式** - 勾选需要的格式（可多选）
4. **设置高级选项**（可选）
   - ☑ 独立文档 (--standalone)
   - ☑ 生成目录 (--toc)
   - ☑ 章节编号 (--number-sections)
5. **开始转换** - 点击"开始转换"按钮

### 快速选择
- **常用格式** - 自动选择 Markdown、HTML5、DOCX、PDF、TXT、PPTX
- **全选** - 选择所有格式
- **清除** - 取消所有选择

## 💡 使用技巧

### 1. 批量转换
一次性勾选多个输出格式，程序会自动依次转换，节省时间。

### 2. 格式转换建议
- **Markdown → DOCX**：适合提交文档、编辑修改
- **Markdown → PDF**：适合打印、正式分享
- **DOCX → Markdown**：便于版本控制、协作编辑
- **HTML → PDF**：网页转文档

### 3. PDF 转换注意事项
- 首次转换 PDF 时，MiKTeX 会自动下载必要的包，可能需要几分钟
- 确保网络连接稳定
- 后续转换会快很多

### 4. 提高文档质量
- 使用"独立文档"选项获得更完整的输出
- 使用"生成目录"让长文档更易阅读
- 使用"章节编号"自动为标题添加编号

## ❓ 常见问题

### Q: 转换 PDF 失败，显示"pdflatex not found"？
**A:** 需要安装 LaTeX。请按照上面的安装指南安装 MiKTeX（Windows）或其他 LaTeX 发行版。安装后需要重启程序。

### Q: PDF 转换很慢或卡住？
**A:** 首次转换 PDF 时，MiKTeX 会自动下载必要的包，可能需要几分钟。请耐心等待，确保有稳定的网络连接。后续转换会快很多。

### Q: 某些格式转换失败？
**A:** 检查转换日志中的错误信息，可能原因：
- 输入文件格式不正确
- 缺少必要的依赖（如 LaTeX）
- 文件包含不支持的特殊元素

### Q: 如何提高转换质量？
**A:** 
- 使用标准的 Markdown 语法
- 勾选"独立文档"选项
- 确保输入文件格式正确
- 对于 PDF：确保 LaTeX 正确安装

### Q: MiKTeX 和 TeX Live 选哪个？
**A:** 
- **MiKTeX** - 推荐 Windows 用户，轻量、易用、自动安装缺失包
- **TeX Live** - 跨平台，功能完整，适合专业用户
- **TinyTeX** - 最小安装，仅 PDF 转换，适合新手

建议：普通用户选 MiKTeX，专业用户选 TeX Live。

## 📸 界面截图

程序界面包含：
- 📌 常用格式优先显示（加粗高亮）
- 📋 其他格式按字母顺序排列
- 🔄 实时转换日志
- ✅ 转换成功/失败统计
- ❓ 详细的使用说明（点击帮助按钮）

## 🔗 相关链接

### Pandoc
- [Pandoc 官网](https://pandoc.org/)
- [Pandoc 文档](https://pandoc.org/MANUAL.html)
- [Pandoc 安装](https://pandoc.org/installing.html)

### LaTeX 发行版
- [MiKTeX (Windows 推荐)](https://miktex.org/download)
- [TeX Live (跨平台)](https://tug.org/texlive/)
- [MacTeX (macOS)](https://www.tug.org/mactex/)
- [TinyTeX (轻量级)](https://yihui.org/tinytex/)

## 📝 版本历史

### v1.0.0 (2024-10-05)
- ✨ 首次发布
- 🎨 支持 30+ 输入格式，40+ 输出格式
- 🚀 智能格式识别
- 📦 批量多格式输出
- 📖 详细的使用说明
- 💡 常用格式优先显示
- ⚙️ 高级转换选项

## 📄 许可证

MIT License

## 👨‍💻 技术栈

- **Python 3.7+**
- **Tkinter** - 图形界面
- **pypandoc** - Pandoc Python 接口
- **Pandoc** - 文档转换引擎

## 🙏 致谢

本项目基于以下优秀开源项目：
- [Pandoc](https://pandoc.org/) - 通用文档转换工具
- [pypandoc](https://github.com/bebraw/pypandoc) - Pandoc Python 包装器

---

**© 2024 Pandoc 全功能文档转换器 v1.0.0**


