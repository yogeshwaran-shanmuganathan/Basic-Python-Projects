# prerequisites
# pip install forex-python

import tkinter as tk
from tkinter import *
import tkinter.messagebox

root = tk.Tk()

root.title("GUI Currency Converter")

Tops = Frame(root, bg='black', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('Verdana', 20, 'bold'), text='Currency Converter',
                     bg='black', fg='white')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")


def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\nPlease enter a valid amount.")

    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\nPlease select 'FROM and TO Currency' from the menu.")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))


def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

# CURRENCY CODES:
#EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |
#GBP - United Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |
#HUF - Hungary Forint |RON - Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |
#SGD - Singapore Dollar |HKD - Hong Kong Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |
#KRW - Korea (South) Won |CNY - China Yuan Renminbi |TRY - Turkey Lira |HRK - Croatia Kuna |
#NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States Dollar |NOK - Norway Krone |
#RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic Koruna |
#BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand|

CurrenyCode_list = ["INR", "USD", "EUR", "GBP", "CAD", "AUD", "CHF", "JPY", "SGD",
                    "SEK", "HKD", "KRW", "HRK", "ZAR", "PHP", "HUF", "TRY", "NZD",
                    "NOK", "THB", "BRL", "RUB", "CNY", "ILS", "MXN", "BGN", "PLN",
                    "CZK", "RON", "MYR", "DKK", "IDR"]

root.configure(background='black')
root.geometry("700x400")

Label_1 = Label(root, font=('Verdana', 27, 'bold'), text="", padx=2, pady=2, bg="black", fg="white")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('Verdana', 15, 'bold'), text="Amount  :", bg="black", fg="white")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('Verdana', 15, 'bold'), text="From Currency  :", bg="black", fg="white")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('Verdana', 15, 'bold'), text="To Currency  :", bg="black", fg="white")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('Verdana', 15, 'bold'), text="Converted Amount  :", bg="black", fg="white")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('Verdana', 7, 'bold'), text="", padx=2, pady=2, bg="black", fg="white")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('Verdana', 7, 'bold'), text="", padx=2, pady=2, bg="black", fg="white")
Label_1.grid(row=7, column=0, sticky=W)

FromCurrency = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency.grid(row=3, column=1, ipadx=45, sticky=E)
ToCurrency.grid(row=4, column=1, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=1, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=1, ipadx=31, sticky=E)

Label_2 = Button(root, font=('arial', 15, 'bold'), text="Convert", padx=2, pady=2, bg="cyan3", fg="black",
                 command=RealTimeCurrencyConversion)
Label_2.grid(row=6, column=0)

Label_1 = Label(root, font=('Verdana', 7, 'bold'), text="", padx=2, pady=2, bg="black", fg="white")
Label_1.grid(row=9, column=0, sticky=W)

Label_2 = Button(root, font=('arial', 15, 'bold'), text="Clear All", padx=2, pady=2, bg="cyan3", fg="black",
                 command=clear_all)
Label_2.grid(row=10, column=0)

root.mainloop()