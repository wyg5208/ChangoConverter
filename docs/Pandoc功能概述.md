Pandoc 是一个功能强大的通用文档转换工具，支持非常广泛的输入和输出格式。以下是截至 Pandoc 最新版本（通常指 3.x 系列）所支持的主要格式：

---

### 📥 支持的输入格式（可读格式）

- **Markdown**（包括多种变体）：
  - `markdown`（Pandoc 自己的 Markdown 扩展）
  - `commonmark`
  - `gfm`（GitHub Flavored Markdown）
  - `markdown_mmd`（MultiMarkdown）
  - `markdown_phpextra`
  - `markdown_strict`（原始 Markdown）

- **HTML**：
  - `html` / `html5`

- **LaTeX**

- **DocBook**（`docbook`, `docbook5`）

- **EPUB**（`epub`, `epub3`）

- **Microsoft Word**：
  - `docx`

- **OpenDocument**：
  - `odt`（OpenDocument Text）

- **RTF**（富文本格式）

- **Textile**

- **reStructuredText**（`rst`）

- **MediaWiki markup**（维基百科使用的格式）

- **Org mode**（Emacs Org-mode）

- **Haddock**（Haskell 文档格式）

- **JATS**（Journal Article Tag Suite）

- **OPML**（Outline Processor Markup Language）

- **TEI Simple**（Text Encoding Initiative）

- **FB2**（FictionBook 电子书格式）

- **Man**（Unix 手册页）

- **TikiWiki**, **Vimwiki**, **ZimWiki** 等 wiki 格式

---

### 📤 支持的输出格式（可写格式）

- **Markdown**（同上，支持多种变体）
- **HTML**（`html`, `html5`, `html4`）
- **LaTeX**
- **PDF**（通过 LaTeX 或其他引擎间接生成）
- **EPUB**（`epub`, `epub3`）
- **DocBook**（`docbook`, `docbook5`）
- **Microsoft Word**（`docx`）
- **OpenDocument Text**（`odt`）
- **RTF**
- **reStructuredText**（`rst`）
- **Textile**
- **AsciiDoc**
- **MediaWiki**
- **DokuWiki**
- **Org mode**
- **ICML**（InDesign 标记语言）
- **Slidy**, **Slideous**, **S5**, **DZSlides**, **reveal.js**, **PowerPoint**（`pptx`）——用于幻灯片
- **JATS**
- **Man**（Unix 手册页）
- **OPML**
- **TEI**
- **FB2**
- **Plain text**（`plain`）
- **Custom writers**（可通过 Lua 脚本扩展）

---

### ⚙️ 特别说明

- **PDF 输出**：Pandoc 本身不直接生成 PDF，而是通过调用 LaTeX（如 `pdflatex`、`xelatex`、`lualatex`）或使用 `wkhtmltopdf`（HTML 转 PDF）等外部工具实现。
- **自定义格式**：从 Pandoc 2.0 起，支持使用 **Lua 编写自定义读写器（custom readers/writers）**，极大扩展了格式支持能力。
- **元数据支持**：大多数格式支持 YAML 元数据块（如标题、作者、日期等）。

---

### ✅ 查看当前安装版本支持的格式

你可以在终端运行以下命令查看你的 Pandoc 版本支持的所有格式：

```bash
pandoc --list-input-formats
pandoc --list-output-formats
```

---

如需最新和最完整的格式列表，建议查阅官方文档：  
👉 https://pandoc.org/

希望这能帮到你！如果你有特定的转换需求（比如 Markdown 转 Word 或 LaTeX 转 HTML），也可以告诉我，我可以提供具体命令示例。