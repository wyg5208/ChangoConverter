# ChangoConverter 全功能文档转换器

![Version](https://img.shields.io/badge/version-1.4.1-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Pandoc](https://img.shields.io/badge/pandoc-required-orange.svg)

🔄 基于Pandoc的强大文档格式转换工具，支持批量转换、字体设置、智能UI等功能。

---

<div align="center">
  <img src="resources/icon.png" alt="ChangoConverter Logo" width="128"/>
  
  **让文档转换更简单、更专业、更高效！**
  
  [快速开始](#-快速开始) • 
  [功能特性](#-核心特性) • 
  [使用说明](#-使用说明) • 
  [下载发布](https://github.com/wyg5208/ChangoConverter/releases) • 
  [问题反馈](https://github.com/wyg5208/ChangoConverter/issues)
</div>

---

## ✨ 核心特性

- 🔄 **批量转换**：自动遍历文件夹和子文件夹，批量处理文档
- 📝 **多格式支持**：Markdown、HTML、Word、PDF、PowerPoint等12+种格式
- 🎨 **字体定制**：支持设置DOCX文件的字体和字号
- 📊 **实时日志**：转换进度实时显示，状态一目了然
- 🎯 **智能识别**：自动识别文件格式，减少手动操作
- 💾 **覆盖策略**：灵活的文件覆盖/重命名/跳过选项
- 🌟 **现代UI**：左右布局，TAB页面，高度优化

## 📦 快速开始

### 1. 安装依赖

```bash
# 运行依赖安装脚本
安装依赖.bat

# 或手动安装
pip install -r requirements_build.txt
```

### 2. 安装Pandoc

下载并安装Pandoc: https://pandoc.org/installing.html

### 3. 运行程序

```bash
# 直接运行Python脚本
python app_all_function.py

# 或使用快捷脚本
pandoc.bat
```

### 4. （可选）安装LaTeX

如需转换为PDF，需要安装LaTeX：
- Windows: 安装MiKTeX (https://miktex.org/)
- 运行 `install_latex_packages.bat` 安装必要的LaTeX包

## 📁 目录结构

```
ChangoConverter/
├── app_all_function.py          # 主程序文件
├── version.py                   # 版本信息
├── build_config.py              # 打包配置
├── requirements_build.txt       # Python依赖
├── 安装依赖.bat                  # 依赖安装脚本
├── pandoc.bat                   # 快速启动脚本
├── install_latex_packages.bat   # LaTeX包安装脚本
├── 快速打包.bat                  # 打包脚本
├── docs/                        # 📚 文档目录
│   ├── 快速使用指南_v1.1.0.txt
│   ├── 批量转换快速开始.txt
│   ├── PDF转换问题快速解决.txt
│   ├── v1.4.0完成总结.txt
│   └── ...更多文档
├── resources/                   # 🎨 资源文件
│   ├── icon.ico                # 应用图标
│   ├── icon.png                # PNG图标
│   └── docx_font_filter.lua    # Pandoc Lua过滤器
└── test_scripts/                # 🧪 测试脚本
    ├── test_conversion.py
    ├── generate_icon.py
    └── ...更多测试脚本
```

## 🎯 使用说明

### 单文件转换
1. 选择"单文件转换"模式
2. 选择输入文件
3. 选择输出路径
4. 选择目标格式
5. 点击"开始转换"

### 批量转换
1. 选择"批量转换"模式
2. 选择包含待转换文件的文件夹
3. 选择"输入文件格式"（md/html/docx/txt/pptx/pdf）
4. 选择目标格式
5. 点击"开始转换"
6. 系统会自动遍历文件夹和所有子文件夹

### 高级选项
- 点击"高级选项"按钮打开设置窗口
- 设置DOCX字体：Times New Roman、Arial等
- 设置字号：10-16pt
- 应用于PDF转换时的中文支持

### 文件覆盖策略
当目标文件已存在时，系统会提示：
- **覆盖**：覆盖现有文件
- **重命名**：自动添加数字后缀
- **跳过**：跳过该文件
- **记住选择**：对本批次后续文件应用相同策略

## 📊 支持的格式

### 输入格式
- Markdown (.md)
- HTML (.html, .htm)
- Word (.docx)
- 纯文本 (.txt)
- PowerPoint (.pptx)
- PDF (.pdf)
- 等12+种格式

### 输出格式
- **常用格式**：Word、HTML、PDF、Markdown、纯文本、PowerPoint
- **其它格式**：LaTeX、reStructuredText、AsciiDoc、MediaWiki、EPUB、Jupyter Notebook

## ⚠️ 注意事项

1. **PDF转换**：需要安装MiKTeX和LaTeX包
2. **Emoji支持**：PDF转换时会自动替换/移除Emoji
3. **中文支持**：PDF转换自动使用XeLaTeX引擎和微软雅黑字体
4. **权限问题**：请勿以管理员身份运行程序

## 🔧 高级功能

### Emoji处理
系统会自动处理Markdown中的Emoji，避免LaTeX转换错误：
- 常用Emoji → ASCII符号
- 未映射Emoji → 移除
- 特殊字符 → 转义处理

### 字体后处理
DOCX文件会在转换后自动应用字体设置：
- 修改Normal样式
- 遍历所有段落和表格
- 确保字体一致性

## 📦 打包发布

```bash
# 快速打包
快速打包.bat

# 或使用完整打包流程
build_exe.bat
```

打包后的可执行文件位于 `dist/` 目录。

## 🐛 故障排除

### 问题1：Pandoc未安装
**解决方案**：下载安装 https://pandoc.org/installing.html

### 问题2：LaTeX包缺失
**解决方案**：运行 `install_latex_packages.bat`

### 问题3：转换失败
**解决方案**：
- 检查输入文件格式是否正确
- 查看日志区域的详细错误信息
- 确认Pandoc版本是否最新

### 问题4：PDF中文显示问题
**解决方案**：系统自动使用XeLaTeX和微软雅黑字体

详细说明请查看 `docs/` 目录下的相关文档。

## 📝 更新日志

### v1.4.1 (最新)
- ✅ 最终UI高度优化（减少20%）
- ✅ 开始转换按钮文字颜色优化（深色）
- ✅ PDF转换Emoji处理增强
- ✅ XeLaTeX引擎支持
- ✅ 系统名称更新为ChangoConverter
- ✅ 应用图标设计与应用
- ✅ 目录结构清理优化

### v1.4.0
- ✅ 左右布局优化（日志在右侧）
- ✅ 批量转换输入格式选择
- ✅ 开始转换按钮深绿色背景
- ✅ 主窗体宽度增加20%

### v1.3.1
- ✅ 高级选项按钮位置优化
- ✅ DOCX字体设置改为单选框

### v1.3.0
- ✅ TAB页面展示输出格式
- ✅ 高级选项弹出窗口
- ✅ 转换日志高度增加4倍
- ✅ 文件覆盖弹窗优化

查看完整版本历史：`docs/` 目录

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

---

**ChangoConverter** - 让文档转换更简单！ 🚀

