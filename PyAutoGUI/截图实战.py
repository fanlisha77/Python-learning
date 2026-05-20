from cnocr import CnOcr
import time
import pyautogui
left = 0
top = 0
width = 0
height = 0

for i in range(1,5):
    print(f"请把鼠标移到第{i}个位置")
    time.sleep(3)
    loc = pyautogui.position()
    if i == 1:
        left = loc.x
        top = loc.y
    if i == 3:
        width = loc.x - left
        height = loc.y - top
region = (left, top, width, height)
pyautogui.screenshot("a.jpg",region)
