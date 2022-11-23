from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import Place, ttk
import math

window = Tk()
window.title("Vector Operation") 
window.geometry('300x200')

#bikin frame
frame = ttk.Frame(window)
frame.pack(padx=20,pady=20,fill="x", expand = True)

#Nama Vektor A
vektor_A = Label(frame, text='Vektor A')
vektor_A.grid()
#Membuat frame untuk vektor pertama
komponen_i1 = Label(frame, text="i",anchor="e",width=1)
komponen_i1.grid(column=1, row=1)
i1 = Entry(frame,width=5)
i1.grid(column=0,row=1)

tambah1= Label(frame, text="+",anchor="e",width=1)
tambah1.grid (column=2,row=1)

komponen_j1 = Label(frame, text="j ",anchor="e",width=1)
komponen_j1.grid(column=4, row=1)
j1 = Entry(frame,width=5)
j1.grid(column=3,row=1)

tambah2= Label(frame, text="+",anchor="e",width=1)
tambah2.grid (column=5,row=1)

komponen_k1 = Label(frame, text="k ",anchor="e",width=1)
komponen_k1.grid(column=7, row=1)
k1 = Entry(frame,width=5)
k1.grid(column=6,row=1)

#Nama Vektor B
vektor_B = Label(frame, text='Vektor B')
vektor_B.grid(column=0,row=2)
#Membuat frame untuk vektor pertama
komponen_i2 = Label(frame, text="i",anchor="e",width=1)
komponen_i2.grid(column=1, row=3)
i2 = Entry(frame,width=5)
i2.grid(column=0,row=3)

tambah1= Label(frame, text="+",anchor="e",width=1)
tambah1.grid (column=2,row=3)

komponen_j2 = Label(frame, text="j",anchor="e",width=1)
komponen_j2.grid(column=4, row=3)
j2 = Entry(frame,width=5)
j2.grid(column=3,row=3)

tambah2= Label(frame, text="+",anchor="e",width=1)
tambah2.grid (column=5,row=3)

komponen_k2 = Label(frame, text="k",anchor="e",width=1)
komponen_k2.grid(column=7, row=3)
k2 = Entry(frame,width=5)
k2.grid(column=6,row=3)

#Dot Product = a.b = |a||b|cosθ
def modOfVektor():
    AxB=((float(i1.get())**2 + float(j1.get())**2 + float(k1.get())**2)**0.5)*(((float(i2.get())**2 + float(j2.get())**2 + float(k2.get())**2))**0.5)
    showinfo(title ="Sudut Antara", message= AxB)
    return AxB
    pass
def panjangA():
    A = float(i1.get()) + float(j1.get()) + float(k1.get())
    showinfo(title ="coba", message= panjangA) 
    return A
    pass
def cari_sudut():
    cos_theta = (float(i1.get())*float(i2.get()) + 
                float(k1.get())*float(k2.get()) + 
                float(j1.get())*float(j2.get()))/(((float(i1.get())**2 + float(j1.get())**2 + float(k1.get())**2)**0.5)*(((float(i2.get())**2 + float(j2.get())**2 + float(k2.get())**2))**0.5))
    sudut = math.acos(math.radians(cos_theta))
    showinfo(title ="Sudut Antara", message= sudut)
    return sudut 
    pass

def dot_product():
    hasil_dot = (float(i1.get())*float(i2.get()) + 
                float(k1.get())*float(k2.get()) + 
                float(j1.get())*int(j2.get())) 
    showinfo(title ="Hasil Dot Product", message= hasil_dot)

def cross_product():
    komponen_i = (float(j1.get())*float(k2.get()))-(float(j2.get())*float(k1.get()))
    komponen_j = -((float(i1.get())*float(k2.get()))-(float(i2.get())*float(k1.get())))
    komponen_k = (float(i1.get())*float(j2.get()))-(float(i2.get())*float(j1.get()))
    hasil_cross = (komponen_i,'i','+',komponen_j,'j','+',komponen_k,'k')
    showinfo(title ="Hasil Cross Product", message= hasil_cross)
   

# Membuat tombol Dot Product
tombol_dot = Button(window, text = "Dot Product", command = dot_product)
tombol_dot.pack(padx=5,pady=5,fill="x", expand = True)
tombol_cs = Button(window, text = "Cross Product", command = cross_product)
tombol_cs.pack(padx=6,pady=6,fill="x", expand = True)
window.mainloop()