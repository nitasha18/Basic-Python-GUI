from tkinter import Tk,Entry,Button,INSERT,END,Label,StringVar
root=Tk()

# entry=Entry(root)
# entry.pack()

entry= Entry(root,font=inp_font)
entry.pack()

# entry.insert(INSERT,'Ready')
entry.insert(INSERT,' ')
    # Specifying character position in entry
    # - END: After last character of entry widget
    # - ANCHOR: The beginning of the current selection
    # - INSERT: Current text cursor position
    # - "@x": Mouse coordinates

def print_content():
    print(entry.get())
    entry.delete(0,END)

root.geometry("600x300+150+150")
button=Button(root,text='Submit',font=inp_font,command=print_content)
button.pack()

root.mainloop()