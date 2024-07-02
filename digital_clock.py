from tkinter import *
from datetime import datetime
from time import strftime

def time():
    a=strftime('%H : %M : %S')
    l1.config(text=c+'  '+a)
    l1.after(1000,time)



def labels():
    l3=Label(frame1,font=("technology",8),bg="#0e1013",fg="#7f7f7f", text='DAY')
    l3.place(x=135,y=130)

    l3=Label(frame1,font=("technology",8),bg="#0e1013",fg="#7f7f7f", text='HOURS')
    l3.place(x=310,y=130)

    l3=Label(frame1,font=("technology",8),bg="#0e1013",fg="#7f7f7f", text='MINUTES')
    l3.place(x=475,y=130)

    l3=Label(frame1,font=("technology",8),bg="#0e1013",fg="#7f7f7f", text='SECONDS')
    l3.place(x=665,y=130)


window=Tk()
window.title("Digital clock")
window.geometry('800x200+1100+50') #set size and position on the screen
frame1=Frame(window,width=800,height=200, bg="#0e1013")
frame1.place(x=0,y=0)

a=datetime.today().strftime("%A").upper()

c=a[0:3]
    
l1=Label(frame1,font=('technology',80),bg="#0e1013",foreground="#d3d3d3")
l1.place(x=75,y=35)
labels()
time()
window.mainloop()