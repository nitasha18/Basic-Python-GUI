from tkinter import Tk,Button,Label
root=Tk()

#exit button which will leave the main window when called
exit_button=Button(root,text='Exit Window',command=root.destroy)
exit_button.pack()

# label=Label(root,text='Click me!')
# label.pack()

def call_back():
    text=Label(root,text="Button Clicked")  #print('Clicked')
    text.pack()

print_button=Button(root,text='Click',command=call_back)
print_button.pack()

# label.bind("<Button-1>",lambda e:call_back())

root.mainloop()