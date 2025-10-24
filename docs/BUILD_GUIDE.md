# Pandoc 全功能文档转换器 - 打包指南

完整的打包方案，包括 EXE 文件和 MSI 安装包的制作。

---

## 📋 目录

1. [准备工作](#准备工作)
2. [方案一：打包为 EXE 文件（推荐）](#方案一打包为-exe-文件推荐)
3. [方案二：打包为 MSI 安装包](#方案二打包为-msi-安装包)
4. [方案三：使用 NSIS 创建安装程序](#方案三使用-nsis-创建安装程序)
5. [常见问题](#常见问题)
6. [分发建议](#分发建议)

---

## 📦 准备工作

### 1. 安装打包工具

```bash
# 激活虚拟环境
venv\Scripts\activate

# 安装打包依赖
pip install -r requirements_build.txt
```

或者手动安装：

```bash
pip install pyinstaller
pip install cx-Freeze
```

### 2. 准备图标文件（可选）

如果想要自定义图标，准备一个 `icon.ico` 文件（推荐尺寸：256x256）

可以使用在线工具转换：
- https://www.icoconverter.com/
- https://convertio.co/zh/png-ico/

---

## 🎯 方案一：打包为 EXE 文件（推荐）

### 优点
✅ 单文件，易于分发  
✅ 无需安装，双击运行  
✅ 文件体积较小（约 10-20MB）  
✅ 快速打包  

### 步骤

#### 方法 A：使用自动化脚本（推荐）

```bash
# 直接运行打包脚本
build_exe.bat
```

#### 方法 B：手动命令

```bash
# 1. 激活虚拟环境
venv\Scripts\activate

# 2. 基本打包（单文件）
pyinstaller --onefile --windowed --name=PandocConverter app_all_function.py

# 3. 完整打包（包含图标和数据文件）
pyinstaller --onefile --windowed ^
    --name=PandocConverter ^
    --icon=icon.ico ^
    --add-data="README_app_all_function.md;." ^
    app_all_function.py
```

### 输出结果

```
dist/
└── PandocConverter.exe  ← 可独立运行的 EXE 文件
```

### 测试运行

```bash
# 测试打包的程序
dist\PandocConverter.exe
```

---

## 📦 方案二：打包为 MSI 安装包

### 优点
✅ 专业的安装体验  
✅ 自动创建快捷方式  
✅ 支持卸载  
✅ 注册到系统程序列表  

### 步骤

#### 方法 A：使用自动化脚本（推荐）

```bash
# 直接运行打包脚本
build_msi.bat
```

#### 方法 B：手动命令

```bash
# 1. 激活虚拟环境
venv\Scripts\activate

# 2. 创建 MSI 安装包
python setup.py bdist_msi
```

### 输出结果

```
dist/
└── PandocConverter-1.0.0-win64.msi  ← MSI 安装包
```

### 安装特性

- 📍 默认安装位置：`C:\Program Files\PandocConverter\`
- 🖥️ 自动创建桌面快捷方式
- 📋 添加到开始菜单
- ➕ 注册到"添加/删除程序"
- 🔄 支持升级和卸载

---

## 🔧 方案三：使用 NSIS 创建安装程序

### 优点
✅ 更灵活的安装选项  
✅ 可以捆绑 Pandoc 安装程序  
✅ 自定义安装界面  
✅ 体积更小  

### 步骤

#### 1. 下载安装 NSIS

下载地址：https://nsis.sourceforge.io/Download

#### 2. 创建 NSIS 脚本

创建文件 `installer.nsi`：

```nsis
; Pandoc Converter 安装脚本

!include "MUI2.nsh"

; 应用信息
Name "Pandoc 全功能文档转换器"
OutFile "PandocConverter-Setup-1.0.0.exe"
InstallDir "$PROGRAMFILES\PandocConverter"
RequestExecutionLevel admin

; 界面配置
!define MUI_ABORTWARNING
!define MUI_ICON "icon.ico"
!define MUI_UNICON "icon.ico"

; 安装页面
!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; 卸载页面
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

; 语言
!insertmacro MUI_LANGUAGE "SimpChinese"

; 安装部分
Section "Install"
    SetOutPath "$INSTDIR"
    
    ; 复制文件
    File "dist\PandocConverter.exe"
    File "README_app_all_function.md"
    
    ; 创建快捷方式
    CreateDirectory "$SMPROGRAMS\Pandoc Converter"
    CreateShortcut "$SMPROGRAMS\Pandoc Converter\Pandoc Converter.lnk" "$INSTDIR\PandocConverter.exe"
    CreateShortcut "$DESKTOP\Pandoc Converter.lnk" "$INSTDIR\PandocConverter.exe"
    
    ; 写入卸载信息
    WriteUninstaller "$INSTDIR\Uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PandocConverter" "DisplayName" "Pandoc 全功能文档转换器"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PandocConverter" "UninstallString" "$INSTDIR\Uninstall.exe"
SectionEnd

; 卸载部分
Section "Uninstall"
    Delete "$INSTDIR\PandocConverter.exe"
    Delete "$INSTDIR\README_app_all_function.md"
    Delete "$INSTDIR\Uninstall.exe"
    
    Delete "$SMPROGRAMS\Pandoc Converter\Pandoc Converter.lnk"
    RMDir "$SMPROGRAMS\Pandoc Converter"
    Delete "$DESKTOP\Pandoc Converter.lnk"
    
    RMDir "$INSTDIR"
    
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PandocConverter"
SectionEnd
```

#### 3. 编译安装程序

```bash
# 右键点击 installer.nsi → "Compile NSIS Script"
# 或使用命令行：
makensis installer.nsi
```

---

## ❓ 常见问题

### Q1: 打包后程序无法运行？

**A:** 检查以下几点：
1. 确保所有依赖都已安装：`pip list | findstr pypandoc`
2. 使用 `--debug` 模式查看详细错误：
   ```bash
   pyinstaller --onefile --windowed --debug=all app_all_function.py
   ```
3. 检查是否缺少隐藏导入：
   ```bash
   pyinstaller --onefile --windowed --hidden-import=pypandoc app_all_function.py
   ```

### Q2: EXE 文件体积太大？

**A:** 优化方案：
```bash
# 使用 UPX 压缩（需要下载 UPX）
pyinstaller --onefile --windowed --upx-dir=upx app_all_function.py

# 排除不必要的模块
pyinstaller --onefile --windowed --exclude-module=matplotlib app_all_function.py
```

### Q3: 打包后 Pandoc 检测失败？

**A:** 这是正常的。打包后的程序不包含 Pandoc 本身，用户需要：
1. 单独安装 Pandoc：https://pandoc.org/installing.html
2. 程序会自动检测并提示用户安装

### Q4: 如何在安装包中捆绑 Pandoc？

**A:** 可以使用 NSIS 方案：
```nsis
Section "Install Pandoc" SecPandoc
    SetOutPath "$TEMP"
    File "pandoc-3.x.x-windows-x86_64.msi"
    ExecWait 'msiexec /i "$TEMP\pandoc-3.x.x-windows-x86_64.msi" /quiet'
    Delete "$TEMP\pandoc-3.x.x-windows-x86_64.msi"
SectionEnd
```

### Q5: 杀毒软件报毒？

**A:** 这是误报，解决方法：
1. 使用 `--debug=bootloader` 查看详情
2. 在杀毒软件中添加白名单
3. 使用代码签名证书（适合商业发布）

---

## 🚀 分发建议

### 1. 文件准备

打包后准备分发包：

```
PandocConverter-v1.0.0/
├── PandocConverter.exe          # 可执行文件
├── README.txt                   # 使用说明
├── LICENSE.txt                  # 许可证
└── 安装说明.txt                  # 安装Pandoc和LaTeX的说明
```

### 2. 创建说明文件

**安装说明.txt**：

```
Pandoc 全功能文档转换器 v1.0.0
=====================================

使用前请安装以下软件：

1. 【必需】Pandoc - 文档转换引擎
   下载地址: https://pandoc.org/installing.html
   安装后点击程序中的"重新检测"按钮

2. 【可选】LaTeX - PDF 转换支持
   Windows 推荐: MiKTeX
   下载地址: https://miktex.org/download
   
   注意：首次转换 PDF 时会自动下载必要组件

快速开始：
1. 双击 PandocConverter.exe 运行程序
2. 点击"重新检测"验证环境
3. 选择输入文件和输出格式
4. 点击"开始转换"

更多帮助请点击程序中的"使用说明"按钮。
```

### 3. 压缩打包

```bash
# 创建 ZIP 压缩包
powershell Compress-Archive -Path PandocConverter-v1.0.0 -DestinationPath PandocConverter-v1.0.0.zip
```

### 4. 发布平台

推荐发布平台：
- **GitHub Releases** - 开源项目首选
- **SourceForge** - 老牌软件发布平台
- **蓝奏云** - 国内高速下载
- **百度网盘** - 大文件分享

### 5. 发布文案模板

```markdown
# Pandoc 全功能文档转换器 v1.0.0

## 📥 下载

- [Windows 64位 (EXE)](链接) - 10MB
- [Windows 安装包 (MSI)](链接) - 15MB

## ✨ 主要功能

- 支持 30+ 输入格式，40+ 输出格式
- 智能格式识别
- 批量多格式转换
- 环境自动检测

## 📦 系统要求

- Windows 7/8/10/11 (64位)
- 需要单独安装 [Pandoc](https://pandoc.org/installing.html)
- PDF 转换需要 [MiKTeX](https://miktex.org/download)

## 🚀 快速开始

1. 下载并运行程序
2. 安装 Pandoc
3. 点击"重新检测"
4. 开始转换！

详细说明请查看程序内置的"使用说明"。
```

---

## 📊 打包对比

| 方案 | 优点 | 缺点 | 推荐场景 |
|------|------|------|---------|
| **PyInstaller EXE** | 简单快速，单文件 | 体积较大 | 快速分享 |
| **cx_Freeze MSI** | 专业安装体验 | 打包复杂 | 正式发布 |
| **NSIS 安装程序** | 高度定制，可捆绑依赖 | 需要学习 NSIS | 商业发布 |

---

## 🎓 最佳实践

1. **版本管理**
   - 在文件名中包含版本号
   - 使用语义化版本：`v主版本.次版本.修订号`

2. **测试流程**
   - 在干净的虚拟机中测试
   - 测试不同 Windows 版本
   - 测试有/无 Pandoc 的环境

3. **更新策略**
   - 提供更新日志
   - 使用相同的升级代码（MSI）
   - 提供增量更新包

4. **用户支持**
   - 提供详细的安装说明
   - 包含故障排除指南
   - 留下联系方式或反馈渠道

---

## 📝 检查清单

打包前检查：
- [ ] 代码无错误
- [ ] 所有功能正常
- [ ] 版本号已更新
- [ ] README 已更新
- [ ] 图标文件已准备
- [ ] 许可证文件已添加

打包后检查：
- [ ] EXE 可以运行
- [ ] 环境检测正常
- [ ] 转换功能正常
- [ ] 帮助文档显示正常
- [ ] 文件大小合理
- [ ] 无杀毒软件误报

发布前检查：
- [ ] 在干净系统测试通过
- [ ] 安装说明清晰完整
- [ ] 下载链接有效
- [ ] 文件完整性校验
- [ ] 发布说明完整

---

**祝打包顺利！** 🎉

如有问题，请查看 [常见问题](#常见问题) 或提交 Issue。


