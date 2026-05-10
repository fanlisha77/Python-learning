import random
import time
#一.变量和数据类型
#1.变量命名规范：由字母，数字，下划线组成。不能由数字开头，不能使用关键字！！！

#2.数据类型：
#（1）单值数据类型：
#整型 int  浮点型 float  布尔类型 bool  空值类型 None
#type函数：用来获取数据的类型
int1 = 777
float1 = 1.777
a = 7777
b = None
print(int1)
print(float1)
print(a !=7777)
print(b is not None)
print(type(int1))
print(type(float1))
print(type(a))
print(type(b))
#三种输出方式：
name = "张三"
age = 19
sex = "男"
#1.print多个参数输出，逗号分割
print("姓名:",name,"年龄:",age,"性别:",sex)
#2.连字符：+拼接          !!!字符串只能和字符串相连
print("姓名:"+name+"年龄:"+str(age)+"性别"+sex)
#3.f格式化
print(f"姓名:{name} 年龄:{age} 性别:{sex}")

#输入:input()      获取的是字符串类型

#（2）组合数据类型
#字符串 str  单引号或双引号
# 列表 list  中括号
# 字典 dict  大括号
# 元组 tuple  小括号
str1 = 'asdfghj'
list1 = ["李四",20,"男"]
dict1 = {
    "name":"李四",
    "age":20,
    "sex":"男"
}
tuple1 = ("李四",20,"男")
print(str1)
print(list1)
print(dict1)
print(tuple1)
#!!!只有字符串，列表，元组有索引和切片
#(1)索引:获取数据中某个值
# 从左往右：0 1 2 3...
# 从右往左：... -3 -2 -1
#(2)切片:获取数据中多个连续的值
#格式：变量名[开始索引：结束索引：步长]
#!!! 包含开始索引，不包含结束索引    不写步长时，默认为1
print(str1[0],str1[1],str1[2])
print(str1[-1],str1[-2],str1[-3])
print(str1[0:7:2])
print(list1[0:3])
print(tuple1[0:3])

#二.运算符
#1.算术运算符  + - * / 求整数:// 幂运算:** 取余数:%
m = 10
n = 5
print(m + n)
print(m - n)
print(m * n)
print(m / n)
print(m % n)
print(m ** n)
print(m // n)

#(2)赋值运算符  = += -= *= /=
f = 99
f += 1
f -= 1
f *= 2
f /= 9
print(f)

#(3)比较运算符: > < >= <= == !=        返回的是bool类型
print(4>2)
print(4>=2)
print(4<=2)
print(3==2)
print(3!=2)

#(4)逻辑运算符: and  or  not

#(5)成员运算符:检查某个数据是否在另一个数据中       返回的是bool类型
# in        not in

#三.内置变量函数
#1.查看当前文件在电脑中的位置：
print(__file__)
#2.列表的追加函数:
list2 = [1,2,3]
list2.append(4)
print(list2)
#3.类型转换:
#(1)字符串转换成列表：
str3 = 'abc'
list3 = str3.split(',')
print(list3)
#(2)列表转换成字符串:
list4 = ["苹果","香蕉","橘子"]
str4 = " ".join(list4)
print(str4)
#4.（1）最大值:max()         最小值：min()
list5 = [2,3,4,5,6,7]
print(max(list5))
print(min(list5))
#(2)升序：变量名.sort()          降序:变量名.sort(reverse = True)
list6 = [0,99,4,34,79,2]
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)
#(3)round(数字，要保留的小数位数)
g = 7.1234567
print(round(g))
print(round(g,3))
#(4)count()统计某个数字出现的总次数
list7 = [2,3,2,2,2,7,7]
print(list7.count(2))
#5.内部模块调用        在程序最上面用import引入
#(1)随机模块:random.sample(变量名，个数)
#(2)时间模块:
#让程序休眠t秒：time.sleep(t)
time.sleep(7)
p = 7
print(p)
#获取系统当前的秒数:time.time()
print(time.time())
#获取系统当前的年月日:time.localtime()

#四.流程控制
#1.顺序结构：程序从上往下读取代码
#若两个变量重名，则后一个会覆盖前一个

#2.分支结构：
#（1）单分支结构：if      else
age2 = 20
if age2 >= 18:
    print("你成年了")
else:
    print("你还没有成年")
#（2）双分支结构: if   elif   elif ... else
score = 700
if score <= 60:
    print("成绩及格")
elif score >= 130:
    print("成绩优秀")
elif score >= 150:
    print("成绩满分")
else:
    print("不及格")
#3.循环结构:   for i in range(开始值，结束值)
sum = 0
for i in range(1,101):
    sum += i
print(sum)
#循环控制语句:continue     break
for i in range(1,6):
    if i == 3:
        continue
    print(i)
    

