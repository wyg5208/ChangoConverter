"""
PyInstaller 打包配置文件
用于将 Pandoc 全功能文档转换器打包成 EXE 文件
"""

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app_all_function.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'pypandoc',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'pathlib',
        'threading',
        'subprocess',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PandocConverter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 不显示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,  # 如果有图标文件
)


