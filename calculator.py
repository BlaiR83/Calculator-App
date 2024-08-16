import tkinter as tk

class number:
    '２項演習のモデル'
    
    #入力中の数字
    current = 0
    
    #第１項
    first = 0
    
    #第２項
    second = None
    
    #演算子
    op = None
    
#------関数------#

def calculate():
    if number.second != None:
        if number.op == 1:
            number.first += number.second
        elif number.op == 2:
            number.first -= number.second
        elif number.op == 3:
            number.first *= number.second
        else:
            number.first /= number.second
    number.current = 0
    number.second = None
    number.op = None
    show_number(number.first)
    
def key(n):
    number.current = number.current*10 + n
    if number.op == None:
        number.first = number.current
    else:
        number.second = number.current
    show_number(number.current)
    
def action(n):
    if n == 1: #足算
        calculate()
        number.op = 1
    elif n == 2: #引算
        calculate()
        number.op = 2
    elif n == 3: #乗算
        calculate()
        number.op = 3
    elif n == 4: #除算
        calculate()
        number.op = 4
    elif n == 5: #計算
        calculate()
    else: #クリア
        number.current = 0
        number.first = 0
        number.second = None
        number.op = None
        show_number(number.current)

def show_number(number):
    e.delete(0,tk.END)
    e.insert(0,str(number))

#------tkinterの画面構成------#

root = tk.Tk()
f = tk.Frame(root)
f.grid()

#------ウィジェットの作成------#

b1 = tk.Button(f, text='1', command=lambda: key(1))
b2 = tk.Button(f, text='2', command=lambda: key(2))
b3 = tk.Button(f, text='3', command=lambda: key(3))
b4 = tk.Button(f, text='4', command=lambda: key(4))
b5 = tk.Button(f, text='5', command=lambda: key(5))
b6 = tk.Button(f, text='6', command=lambda: key(6))
b7 = tk.Button(f, text='7', command=lambda: key(7))
b8 = tk.Button(f, text='8', command=lambda: key(8))
b9 = tk.Button(f, text='9', command=lambda: key(9))
b0 = tk.Button(f, text='0', command=lambda: key(0))
bp = tk.Button(f, text='+', command=lambda: action(1))
bm = tk.Button(f, text='-', command=lambda: action(2))
bx = tk.Button(f, text='*', command=lambda: action(3))
bd = tk.Button(f, text='/', command=lambda: action(4))
be = tk.Button(f, text='=', command=lambda: action(5))
bc = tk.Button(f, text='c', command=lambda: action(6))

#------Grid型によるウィジェットの割付------#

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
bc.grid(row=1, column=3)
bp.grid(row=2, column=3)
bm.grid(row=3, column=3)
bx.grid(row=2, column=4)
bd.grid(row=3, column=4)
be.grid(row=4, column=3)

#------数値を表示するウィジェット------#
e = tk.Entry(f)
e.grid(row=0, column=0, columnspan=4)

root.mainloop()