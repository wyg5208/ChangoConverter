@echo off
chcp 65001 > nul
echo ================================================================
echo     ChangoConverter PDF转换 - LaTeX包自动安装工具
echo ================================================================
echo.
echo 本工具将自动安装Pandoc PDF转换所需的LaTeX包
echo 请确保您已安装 MiKTeX 或 TeX Live
echo.
echo ================================================================

REM 检查是否以管理员身份运行
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo [错误] 请以管理员身份运行此脚本！
    echo.
    echo 操作步骤：
    echo 1. 右键点击此文件
    echo 2. 选择"以管理员身份运行"
    echo.
    pause
    exit /b 1
)

echo [√] 已获取管理员权限
echo.

REM 检查MiKTeX是否安装
where mpm >nul 2>&1
if %errorLevel% EQU 0 (
    set LATEX_TYPE=MiKTeX
    set INSTALL_CMD=mpm --install
    echo [√] 检测到 MiKTeX
) else (
    REM 检查TeX Live是否安装
    where tlmgr >nul 2>&1
    if %errorLevel% EQU 0 (
        set LATEX_TYPE=TeX Live
        set INSTALL_CMD=tlmgr install
        echo [√] 检测到 TeX Live
    ) else (
        echo [错误] 未检测到 MiKTeX 或 TeX Live
        echo.
        echo 请先安装LaTeX发行版：
        echo   - MiKTeX: https://miktex.org/download
        echo   - TeX Live: https://www.tug.org/texlive/
        echo.
        pause
        exit /b 1
    )
)

echo [√] 使用 %LATEX_TYPE% 包管理器
echo.
echo ================================================================
echo 开始安装必需的LaTeX包...
echo ================================================================
echo.

set TOTAL=9
set CURRENT=0

REM 定义要安装的包
set PACKAGES=parskip xcolor fancyhdr caption booktabs hyperref geometry fontspec ctex

REM 逐个安装包
for %%p in (%PACKAGES%) do (
    set /a CURRENT+=1
    echo [!CURRENT!/%TOTAL%] 正在安装 %%p...
    
    if "%LATEX_TYPE%"=="MiKTeX" (
        mpm --install=%%p
    ) else (
        tlmgr install %%p
    )
    
    if %errorLevel% EQU 0 (
        echo       [√] %%p 安装成功
    ) else (
        echo       [!] %%p 安装可能失败，请检查网络连接
    )
    echo.
)

echo ================================================================
echo 正在刷新LaTeX文件数据库...
echo ================================================================

if "%LATEX_TYPE%"=="MiKTeX" (
    echo [1/2] 更新文件名数据库...
    initexmf --update-fndb >nul 2>&1
    
    echo [2/2] 重建映射文件...
    initexmf --mkmaps >nul 2>&1
) else (
    echo [1/1] 更新TeX Live数据库...
    mktexlsr >nul 2>&1
)

echo [√] 数据库刷新完成
echo.

echo ================================================================
echo 安装完成！
echo ================================================================
echo.
echo 已安装的包：
echo   √ parskip      - 段落间距处理
echo   √ xcolor       - 颜色支持
echo   √ fancyhdr     - 页眉页脚
echo   √ caption      - 图表标题
echo   √ booktabs     - 专业表格
echo   √ hyperref     - 超链接支持
echo   √ geometry     - 页面布局
echo   √ fontspec     - 字体设置
echo   √ ctex         - 中文支持
echo.
echo 现在您可以正常使用ChangoConverter转换PDF文件了！
echo.
echo ================================================================
echo 温馨提示
echo ================================================================
echo.
echo 1. 如果仍然遇到缺失包的问题，可以配置自动安装：
echo    - 打开 MiKTeX Console
echo    - 进入 Settings ^> General
echo    - 设置 "Install missing packages on-the-fly" 为 "Yes"
echo.
echo 2. 或者运行以下命令启用自动安装：
echo    initexmf --set-config-value [MPM]AutoInstall=1
echo.
echo ================================================================
pause

