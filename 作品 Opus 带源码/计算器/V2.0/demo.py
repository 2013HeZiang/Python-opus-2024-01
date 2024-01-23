import tkinter as tk
from tkinter import ttk

y = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
n = ['+', '-', '*', '/', '.']

root = tk.Tk()
root.title('计算机 V2.0')
root.geometry('300x240+500+200')
font = ('宋体', 20)
font_16 = ('宋体', 16)

root.attributes('-alpha', 0.9)
root['background'] = '#ffffff'

result_num = tk.StringVar()
result_num.set('0')

ttk.Entry(root, textvariable=result_num, font=font, width=20, justify=tk.RIGHT).grid(row=2, column=1, columnspan=4)

button_clear = tk.Button(root, text='C', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_back = tk.Button(root, text='←', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_division = tk.Button(root, text='÷', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_multiplication = tk.Button(root, text='×', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_clear.grid(row=3, column=1, padx=4, pady=2)
button_back.grid(row=3, column=2, padx=4, pady=2)
button_division.grid(row=3, column=3, padx=4, pady=2)
button_multiplication.grid(row=3, column=4, padx=4, pady=2)

button_seven = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_eight = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_nine = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_subtraction = tk.Button(root, text='﹣', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_seven.grid(row=4, column=1, padx=4, pady=2)
button_eight.grid(row=4, column=2, padx=4, pady=2)
button_nine.grid(row=4, column=3, padx=4, pady=2)
button_subtraction.grid(row=4, column=4, padx=4, pady=2)

button_four = tk.Button(root, text='4', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_five = tk.Button(root, text='5', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_six = tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_addition = tk.Button(root, text='+', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_four.grid(row=5, column=1, padx=4, pady=2)
button_five.grid(row=5, column=2, padx=4, pady=2)
button_six.grid(row=5, column=3, padx=4, pady=2)
button_addition.grid(row=5, column=4, padx=4, pady=2)

button_one = tk.Button(root, text='1', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_two = tk.Button(root, text='2', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_three = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_equal = tk.Button(root, text='=', width=5, font=font_16, height=3, relief=tk.FLAT, bg='#b1b2b2')
button_one.grid(row=6, column=1, padx=4, pady=2)
button_two.grid(row=6, column=2, padx=4, pady=2)
button_three.grid(row=6, column=3, padx=4, pady=2)
button_equal.grid(row=6, column=4, padx=4, pady=2, rowspan=2)

button_zero = tk.Button(root, text='0', width=12, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_dot = tk.Button(root, text='.', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_zero.grid(row=7, column=1, padx=4, pady=2, columnspan=2)
button_dot.grid(row=7, column=3, padx=4, pady=2)


# 点击事件
def click_button(x):
    # print('x:\t', x)
    if x in y:
        if result_num.get() == '0':
            result_num.set('')
    result_num.set(result_num.get() + x)

def calculation():
    opt_str_0 = result_num.get()
    opt_str = ''
    for i in opt_str_0:
        if i == 'x' or i == 'X' or i == '×' or i == '*':
            opt_str = opt_str + '*'
        elif i == '/' or i == '%' or i == '÷':
            opt_str = opt_str + '/'
        elif i != '=':
            opt_str = opt_str + i
    try:
        result = eval(opt_str)
        result_num.set(str(result))
    except:
        result_num.set('错误')
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
button_multiplication.config(command=lambda : click_button('×'))
button_division.config(command=lambda : click_button('÷'))
button_dot.config(command=lambda : click_button('.'))
button_clear.config(command=clean)
button_back.config(command=back)

button_equal.config(command=calculation)


root.mainloop()
