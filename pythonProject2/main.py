from tkinter import *
root = Tk()
root.geometry("400x200")

Label(root, text="Python  Form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
payment = Label(root, text="payment")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
payment.grid(row=3, column=2)

namevalue = StringVar
phonevalue = StringVar
paymentvalue = StringVar
chekvalue = IntVar

nameentry =Entry(root, textvariable=namevalue)
phoneentry =Entry(root, textvariable=phonevalue)
paymenten =Entry(root, textvariable=paymentvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
paymenten.grid(row=3, column=3)



chekbtn = Checkbutton(text="Remember me?", variable = chekvalue)
chekbtn.grid(row=6, column=3)


def getvals():
    print("Accepted")


Button(text="Submit", command =getvals).grid(row=7, column=3)

root.mainloop()