"""
生成ChangoConverter应用图标
使用PIL创建一个简单但专业的图标
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    # 创建resources目录
    if not os.path.exists('resources'):
        os.makedirs('resources')
    
    # 创建一个256x256的图标（多个尺寸）
    sizes = [256, 128, 64, 48, 32, 16]
    images = []
    
    for size in sizes:
        # 创建图像
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # 深绿色背景圆形
        margin = size // 16
        draw.ellipse(
            [margin, margin, size - margin, size - margin],
            fill='#006400',
            outline='#004d00',
            width=max(1, size // 32)
        )
        
        # 绘制转换箭头符号 (<<>>)
        try:
            # 尝试使用系统字体
            font_size = size // 3
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                try:
                    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
            
            # 绘制文字 "CC" (ChangoConverter)
            text = "CC"
            
            # 获取文字大小
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # 居中绘制
            x = (size - text_width) // 2
            y = (size - text_height) // 2 - size // 20
            
            # 绘制白色文字
            draw.text((x, y), text, fill='white', font=font)
            
        except Exception as e:
            print(f"字体渲染失败: {e}")
            # 如果字体失败，绘制简单的转换符号
            arrow_width = size // 3
            arrow_height = size // 6
            center_x = size // 2
            center_y = size // 2
            
            # 左箭头
            draw.polygon([
                (center_x - arrow_width, center_y - arrow_height // 2),
                (center_x - arrow_width // 2, center_y),
                (center_x - arrow_width, center_y + arrow_height // 2),
            ], fill='white')
            
            # 右箭头
            draw.polygon([
                (center_x + arrow_width, center_y - arrow_height // 2),
                (center_x + arrow_width // 2, center_y),
                (center_x + arrow_width, center_y + arrow_height // 2),
            ], fill='white')
        
        images.append(img)
    
    # 保存为ICO格式（Windows图标）
    images[0].save(
        'resources/icon.ico',
        format='ICO',
        sizes=[(s, s) for s in sizes]
    )
    
    # 保存为PNG格式（用于显示）
    images[0].save('resources/icon.png', format='PNG')
    
    print("✅ 图标生成成功！")
    print("   - resources/icon.ico (Windows图标)")
    print("   - resources/icon.png (PNG图标)")
    
except ImportError:
    print("❌ PIL/Pillow库未安装")
    print("   请运行: pip install Pillow")
except Exception as e:
    print(f"❌ 图标生成失败: {e}")

