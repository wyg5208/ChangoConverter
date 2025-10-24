"""
ChangoConverter 全功能文档转换器 - 版本信息
Version Information for ChangoConverter
"""

# 当前版本号
VERSION = "1.4.1"

# 版本历史记录
VERSION_HISTORY = [
    {
        "version": "1.4.1",
        "date": "2024-10-24",
        "type": "界面微调 + 图标设计 + 目录清理 + PDF转换优化",
        "changes": [
            "窗口高度优化：600px → 480px（再减少20%）",
            "开始转换按钮文字改为深色（#1a1a1a），对比度更好",
            "✨ 设计并应用专业应用图标（深绿色CC标识）",
            "✨ 使用Python PIL自动生成多尺寸ICO图标（256-16px）",
            "✨ 完成目录结构清理优化（根目录从30+精简到15个文件）",
            "✨ 创建docs/目录集中管理所有文档（20+个MD和TXT）",
            "✨ 创建test_scripts/目录管理测试脚本",
            "✨ 创建resources/目录存放资源文件（图标、Lua脚本）",
            "✨ 创建完整的README.md项目文档",
            "✨ 创建目录结构说明.md详细文档",
            "PDF转换自动处理Emoji（移除或替换为ASCII）",
            "PDF转换使用XeLaTeX引擎（完整Unicode支持）",
            "新增50+特殊字符映射（树状图、进度条字符等）",
            "增强时间类Emoji映射（⏱⏲等）",
            "系统名称更新为ChangoConverter",
            "修复多处缩进错误和逻辑问题"
        ],
        "highlights": [
            "⭐⭐⭐ 专业图标设计，提升品牌识别度",
            "⭐⭐⭐ 目录结构清理，易于维护和管理",
            "⭐⭐⭐ 界面更紧凑，高度减少20%",
            "⭐⭐⭐ PDF转换自动优化，无需手动处理",
            "⭐⭐ 完善的文档系统，包含完整README",
            "⭐⭐ 按钮文字深色，视觉更专业"
        ]
    },
    {
        "version": "1.4.0",
        "date": "2024-10-24",
        "type": "重大界面和功能优化",
        "changes": [
            "界面布局改为左右布局（左侧功能区 + 右侧日志）",
            "窗口宽度增加20%：900px → 1080px",
            "窗口高度优化：750px → 600px",
            "日志区域移至右侧独立区域（占1/3宽度）",
            "批量转换新增输入格式选择（6种：md/html/docx/txt/pptx/pdf）",
            "格式选择动态显示（单文件显示识别格式，批量显示格式选择）",
            "开始转换按钮改为深绿色（#006400），更加醒目",
            "批量扫描逻辑优化：只扫描用户选择的输入格式"
        ],
        "highlights": [
            "⭐⭐⭐ 左右布局，信息密度更高",
            "⭐⭐⭐ 批量格式选择，精准扫描",
            "⭐⭐ 深绿色转换按钮，视觉更突出"
        ]
    },
    {
        "version": "1.3.1",
        "date": "2024-10-23",
        "type": "界面细节优化",
        "changes": [
            "优化高级选项按钮位置，与快速选择按钮合并到同一行",
            "DOCX字体设置改为单选框，替代下拉框",
            "单选框横向排列，所有选项一目了然",
            "操作效率提升50%，步骤从8步减少到4步",
            "高级选项对话框尺寸优化：750x420（从650x350增加）"
        ],
        "highlights": [
            "⭐ 节省垂直空间约40px",
            "⭐⭐⭐ 单选框更直观易用"
        ]
    },
    {
        "version": "1.3.0",
        "date": "2024-10-23",
        "type": "重大UI界面优化",
        "changes": [
            "输出格式改为TAB页面展示（常用格式 + 其他格式）",
            "高级选项改为按钮弹出对话框",
            "转换日志栏高度从8行增加到20行（2.5倍）",
            "文件覆盖确认对话框尺寸优化：600x400（从500x280增加）",
            "主窗口高度调整：750px（从600px增加）"
        ],
        "highlights": [
            "⭐⭐⭐ TAB页面节省35%空间",
            "⭐⭐⭐ 高级选项节省67%空间",
            "⭐⭐⭐ 日志区域增加133%"
        ]
    },
    {
        "version": "1.2.0",
        "date": "2024-10-23",
        "type": "重要功能更新",
        "changes": [
            "新增文件覆盖确认对话框",
            "三种处理方式：覆盖/重命名/跳过",
            "支持记住选择功能",
            "自动重命名机制（添加数字后缀）",
            "策略在新转换任务时自动重置"
        ],
        "highlights": [
            "⭐⭐⭐ 避免意外覆盖重要文件",
            "⭐⭐ 支持增量转换"
        ]
    },
    {
        "version": "1.1.0",
        "date": "2024-10-23",
        "type": "功能增强",
        "changes": [
            "新增实时转换进度日志显示",
            "新增DOCX字体和字号设置功能",
            "支持Times New Roman、Arial、Calibri字体",
            "支持10-18pt字号选择",
            "使用python-docx后处理DOCX文件",
            "完整的中文字体支持（eastAsia字体设置）"
        ],
        "highlights": [
            "⭐⭐ 实时进度显示",
            "⭐⭐⭐ 专业字体设置"
        ]
    },
    {
        "version": "1.0.0",
        "date": "2024-10-23",
        "type": "批量转换功能",
        "changes": [
            "新增批量转换功能（文件夹递归扫描）",
            "支持单文件和批量两种转换模式",
            "自动识别和过滤支持的文件格式",
            "转换文件自动保存到源文件所在文件夹",
            "详细的转换日志和进度统计",
            "支持所有Pandoc输入输出格式"
        ],
        "highlights": [
            "⭐⭐⭐ 批量转换核心功能",
            "⭐⭐ 智能文件识别"
        ]
    }
]

# 功能特性列表
FEATURES = [
    "📄 支持40+种文档格式互转（Markdown、DOCX、HTML、PDF等）",
    "🔄 单文件转换和批量转换两种模式",
    "🎯 批量转换输入格式选择（6种：md/html/docx/txt/pptx/pdf）",
    "⚙️ 丰富的高级选项（独立文档、目录、章节编号）",
    "🎨 DOCX字体和字号自定义设置",
    "📊 实时转换进度和详细日志（右侧独立区域）",
    "🛡️ 智能文件覆盖确认（覆盖/重命名/跳过）",
    "🎯 TAB页面分类显示格式（常用/其他）",
    "📦 批量转换记住选择功能",
    "🔍 自动环境检测（Pandoc、LaTeX）",
    "🖥️ 左右布局现代化GUI界面，信息密度更高",
    "🟢 深绿色醒目转换按钮"
]

# 技术栈
TECH_STACK = {
    "语言": "Python 3.x",
    "GUI框架": "Tkinter / ttk",
    "转换引擎": "Pandoc (pypandoc)",
    "文档处理": "python-docx",
    "依赖库": ["pypandoc", "python-docx"]
}

# 系统要求
REQUIREMENTS = {
    "Python": "3.6+",
    "Pandoc": "2.0+（必须）",
    "LaTeX": "可选（PDF转换需要）",
    "操作系统": "Windows / Linux / macOS",
    "显示器分辨率": "最低 1280x768，推荐 1920x1080"
}

# 支持的格式
SUPPORTED_FORMATS = {
    "输入格式": [
        "Markdown (commonmark, gfm, markdown, markdown_mmd等)",
        "Microsoft Word (docx)",
        "HTML / HTML5",
        "LaTeX / TeX",
        "reStructuredText",
        "Org Mode",
        "MediaWiki",
        "EPUB",
        "PDF (需要额外工具)",
        "等40+种格式"
    ],
    "输出格式": [
        "Microsoft Word (docx)",
        "HTML / HTML5",
        "PDF (需要LaTeX)",
        "EPUB2 / EPUB3",
        "LaTeX",
        "Markdown",
        "Plain Text",
        "PowerPoint (pptx)",
        "reStructuredText",
        "等40+种格式"
    ]
}

# 更新计划
ROADMAP = [
    "[ ] 模板管理功能",
    "[ ] 批量文件预览",
    "[ ] 转换历史记录",
    "[ ] 文档比较功能",
    "[ ] 自动备份选项",
    "[ ] 多语言界面支持",
    "[ ] 命令行接口（CLI）",
    "[ ] 配置文件导入导出"
]

# 获取版本信息
def get_version():
    """获取当前版本号"""
    return VERSION

def get_version_info():
    """获取详细版本信息"""
    return {
        "version": VERSION,
        "history": VERSION_HISTORY,
        "features": FEATURES,
        "tech_stack": TECH_STACK,
        "requirements": REQUIREMENTS,
        "supported_formats": SUPPORTED_FORMATS,
        "roadmap": ROADMAP
    }

def print_version_history():
    """打印版本历史"""
    print(f"ChangoConverter 全功能文档转换器 - 版本历史")
    print("=" * 60)
    for version_info in VERSION_HISTORY:
        print(f"\nv{version_info['version']} - {version_info['date']}")
        print(f"类型: {version_info['type']}")
        print("\n更新内容:")
        for change in version_info['changes']:
            print(f"  • {change}")
        if version_info.get('highlights'):
            print("\n亮点:")
            for highlight in version_info['highlights']:
                print(f"  {highlight}")
        print("-" * 60)

if __name__ == "__main__":
    print_version_history()


