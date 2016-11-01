from tkinter import *

root = Tk()

button1 = Button(master=root, text='1', width=5)
button1.grid(row=0, column=0, pady=2, padx=2)

button2 = Button(master=root, text='2', width=5)
button2.grid(row=0, column=1, pady=2, padx=2)

button3 = Button(master=root, text='3', width=5)
button3.grid(row=0, column=2, pady=2, padx=2)

button4 = Button(master=root, text='4', width=5)
button4.grid(row=1, column=0, pady=2, padx=2)

button5 = Button(master=root, text='5', width=5)
button5.grid(row=1, column=1, pady=2, padx=2)

button6 = Button(master=root, text='6', width=5)
button6.grid(row=1, column=2, pady=2, padx=2)

button7 = Button(master=root, text='7', width=5)
button7.grid(row=2, column=0, pady=2, padx=2)

button8 = Button(master=root, text='8', width=5)
button8.grid(row=2, column=1, pady=2, padx=2)

button9 = Button(master=root, text='9', width=5)
button9.grid(row=2, column=2, pady=2, padx=2)

button0 = Button(master=root, text='0', width=5)
button0.grid(row=3, column=1, pady=2, padx=2)

root.mainloop()

print(code)
