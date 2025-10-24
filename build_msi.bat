@echo off
REM 中文支持
chcp 65001 >nul

REM ============================================
REM Pandoc 全功能文档转换器 - MSI 打包脚本
REM ============================================

echo ========================================
echo  Pandoc 全功能文档转换器 v1.0.0
echo  正在打包为 MSI 安装包...
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

REM 检查 cx_Freeze 是否安装
echo [1/4] 检查 cx_Freeze...
python -c "import cx_Freeze" 2>nul
if errorlevel 1 (
    echo cx_Freeze 未安装，正在安装...
    pip install cx_Freeze
)

REM 清理旧的构建文件
echo.
echo [2/4] 清理旧的构建文件...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist

REM 使用 cx_Freeze 打包
echo.
echo [3/4] 开始打包 MSI (这可能需要几分钟)...
python setup.py bdist_msi

REM 检查打包结果
echo.
echo [4/4] 检查打包结果...
if exist "dist\*.msi" (
    echo.
    echo ========================================
    echo  打包成功！
    echo ========================================
    echo.
    echo MSI 文件位置: dist\
    dir dist\*.msi
    echo.
    echo 提示:
    echo 1. 双击 MSI 文件即可安装程序
    echo 2. 程序会安装到 C:\Program Files\PandocConverter\
    echo 3. 自动创建桌面快捷方式和开始菜单项
    echo 4. 用户仍需要单独安装 Pandoc 和 LaTeX
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


