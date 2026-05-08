# 🐍 Python 基础知识完整指南

> 本文档为我的第一个 Python 学习 Markdown 文件，可直接上传到 GitHub。  
> 内容覆盖 Python 初学者需要掌握的所有基础知识点。

---

# 📚 目录

1. Python 简介  
2. Python 安装  
3. 第一个 Python 程序  
4. 注释  
5. 变量  
6. 数据类型  
7. 输入与输出  
8. 运算符  
9. 条件判断  
10. 循环语句  
11. 函数  
12. 列表  
13. 元组  
14. 字典  
15. 集合  
16. 字符串  
17. 模块与库  
18. 文件操作  
19. 异常处理  
20. 面向对象编程  
21. 常用库介绍  
22. 初学者练习项目  
23. 总结

---

# 1️⃣ Python 简介

Python 是一种**高级编程语言**，语法简洁、易学、功能强大，广泛应用于：

- Web 开发  
- 人工智能与机器学习  
- 数据分析与科学计算  
- 自动化脚本与办公自动化  
- 游戏开发  
- 网络安全与爬虫

---

# 2️⃣ Python 安装

从官方网站下载安装：

[Python 官网](https://www.python.org/)

安装时注意勾选：

安装完成后验证：

```bash
python --version

3️⃣ 第一个 Python 程序
print("Hello, World!")

输出：

Hello, World!

4️⃣ 注释
# 单行注释

"""
多行注释
用于解释复杂逻辑或文档说明
"""

5️⃣ 变量
name = "张三"
age = 20
height = 175.5
is_student = True

6️⃣ 数据类型
类型	示例
字符串	"Hello"
整数	10
浮点数	3.14
布尔值	True
列表	[1,2,3]
元组	(1,2,3)
字典	{"name":"Tom"}
集合	{1,2,3}

7️⃣ 输入与输出
name = input("请输入姓名：")
print("你好,", name)

8️⃣ 运算符
算术运算
+  -  *  /  //  %  **
比较运算
== != > < >= <=
逻辑运算
and or not

9️⃣ 条件判断
age = 20

if age >= 18:
    print("成年人")
elif age >= 13:
    print("青少年")
else:
    print("儿童")

🔟 循环语句
for 循环
for i in range(5):
    print(i)
while 循环
i = 0
while i < 5:
    print(i)
    i += 1

1️⃣1️⃣ 函数
def add(a, b):
    return a + b

print(add(3, 5))

1️⃣2️⃣ 列表
fruits = ["苹果", "香蕉", "橘子"]

print(fruits[0])
fruits.append("葡萄")

1️⃣3️⃣ 元组
numbers = (1, 2, 3)

元组不可修改，适合存储固定数据。

1️⃣4️⃣ 字典
student = {
    "name": "张三",
    "age": 20
}

print(student["name"])

1️⃣5️⃣ 集合
nums = {1,2,3,3,2}
print(nums)

输出：

{1,2,3}

1️⃣6️⃣ 字符串操作
text = "Python"
print(text.upper())  # 全大写
print(text.lower())  # 全小写
print(len(text))     # 字符长度
print(text[0])       # 访问首字符

1️⃣7️⃣ 模块与库
import math

print(math.sqrt(16))  # 开平方

1️⃣8️⃣ 文件操作
写入文件
file = open("test.txt", "w")
file.write("Hello Python")
file.close()
读取文件
file = open("test.txt", "r")
print(file.read())
file.close()

1️⃣9️⃣ 异常处理
try:
    x = 10 / 0
except ZeroDivisionError:
    print("除零错误！")
finally:
    print("执行完成")

2️⃣0️⃣ 面向对象编程
class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("你好，", self.name)

s1 = Student("张三")
s1.say_hello()

2️⃣1️⃣ 常用库
库	用途
math	数学运算
random	随机数
os	操作系统操作
time	时间处理
pandas	数据分析
numpy	科学计算

2️⃣2️⃣ 初学者练习项目
计算器
猜数字游戏
学生成绩管理系统
待办事项列表
密码生成器

2️⃣3️⃣ 总结

Python 简单易学、功能强大，是编程初学者的首选语言。

学习方法：

学习语法 → 练习代码 → 实战项目 → 提升技能
