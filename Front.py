"""
GUI Of Book Store Data
Author : Ritesh Kumar
"""

from Back import Database
from tkinter import *
window=Tk()
window.wm_title("Book Store Data")

Backend=Database()

def view_command():
    list1.delete(0,END)
    for row in Backend.View():
        list1.insert(END,row)

def search_comand():
    list1.delete(0,END)
    for row in Backend.Search(title_text.get(),Author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_comand():
    Backend.Insert(title_text.get(),Author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),Author_text.get(),year_text.get(),isbn_text.get()))

def close_comand():
    return 0


def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])   
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])   
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])  
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])  
    
def delete_comand():
    Backend.Delete(selected_tuple[0])

def update_comand():
    Backend.Update(selected_tuple[0],title_text.get(),Author_text.get(),year_text.get(),isbn_text.get())


l1=Label(window,text="Title")
l1.grid(row=0,column=0)
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)
Author_text=StringVar()
e2=Entry(window,textvariable=Author_text)
e2.grid(row=0,column=3)
    
l3=Label(window,text="Year")    
l3.grid(row=1,column=0)    
year_text=StringVar()    
e3=Entry(window,textvariable=year_text)    
e3.grid(row=1,column=1)    
    
l4=Label(window,text="ISBN")    
l4.grid(row=1,column=2)    
isbn_text=StringVar()    
e4=Entry(window,textvariable=isbn_text)    
e4.grid(row=1,column=3)    
    
list1=Listbox(height=6,width=35)    
list1.grid(row=2,column=0,rowspan=6,columnspan=2)    
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_comand)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_comand)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_comand)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete_comand)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()