import sys
import tkinter
from tkinter import Tk,PhotoImage,Label,Message,Y,RIGHT,StringVar
print(tkinter.TkVersion)    #version of tkinter
root=Tk()
#root.mainloop()             #minimal program
#root.iconphoto(root,PhotoImage(file=sys.argv[1]))  #set icon
# root.title("Tkinter Test")      #set title

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
print("Screen width:",screen_width)
print("Screen height:",screen_height)

# root.attributes('-topmost',True)    #-fullscreen,

root.geometry("400x200+500+300")       #to set the size of the screen
text=Label(root,
           text="First texts!\n",
           bd=1,    #border
           relief="solid",
           font='Times 30',
           width=15,
           height=4,
           anchor=N)    #bydefault is in center
text.pack()
# text.pack_forget()


# msg=Message(root,text="Font changing!")
# msg.config(font=('times',28,'italic bold underline'))   #chaing font style
# msg.pack()

# label1=Label(root,text='first',background='yellow')
# label2=Label(root,text='Second',background='orange')
# label1.pack(fill=Y, padx=30,ipady=15, side=RIGHT)
# label2.pack(fill=Y, padx=30,ipady=15, side=RIGHT)
    #note:
    # fill: tells the widget to expand to take up any space (X,Y or BOTH)
    # padx/pady:outer padding
    # ipadx/ipady:inner padding
    # side: which side to stack from. Default is TOP(to botton)

###Label apperaing for only a period of time
def hide():
    label.pack_forget()
v=StringVar()
label=Label(root,textvariable=v)
v.set('some text/ variable')
label.pack()

root.after(5000,hide)
root.mainloop()
