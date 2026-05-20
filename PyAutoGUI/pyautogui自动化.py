import pyautogui as pg
import time

import pyperclip

#1.基础操作
# print(pg.size())#获取屏幕的大小
# print(pg.position())#获取鼠标的坐标
# print(pg.onScreen(3000,2000))#判断坐标是否在屏幕内

#2.鼠标
#移动
# pg.moveTo(700,700,duration=2)#绝对移动
# pg.moveRel(200,200,duration=2)#相对移动
#拖拽
# pg.dragTo(700,700,duration=2)#绝对拖拽
# pg.dragRel(200,200,duration=2)#相对拖拽
#点击
# pg.click(200,200)#左键单击
# pg.click(clicks=2)#左键双击
# pg.doubleClick(700,700)
#pg.rightClick()#右键单击
#滚动
# time.sleep(3)
# pg.scroll(800)#正数向上滚动
# pg.scroll(-800)#负数向下滚动Ilove

#3.键盘
# pg.write("I love Python",interval=0.1)#自动打出一句话   不支持中文
# print(pg.KEY_NAMES)#打印所有可识别按键
# pg.press("a")#模拟我按下一个键
# pg.hotkey('ctrl','c')#控制多个键
# pg.hotkey('ctrl','v')
# pyperclip.copy("abcdefghik")复制到了剪切板 win+v 中

#4.屏幕弹框
#警告/提示框
# s = pg.alert(title="警告",text="这里有风险",button="知道了")
# print(s)
#选择框
# s = pg.confirm(
#     title="别犹豫",
#     text="请选择你的爱车",
#     buttons=["春风250", "春风450", "张雪","杜卡迪","雅马哈"],
# )     无buttons时，按键为确定和取消
# print(s)
#输入框
# s = pg.prompt(title="别犹豫，勇敢点",text="请输入你的爱车",default="杜卡迪")
# print(s)
#密码框
# s = pg.password(title="这是一个密码框",text="请输入你的密码",default="1234567",mask="@")
# print(s)

#5.屏幕截图
# pg.screenshot("1.png",region=(429,53,900,1200))#截图
# pg.locateOnScreen("1.png",confidence=0.9)#识别图片并返回图片的坐标
# pg.locateAllOnScreen("2.png",confidence=0.8)#识别多个图片
res = pg.locateCenterOnScreen("1.png",confidence=0.9)  #返回图片中心坐标
print(res)