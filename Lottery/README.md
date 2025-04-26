# 抽奖小程序 🎲

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge) ![License](https://img.shields.io/badge/License-GPL_3.0-green?style=for-the-badge)

## 📦 功能特性

### 核心功能
- 📁 JSON文件存储参与名单
- 🎯 开始/停止式随机抽取
- ⚡ 30次/秒名字刷新速率（可调节）
- 🛠 自动错误检测机制
- 🌐 原生支持UTF-8中文显示

### 界面特性
- 🖥 响应式简约设计（320x240）
- 🎨 Material Design配色方案
- 📱 移动端友好布局
- 🌓 高对比度显示

## 🚀 快速开始

### 环境要求
- Python 3.6+
- Tkinter（通常内置）

### 使用方法
1. 准备名单文件：
   ```bash
   # 在程序目录创建 index.json
   echo '["张三", "李四", "王五"]' > index.json
   ```

1. 运行程序：

	```bash
	python index.py
	```

2. 操作流程：

	```
	[点击开始] → 名字快速滚动 → [点击停止] → 显示最终结果
	```

## 🎨 界面自定义

### 基础配置

```python
# 修改窗口尺寸
master.geometry("320x240")  # 格式: "宽x高"

# 调整刷新速度（33ms ≈ 30次/秒）
self.update_interval = 33

# 设置初始文本
self.result_label.config(text="点击开始")
```

### 视觉样式

```python
# 颜色方案（HEX格式）
COLOR_SCHEME = {
    "background": "#f5f5f5",      # 背景色
    "text_primary": "#424242",    # 主文字
    "highlight": "#1976d2",       # 高亮色
    "button_active": "#616161",   # 激活按钮
    "button_inactive": "#757575"  # 禁用按钮
}

# 字体配置
FONT_CONFIG = {
    "result": ("Helvetica", 24),  # 结果字体
    "button": ("Helvetica", 12),  # 按钮字体
    "status": ("Helvetica", 9)    # 状态字体
}
```

### 布局调整

```python
# 按钮间距调整（单位：像素）
self.start_btn.pack(side=tk.LEFT, padx=5)

# 外围边距设置
main_frame.pack(padx=20, pady=20)

# 状态栏位置
self.status_label.pack(pady=(10, 0))
```

## ⚙️ 高级配置

### 名单验证规则

```python
def load_members(self):
    # 现有代码...
    
    # 添加自定义校验
    if len(self.members) < 3:
        messagebox.showwarning("提示", "至少需要3个参与者")
    return [name for name in self.members if name.strip() != ""]
```

### 快捷键绑定

```python
# 在__init__()中添加：
master.bind("<space>", lambda e: self.toggle_drawing())
master.bind("<Return>", lambda e: self.stop_drawing())

def toggle_drawing(self):
    if self.is_running:
        self.stop_drawing()
    else:
        self.start_drawing()
```

## ❓ 常见问题

### 文件加载失败

✅ **解决方案：**

1. 确认文件名为`index.json`

2. 检查JSON格式有效性：

	```bash
	python -c "import json; json.load(open('index.json'))"
	```

3. 确保文件编码为UTF-8

### 界面显示异常

✅ **调试步骤：**

1. 临时禁用系统主题：

	```python
	master.tk.call("tk", "scaling", 1.0)
	```

2. 检查字体可用性：

	```python
	print(tk.font.families())  # 查看可用字体
	```

### 性能优化

💡 **建议配置：**

```python
# 在创建窗口前添加：
tk.Tk().tk.call('tk', 'scaling', 2.0)  # 高DPI适配
master.tk_setPalette(background='#f5f5f5')  # 强制背景色
```

## 📜 代码结构

复制

```
Lottery/
├── index.py        # 主程序
├── index.json      # 名单文件
└── README.md       # 说明文档
```

## 📄 开源协议

[GNU通用公共许可证 v3.0 - GNU工程 - 自由软件基金会](https://www.gnu.org/licenses/gpl-3.0.html)

> 🛠 提示：建议使用IDE进行可视化调试，可通过修改`MinimalLotteryApp`类实现深度定制