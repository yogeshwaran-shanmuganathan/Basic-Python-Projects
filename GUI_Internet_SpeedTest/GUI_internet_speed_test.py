import tkinter as tk
import speedtest
from tkinter import messagebox

st = speedtest.Speedtest()
root = tk.Tk()
root.geometry("400x400")
root.title("Internet Speed test")
root.configure(bg="black")
font=("Verdana", 15, "bold")

def check():
    messagebox.showinfo("Testing your Internet speed!!!", "It may take a while to complete.")
    d.configure(text=str(st.download()//10**6)+" Mbps")
    u.configure(text=str(st.upload()//10**6)+" Mbps")
    p.configure(text=str(int(st.results.ping))+" Ms")
    l.configure(text="Internet Speed test completed!")

dspeed = tk.Label(root,text="Download Speed: ", bg="black",fg="cyan3",font=font)
dspeed.place(x=10,y=10)
d = tk.Label(root,text="0 Mbps", bg="black",fg="cyan3",font=font)
d.place(x=250,y=10)
uspeed = tk.Label(root,text="Upload Speed: ", bg="black",fg="cyan3",font=font)
uspeed.place(x=10,y=50)
u = tk.Label(root,text="0 Mbps", bg="black",fg="cyan3",font=font)
u.place(x=250,y=50)
ping = tk.Label(root,text="Ping: ", bg="black",fg="cyan3",font=font)
ping.place(x=10,y=90)
p = tk.Label(root,text="0 Ms", bg="black",fg="cyan3",font=font)
p.place(x=250,y=90)

l = tk.Label(root,text="Click here to start Internet Speed Test", bg="black",fg="cyan3",font=(15))
l.place(x=50,y=250)
b = tk.Button(root,text="Test Internet Speed", command=check, bg="cyan3",fg="black")
b.place(x=50,y=300,height=40,width=300)
root.mainloop()
