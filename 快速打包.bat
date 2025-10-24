@echo off
chcp 65001 >nul
REM ============================================
REM ChangoConverter 全功能文档转换器 - 一键打包脚本
REM ============================================

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║   ChangoConverter v1.4.1 全功能文档转换器         ║
echo ║   一键打包工具                                    ║
echo ╚══════════════════════════════════════════════════╝
echo.
echo 请选择打包方式：
echo.
echo [1] 快速打包 - 仅生成 EXE 文件 (推荐)
echo [2] 完整打包 - 生成 EXE + MSI 安装包
echo [3] 准备发布 - 创建发布压缩包
echo [0] 退出
echo.

set /p choice=请输入选项 (0-3): 

if "%choice%"=="1" goto quick_build
if "%choice%"=="2" goto full_build
if "%choice%"=="3" goto prepare_release
if "%choice%"=="0" goto end
echo 无效选项！
pause
exit /b 1

:quick_build
echo.
echo ========================================
echo  开始快速打包...
echo ========================================
call build_exe.bat
goto end

:full_build
echo.
echo ========================================
echo  开始完整打包...
echo ========================================
echo.
echo [步骤 1/2] 打包 EXE 文件...
call build_exe.bat
echo.
echo [步骤 2/2] 打包 MSI 安装包...
pause
call build_msi.bat
goto end

:prepare_release
echo.
echo ========================================
echo  准备发布包...
echo ========================================
call prepare_release.bat
goto end

:end
echo.
echo ========================================
echo  完成！
echo ========================================
echo.
pause


