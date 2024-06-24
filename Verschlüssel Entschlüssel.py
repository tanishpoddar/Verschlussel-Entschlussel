from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font
# Encoding Function
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) + ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
# Decoding Function
def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
        dec.append(list_dec)
    return "".join(dec)
# Show Message function
def Result():
    msg = Message.get()
    k = key.get()
    i = mode.get()
    if (i == 1):
        Output.set(encode(k, msg))
    elif(i == 2):
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo('Verschlüssel Entschlüssel', 'Please Choose one of Encryption or Decryption. Try again.')
# Reset function
def Reset():
    Message.set("")
    key.set("")
    mode.set(0)
    Output.set("")
#GUI APPLICATION
wn = Tk()
wn.geometry("1920x1000")
wn.configure(bg='#282a36')
wn.title("Verschlüssel Entschlüssel by Tanish Poddar")
Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()
headingLabel = Label(wn, text="Verschlüssel Entschlüssel", fg='#f8f8f2', font=('Matura MT Script Capitals', 40, 'bold'), bg='#282a36')
label0 = Label(wn, text="Made By: \n Tanish Poddar [RA2311003010959]", fg='#f8f8f2', font=('Times new roman', 13, 'bold'), bg='#282a36')
label0.place(x=500, y=120)
headingLabel.place(x=400, y=60)
label1 = Label(wn, text='Type Your Message: ', font=('Centaur', 13), bg='#282a36', fg='#f8f8f2')
label1.place(x=400, y=200)
msg = Entry(wn, textvariable=Message, width=28, font=('Centaur', 14, 'normal'), bg='#44475a', fg='#f8f8f2')
msg.place(x=570, y=200)
label2 = Label(wn, text='Enter The Key: ', font=('Centaur', 13), bg='#282a36', fg='#f8f8f2')
label2.place(x=400, y=250)
InpKey = Entry(wn, textvariable=key, width=35, font=('Centaur', 10, 'normal'), bg='#44475a', fg='#f8f8f2')
InpKey.place(x=570, y=250)
label3 = Label(wn, text='Check The Bullet What You Want - Encryption or Decryption?', font=('Helvetica', 15), bg='#282a36', fg='#f8f8f2')
label3.place(x=430, y=300)
Radiobutton(wn, text='Encryption!', variable=mode, value=1, bg='#282a36', fg='#f8f8f2').place(x=550, y=350)
Radiobutton(wn, text='Decryption!', variable=mode, value=2, bg='#282a36', fg='#f8f8f2').place(x=650, y=350)
label3 = Label(wn, text='Result: ', font=('Centaur', 13), bg='#282a36', fg='#f8f8f2')
label3.place(x=400, y=400)
res = Entry(wn, textvariable=Output, width=35, font=('Centaur', 10, 'normal'), bg='#44475a', fg='#f8f8f2')
res.place(x=570, y=400)
ShowBtn = Button(wn, text="Show Message!", bg='#50fa7b', fg='black', width=15, height=1, command=Result, font=('Helvetica', 12))
ShowBtn.place(x=700, y=450)
ResetBtn = Button(wn, text='Reset', bg='#ff79c6', fg='black', width=15, height=1, command=Reset, font=('Helvetica', 12))
label4 = Label(wn, text='Copyright 2023 -   ©️ Tanish Poddar \n Students of SRMIST, KTR Campus (Batch 2023-2027)', font=('Times new roman', 13), bg='#282a36', fg='#f8f8f2')
label4.place(x=550, y=600)
ResetBtn.place(x=550, y=450)
ResetBtn.place(x=550, y=450)
wn.mainloop()
