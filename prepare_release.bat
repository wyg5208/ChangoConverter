@echo off
REM ============================================
REM ChangoConverter 全功能文档转换器 - 发布准备脚本
REM ============================================

echo ========================================
echo  ChangoConverter 全功能文档转换器 v1.4.1
echo  准备发布包...
echo ========================================
echo.

REM 创建发布目录
set RELEASE_DIR=ChangoConverter-v1.4.1
if exist "%RELEASE_DIR%" rmdir /s /q "%RELEASE_DIR%"
mkdir "%RELEASE_DIR%"

echo [1/5] 创建发布目录: %RELEASE_DIR%
echo.

REM 检查 EXE 文件
if not exist "dist\ChangoConverter.exe" (
    echo [错误] 未找到 ChangoConverter.exe
    echo 请先运行 build_exe.bat 打包程序
    pause
    exit /b 1
)

REM 复制文件
echo [2/5] 复制文件...
copy "dist\ChangoConverter.exe" "%RELEASE_DIR%\" >nul
copy "README_app_all_function.md" "%RELEASE_DIR%\README.txt" >nul

REM 创建安装说明
echo [3/5] 创建安装说明...
(
echo ChangoConverter 全功能文档转换器 v1.4.1
echo =====================================
echo.
echo 使用前请安装以下软件：
echo.
echo 1. 【必需】Chango - 文档转换引擎
echo    下载地址: https://pandoc.org/installing.html
echo    安装后点击程序中的"重新检测"按钮
echo.
echo 2. 【可选】LaTeX - PDF 转换支持
echo    Windows 推荐: MiKTeX
echo    下载地址: https://miktex.org/download
echo    
echo    注意：首次转换 PDF 时会自动下载必要组件
echo.
echo 快速开始：
echo 1. 双击 ChangoConverter.exe 运行程序
echo 2. 点击"重新检测"验证环境
echo 3. 选择输入文件和输出格式
echo 4. 点击"开始转换"
echo.
echo 更多帮助请点击程序中的"使用说明"按钮。
echo.
echo 软件版本: v1.4.1
echo 更新日期: %date%
) > "%RELEASE_DIR%\安装说明.txt"

REM 创建许可证文件
echo [4/5] 创建许可证...
(
echo MIT License
echo.
echo Copyright ^(c^) 2024 ChangoConverter
echo.
echo Permission is hereby granted, free of charge, to any person obtaining a copy
echo of this software and associated documentation files ^(the "Software"^), to deal
echo in the Software without restriction, including without limitation the rights
echo to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
echo copies of the Software, and to permit persons to whom the Software is
echo furnished to do so, subject to the following conditions:
echo.
echo The above copyright notice and this permission notice shall be included in all
echo copies or substantial portions of the Software.
echo.
echo THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
echo IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
echo FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
echo AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
echo LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
echo OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
echo SOFTWARE.
) > "%RELEASE_DIR%\LICENSE.txt"

REM 创建 ZIP 压缩包
echo [5/5] 创建 ZIP 压缩包...
powershell -Command "Compress-Archive -Path '%RELEASE_DIR%' -DestinationPath '%RELEASE_DIR%.zip' -Force"

REM 显示结果
echo.
echo ========================================
echo  发布包准备完成！
echo ========================================
echo.
echo 发布文件夹: %RELEASE_DIR%\
dir "%RELEASE_DIR%" /b
echo.
echo 压缩包: %RELEASE_DIR%.zip
dir "%RELEASE_DIR%.zip" | find ".zip"
echo.
echo 提示：
echo 1. 检查文件夹内容是否完整
echo 2. 测试 EXE 文件是否可以运行
echo 3. 上传 ZIP 压缩包到发布平台
echo.

pause


