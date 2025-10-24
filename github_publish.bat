@echo off
chcp 65001 >nul
cls

echo ============================================================
echo ChangoConverter GitHub 发布助手
echo ============================================================
echo.

:menu
echo 请选择操作：
echo.
echo [1] 初始化Git仓库（第一次使用）
echo [2] 添加并提交更改
echo [3] 推送到GitHub
echo [4] 创建版本标签（v1.4.1）
echo [5] 完整发布流程（一键完成）
echo [6] 查看Git状态
echo [7] 退出
echo.
set /p choice="请输入选项 (1-7): "

if "%choice%"=="1" goto init
if "%choice%"=="2" goto commit
if "%choice%"=="3" goto push
if "%choice%"=="4" goto tag
if "%choice%"=="5" goto full
if "%choice%"=="6" goto status
if "%choice%"=="7" goto end

echo 无效选项，请重试
pause
cls
goto menu

:init
echo.
echo ============================================================
echo 初始化Git仓库
echo ============================================================
echo.

echo [1/4] 检查Git是否安装...
git --version
if errorlevel 1 (
    echo [错误] 未安装Git，请先安装：https://git-scm.com/
    pause
    goto menu
)

echo.
echo [2/4] 初始化Git仓库...
git init

echo.
echo [3/4] 配置用户信息...
set /p username="请输入GitHub用户名（默认：wyg5208）: "
if "%username%"=="" set username=wyg5208

set /p email="请输入邮箱地址（默认：wyg5208@126.com）: "
if "%email%"=="" set email=wyg5208@126.com

git config user.name "%username%"
git config user.email "%email%"

echo.
echo [4/4] 添加远程仓库...
echo 如果仓库不存在，请先在GitHub上创建仓库
echo.
set /p repo="请输入仓库URL（默认：https://github.com/wyg5208/ChangoConverter.git）: "
if "%repo%"=="" set repo=https://github.com/wyg5208/ChangoConverter.git

git remote add origin %repo%

echo.
echo ✅ Git仓库初始化完成！
echo.
pause
cls
goto menu

:commit
echo.
echo ============================================================
echo 添加并提交更改
echo ============================================================
echo.

echo [1/3] 添加所有文件...
git add .

echo.
echo [2/3] 查看变更文件...
git status

echo.
echo [3/3] 提交更改...
set /p message="请输入提交信息（默认：Update files）: "
if "%message%"=="" set message=Update files

git commit -m "%message%"

echo.
echo ✅ 更改已提交！
echo.
pause
cls
goto menu

:push
echo.
echo ============================================================
echo 推送到GitHub
echo ============================================================
echo.

echo 正在推送到远程仓库...
git push -u origin main

if errorlevel 1 (
    echo.
    echo [提示] 如果推送失败，可能是因为分支名称问题
    echo 尝试切换到main分支...
    git branch -M main
    git push -u origin main
)

echo.
echo ✅ 推送完成！
echo.
pause
cls
goto menu

:tag
echo.
echo ============================================================
echo 创建版本标签
echo ============================================================
echo.

set /p tagname="请输入标签名称（默认：v1.4.1）: "
if "%tagname%"=="" set tagname=v1.4.1

set /p tagmsg="请输入标签说明（默认：Release %tagname%）: "
if "%tagmsg%"=="" set tagmsg=Release %tagname%

echo.
echo [1/2] 创建标签...
git tag -a %tagname% -m "%tagmsg%"

echo.
echo [2/2] 推送标签...
git push origin %tagname%

echo.
echo ✅ 标签创建完成！
echo.
echo 现在可以在GitHub上创建Release：
echo https://github.com/wyg5208/ChangoConverter/releases/new
echo 选择标签：%tagname%
echo.
pause
cls
goto menu

:full
echo.
echo ============================================================
echo 完整发布流程
echo ============================================================
echo.
echo 这将执行以下操作：
echo 1. 添加所有文件
echo 2. 提交更改
echo 3. 推送到GitHub
echo 4. 创建版本标签
echo.
set /p confirm="确认执行？(Y/N): "
if /i not "%confirm%"=="Y" goto menu

echo.
echo [步骤 1/5] 添加所有文件...
git add .

echo.
echo [步骤 2/5] 查看变更...
git status
echo.

set /p message="请输入提交信息: "
if "%message%"=="" (
    echo 未输入提交信息，取消操作
    pause
    goto menu
)

echo.
echo [步骤 3/5] 提交更改...
git commit -m "%message%"

echo.
echo [步骤 4/5] 推送到GitHub...
git branch -M main
git push -u origin main

echo.
echo [步骤 5/5] 创建版本标签...
set /p tagname="请输入标签名称（如：v1.4.1）: "
if "%tagname%"=="" (
    echo 未输入标签名称，跳过标签创建
) else (
    git tag -a %tagname% -m "Release %tagname%"
    git push origin %tagname%
    echo ✅ 标签 %tagname% 创建完成！
)

echo.
echo ============================================================
echo ✅ 完整发布流程完成！
echo ============================================================
echo.
echo 后续步骤：
echo 1. 访问 https://github.com/wyg5208/ChangoConverter
echo 2. 点击 "Releases" → "Create a new release"
echo 3. 选择刚创建的标签：%tagname%
echo 4. 填写Release说明
echo 5. 上传可执行文件（在dist目录）
echo 6. 发布Release
echo.
pause
cls
goto menu

:status
echo.
echo ============================================================
echo Git 状态
echo ============================================================
echo.

echo [当前分支和状态]
git status

echo.
echo [最近的提交]
git log --oneline -5

echo.
echo [远程仓库]
git remote -v

echo.
pause
cls
goto menu

:end
echo.
echo 感谢使用 ChangoConverter GitHub 发布助手！
echo.
timeout /t 2 >nul
exit

