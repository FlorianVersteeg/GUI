from tkinter import *

def registreren():
    def Confirm():
        if len(phone.get()) is not 10 and len(password.get()) is not 4:
            tryagain = Label(master=subwindow, text='try again')
            tryagain.pack(pady=2)
            return tryagain
        else:
            #geef ID
            bedankt = Label(master=root, text='Bedankt voor registreren')
            bedankt.pack(pady=14)
            subwindow.withdraw()
    subwindow = Toplevel(master=root)
    label1 = Label(master=subwindow, text='Naam')
    label1.pack(pady=2)

    name = Entry(master=subwindow)
    name.pack(pady=2, padx=10)

    label2 = Label(master=subwindow, text='Telefoon nummer')
    label2.pack(pady=2)

    phone = Entry(master=subwindow)
    phone.pack(pady=2, padx=10)

    label3 = Label(master=subwindow, text='Wachtwoord')
    label3.pack(pady=2)

    password = Entry(master=subwindow)
    password.pack(pady=2, padx=10)

    button1 = Button(master=subwindow, text='Confirm', command=Confirm)
    button1.pack(pady=10, padx=10)

def login():
    def confirm():
        if len(password.get()) is not 4:
            wrong = Label(master=log, text='wrong entry')
            wrong.pack(pady=2)
        else:
            bedankt = Label(master=root, text='Bedankt voor gerbuik maken von onze fietsenstalling')
            bedankt.pack(pady=14)
            log.withdraw()
            def options():
                option.withdraw()

            option = Toplevel(master=root)
            close = Button(master=option, text='close', command=options, background='red', foreground='white')
            close.pack(side=BOTTOM, pady=4, padx=4)

            keuze= Label(master=option, text='Maak uw keuze',
                         background='yellow', foreground='blue',
                         font=('Helvetica', 16, 'bold'))
            keuze.pack(pady=5, fill=X)

            ophalen = Button(master=option, text='Ophalen',
                             background='blue', foreground='yellow',
                             font=('Helvetica', 16, 'bold'))
            ophalen.pack(pady=5, padx=10, side=LEFT)

            neerzetten = Button(master=option, text='Neerzetten',
                                background='blue', foreground='yellow',
                                font=('Helvetica', 16, 'bold'))
            neerzetten.pack(pady=5, padx=10, side=LEFT)

            informatie = Button(master=option, text='Informatie',
                                background='blue', foreground='yellow',
                                font=('Helvetica', 16, 'bold'))
            informatie.pack(pady=5, padx=10, side=LEFT)

    log = Toplevel(master=root)
    label2 = Label(master=log, text='Telefoon nummer')
    label2.pack(pady=2)

    phone = Entry(master=log)
    phone.pack(pady=2, padx=10)

    label3 = Label(master=log, text='Wachtwoord')
    label3.pack(pady=2)

    password = Entry(master=log)
    password.pack(pady=2, padx=10)

    button1 = Button(master=log, text='Confirm', command=confirm)
    button1.pack(pady=10, padx=10)

root = Tk()

welkom = Label(master=root, text='Welkom bij de fietsenstalling van NS',
               background='yellow', foreground='blue',
               font=('Helvetica', 16, 'bold'))
welkom.pack(pady=5, fill=X)

log_in = Button(master=root, text='Log in',
                background='blue', foreground='yellow',
                font=('Helvetica', 16, 'bold'), command=login)
log_in.pack(pady=5, padx=10, side=LEFT)

registreren = Button(master=root, text='Registreren',
                     background='blue', foreground='yellow',
                     font=('Helvetica', 16, 'bold'), command=registreren)
registreren.pack(pady=5, padx=10, side=RIGHT)

root.mainloop()
