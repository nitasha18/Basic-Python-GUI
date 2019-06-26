from tkinter import messagebox
dialog_title='Attention'
dialog_text='Do you wanna exit?'
answer=messagebox.askquestion(dialog_title,dialog_text)

if answer=='yes':
else:
    print('Staying')