@echo off
chcp 65001 >nul
REM ============================================
REM ChangoConverter 全功能文档转换器 - 依赖安装工具
REM ============================================
echo.
echo ========================================
echo  ChangoConverter 全功能文档转换器 v1.4.1
echo  依赖安装工具...
echo ========================================
echo.
echo 正在检查Python环境...
python --version >nul
if errorlevel 1 (
    echo.
    echo [错误] 未找到Python！
    echo 请先安装Python: https://www.python.org/
    pause
    exit /b 1
)

echo.
echo 正在安装核心依赖...
echo.

REM 激活虚拟环境（如果存在）
if exist "venv\Scripts\activate.bat" (
    echo 检测到虚拟环境，正在激活...
    call venv\Scripts\activate.bat
)

REM 安装依赖
echo [1/2] 安装 pypandoc...
pip install pypandoc>=1.13
if errorlevel 1 (
    echo [错误] pypandoc 安装失败！
    pause
    exit /b 1
)

echo.
echo [2/2] 安装 python-docx (用于DOCX字体设置)...
pip install python-docx>=1.1.0
if errorlevel 1 (
    echo [警告] python-docx 安装失败，DOCX字体设置功能将不可用
    echo 可以稍后手动安装: pip install python-docx
)

echo.
echo ========================================
echo   ✓ 依赖安装完成！
echo ========================================
echo.
echo 提示：
echo   - 确保已安装 Pandoc: https://pandoc.org/
echo   - 如需PDF转换，请安装 LaTeX (MiKTeX)
echo   - 运行程序: python app_all_function.py
echo.
pause

