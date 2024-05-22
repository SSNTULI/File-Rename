# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:12:10 2024

@author: 0154640
"""
import os
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

main_window = tk.Tk()

main_window.title('Rename Files')

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

main_window.geometry("%dx%d"%(screen_width*(1/3),screen_height*1/3))

main_window.resizable(0,0)

frm1 = tk.Frame(main_window,borderwidth=0,relief=tk.RAISED)
frm1.grid()

frm2 = tk.Frame(main_window,borderwidth=0,relief=tk.RAISED)
frm2.grid(row=0,column=1,rowspan=7)

file_var = tk.StringVar()
txt = ScrolledText(frm2,width=24,height=14,bg="black")
txt.grid(row=0,column=0,sticky="w"+"n",pady=20)


lbl1 = tk.Label(frm1,text="Insert file directory:")
lbl1.grid(padx=5,sticky='w')

txt1 = tk.Entry(frm1,width=40)
txt1.grid(padx=5,sticky='w')

lbl2 = tk.Label(frm1,text="Insert file name:")
lbl2.grid(padx=5,sticky='w')

txt2 = tk.Entry(frm1,width=40)
txt2.grid(padx=5,sticky='w')

file_name_label = tk.Label(frm1,text= "File format:")
file_name_label.grid(padx=5,sticky='w')

file_type_entrybox = tk.Entry(frm1,width=10)
file_type_entrybox.grid(padx=5,sticky='w')

perc = tk.StringVar()
lbl3 = tk.Label(frm1,textvariable=perc)
lbl3.grid(padx=5,sticky='w'+'s')
perc.set("......")


prog = tk.IntVar()
pb1 = ttk.Progressbar(frm1,length=244,variable=prog)
pb1.grid(padx=5,sticky='w')


def Cut_Paste_Files():
    
    folder = txt1.get()
    file_name = txt2.get()
    lbl3.configure(text="Loading")
    try:
        pb1.configure(maximum= float(len(os.listdir(folder))))
    except:
        txt.config(fg="red")
        txt.insert(tk.END,"Path Not found!!\n")

    fil_form = file_type_entrybox.get()

    if (len(fil_form)==0):
        txt.config(fg="red")
        txt.insert(tk.END,"Format Not Specified!!\n")
    else:
        txt.config(fg="white")

        txt.delete('1.0',tk.END)
   
        for count, filename in enumerate(os.listdir(folder)):
            btn.config(state='disabled')
            per = (round(count/(len(os.listdir(folder)))*100))
            perc.set(f"{per}%")
            prog.set(count)
            dst = f"{file_name}{str(count)}.{fil_form}"
            src =f"{folder}/{filename}"
            dst =f"{folder}/{dst}"
            os.rename(src, dst)
            txt.insert(tk.END,f"{dst}\n")
            main_window.after(200,main_window.update())     
        perc.set("Progess Complete")
        btn.config(state='normal')

btn =tk.Button(frm1,width=15,text='Execute',command=Cut_Paste_Files)
btn.grid(padx=5,pady=5,sticky='w')

main_window.mainloop()