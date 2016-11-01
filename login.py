from tkinter import *

def registreren():
    def Confirm():
        if len(phone.get()) is not 10 and len(password.get()) is not 4:
            tryagain = Label(master=root, text='try again')
            tryagain.pack(side=BOTTOM, pady=2)
            return tryagain

    label1 = Label(master=root, text='Naam')
    label1.pack(pady=2)

    name = Entry(master=root)
    name.pack(pady=2, padx=10)

    label2 = Label(master=root, text='Telefoon nummer')
    label2.pack(pady=2)

    phone = Entry(master=root)
    phone.pack(pady=2, padx=10)

    label3 = Label(master=root, text='Wachtwoord')
    label3.pack(pady=2)

    password = Entry(master=root)
    password.pack(pady=2, padx=10)

    button1 = Button(master=root, text='Confirm', command=Confirm)
    button1.pack(pady=10, padx=10)

root = Tk()

welkom = Label(master=root, text='Welkom bij de fietsenstalling van NS',
               background='yellow', foreground='blue',
               font=('Helvetica', 16, 'bold'))
welkom.pack(pady=5, fill=X)

log_in = Button(master=root, text='Log in',
                background='blue', foreground='yellow',
                font=('Helvetica', 16, 'bold'))
log_in.pack(pady=5, padx=10, side=LEFT)

registreren = Button(master=root, text='Registreren',
                     background='blue', foreground='yellow',
                     font=('Helvetica', 16, 'bold'), command=registreren)
registreren.pack(pady=5, padx=10, side=RIGHT)

root.mainloop()
