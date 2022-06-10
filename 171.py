from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time
root=Tk()
root.title("World Clocks Using Polymorphism")
root.geometry("600x450")
root.configure(background="white")
label_usa=Label(root,text="U.S.A")
label_usa.place(relx=0.2,rely=0.05,anchor=CENTER)
label_india=Label(root,text="INDIA")
label_india.place(relx=0.7,rely=0.05,anchor=CENTER)

clock_img=ImageTk.PhotoImage(Image.open("clock.jpg"))
label_usa_img=Label(root,image=clock_img)
label_usa_img.place(relx=0.2,rely=0.35,anchor=CENTER)

label_india_img=Label(root,image=clock_img)
label_india_img.place(relx=0.7,rely=0.35,anchor=CENTER)

label_usa_time=Label(root)
label_usa_time.place(relx=0.2,rely=0.75,anchor=CENTER)
label_india_time=Label(root)
label_india_time.place(relx=0.7,rely=0.75,anchor=CENTER)


class USA():
    def times(self):
        home=pytz.timezone("US/Central")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        label_usa_time['text']="Time :"+current_time
        label_usa_time.after(200,self.times)
        
class India():
    def times(self):
        home=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        label_india_time['text']="Time :"+current_time
        label_india_time.after(200,self.times)

obj_india=India()
obj_usa=USA()
btn_usa=Button(root,text="Show Time",command=obj_usa.times)
btn_usa.place(relx=0.2,rely=0.85,anchor=CENTER)
btn_india=Button(root,text="Show Time",command=obj_india.times)
btn_india.place(relx=0.7,rely=0.85,anchor=CENTER)
root.mainloop()

