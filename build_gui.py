"""
ChangoConverter 全功能文档转换器 - 图形化打包工具
提供友好的图形界面进行打包操作
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import threading
import os
import sys

class BuildTool:
    def __init__(self, root):
        self.root = root
        self.root.title("ChangoConverter 全功能文档转换器 v1.4.1 - 打包工具")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        
        self.create_widgets()
        
    def create_widgets(self):
        # 标题
        title_label = ttk.Label(
            self.root,
            text="ChangoConverter 全功能文档转换器 v1.4.1 - 打包工具",
            font=('Arial', 14, 'bold')
        )
        title_label.pack(pady=20)
        
        # 选项框架
        options_frame = ttk.LabelFrame(self.root, text="打包选项", padding="20")
        options_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # 打包类型
        ttk.Label(options_frame, text="打包类型:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.build_type = tk.StringVar(value="exe")
        
        ttk.Radiobutton(
            options_frame,
            text="EXE 文件 (推荐) - 单文件，易分发",
            variable=self.build_type,
            value="exe"
        ).grid(row=0, column=1, sticky=tk.W, padx=10)
        
        ttk.Radiobutton(
            options_frame,
            text="MSI 安装包 - 专业安装体验",
            variable=self.build_type,
            value="msi"
        ).grid(row=1, column=1, sticky=tk.W, padx=10)
        
        ttk.Radiobutton(
            options_frame,
            text="发布包 - 创建完整的发布压缩包",
            variable=self.build_type,
            value="release"
        ).grid(row=2, column=1, sticky=tk.W, padx=10)
        
        # 高级选项
        advanced_frame = ttk.LabelFrame(self.root, text="高级选项", padding="15")
        advanced_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.use_upx = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            advanced_frame,
            text="使用 UPX 压缩 (减小文件体积)",
            variable=self.use_upx
        ).pack(anchor=tk.W, pady=2)
        
        self.clean_build = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            advanced_frame,
            text="清理旧的构建文件",
            variable=self.clean_build
        ).pack(anchor=tk.W, pady=2)
        
        self.open_folder = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            advanced_frame,
            text="完成后打开输出文件夹",
            variable=self.open_folder
        ).pack(anchor=tk.W, pady=2)
        
        # 按钮
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=15)
        
        self.build_button = ttk.Button(
            button_frame,
            text="🚀 开始打包",
            command=self.start_build,
            width=15
        )
        self.build_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="📖 打开指南",
            command=self.open_guide,
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="❌ 关闭",
            command=self.root.quit,
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        # 进度条
        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        self.progress.pack(fill=tk.X, padx=20, pady=5)
        
        # 日志框
        log_frame = ttk.LabelFrame(self.root, text="构建日志", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            wrap=tk.WORD,
            height=10,
            font=('Consolas', 9)
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
    def log(self, message):
        """添加日志"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
        
    def start_build(self):
        """开始打包"""
        build_type = self.build_type.get()
        
        # 禁用按钮
        self.build_button.config(state='disabled')
        self.progress.start()
        
        # 清空日志
        self.log_text.delete(1.0, tk.END)
        
        # 在新线程中执行
        thread = threading.Thread(target=self.build_thread, args=(build_type,))
        thread.daemon = True
        thread.start()
        
    def build_thread(self, build_type):
        """打包线程"""
        try:
            if build_type == "exe":
                self.build_exe()
            elif build_type == "msi":
                self.build_msi()
            elif build_type == "release":
                self.build_release()
                
            self.root.after(0, self.build_complete)
        except Exception as e:
            self.root.after(0, lambda: self.build_error(str(e)))
            
    def build_exe(self):
        """打包 EXE"""
        self.log("=" * 60)
        self.log("开始打包 EXE 文件...")
        self.log("=" * 60)
        
        # 清理
        if self.clean_build.get():
            self.log("\n清理旧文件...")
            if os.path.exists("build"):
                self.run_command("rmdir /s /q build")
            if os.path.exists("dist"):
                self.run_command("rmdir /s /q dist")
        
        # 构建命令
        cmd = [
            "pyinstaller",
            "--noconfirm",
            "--onefile",
            "--windowed",
            "--name=ChangoConverter",
        ]
        
        if self.use_upx.get():
            cmd.append("--upx-dir=upx")
            
        cmd.append("app_all_function.py")
        
        self.log("\n执行打包命令...")
        self.run_command(" ".join(cmd))
        
        if os.path.exists("dist\\ChangoConverter.exe"):
            size = os.path.getsize("dist\\ChangoConverter.exe") / (1024 * 1024)
            self.log(f"\n✓ 打包成功！")
            self.log(f"文件: dist\\ChangoConverter.exe")
            self.log(f"大小: {size:.2f} MB")
        else:
            raise Exception("EXE 文件未生成")
            
    def build_msi(self):
        """打包 MSI"""
        self.log("=" * 60)
        self.log("开始打包 MSI 安装包...")
        self.log("=" * 60)
        
        # 清理
        if self.clean_build.get():
            self.log("\n清理旧文件...")
            if os.path.exists("build"):
                self.run_command("rmdir /s /q build")
            if os.path.exists("dist"):
                self.run_command("rmdir /s /q dist")
        
        self.log("\n执行打包命令...")
        self.run_command("python setup.py bdist_msi")
        
        # 查找 MSI 文件
        if os.path.exists("dist"):
            msi_files = [f for f in os.listdir("dist") if f.endswith(".msi")]
            if msi_files:
                msi_file = msi_files[0]
                size = os.path.getsize(f"dist\\{msi_file}") / (1024 * 1024)
                self.log(f"\n✓ 打包成功！")
                self.log(f"文件: dist\\{msi_file}")
                self.log(f"大小: {size:.2f} MB")
            else:
                raise Exception("MSI 文件未生成")
        else:
            raise Exception("dist 目录未创建")
            
    def build_release(self):
        """准备发布包"""
        self.log("=" * 60)
        self.log("准备发布包...")
        self.log("=" * 60)
        
        if not os.path.exists("dist\\ChangoConverter.exe"):
            self.log("\n[错误] 未找到 ChangoConverter.exe")
            self.log("请先打包 EXE 文件")
            raise Exception("请先打包 EXE 文件")
        
        self.log("\n执行发布准备脚本...")
        self.run_command("prepare_release.bat")
        
        if os.path.exists("ChangoConverter-v1.4.1.zip"):
            size = os.path.getsize("ChangoConverter-v1.4.1.zip") / (1024 * 1024)
            self.log(f"\n✓ 发布包创建成功！")
            self.log(f"文件: ChangoConverter-v1.4.1.zip")
            self.log(f"大小: {size:.2f} MB")
        else:
            raise Exception("发布包未生成")
            
    def run_command(self, cmd):
        """运行命令"""
        self.log(f"\n> {cmd}")
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        for line in iter(process.stdout.readline, ''):
            if line.strip():
                self.log(line.strip())
                
        process.wait()
        if process.returncode != 0:
            raise Exception(f"命令执行失败: {cmd}")
            
    def build_complete(self):
        """构建完成"""
        self.progress.stop()
        self.build_button.config(state='normal')
        
        self.log("\n" + "=" * 60)
        self.log("构建完成！")
        self.log("=" * 60)
        
        messagebox.showinfo("成功", "打包完成！\n\n输出文件位于 dist 目录")
        
        if self.open_folder.get():
            if os.path.exists("dist"):
                os.startfile("dist")
            else:
                os.startfile(".")
                
    def build_error(self, error):
        """构建错误"""
        self.progress.stop()
        self.build_button.config(state='normal')
        
        self.log(f"\n[错误] {error}")
        messagebox.showerror("错误", f"打包失败！\n\n{error}")
        
    def open_guide(self):
        """打开指南"""
        if os.path.exists("BUILD_GUIDE.md"):
            os.startfile("BUILD_GUIDE.md")
        else:
            messagebox.showinfo("提示", "未找到 BUILD_GUIDE.md 文件")

def main():
    root = tk.Tk()
    app = BuildTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()


