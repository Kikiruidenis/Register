from tkinter import Tk, StringVar,ttk
from tkinter import*
import time;
import datetime


root = Tk()
root.title("Attendance Register")
root.configure(background = "black")

#...........FRAMES.........

LeftMayFrame = Frame(root,width =1000, height =650, bd =8, relief ="raise")
LeftMayFrame.pack(side =LEFT)

RightMayFrame = Frame(root,width =350, height =650, bd =8, relief ="raise")
RightMayFrame.pack(side =RIGHT)



LeftMayFrame1 = Frame(LeftMayFrame,width =1000, height =100, bd =8, relief ="raise")
LeftMayFrame1.pack(side =TOP)
LeftMayFrame2 = Frame(LeftMayFrame,width =1000, height =550, bd =8, relief ="raise")
LeftMayFrame2.pack(side =TOP)



RightMayFrame1 = Frame(RightMayFrame,width =350, height =215, bd =8, relief ="raise")
RightMayFrame1.pack(side =TOP)
RightMayFrame2 = Frame(RightMayFrame,width =350, height =415, bd =8, relief ="raise")
RightMayFrame2.pack(side =TOP)


#...........VARIABLES........
DateofOrder =StringVar()
value0=StringVar()
value1=StringVar()
value2=StringVar()
value3=StringVar()
value4=StringVar()
value5=StringVar()
value6=StringVar()
value7=StringVar()
value8=StringVar()
value9=StringVar()
value10=StringVar()
value11=StringVar()
value12=StringVar()

def MarkRegister():
        value1.set("/")
        value2.set("/")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")
        value8.set("/")
        value9.set("/")
        value10.set("/")
        value11.set("/")
        value12.set("/")
        
       

def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12.set("")



#.............COMPONENTS.............

DateofOrder.set(time.strftime("%d/%m,%y"))


#.........LEFTMAYFRAME1 ROW 1..........
lblNo = Label(LeftMayFrame1,font =('ariel', 10, 'bold'), text ='No.', bd =16 )            
lblNo.grid(row=0,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame1,font =('ariel', 10, 'bold'), text ='Student No', bd =16 )  
lblStudentNo.grid(row=0,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame1,font =('ariel', 10, 'bold'), text ='Student Name', bd =16)   
lblStudentName.grid(row=0,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame1,font =('ariel', 10, 'bold'), text ='Course Code', bd =16)   
lblCourseCode.grid(row=0,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame1, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =0,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)



#.........LEFTMAYFRAME2 ROW 1..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1.', bd =16 )            
lblNo.grid(row=0,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1234', bd =16 )  
lblStudentNo.grid(row=0,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Victor Kamau', bd =16)   
lblStudentName.grid(row=0,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1070', bd =16)   
lblCourseCode.grid(row=0,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =0,column =4)






#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 2..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='2.', bd =16 )            
lblNo.grid(row=1,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='2134', bd =16 )  
lblStudentNo.grid(row=1,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Anthony Kameru', bd =16)   
lblStudentName.grid(row=1,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1102', bd =16)   
lblCourseCode.grid(row=1,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =1,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 3..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='3.', bd =16 )            
lblNo.grid(row=2,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='3114', bd =16 )  
lblStudentNo.grid(row=2,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Mercy Kerio', bd =16)   
lblStudentName.grid(row=2,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1122', bd =16)   
lblCourseCode.grid(row=2,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =2,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 4..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='4.', bd =16 )            
lblNo.grid(row=3,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='3421', bd =16 )  
lblStudentNo.grid(row=3,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Makau Mutua', bd =16)   
lblStudentName.grid(row=3,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1132', bd =16)   
lblCourseCode.grid(row=3,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =3,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 5..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='5.', bd =16 )            
lblNo.grid(row=4,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='2324', bd =16 )  
lblStudentNo.grid(row=4,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Denis Koech', bd =16)   
lblStudentName.grid(row=4,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1202', bd =16)   
lblCourseCode.grid(row=4,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =4,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 6..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='6.', bd =16 )            
lblNo.grid(row=5,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1154', bd =16 )  
lblStudentNo.grid(row=5,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Mary Kemto', bd =16)   
lblStudentName.grid(row=5,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='3212', bd =16)   
lblCourseCode.grid(row=5,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =5,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 2..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='7.', bd =16 )            
lblNo.grid(row=6,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='3124', bd =16 )  
lblStudentNo.grid(row=6,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Faith Gachie', bd =16)   
lblStudentName.grid(row=6,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='2011', bd =16)   
lblCourseCode.grid(row=6,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =6,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 2..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='8.', bd =16 )            
lblNo.grid(row=7,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='4311', bd =16 )  
lblStudentNo.grid(row=7,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Nahashon Kiarie', bd =16)   
lblStudentName.grid(row=7,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1222', bd =16)   
lblCourseCode.grid(row=7,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =7,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 2..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='9.', bd =16 )            
lblNo.grid(row=8,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='4323', bd =16 )  
lblStudentNo.grid(row=8,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='Daniel Ndambuki', bd =16)   
lblStudentName.grid(row=8,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1324', bd =16)   
lblCourseCode.grid(row=8,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =8,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)


#.........LEFTMAYFRAME2 ROW 2..........
lblNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='10.', bd =16 )            
lblNo.grid(row=9,column = 0, sticky =W)

lblStudentNo = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='1423', bd =16 )  
lblStudentNo.grid(row=9,column = 1, sticky =W)

lblStudentName = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='MArgrate Kamene', bd =16)   
lblStudentName.grid(row=9,column = 2, sticky =W)

lblCourseCode = Label(LeftMayFrame2,font =('ariel', 10, 'bold'), text ='2143', bd =16)   
lblCourseCode.grid(row=9,column = 3, sticky =W)


box = ttk.Combobox(LeftMayFrame2, textvariable =value0, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S',)
box.current(0)
box.grid (row =9,column =4)


#btnArrow = Buttom(LeftMayFrame1,text ='Fill', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =5)


#btnReset = Buttom(LeftMayFrame1,text ='Reset', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =6)


#btnExit = Buttom(LeftMayFrame1,text ='Exit', padx=2, pady=2, bd=2,fg='black',font=('ariel',10, 'bold'), width=12,height=1).grid(row=0,column =7)


#lblDateofOrder = Label(LeftMayFrame1,textVariable ='lblDateofOrder', padx=2, pady=2, bd=2,fg='black',bg='white',font=('ariel',10, 'bold'), 

#lblDateofOrder.grid(row=0,column =8,sticky)






root.mainloop()


