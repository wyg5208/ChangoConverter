"""
测试转换功能的调试脚本
"""
import tkinter as tk
from app_all_function import ChangoConverter

def test_button():
    """测试按钮点击"""
    print("=" * 60)
    print("测试开始")
    print("=" * 60)
    
    # 创建主窗口
    root = tk.Tk()
    app = ChangoConverter(root)
    
    print(f"Pandoc已安装: {app.pandoc_installed}")
    print(f"Pandoc版本: {app.pandoc_version}")
    print(f"转换按钮状态: {app.convert_button['state']}")
    print(f"start_conversion方法存在: {hasattr(app, 'start_conversion')}")
    
    # 测试方法调用
    print("\n尝试调用start_conversion()...")
    try:
        # 不显示窗口，直接测试方法
        app.start_conversion()
        print("✓ start_conversion()调用成功")
    except Exception as e:
        print(f"✗ 调用失败: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)
    
    # 不启动主循环，直接关闭
    root.destroy()

if __name__ == "__main__":
    test_button()

