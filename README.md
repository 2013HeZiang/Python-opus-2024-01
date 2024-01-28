# Python中的一些小作品  2024-01创办
**Python 一些简单的小游戏，附源码**
==
**—————————————————————————————**
**下面是计算器的教程**

*V1.0*
运行效果：
![](https://raw.githubusercontent.com/2013HeZiang/2024-01/main/%E4%BD%9C%E5%93%81%20Opus%20%E5%B8%A6%E6%BA%90%E7%A0%81/%E8%AE%A1%E7%AE%97%E5%99%A8/V1.0/%E8%BF%90%E8%A1%8C%E6%95%88%E6%9E%9C.png)
```python
import tkinter as tk  # 导入库

root = tk.Tk()  # 窗口初始化
root.title('计算机 V1.0')  # 设置窗口标题
root.geometry('295x280+500+200')  # 窗口大小和位置
font = ('宋体', 20)  # 设置字体样式初始化
font_16 = ('宋体', 16)  # 设置字体样式的初始化

root.attributes('-alpha', 0.9)  # 窗口透明效果
root['background'] = '#ffffff'  # 设置背景颜色
```
上面是这个程序的初始化
————————————————
```python
result_num = tk.StringVar()  # 定义得数绑定显示的变量
result_num.set('0')  # 将得数显示设置显示"0"

tk.Label(root, textvariable=result_num, font=font, height=2, width=20, justify=tk.LEFT, anchor=tk.SE).grid(row=1, column=1, columnspan=4)  # 设置并布局一下的数的信息
```
以上是得数显示
————————————————
```python
button_clear = tk.Button(root, text='C', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_back = tk.Button(root, text='←', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_division = tk.Button(root, text='÷', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_multiplication = tk.Button(root, text='×', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_clear.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_division.grid(row=2, column=3, padx=4, pady=2)
button_multiplication.grid(row=2, column=4, padx=4, pady=2)
# 上面是一系列的按钮
```
————————————————
我们直接开始讲核心语法:

```python
def click_button(x):  # 加入字符串
    if result_num.get() == '0':  # 如果当时得数处于清空的"0"状态时
        result_num.set('')  # 将"0"变成空字符串
    result_num.set(result_num.get() + x)  # 在得数的后面直接添加一个"0"


def calculation():  # 计算得数
    opt_str = result_num.get()  # 获取算式
    result = eval(opt_str)  # 计算得数
    result_num.set(str(result))  # 显示得数


def clean():  # 清零
    result_num.set('0')  # 在得数上清零


def back():  # 回格
    a = result_num.get()  # 读取得数
    result_num.set(a[0:len(a)-1])  # 减最后一个数
    a = result_num.get()  # 再次获取得数
    if a == '':  # 如果没有了得数
        result_num.set('0')  # 将得数设置为"0"


button_one.config(command=lambda : click_button('1'))
button_two.config(command=lambda : click_button('2'))
button_three.config(command=lambda : click_button('3'))
button_four.config(command=lambda : click_button('4'))
button_five.config(command=lambda : click_button('5'))
button_six.config(command=lambda : click_button('6'))
button_seven.config(command=lambda : click_button('7'))
button_eight.config(command=lambda : click_button('8'))
button_nine.config(command=lambda : click_button('9'))
button_zero.config(command=lambda : click_button('0'))
button_addition.config(command=lambda : click_button('+'))
button_subtraction.config(command=lambda : click_button('-'))
button_multiplication.config(command=lambda : click_button('*'))
button_division.config(command=lambda : click_button('/'))
button_dot.config(command=lambda : click_button('.'))
button_clear.config(command=clean)
button_back.config(command=back)
button_equal.config(command=calculation)
# 绑定事件函数

root.mainloop()  # 进入主题循环
```

以上就是计算器V1.0的核心代码原理，主代码如下：
--
```python
import tkinter as tk

root = tk.Tk()
root.title('计算机 V1.0')
root.geometry('295x280+500+200')
font = ('宋体', 20)
font_16 = ('宋体', 16)

root.attributes('-alpha', 0.9)
root['background'] = '#ffffff'

result_num = tk.StringVar()
result_num.set('0')

tk.Label(root, textvariable=result_num, font=font, height=2, width=20, justify=tk.LEFT, anchor=tk.SE).grid(row=1, column=1, columnspan=4)

button_clear = tk.Button(root, text='C', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_back = tk.Button(root, text='←', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_division = tk.Button(root, text='÷', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_multiplication = tk.Button(root, text='×', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_clear.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_division.grid(row=2, column=3, padx=4, pady=2)
button_multiplication.grid(row=2, column=4, padx=4, pady=2)

button_seven = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_eight = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_nine = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_subtraction = tk.Button(root, text='﹣', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_seven.grid(row=3, column=1, padx=4, pady=2)
button_eight.grid(row=3, column=2, padx=4, pady=2)
button_nine.grid(row=3, column=3, padx=4, pady=2)
button_subtraction.grid(row=3, column=4, padx=4, pady=2)

button_four = tk.Button(root, text='4', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_five = tk.Button(root, text='5', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_six = tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_addition = tk.Button(root, text='+', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_four.grid(row=4, column=1, padx=4, pady=2)
button_five.grid(row=4, column=2, padx=4, pady=2)
button_six.grid(row=4, column=3, padx=4, pady=2)
button_addition.grid(row=4, column=4, padx=4, pady=2)

button_one = tk.Button(root, text='1', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_two = tk.Button(root, text='2', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_three = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_equal = tk.Button(root, text='=', width=5, font=font_16, height=3, relief=tk.FLAT, bg='#b1b2b2')
button_one.grid(row=5, column=1, padx=4, pady=2)
button_two.grid(row=5, column=2, padx=4, pady=2)
button_three.grid(row=5, column=3, padx=4, pady=2)
button_equal.grid(row=5, column=4, padx=4, pady=2, rowspan=2)

button_zero = tk.Button(root, text='0', width=12, font=font_16, relief=tk.FLAT, bg='#eacda1')
# button_zero2 = tk.Button(root, text='0', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_dot = tk.Button(root, text='.', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
# button_equal2 = tk.Button(root, text='=', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_zero.grid(row=6, column=1, padx=4, pady=2, columnspan=2)
# button_zero2.grid(row=6, column=2, padx=4, pady=2)
button_dot.grid(row=6, column=3, padx=4, pady=2)
# button_equal2.grid(row=6, column=4, padx=4, pady=2)


# 点击事件
def click_button(x):
    # print('x:\t', x)
    if result_num.get() == '0':
        result_num.set('')
    result_num.set(result_num.get() + x)

def calculation():
    opt_str = result_num.get()
    result = eval(opt_str)
    result_num.set(str(result))
    # print(opt_str)

def clean():
    result_num.set('0')

def back():
    a = result_num.get()
    result_num.set(a[0:len(a)-1])
    a = result_num.get()
    if a == '':
        result_num.set('0')

button_one.config(command=lambda : click_button('1'))
button_two.config(command=lambda : click_button('2'))
button_three.config(command=lambda : click_button('3'))
button_four.config(command=lambda : click_button('4'))
button_five.config(command=lambda : click_button('5'))
button_six.config(command=lambda : click_button('6'))
button_seven.config(command=lambda : click_button('7'))
button_eight.config(command=lambda : click_button('8'))
button_nine.config(command=lambda : click_button('9'))
button_zero.config(command=lambda : click_button('0'))
button_addition.config(command=lambda : click_button('+'))
button_subtraction.config(command=lambda : click_button('-'))
button_multiplication.config(command=lambda : click_button('*'))
button_division.config(command=lambda : click_button('/'))
button_dot.config(command=lambda : click_button('.'))
button_clear.config(command=clean)
button_back.config(command=back)
button_equal.config(command=calculation)


root.mainloop()
```
