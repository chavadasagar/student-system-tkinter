from ast import Global
from cProfile import label
from distutils import command
from email.mime import message
from msilib.schema import ListView
from re import search
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from turtle import color, left, update, width
import com.dao.UserDao as user



def updatestd():
    global updatestd
    updatestd = Toplevel(add)
    updatestd.title("update student")
    updatestd.geometry("400x400")
    
    Label(updatestd,text="update Student",bg="gray",font="arial 20",width="300").pack()
    
    Label(updatestd,text="").pack()

    global sid,name,address,ct,course
    
    sid = StringVar(updatestd)
    name = StringVar(updatestd)
    address = StringVar(updatestd)
   

    
    def getstd():
        data = user.getUser(sid.get())
        name.set(data[0][1])
        address.set(data[0][2])
        click.set(data[0][3])
        if data[0][4] == "bca":
            listbox.selection_set(0)
        else:
            listbox.selection_set(1)
            
        
        
    
    Label(updatestd,text="",width="300",font="arial ").pack()
    Label(updatestd,text="id :",font="arial 10").pack()
    Entry(updatestd,font="arial 10",textvariable=sid).pack()
    Button(updatestd,font="arial 10",text="fetch data",command=getstd).pack()
    
    Label(updatestd,text="name :",font="arial 10").pack()
    Entry(updatestd,font="arial 10",textvariable=name).pack()
    
    
    Label(updatestd,text="address :",font="arial 10").pack()
    Entry(updatestd,font="arial 10",textvariable=address).pack()

    
    ct = ["junagadh","rajkot","bhavanagar"]
    global click
    click = StringVar(updatestd)
    click.set("select your ct")
    Label(updatestd,text="City :",font="arial 10").pack()
    opm = OptionMenu(updatestd,click,*ct).pack()
    
    Label(updatestd,text="Course :",font="arial 10").pack()
    listbox = Listbox(updatestd,height=4)
    listbox.insert(1,"bca")
    listbox.insert(2,"bscit")
    listbox.pack()    
    
    Label(updatestd,text="").pack()
    
    def update():
        user.createTable()
        user.updateUser(sid.get(),name.get(),address.get(),click.get(),listbox.selection_get())            
        messagebox.showinfo(updatestd,"update successfuly!!!")
    Button(updatestd,text="update student",command=update).pack()
    
    
    updatestd.mainloop()   
    
def showall():
    global fetch
    fetch = Toplevel(add)
    fetch.title("show student")
    fetch.geometry("400x400")
    
    # title 
    Label(fetch,text="Students",bg="gray",font="arial 20",width="300").pack()
    Label(fetch,text="").pack()
    
    
    
    
    def searchuser():
        data = user.search(search.get())
        for std in data:
            Label(fetch,text=std,font="arial 10").pack()
            def delthisuser():
                
                confirm = messagebox.askokcancel(fetch,"confirm delete this record ?")
                if(confirm):
                    user.deleteUser(str(std[0]))
                    messagebox.showinfo(fetch,"delete record successfuly!!!")
                else:
                    messagebox.showinfo(fetch,"operation is cancal")
                # messagebox.showinfo(fetch,)
            Button(fetch,text="delete",command=delthisuser).pack()
        
        
    global search
    search = StringVar(fetch)
    Entry(fetch,textvariable=search,font="arial 10").pack()    
    Button(fetch,text="search",command=searchuser).pack()
    
    Label(fetch,text="").pack()
    
   
    fetch.mainloop()


def addstd():
    global add
    add = tk.Tk("add")
    add.geometry("300x400")
    add.title("add student")
    
    global name,address,ct,course
    
    name = StringVar(add)
    address = StringVar(add)
    
    Label(add,text="Add student",width="300",bg="gray",font="arial 20").pack()
    Label(add,text="",width="300",font="arial ").pack()
    Label(add,text="Student Name :",font="arial 10").pack();
    Entry(add,font="arial 10",textvariable=name).pack();
    
    Label(add,text="Address :",font="arial 10").pack()
    Entry(add,font="arial 10",textvariable=address).pack()
    
    
    ct = ["junagadh","rajkot","bhavanagar"]
    global click
    click = StringVar()
    click.set("select your ct")
    Label(add,text="City :",font="arial 10").pack()
    opm = OptionMenu(add,click,*ct).pack()
    
    Label(add,text="Course :",font="arial 10").pack()
    listbox = Listbox(add,height=4)
    listbox.insert(1,"bca")
    listbox.insert(2,"bscit")
    listbox.pack()    
    
    def showmsg():
        user.createTable()
        user.saveUser(name.get(),address.get(),click.get(),listbox.selection_get())
        # messagebox.showinfo(add,listbox.selection_get())
        messagebox.showinfo(add,"student add successfuly!!!")
    
    
    Button(add,text="Add",width="20",font="arial 10",command=showmsg).pack()
    Button(add,text="Update",width="20",font="arial 10",command=updatestd).pack()
    Button(add,text="show all",width="20",font="arial 10",command=showall).pack()
    
    
    
    add.mainloop()
    
addstd()