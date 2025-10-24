@echo off
chcp 65001 >nul
REM 启动图形化打包工具

echo ========================================
echo   ChangoConverter 全功能文档转换器 v1.4.1
echo   打包工具                                    
echo ========================================
echo.

REM 检查虚拟环境
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

REM 运行图形化工具
python build_gui.py

pause


