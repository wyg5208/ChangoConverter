"""
Pandoc 全功能文档转换器 - MSI 安装包配置
使用 cx_Freeze 创建 MSI 安装包
"""

import sys, os
from cx_Freeze import setup, Executable

# 应用程序信息
APP_NAME = "Pandoc Converter"
APP_VERSION = "1.3.1"
APP_DESCRIPTION = "Pandoc 全功能文档转换器 - 支持 30+ 输入格式和 40+ 输出格式"
APP_AUTHOR = "Pandoc Converter Team"
APP_URL = "https://pandoc.org/"

# 依赖项
build_exe_options = {
    "packages": [
        "os",
        "sys",
        "tkinter",
        "threading",
        "pathlib",
        "subprocess",
    ],
    "includes": [
        "pypandoc",
        "tkinter.ttk",
        "tkinter.filedialog",
        "tkinter.messagebox",
    ],
    "excludes": [
        "matplotlib",
        "numpy",
        "scipy",
        "pandas",
        "pytest",
        "PIL",
    ],
    "include_files": [
        ("README_app_all_function.md", "README.md"),
    ],
    "optimize": 2,
}

# MSI 安装包选项
bdist_msi_options = {
    "upgrade_code": "{12345678-1234-5678-1234-567812345678}",  # 唯一标识符
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\PandocConverter",
    "install_icon": "icon.ico" if os.path.exists("icon.ico") else None,
}

# 快捷方式配置
shortcut_table = [
    (
        "DesktopShortcut",        # Shortcut
        "DesktopFolder",          # Directory_
        "Pandoc Converter",       # Name
        "TARGETDIR",              # Component_
        "[TARGETDIR]PandocConverter.exe",  # Target
        None,                     # Arguments
        None,                     # Description
        None,                     # Hotkey
        None,                     # Icon
        None,                     # IconIndex
        None,                     # ShowCmd
        "TARGETDIR",              # WkDir
    ),
    (
        "ProgramMenuShortcut",
        "ProgramMenuFolder",
        "Pandoc Converter",
        "TARGETDIR",
        "[TARGETDIR]PandocConverter.exe",
        None,
        None,
        None,
        None,
        None,
        None,
        "TARGETDIR",
    ),
]

# 添加快捷方式表到 MSI 选项
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options["data"] = msi_data

# 基础配置
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # 使用 GUI 模式，不显示控制台

# 可执行文件配置
executables = [
    Executable(
        "app_all_function.py",
        base=base,
        target_name="PandocConverter.exe",
        icon="icon.ico" if os.path.exists("icon.ico") else None,
        shortcut_name="Pandoc Converter",
        shortcut_dir="DesktopFolder",
    )
]

# 安装配置
setup(
    name=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    author=APP_AUTHOR,
    url=APP_URL,
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=executables,
)

