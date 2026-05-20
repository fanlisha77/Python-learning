PyAutoGUI 中文使用手册
适用于 Windows /macOS/ Linux | 自动化控制鼠标、键盘、截图、弹窗
安装
bash
运行
pip install pyautogui
基础配置（推荐必加）
python
运行
import pyautogui
import time

# 防故障：鼠标移到屏幕左上角立即终止程序
pyautogui.FAILSAFE = True

# 所有操作默认延迟，防止执行过快
pyautogui.PAUSE = 0.5
屏幕与鼠标信息
获取屏幕尺寸
python
运行
width, height = pyautogui.size()
print(f"屏幕分辨率：{width} × {height}")
获取当前鼠标位置
python
运行
x, y = pyautogui.position()
print(f"鼠标坐标：X={x}, Y={y}")
判断坐标是否在屏幕内
python
运行
print(pyautogui.onScreen(100, 100))  # True / False
鼠标操作
鼠标移动
python
运行
# 绝对移动
pyautogui.moveTo(500, 500)
pyautogui.moveTo(500, 500, duration=2)  # 平滑移动

# 相对移动（基于当前位置）
pyautogui.moveRel(100, 0)   # 右移 100
pyautogui.moveRel(0, -50)   # 上移 50
鼠标点击
python
运行
pyautogui.click()               # 左键单击
pyautogui.click(300, 300)       # 指定位置单击
pyautogui.click(button='right') # 右键单击
pyautogui.doubleClick()         # 左键双击
pyautogui.tripleClick()         # 三击
鼠标按下 / 松开
python
运行
pyautogui.mouseDown()
pyautogui.mouseUp()

pyautogui.mouseDown(button='right')
pyautogui.mouseUp(button='right')
鼠标拖拽
python
运行
pyautogui.dragTo(700, 700, duration=1)    # 绝对拖拽
pyautogui.dragRel(200, 0, duration=0.5)  # 相对拖拽
鼠标滚轮
python
运行
pyautogui.scroll(100)   # 向上滚动
pyautogui.scroll(-100)  # 向下滚动
键盘操作
输入文字
python
运行
pyautogui.typewrite('Hello PyAutoGUI')
pyautogui.typewrite('Hello World', interval=0.1)  # 带间隔输入
单按键
python
运行
pyautogui.press('enter')
pyautogui.press('backspace')
pyautogui.press('space')
pyautogui.press(['a', 'b', 'c'], interval=0.2)
组合快捷键
python
运行
pyautogui.hotkey('ctrl', 'c')  # 复制
pyautogui.hotkey('ctrl', 'v')  # 粘贴
pyautogui.hotkey('ctrl', 'a')  # 全选
pyautogui.hotkey('ctrl', 's')  # 保存
pyautogui.hotkey('alt', 'f4')  # 关闭窗口
长按按键
python
运行
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')
弹窗交互
python
运行
# 提示弹窗
pyautogui.alert(text='任务完成', title='提示', button='确定')

# 确认弹窗
result = pyautogui.confirm(text='是否继续？', buttons=['确定', '取消'])

# 输入弹窗
user_input = pyautogui.prompt(text='请输入内容')

# 密码弹窗
password = pyautogui.password(text='请输入密码', mask='*')
截图与图像识别
全屏截图
python
运行
screenshot = pyautogui.screenshot()
screenshot.save('screen.png')
区域截图
python
运行
region_img = pyautogui.screenshot(region=(0, 0, 500, 500))
region_img.save('region.png')
屏幕找图（需安装 opencv-python）
python
运行
# pip install opencv-python

pos = pyautogui.locateOnScreen('target.png', confidence=0.8)
if pos:
    center_x, center_y = pyautogui.center(pos)
    pyautogui.click(center_x, center_y)
