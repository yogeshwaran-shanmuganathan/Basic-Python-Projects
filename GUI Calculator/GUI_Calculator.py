### https://github.com/yogeshwaran-shanmuganathan ###

from tkinter import *
import math


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)


    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.basic_op()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def basic_op(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "subtract":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "powerof":
            self.total = self.total ** self.current
        if self.op == "rootof":
            self.total = self.total ** (1/self.current)
        if self.op == "factorial":
            self.total=int(text_box.get())
            self.total=math.factorial(self.total)
        if self.op == "ln":
            self.total = log(self.total)
        if self.op == "log":
            self.total = log(self.total,10)
        if self.op == "sin":
            self.total=math.sin(self.total)
        if self.op == "cos":
            self.total = math.cos(self.total)
        if self.op == "tan":
            self.total = math.tan(self.total)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "invert":
            self.total = 1/self.total
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.basic_op()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(calc, justify=RIGHT,width=30,font="Times 16 bold")
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "0")

numbers = "789456123"
i = 0
button = []
for j in range(1,4):
    for k in range(3):
        button.append(Button(calc,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
        button[i]["bg"]= "LightSkyBlue1"
        button[i].grid(row = j, column = k,padx=1,pady=1)
        button[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

zero_button = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0",bg="LightSkyBlue1")
zero_button["command"] = lambda: sum1.num_press(0)
zero_button.grid(row = 4, column = 0,  padx=1, pady = 1)

addition = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+",bg="cadet blue")
addition["command"] = lambda: sum1.operation("add")
addition.grid(row = 1, column = 3,  padx=1, pady = 1)

subtract = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-",bg="cadet blue")
subtract["command"] = lambda: sum1.operation("subtract")
subtract.grid(row = 2, column = 3, padx=1, pady = 1)

multiply = Button(calc,height =2,width=4,padx=10, pady = 10, text = "*",bg="cadet blue")
multiply["command"] = lambda: sum1.operation("multiply")
multiply.grid(row = 3, column = 3,  padx=1, pady = 1)

division = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/",bg="cadet blue")
division["command"] = lambda: sum1.operation("divide")
division.grid(row = 4, column = 3, padx=1, pady = 1)

powerof = Button(calc, height=2,width=4,padx=10,pady=10,text="x^y",bg="cyan3")
powerof["command"] = lambda: sum1.operation("powerof")
powerof.grid(row=2,column = 4,padx=1,pady=1)

rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="sqrt", bg = "cyan3")
rootof["command"] = lambda: sum1.operation("rootof")
rootof.grid(row=2, column=5, padx=1, pady=1)

factorial = Button(calc, height=2, width=4, padx=10, pady=10, text="fact !",bg="cyan3")
factorial["command"] = lambda: sum1.operation("factorial")
factorial.grid(row=5,column=0, padx=1, pady=1)

log = Button(calc, height=2, width=4, padx=10, pady=10, text="log",bg="cyan3")
log["command"] = lambda: sum1.operation("ln")
log.grid(row=3, column=5, padx=1, pady=1)

log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log10",bg="cyan3")
log10["command"]= lambda: sum1.operation("log")
log10.grid(row=5, column=1, padx=1 , pady=1)

sine = Button(calc, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "cyan3")
sine["command"]=lambda: sum1.operation("sin")
sine.grid(row=3,column=4,padx=1,pady=1)

cosine = Button(calc, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "cyan3")
cosine["command"]=lambda: sum1.operation("cos")
cosine.grid(row=4,column=4,padx=1,pady=1)

tan = Button(calc, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "cyan3")
tan["command"]=lambda: sum1.operation("tan")
tan.grid(row=5,column=4,padx=1,pady=1)

exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x', bg="cyan3")
exponent["command"]=lambda: sum1.operation("exp")
exponent.grid(row=5,column=3,padx=1,pady=1)

invert = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x", bg="cyan3")
invert["command"] = lambda: sum1.operation("invert")
invert.grid(row=5,column=2,padx=1,pady=1)

dec_point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".",bg="cadet blue")
dec_point["command"] = lambda: sum1.num_press(".")
dec_point.grid(row = 4, column = 1, padx=1, pady = 1)

sign = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="cadet blue")
sign["command"] = sum1.sign
sign.grid(row = 4, column = 2,  padx=1, pady = 1)

clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C",bg="midnight blue",fg="white")
clear["command"] = sum1.clear
clear.grid(row = 1, column = 4,  padx=1, pady = 1)

all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC",bg="midnight blue",fg="white")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 1, column = 5, padx=1, pady = 1)

equals = Button(calc,height =6,width=4,padx=10, pady = 10, text = "=",bg="RoyalBlue3")
equals["command"] = sum1.calc_total
equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)

root.mainloop()
