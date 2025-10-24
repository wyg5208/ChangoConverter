# PDF转换LaTeX包安装指南

## 问题描述

转换为PDF格式时出现错误提示：
```
parskip.sty 找不到，需要安装
```

## 问题原因

- Pandoc转换PDF时使用LaTeX引擎（通常是XeLaTeX或PDFLaTeX）
- LaTeX需要`parskip`包来处理段落间距
- 您的LaTeX发行版缺少这个包

## 解决方案

### 方案1：使用MiKTeX包管理器（自动安装）⭐ 推荐

如果您使用的是**MiKTeX**：

1. **自动安装模式**（推荐）
   - MiKTeX通常会在缺少包时自动提示安装
   - 在弹出的对话框中点击"安装"即可

2. **手动安装**
   ```bash
   # 打开命令提示符（管理员权限）
   mpm --install=parskip
   ```

3. **通过图形界面**
   - 打开 MiKTeX Console
   - 点击 "Packages" 标签
   - 搜索 "parskip"
   - 点击 "+" 号安装

### 方案2：使用TeX Live包管理器

如果您使用的是**TeX Live**：

```bash
# 打开命令提示符（管理员权限）
tlmgr install parskip
```

### 方案3：批量安装常用包（一劳永逸）⭐⭐⭐

为了避免类似问题，建议一次性安装常用的LaTeX包：

#### MiKTeX用户
```bash
# 安装常用包集合
mpm --install=parskip
mpm --install=xcolor
mpm --install=fancyhdr
mpm --install=caption
mpm --install=booktabs
mpm --install=hyperref
mpm --install=geometry
mpm --install=fontspec
mpm --install=unicode-math
```

#### TeX Live用户
```bash
# 安装常用包集合
tlmgr install parskip xcolor fancyhdr caption booktabs hyperref geometry fontspec unicode-math
```

### 方案4：配置MiKTeX自动安装模式

#### 通过MiKTeX Console配置：
1. 打开 **MiKTeX Console**
2. 点击左侧 **Settings**
3. 在 **General** 标签下
4. 找到 **"Install missing packages on-the-fly"**
5. 选择 **"Yes"** 或 **"Ask me first"**

#### 通过命令行配置：
```bash
# 设置为自动安装
initexmf --set-config-value [MPM]AutoInstall=1

# 设置为询问安装
initexmf --set-config-value [MPM]AutoInstall=2
```

## 验证安装

安装完成后，验证包是否可用：

```bash
# MiKTeX用户
mpm --list | findstr parskip

# TeX Live用户
tlmgr info parskip
```

## 重新测试转换

安装完成后，重新运行Pandoc转换器：
1. 选择输入文件
2. 选择PDF输出格式
3. 点击"开始转换"
4. 应该可以正常转换了 ✓

## 常见其他缺失的包

如果后续还遇到其他包缺失错误，以下是常见的必需包：

| 包名 | 用途 |
|------|------|
| `parskip` | 段落间距处理 |
| `xcolor` | 颜色支持 |
| `fancyhdr` | 页眉页脚 |
| `caption` | 图表标题 |
| `booktabs` | 专业表格 |
| `hyperref` | 超链接支持 |
| `geometry` | 页面布局 |
| `fontspec` | 字体设置（XeLaTeX） |
| `ctex` | 中文支持 |

## 完整解决方案（一次搞定）

### Windows用户（MiKTeX）

创建一个批处理文件 `install_latex_packages.bat`：

```batch
@echo off
echo ================================================
echo 正在安装Pandoc PDF转换所需的LaTeX包...
echo ================================================

echo.
echo [1/9] 安装 parskip...
mpm --install=parskip

echo [2/9] 安装 xcolor...
mpm --install=xcolor

echo [3/9] 安装 fancyhdr...
mpm --install=fancyhdr

echo [4/9] 安装 caption...
mpm --install=caption

echo [5/9] 安装 booktabs...
mpm --install=booktabs

echo [6/9] 安装 hyperref...
mpm --install=hyperref

echo [7/9] 安装 geometry...
mpm --install=geometry

echo [8/9] 安装 fontspec...
mpm --install=fontspec

echo [9/9] 安装 ctex（中文支持）...
mpm --install=ctex

echo.
echo ================================================
echo 所有包安装完成！
echo 现在可以正常转换PDF了。
echo ================================================
pause
```

右键"以管理员身份运行"此批处理文件。

### Linux/Mac用户（TeX Live）

创建一个脚本 `install_latex_packages.sh`：

```bash
#!/bin/bash
echo "================================================"
echo "正在安装Pandoc PDF转换所需的LaTeX包..."
echo "================================================"

sudo tlmgr install parskip xcolor fancyhdr caption booktabs \
                   hyperref geometry fontspec unicode-math ctex

echo "================================================"
echo "所有包安装完成！"
echo "================================================"
```

执行：`chmod +x install_latex_packages.sh && ./install_latex_packages.sh`

## 故障排除

### 问题1：mpm命令找不到

**解决方法**：
- 确保MiKTeX已正确安装
- 将MiKTeX的bin目录添加到系统PATH
- 默认路径通常是：`C:\Program Files\MiKTeX\miktex\bin\x64\`

### 问题2：权限不足

**解决方法**：
- 以管理员身份运行命令提示符
- 右键"命令提示符" → "以管理员身份运行"

### 问题3：网络连接问题

**解决方法**：
- 检查防火墙设置
- 尝试更换MiKTeX镜像源
- 在MiKTeX Console → Settings → General → Package Repository

### 问题4：安装后仍然报错

**解决方法**：
```bash
# 刷新LaTeX文件名数据库
initexmf --update-fndb

# 重建格式文件
initexmf --mkmaps
```

## 预防措施

### 安装完整版LaTeX发行版

#### MiKTeX完整版
下载并安装MiKTeX完整版（约4GB），包含所有常用包：
- 下载地址：https://miktex.org/download
- 选择 **Complete MiKTeX**

#### TeX Live完整版
下载并安装TeX Live完整版（约7GB）：
- 下载地址：https://www.tug.org/texlive/
- 选择 **Full Installation**

## 技术说明

### Pandoc的PDF转换流程

```
Markdown/DOCX等
    ↓
Pandoc处理
    ↓
生成LaTeX中间文件
    ↓
调用XeLaTeX/PDFLaTeX
    ↓
编译为PDF
```

### 为什么需要parskip包

- **parskip包**：控制段落间距的LaTeX包
- Pandoc默认模板使用此包来美化段落排版
- 使用`\usepackage{parskip}`实现段落间空行效果

## 快速参考

| 操作 | 命令 |
|------|------|
| 安装单个包 | `mpm --install=包名` |
| 搜索包 | `mpm --list \| findstr 包名` |
| 更新所有包 | `mpm --update` |
| 刷新数据库 | `initexmf --update-fndb` |
| 配置自动安装 | MiKTeX Console → Settings → General |

## 总结

**最简单的解决方案**：
1. 打开命令提示符（管理员）
2. 运行：`mpm --install=parskip`
3. 重新转换PDF

**一劳永逸的方案**：
1. 在MiKTeX Console中启用"自动安装缺失包"
2. 或安装MiKTeX/TeX Live完整版

---

**遇到问题？** 尝试以下步骤：
1. ✓ 确认LaTeX已正确安装
2. ✓ 以管理员身份运行安装命令
3. ✓ 安装parskip包：`mpm --install=parskip`
4. ✓ 刷新数据库：`initexmf --update-fndb`
5. ✓ 重新测试转换

---

**现在您可以正常转换PDF了！** 🎉

