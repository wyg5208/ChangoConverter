@echo off
chcp 65001 >nul
cls

echo ============================================================
echo Git 文件状态检查工具
echo ============================================================
echo.

echo [检查1] 验证Git是否安装
echo ────────────────────────────────────────────────────
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未安装Git
    echo    请安装：https://git-scm.com/
    pause
    exit /b 1
) else (
    git --version
    echo ✅ Git已安装
)

echo.
echo [检查2] 验证重要文件是否会被忽略
echo ────────────────────────────────────────────────────

set ALL_GOOD=1

echo 检查 README.md...
git check-ignore README.md >nul 2>&1
if errorlevel 1 (
    echo ✅ README.md - 不会被忽略（正常）
) else (
    echo ❌ README.md - 会被忽略（错误！）
    set ALL_GOOD=0
)

echo 检查 docs/目录...
git check-ignore docs/GitHub发布指南.md >nul 2>&1
if errorlevel 1 (
    echo ✅ docs/ - 不会被忽略（正常）
) else (
    echo ❌ docs/ - 会被忽略（错误！）
    set ALL_GOOD=0
)

echo 检查 test_scripts/目录...
git check-ignore test_scripts/generate_icon.py >nul 2>&1
if errorlevel 1 (
    echo ✅ test_scripts/ - 不会被忽略（正常）
) else (
    echo ❌ test_scripts/ - 会被忽略（错误！）
    set ALL_GOOD=0
)

echo 检查 app_all_function.py...
git check-ignore app_all_function.py >nul 2>&1
if errorlevel 1 (
    echo ✅ app_all_function.py - 不会被忽略（正常）
) else (
    echo ❌ app_all_function.py - 会被忽略（错误！）
    set ALL_GOOD=0
)

echo 检查 version.py...
git check-ignore version.py >nul 2>&1
if errorlevel 1 (
    echo ✅ version.py - 不会被忽略（正常）
) else (
    echo ❌ version.py - 会被忽略（错误！）
    set ALL_GOOD=0
)

echo 检查 resources/icon.ico...
git check-ignore resources/icon.ico >nul 2>&1
if errorlevel 1 (
    echo ✅ resources/icon.ico - 不会被忽略（正常）
) else (
    echo ❌ resources/icon.ico - 会被忽略（错误！）
    set ALL_GOOD=0
)

echo.
echo [检查3] 验证临时文件是否会被忽略
echo ────────────────────────────────────────────────────

echo 检查 __pycache__/...
git check-ignore __pycache__ >nul 2>&1
if errorlevel 1 (
    echo ⚠️  __pycache__/ - 不会被忽略（建议忽略）
) else (
    echo ✅ __pycache__/ - 会被忽略（正常）
)

echo 检查 *.log...
git check-ignore test.log >nul 2>&1
if errorlevel 1 (
    echo ⚠️  *.log - 不会被忽略（建议忽略）
) else (
    echo ✅ *.log - 会被忽略（正常）
)

echo 检查 temp_content.md...
git check-ignore temp_content.md >nul 2>&1
if errorlevel 1 (
    echo ⚠️  temp_content.md - 不会被忽略（建议忽略）
) else (
    echo ✅ temp_content.md - 会被忽略（正常）
)

echo 检查 build/目录...
git check-ignore build/ >nul 2>&1
if errorlevel 1 (
    echo ⚠️  build/ - 不会被忽略（建议忽略）
) else (
    echo ✅ build/ - 会被忽略（正常）
)

echo 检查 dist/目录...
git check-ignore dist/ >nul 2>&1
if errorlevel 1 (
    echo ⚠️  dist/ - 不会被忽略（建议忽略）
) else (
    echo ✅ dist/ - 会被忽略（正常）
)

echo.
echo [检查4] Git仓库状态
echo ────────────────────────────────────────────────────

git status >nul 2>&1
if errorlevel 1 (
    echo ℹ️  尚未初始化Git仓库
    echo    运行 github_publish.bat 初始化
) else (
    echo Git仓库已初始化，当前状态：
    echo.
    git status --short
)

echo.
echo ============================================================
echo 检查结果总结
echo ============================================================

if %ALL_GOOD%==1 (
    echo.
    echo ✅✅✅ 所有检查通过！ ✅✅✅
    echo.
    echo .gitignore 配置正确，重要文件不会被忽略
    echo 可以安全地推送到GitHub
    echo.
    echo 下一步：运行 github_publish.bat 发布到GitHub
    echo.
) else (
    echo.
    echo ❌❌❌ 发现问题！ ❌❌❌
    echo.
    echo 重要文件会被.gitignore忽略
    echo 请检查.gitignore文件配置
    echo.
    echo 解决方案：
    echo 1. 检查.gitignore末尾是否有过度忽略的规则
    echo 2. 移除 *.md、*.txt、docs/、test_scripts/ 等规则
    echo 3. 查看 docs\gitignore修复说明.md 获取详细帮助
    echo 4. 重新运行本检查脚本验证
    echo.
)

echo ============================================================
pause

