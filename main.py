from tkinter import *
from tkinter import ttk


root =Tk()
root.title('Emloyee Management System')
root.geometry('1366x768+0+0')
root.config(bg='#2c3e50')
root.state("zoomed")


name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

#entry frame
entry_frame =Frame(root,bg="#535c68")
entry_frame.pack(side=TOP,fill=X)
title =Label(entry_frame,text='Emloyee Mangemen System',font=('Calibari',20,'bold'),bg="#535c68",fg='white')
title.grid(columnspan=2,row=1,padx=10,pady=20)

lblname=Label(entry_frame,text="Name",bg="#535c68",fg='white',font=16)
lblname.grid(column=0,row=2,padx=10,pady=10,sticky="w")
txtname=Entry(entry_frame,textvariable=name,font=('calibri',16),width=28)
txtname.grid(column=1,row=2,padx=10,pady=10)

lblage=Label(entry_frame,text="Age",bg="#535c68",fg='white',font=16)
lblage.grid(column=2,row=2,padx=10,pady=10,sticky="w")
txtage=Entry(entry_frame,textvariable=age,font=('calibri',16),width=28)
txtage.grid(column=3,row=2,padx=10,pady=10)

lbldoj=Label(entry_frame,text="d.o.j",bg="#535c68",fg='white',font=16)
lbldoj.grid(column=0,row=3,padx=10,pady=10,sticky="w")
txtdoj=Entry(entry_frame,textvariable=doj,font=('calibri',16),width=28)
txtdoj.grid(column=1,row=3,padx=10,pady=10)

lblemail=Label(entry_frame,text="Email",bg="#535c68",fg='white',font=16)
lblemail.grid(column=2,row=3,padx=10,pady=10,sticky="w")
txtemail=Entry(entry_frame,textvariable=age,font=('calibri',16),width=28)
txtemail.grid(column=3,row=3,padx=10,pady=10)


lblgender=Label(entry_frame,text="Gender",bg="#535c68",fg='white',font=('calibri',16))
lblgender.grid(column=0,row=4,padx=10,pady=10,sticky='w')
combogender=ttk.Combobox(entry_frame,font=('calibri',16),textvariable=gender,width=24,state='readonly')
combogender['value']=('Male','Female')
combogender.grid(column=1,row=4,padx=10,sticky='w')

#table frame


root.mainloop()