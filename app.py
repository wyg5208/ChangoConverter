import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
import threading

try:
    import pypandoc
    PANDOC_AVAILABLE = True
except ImportError:
    PANDOC_AVAILABLE = False
    pypandoc = None

class PandocMarkdownConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Pandoc Markdown 转 DOCX 转换器")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        
        # 检查 Pandoc 是否可用
        self.check_pandoc_availability()
        
        # 创建界面
        self.create_widgets()
        
    def check_pandoc_availability(self):
        """检查 Pandoc 是否可用"""
        if not PANDOC_AVAILABLE:
            messagebox.showerror(
                "依赖缺失", 
                "pypandoc 未安装！\n请运行: pip install pypandoc"
            )
            self.root.quit()
            return
            
        try:
            # 尝试获取 pandoc 版本
            pypandoc.get_pandoc_version()
        except OSError:
            messagebox.showerror(
                "Pandoc 未安装", 
                "Pandoc 未在系统中找到！\n"
                "请从 https://pandoc.org/installing.html 下载并安装 Pandoc"
            )
            self.root.quit()
            
    def create_widgets(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # 标题
        title_label = ttk.Label(
            main_frame, 
            text="Pandoc Markdown 转 DOCX 转换器", 
            font=('Arial', 14, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Markdown文件选择
        ttk.Label(main_frame, text="Markdown文件:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.md_path_var = tk.StringVar()
        md_entry = ttk.Entry(main_frame, textvariable=self.md_path_var, width=60)
        md_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=5)
        ttk.Button(main_frame, text="浏览", command=self.browse_md_file).grid(row=1, column=2, padx=(0, 5), pady=5)
        
        # 输出文件选择
        ttk.Label(main_frame, text="输出DOCX文件:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.docx_path_var = tk.StringVar()
        docx_entry = ttk.Entry(main_frame, textvariable=self.docx_path_var, width=60)
        docx_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=5)
        ttk.Button(main_frame, text="浏览", command=self.browse_docx_file).grid(row=2, column=2, padx=(0, 5), pady=5)
        
        # 高级选项框架
        advanced_frame = ttk.LabelFrame(main_frame, text="高级选项", padding="10")
        advanced_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=15)
        advanced_frame.columnconfigure(1, weight=1)
        
        # CSS 样式文件（可选）
        ttk.Label(advanced_frame, text="CSS样式文件 (可选):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.css_path_var = tk.StringVar()
        css_entry = ttk.Entry(advanced_frame, textvariable=self.css_path_var, width=50)
        css_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=5)
        ttk.Button(advanced_frame, text="浏览", command=self.browse_css_file).grid(row=0, column=2, padx=(0, 5), pady=5)
        
        # 转换选项
        options_frame = ttk.Frame(advanced_frame)
        options_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        self.standalone_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            options_frame, 
            text="独立文档 (--standalone)", 
            variable=self.standalone_var
        ).grid(row=0, column=0, sticky=tk.W, padx=(0, 20))
        
        self.wrap_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            options_frame, 
            text="自动换行", 
            variable=self.wrap_var
        ).grid(row=0, column=1, sticky=tk.W)
        
        # 转换按钮
        convert_button = ttk.Button(
            main_frame, 
            text="开始转换", 
            command=self.start_conversion,
            style='Accent.TButton'
        )
        convert_button.grid(row=4, column=1, columnspan=2, pady=20, sticky=tk.E)
        
        # 进度条
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # 状态标签
        self.status_var = tk.StringVar()
        self.status_var.set("准备就绪 - Pandoc 已就绪")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, foreground="green")
        status_label.grid(row=6, column=0, columnspan=3, pady=5)
        
        # 日志/预览区域
        ttk.Label(main_frame, text="转换日志:").grid(row=7, column=0, columnspan=3, sticky=tk.W, pady=(20, 5))
        
        # 创建文本框和滚动条
        log_frame = ttk.Frame(main_frame)
        log_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = tk.Text(log_frame, wrap=tk.WORD, height=12, font=('Consolas', 9))
        scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # 配置主框架的行权重
        main_frame.rowconfigure(8, weight=1)
        
        # 添加样式
        style = ttk.Style()
        if sys.platform == "win32":
            style.configure('Accent.TButton', font=('Arial', 10, 'bold'))
        else:
            style.configure('Accent.TButton', font=('Arial', 10, 'bold'))
    
    def browse_md_file(self):
        """浏览选择Markdown文件"""
        file_path = filedialog.askopenfilename(
            title="选择Markdown文件",
            filetypes=[
                ("Markdown文件", "*.md *.markdown *.mdown"),
                ("所有文件", "*.*")
            ]
        )
        if file_path:
            self.md_path_var.set(file_path)
            
            # 自动设置输出文件路径
            if not self.docx_path_var.get():
                docx_path = os.path.splitext(file_path)[0] + ".docx"
                self.docx_path_var.set(docx_path)
    
    def browse_docx_file(self):
        """浏览选择输出DOCX文件"""
        file_path = filedialog.asksaveasfilename(
            title="保存DOCX文件",
            defaultextension=".docx",
            filetypes=[("Word文档", "*.docx"), ("所有文件", "*.*")]
        )
        if file_path:
            self.docx_path_var.set(file_path)
    
    def browse_css_file(self):
        """浏览选择CSS文件"""
        file_path = filedialog.askopenfilename(
            title="选择CSS样式文件",
            filetypes=[("CSS文件", "*.css"), ("所有文件", "*.*")]
        )
        if file_path:
            self.css_path_var.set(file_path)
    
    def start_conversion(self):
        """开始转换（在新线程中执行）"""
        md_path = self.md_path_var.get()
        docx_path = self.docx_path_var.get()
        
        # 验证输入
        if not md_path:
            messagebox.showwarning("警告", "请选择Markdown文件")
            return
        
        if not docx_path:
            messagebox.showwarning("警告", "请指定输出DOCX文件路径")
            return
        
        if not os.path.exists(md_path):
            messagebox.showerror("错误", "Markdown文件不存在")
            return
        
        # 禁用按钮，显示进度
        self.status_var.set("正在转换...")
        self.status_var.set("正在转换...")
        self.progress.start()
        self.root.update()
        
        # 在新线程中执行转换
        thread = threading.Thread(target=self.convert_file_thread)
        thread.daemon = True
        thread.start()
    
    def convert_file_thread(self):
        """在后台线程中执行转换"""
        try:
            self.convert_with_pandoc()
            self.root.after(0, self.conversion_success)
        except Exception as e:
            error_msg = str(e)
            self.root.after(0, lambda: self.conversion_error(error_msg))
    
    def convert_with_pandoc(self):
        """使用 Pandoc 执行转换"""
        md_file = self.md_path_var.get()
        docx_file = self.docx_path_var.get()
        css_file = self.css_path_var.get() if self.css_path_var.get() else None
        
        # 构建额外参数
        extra_args = []
        
        if self.standalone_var.get():
            extra_args.append('--standalone')
            
        if self.wrap_var.get():
            extra_args.append('--wrap=auto')
        else:
            extra_args.append('--wrap=none')
            
        if css_file and os.path.exists(css_file):
            extra_args.extend(['--css', css_file])
            self.log_message(f"使用CSS样式文件: {css_file}")
        
        # 记录转换信息
        self.log_message(f"输入文件: {md_file}")
        self.log_message(f"输出文件: {docx_file}")
        self.log_message(f"额外参数: {' '.join(extra_args)}")
        self.log_message("开始转换...")
        
        # 执行转换
        try:
            output = pypandoc.convert_file(
                md_file,
                'docx',
                outputfile=docx_file,
                extra_args=extra_args
            )
            self.log_message("转换成功完成!")
        except Exception as e:
            self.log_message(f"转换失败: {str(e)}")
            raise e
    
    def log_message(self, message):
        """在日志区域添加消息"""
        self.root.after(0, lambda: self._add_log_message(message))
    
    def _add_log_message(self, message):
        """实际添加日志消息的方法"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def conversion_success(self):
        """转换成功后的处理"""
        self.progress.stop()
        self.status_var.set("转换完成!")
        docx_path = self.docx_path_var.get()
        messagebox.showinfo("成功", f"文件已成功转换并保存到:\n{docx_path}")
    
    def conversion_error(self, error_message):
        """转换失败后的处理"""
        self.progress.stop()
        self.status_var.set("转换失败")
        messagebox.showerror("错误", f"转换过程中出现错误:\n{error_message}")

def main():
    root = tk.Tk()
    app = PandocMarkdownConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()