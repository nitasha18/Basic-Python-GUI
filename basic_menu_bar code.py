from tkinter import Tk,Menu
root=Tk()
menu_bar=Menu(root)
file_menu=Menu(root,tearoff=0)
# main_menu.add_command(label='Quit',command=root.destroy)
file_menu.add_command(label="Menu",command=root.destroy)
file_menu.add_command(label="Temp",command=root.destroy)
file_menu.add_command(label="Quit",command=root.destroy)

menu_bar.add_cascade(label='File',menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()