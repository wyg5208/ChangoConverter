@echo off
chcp 65001 >nul
REM ============================================
REM Pandoc 全功能文档转换器 - EXE 打包脚本
REM ============================================

echo ========================================
echo  Pandoc 全功能文档转换器 v1.3.1
echo  正在打包为 EXE 文件...
echo ========================================
echo.

REM 检查虚拟环境
if not exist "venv\Scripts\activate.bat" (
    echo [错误] 未找到虚拟环境！
    echo 请先创建虚拟环境: python -m venv venv
    pause
    exit /b 1
)

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 检查 PyInstaller 是否安装
echo [1/4] 检查 PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller 未安装，正在安装...
    pip install pyinstaller
)

REM 清理旧的构建文件
echo.
echo [2/4] 清理旧的构建文件...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "PandocConverter.spec" del PandocConverter.spec

REM 使用 PyInstaller 打包
echo.
echo [3/4] 开始打包 (这可能需要几分钟)...
pyinstaller --noconfirm ^
    --onefile ^
    --windowed ^
    --name=PandocConverter ^
    --add-data="README_app_all_function.md;." ^
    --hidden-import=pypandoc ^
    --hidden-import=tkinter ^
    --hidden-import=tkinter.ttk ^
    --hidden-import=tkinter.filedialog ^
    --hidden-import=tkinter.messagebox ^
    app_all_function.py

REM 检查打包结果
echo.
echo [4/4] 检查打包结果...
if exist "dist\PandocConverter.exe" (
    echo.
    echo ========================================
    echo  打包成功！
    echo ========================================
    echo.
    echo EXE 文件位置: dist\PandocConverter.exe
    echo 文件大小: 
    dir dist\PandocConverter.exe | find "PandocConverter.exe"
    echo.
    echo 提示:
    echo 1. 此 EXE 文件可以独立运行
    echo 2. 用户仍需要安装 Pandoc: https://pandoc.org/installing.html
    echo 3. 如需转换 PDF，还需要安装 LaTeX
    echo.
) else (
    echo.
    echo [错误] 打包失败！
    echo 请检查错误信息
    echo.
    pause
    exit /b 1
)

pause


