import tkinter as tk

#Q1
def change_label():
    return label.config(text='Button Clicked')
window = tk.Tk()
window.geometry('400x300')
window.title('My App')
label = tk.Label(window, text='Welcome to tkinter')
label.pack()
button = tk.Button(window, text='Button', command= change_label)
button.pack()
window.mainloop()

#Q2
"""
a.
    A window titled "Text Changer", with a text "Öriginal Text" and a button

b.
    After click the button, the text change to "Text changed!"

c.
    Add a new function to change the title and add that function into button
"""

#Q3
"""
a.
    Label1 (red)
    Label2 (green)
    label3 (blue)

b.
    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)
    label3.grid(row=1, column=0)
"""

#Q4
"""
a.
    No label has exist

b.
    after window, write a label and pack it
"""