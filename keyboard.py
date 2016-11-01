from tkinter import *

keyboard = Tk()

q = Button(master=keyboard, text='q', width=2)
q.grid(row=0, column=0, pady=1, padx=1)

w = Button(master=keyboard, text='w', width=2)
w.grid(row=0, column=1, pady=1, padx=1)

e = Button(master=keyboard, text='e', width=2)
e.grid(row=0, column=2, pady=1, padx=1)

r = Button(master=keyboard, text='r', width=2)
r.grid(row=0, column=3, pady=1, padx=1)

t = Button(master=keyboard, text='t', width=2)
t.grid(row=0, column=4, pady=1, padx=1)

y = Button(master=keyboard, text='y', width=2)
y.grid(row=0, column=5, pady=1, padx=1)

u = Button(master=keyboard, text='u', width=2)
u.grid(row=0, column=6, pady=1, padx=1)

i = Button(master=keyboard, text='i', width=2)
i.grid(row=0, column=7, pady=1, padx=1)

o = Button(master=keyboard, text='o', width=2)
o.grid(row=0, column=8, pady=1, padx=1)

p = Button(master=keyboard, text='p', width=2)
p.grid(row=0, column=9, pady=1, padx=1)

backspace = Button(master=keyboard, text='backspace', width=8)
backspace.grid(row=0, column=10, pady=1, padx=1)

enter = Button(master=keyboard, text='Enter', width=8)
enter.grid(row=1, column=10, pady=1, padx=1)

shift = Button(master=keyboard, text='Shift', width=8)
shift.grid(row=2, column=10, pady=1, padx=1)

a = Button(master=keyboard, text='a', width=2)
a.grid(row=1, column=0, pady=1, padx=1)

s = Button(master=keyboard, text='s', width=2)
s.grid(row=1, column=1, pady=1, padx=1)

d = Button(master=keyboard, text='d', width=2)
d.grid(row=1, column=2, pady=1, padx=1)

f = Button(master=keyboard, text='f', width=2)
f.grid(row=1, column=3, pady=1, padx=1)

g = Button(master=keyboard, text='g', width=2)
g.grid(row=1, column=4, pady=1, padx=1)

h = Button(master=keyboard, text='h', width=2)
h.grid(row=1, column=5, pady=1, padx=1)

j = Button(master=keyboard, text='j', width=2)
j.grid(row=1, column=6, pady=1, padx=1)

k = Button(master=keyboard, text='k', width=2)
k.grid(row=1, column=7, pady=1, padx=1)

l = Button(master=keyboard, text='l', width=2)
l.grid(row=1, column=8, pady=1, padx=1)

z = Button(master=keyboard, text='z', width=2)
z.grid(row=2, column=1, pady=1, padx=1)

x = Button(master=keyboard, text='x', width=2)
x.grid(row=2, column=2, pady=1, padx=1)

c = Button(master=keyboard, text='c', width=2)
c.grid(row=2, column=3, pady=1, padx=1)

v = Button(master=keyboard, text='v', width=2)
v.grid(row=2, column=4, pady=1, padx=1)

b = Button(master=keyboard, text='b', width=2)
b.grid(row=2, column=5, pady=1, padx=1)

n = Button(master=keyboard, text='n', width=2)
n.grid(row=2, column=6, pady=1, padx=1)

m = Button(master=keyboard, text='m', width=2)
m.grid(row=2, column=7, pady=1, padx=1)

keyboard.mainloop()
