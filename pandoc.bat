@echo off
chcp 65001 >nul

echo.
echo ========================================
echo  PANDOC文档转换系统 - 统一启动
echo ========================================
echo.


if not exist "venv\Scripts\activate.bat" (
    echo [错误] 虚拟环境不存在!
    echo 当前目录: %CD%
    pause
    exit /b 1
)

echo [信息] 激活虚拟环境...
call venv\Scripts\activate.bat



python app_all_function.py

pause

