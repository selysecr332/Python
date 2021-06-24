from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime

import self as self
#from Tools.scripts.make_ctype import values


class Rental_Inventory:

    def __init__(self, root):
        self.root = root
        self.root.title("real estate company")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')

        # ========================================================Frame=======================================

        MainFrame = Frame(self.root, bd=20, width=1350, height=700, bg="black", relief=RIDGE)
        MainFrame.grid()

        LeftFrame = Frame(MainFrame, bd=10, width=750, height=600, bg="black", relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(MainFrame, bd=10, width=560, height=600, bg="black", relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        # ========================================================Div_Frame====================================

        LeftFrame0 = Frame(LeftFrame, bd=5, width=712, height=143, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame0.grid(row=0, column=0)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=712, height=170, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame1.grid(row=1, column=0)
        LeftFrame2 = Frame(LeftFrame, bd=5, width=712, height=168, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame2.grid(row=2, column=0)
        LeftFrame3 = Frame(LeftFrame, bd=5, width=712, height=95, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame3.grid(row=3, column=0)

        RightFrame0 = Frame(RightFrame, bd=5, width=522, height=200, padx=5, bg="gainsboro", relief=RIDGE)
        RightFrame0.grid(row=0, column=0)
        RightFrame1 = Frame(RightFrame, bd=5, width=522, height=280, padx=5, bg="gainsboro", relief=RIDGE)
        RightFrame1.grid(row=1, column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=522, height=95, padx=0, bg="gainsboro", relief=RIDGE)
        RightFrame2.grid(row=2, column=0)





# ========================================================variable===================================================

        AcctOpen = StringVar()
        AppData = StringVar()
        NextCreditReview = StringVar()
        LastCreditReview = StringVar()
        DateRev = StringVar()
        ProdCode = StringVar()
        ProdType = StringVar()
        NoDays = StringVar()
        CostPDay = StringVar()
        CreLimit = StringVar()
        CreCheck = StringVar()

        SettDueDay = StringVar()
        PaymentD = StringVar()
        Discount = StringVar()
        Deposit = StringVar()
        PayDueDay = StringVar()
        PaymetM = StringVar()

        Var1 = IntVar()
        Var2 = IntVar()
        Var3 = IntVar()
        Var4 = IntVar()

        Tex = StringVar()
        SubTotal = StringVar()
        Total = StringVar()
        Receipt_Ref = StringVar()

        #الداله المسوالة عن الخروج من البرنامج

        def iExit():
            iExit = tkinter.messagebox.askyesno("property rental system", "Confirm if you want to Exit")
            if iExit > 0:
                root.destroy()
                return

        #هنعمل دالة لاعادة الاعدادات

        def Reset():
            self.txtInfo0.delete("1.0", END)
            self.txtInfo1.delete("1.0", END)
            self.txtInfo2.delete("1.0", END)
            self.txtInfo3.delete("1.0", END)
            self.txtReceipt.delete("1.0", END)

            AcctOpen.set("")
            AppData.set("")
            NextCreditReview.set("")
            LastCreditReview.set("")
            DateRev.set("")
            ProdCode.set("")
            ProdType.set("")
            NoDays.set("")
            CostPDay.set("")
            CreLimit.set("")
            CreCheck.set("")
            SettDueDay.set("")
            PaymentD.set("")
            Discount.set("")
            Deposit.set("")
            PayDueDay.set("")
            PaymetM.set("")
            Var1.set(0)
            Var2.set(0)
            Var3.set(0)
            Var4.set(0)
            Tex.set("")
            SubTotal.set("")
            Total.set("")
            return

        def  checkCredit():
            if(Var1.get() == 1):
                self.txtInfo0.insert(END, "Customer Check Credit Approved")
            elif(Var1.get() == 0):
                self.txtInfo0.insert("1.0", END)



        def  TermAgreed():
            if(Var2.get() == 1):
                self.txtInfo1.insert(END, "Term Agreed")
            elif(Var2.get() == 0):
                self.txtInfo1.insert("1.0", END)


        def  AcctOnHold():
            if(Var3.get() == 1):
                self.txtInfo2.insert(END, "Customer Account on Hold")
            elif(Var3.get() == 0):
                self.txtInfo2.insert("1.0", END)



        def  RestrictedMails():
            if(Var4.get() == 1):
                self.txtInfo3.insert(END, " Restricted Mails for customer ")
            elif(Var4.get() == 0):
                self.txtInfo3.insert("1.0", END)


        def Product(evt):
            value =str(self.cboProdType.get())
            pType = value
            if pType =="Flat":
                ProdCode.set("Flat_N342")
                CostPDay.set("30$")
                CreCheck.set("yes")
                SettDueDay.set("20")
                PaymentD.set("Yes")
                Deposit.set("NO")
                PaymetM.set("Master Card")

                n = float(LastCreditReview.get())
                s = float(SettDueDay.get())
                Price =(n * s)
                TC="$", str('%.2f'%(Price))
                PayDueDay.set(TC)

            elif pType =="A house":
                ProdCode.set("A house N 1230")
                CostPDay.set("50$")
                CreCheck.set("No")
                SettDueDay.set("15")
                PaymentD.set("No")
                Deposit.set("Yes")
                PaymetM.set("Vis Card")

                n = float(LastCreditReview.get())
                s = float(SettDueDay.get())
                Price =(n * s)
                TC="$", str('%.2f'%(Price))
                PayDueDay.set(TC)


            elif pType =="villa":
                ProdCode.set("villa 3214")
                CostPDay.set("12$")
                CreCheck.set("No")
                SettDueDay.set("12")
                PaymentD.set("No")
                Deposit.set("NO")
                PaymetM.set("Cash")

                n = float(LastCreditReview.get())
                s = float(SettDueDay.get())
                Price =(n * s)
                TC="$", str('%.2f'%(Price))
                PayDueDay.set(TC)


        def iDates(evt):
            valuess = str(self.cboNoDays.get())
            NDays = valuess
            if NDays == "100m-150m":
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=30)
                d3 = (d1 + d2)
                AppData.set(d1)
                NextCreditReview.set(d3)
                LastCreditReview.set(30)
                DateRev.set(d3)

                CreLimit.set("150$")
                Discount.set("5%")
                AcctOpen.set("Yes")

            elif NDays == "150m-300m":
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=30)
                d3 = (d1 + d2)
                AppData.set(d1)
                NextCreditReview.set(d3)
                LastCreditReview.set(30)
                DateRev.set(d3)

                CreLimit.set("150$")
                Discount.set("15%")
                AcctOpen.set("Yes")

            elif NDays == "300m-1000m":
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=30)
                d3 = (d1 + d2)
                AppData.set(d1)
                NextCreditReview.set(d3)
                LastCreditReview.set(30)
                DateRev.set(d3)

                CreLimit.set("1500$")
                Discount.set("50%")
                AcctOpen.set("Yes")

            elif(NDays == ""):
                messagebox.showinfo("Zero selected","You choosed Nothing?")
                Reset()

        def TotalCost():
            n = float(LastCreditReview.get())
            s = float(SettDueDay.get())

            Price = (n * s)

            ST = "$", str('%.2f' % (Price))
            iTex = "$", str('%.2f' % ((Price) * 0.15))
            Tex.Set(iTex)
            SubTotal.set(ST)

            TC = "$", str('%.2f' % (((Price) * 0.15) + Price))
            Total.set(TC)

            self.txtReceipt.delete("1.0", END)
            x = random.randint(10908, 500876)
            randomRef = str(x)
            Receipt_Ref.set("BILL" + randomRef)



            self.txtReceipt.insert(END, 'Receipt_Ref:\t\t\t\t' + Receipt_Ref.get()+'\t\t\t'+AppData.get()+"n")
            self.txtReceipt.insert(END, 'Product Type:\t\t\t\t' + ProdType.get()+"\n")
            self.txtReceipt.insert(END, 'Product Code:\t\t\t\t' +ProdCode.get() + "\n")
            self.txtReceipt.insert(END, 'No of Days:\t\t\t\t'+ NoDays.get()+ "\n")
            self.txtReceipt.insert(END, 'Account Open:\t\t\t\t'+ AcctOpen.get()+ "\n")

            self.txtReceipt.insert(END, 'NextCreditReview:\t\t\t\t' + NextCreditReview.get()+ "\n")
            self.txtReceipt.insert(END, 'LastCreditReview:\t\t\t\t' + LastCreditReview.get()+ "\n")
            self.txtReceipt.insert(END, '\nTax:\t\t\t\t' + Tex.get() + "\n")
            self.txtReceipt.insert(END,'\nSubtotal:\t\t\t\t' + str(SubTotal.get())+"\n" )
            self.txtReceipt.insert(END, '\n Total Cost:\t\t\t\t' + str(Total.get()))








# ========================================================RightFrame0===================================================#
        self.lblAcctOpen= Label(RightFrame0, font=('arial', 18, 'bold'), text="Account Opend: ", padx =2, pady =2, bg= "gainsboro")
        self.lblAcctOpen.grid(row=0, column=0, sticky=W)
        self.cboAcctOpen=ttk.Combobox(RightFrame0, textvariable=AcctOpen, state='readonly',
                                      font=('arial', 18, 'bold'), width=19)
        self.cboAcctOpen['value']=('', 'Select An Option', 'Yes', 'No')
        self.cboAcctOpen.current(0)
        self.cboAcctOpen.grid(row=0, column=1, pady=2 )

        #-----
        self.lblAppData = Label(RightFrame0, font=('arial', 18, 'bold'), text="Abblecation Data: ", padx=2, pady=2,
                                 bg="gainsboro")
        self.lblAppData.grid(row=1, column=0, sticky=W)
        self.cboAppData = ttk.Combobox(RightFrame0, textvariable=AppData, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboAppData['value'] = ('', 'Select An Option', 'Yes', 'No')
        self.cboAppData.current(0)
        self.cboAppData.grid(row=1, column=1, pady=2)

        #----

        self.lblNextCreditReview = Label(RightFrame0, font=('arial', 18, 'bold'), text="Next Credit Review: ", padx=2, pady=2,
                                bg="gainsboro")
        self.lblNextCreditReview.grid(row=2, column=0, sticky=W)
        self.cboNextCreditReview = ttk.Combobox(RightFrame0, textvariable=NextCreditReview, state='readonly',
                                       font=('arial', 18, 'bold'), width=19)
        self.cboNextCreditReview['value'] = ('', 'Select An Option', 'Yes', 'No')
        self.cboNextCreditReview.current(0)
        self.cboNextCreditReview.grid(row=2, column=1, pady=2)


        #------
        self.lblLastCreditReview= Label(RightFrame0, font=('arial', 18, 'bold'), text="Last Credit Review: ", padx=2, pady=2,
                                 bg="gainsboro")
        self.lblLastCreditReview.grid(row=3, column=0, sticky=W)
        self.cboLastCreditReview = ttk.Combobox(RightFrame0, textvariable=LastCreditReview, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboLastCreditReview['value'] = ('', 'Select An Option', 'Yes', 'No')
        self.cboLastCreditReview.current(0)
        self.cboLastCreditReview.grid(row=3, column=1, pady=2)


        #------

        self.lblDateRev = Label(RightFrame0, font=('arial', 18, 'bold'), text="Date Review: ", padx=2, pady=2,
                                 bg="gainsboro")
        self.lblDateRev.grid(row=4, column=0, sticky=W)
        self.cboDateRev = ttk.Combobox(RightFrame0, textvariable=DateRev, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboDateRev['value'] = ('', 'Select An Option', 'Yes', 'No')
        self.cboDateRev.current(0)
        self.cboDateRev.grid(row=4, column=1, pady=2)

        # ========================================================RightFrame1===================================================#

        self.txtReceipt = Text(RightFrame1, pady =2, height=14, width=71, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0,pady=2)

        # ========================================================RightFrame2===================================================#

        self.lblTex = Label(RightFrame2, font=('arial', 18, 'bold'), text="Tax", padx=4, pady=1, fg="black", bg="gainsboro")
        self.lblTex.grid(row=0, column=0, sticky=W)
        self.txtTex= Entry(RightFrame2, textvariable=Tex, font=('arial', 16, 'bold'),bd=8,
                           fg="black", width=30, justify=LEFT).grid(row=0, column=1, pady=1, padx=4)

          #---

        self.lblSubTotal = Label(RightFrame2, font=('arial', 18, 'bold'), text="SubTotal", padx=4, pady=1, fg="black",bg="gainsboro")
        self.lblSubTotal.grid(row=1, column=0, sticky=W)
        self.txtSubTotal = Entry(RightFrame2, textvariable=SubTotal, font=('arial', 16, 'bold'), bd=8,
                            fg="black", width=30, justify=LEFT).grid(row=1, column=1, pady=1, padx=4)


           #---

        self.lblTotal = Label(RightFrame2, font=('arial', 18, 'bold'), text="Total", padx=4, pady=1, fg="black", bg="gainsboro")
        self.lblTotal.grid(row=2, column=0, sticky=W)
        self.txtTotal = Entry(RightFrame2, textvariable=Total, font=('arial', 16, 'bold'), bd=8,
                                 fg="black", width=30, justify=LEFT).grid(row=2, column=1, pady=1, padx=4)


        # ========================================================LeftFrame0===================================================#

        self.lblProdType = Label(LeftFrame0, font=('arial', 18, 'bold'), text="Product Type ", padx=2, pady=16,bg="gainsboro")
        self.lblProdType.grid(row=0, column=0, sticky=W)
        self.cboProdType = ttk.Combobox(LeftFrame0, textvariable=ProdType, state='readonly',
                                        font=('arial', 18, 'bold'), width=12)

        self.cboProdType.bind("<<ComboboxSelected>>", Product)
        self.cboProdType['value'] = ('', 'Flat', 'A house', 'villa')
        self.cboProdType.current(0)
        self.cboProdType.grid(row=0, column=1,)

       #اعتبرها هنا مساحة السكن
        self.lblNoDays = Label(LeftFrame0, font=('arial', 18, 'bold'), text="The space ", padx=2, pady=2, bg="gainsboro")
        self.lblNoDays.grid(row=0, column=2, sticky=W)
        self.cboNoDays = ttk.Combobox(LeftFrame0, textvariable=NoDays, state='readonly',
                                        font=('arial', 18, 'bold'), width=12)

        self.cboNoDays.bind("<<ComboboxSelected>>", iDates)
        self.cboNoDays['value'] = ('', '100m-150m','150m-300m', '300m-1000m')
        self.cboNoDays.current(0)
        self.cboNoDays.grid(row=0, column=3)

        self.lblProdCode = Label(LeftFrame0, font=('arial', 16, 'bold'), text="The Product Code ", padx=1, pady=16, bg="gainsboro")
        self.lblProdCode.grid(row=1, column=0, sticky=W)

        self.txtProdCode = Entry(LeftFrame0, textvariable=ProdCode, font=('arial', 16, 'bold'), bd=8,
                              fg="black", width=14, justify=LEFT).grid(row=1, column=1)

        self.lblProdCode = Label(LeftFrame0, font=('arial', 16, 'bold'), text="The Product Code ", padx=1, pady=2,
                                 bg="gainsboro")
        self.lblProdCode.grid(row=1, column=2, sticky=W)

        self.txtCostPDay = Entry(LeftFrame0, textvariable=CostPDay, font=('arial', 16, 'bold'), bd=8,
                                 fg="black", width=14, justify=LEFT).grid(row=1, column=3)

        # ========================================================LeftFrame1===================================================#

        self.lblCreLimit = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Credit Limit ", padx=2, pady=2, bg="gainsboro")
        self.lblCreLimit.grid(row=0, column=0, sticky=W)
        self.cboCreLimit = ttk.Combobox(LeftFrame1, textvariable=CreLimit, state='readonly',
                                        font=('arial', 18, 'bold'), width=12)
        self.cboCreLimit['value'] = ('', 'Select An Option', '300$', '500$','1000$')
        self.cboCreLimit.current(0)
        self.cboCreLimit.grid(row=0, column=1, pady=2)

        #---
        self.lblCreCheck = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Credit Check ", padx=2, pady=2,bg="gainsboro")
        self.lblCreCheck.grid(row=0, column=2, sticky=W)
        self.cboCreCheck = ttk.Combobox(LeftFrame1, textvariable=CreCheck, state='readonly',
                                        font=('arial', 18, 'bold'), width=10)
        self.cboCreCheck['value'] = ('', 'Select An Option', 'Yes', 'No')
        self.cboCreCheck.current(0)
        self.cboCreCheck.grid(row=0, column=3, pady=2)

        #--

        self.lblSettDueDay = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Sett.Due ", padx=2, pady=2,bg="gainsboro")
        self.lblSettDueDay.grid(row=1, column=0, sticky=W)

        self.txtSettDueDay = Entry(LeftFrame1, textvariable=SettDueDay, font=('arial', 16, 'bold'), bd=2,
                                 fg="black", width=14, justify=LEFT).grid(row=1, column=1)

        #--

        self.lblPaymentD = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Payment Due ", padx=1, pady=2,bg="gainsboro")
        self.lblPaymentD.grid(row=1, column=2, sticky=W)
        self.cboPaymentD = ttk.Combobox(LeftFrame1, textvariable=PaymentD, state='readonly',
                                        font=('arial', 18, 'bold'), width=10)
        self.cboPaymentD['value'] = ('', 'Select An Option', 'Yes', 'No')
        self.cboPaymentD.current(0)
        self.cboPaymentD.grid(row=1, column=3, pady=2)

        #--

        self.lblDiscount = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Discount ", padx=1, pady=2,bg="gainsboro")
        self.lblDiscount.grid(row=2, column=0, sticky=W)
        self.cboDiscount = ttk.Combobox(LeftFrame1, textvariable=Discount, state='readonly',
                                        font=('arial', 18, 'bold'), width=12)
        self.cboDiscount['value'] = ('0', '15%', '30%', '50%', '75%')
        self.cboDiscount.current(0)
        self.cboDiscount.grid(row=2, column=1, pady=2)

        #--
        #الوديعة

        self.lblDeposit = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Deposit ", padx=1, pady=2,bg="gainsboro")
        self.lblDeposit.grid(row=2, column=2, sticky=W)
        self.cboDeposit = ttk.Combobox(LeftFrame1, textvariable=Deposit, state='readonly',
                                        font=('arial', 18, 'bold'), width=10)
        self.cboDeposit['value'] = ('', 'Select An Option', 'Yes', 'No')
        self.cboDeposit.current(0)
        self.cboDeposit.grid(row=2, column=3, pady=2)

        #--

        self.lblPayDueDay = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Pay Due Day ", padx=1, pady=2, bg="gainsboro")
        self.lblPayDueDay.grid(row=3, column=0, sticky=W)

        self.txtPayDueDay = Entry(LeftFrame1, textvariable=PayDueDay, font=('arial', 16, 'bold'), bd=2,
                                   fg="Blue", width=14, justify=LEFT).grid(row=3, column=1)


        #---

        self.lblPaymetM = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Payment Method ", padx=0, pady=4, bg="gainsboro")
        self.lblPaymetM.grid(row=3, column=2, sticky=W)
        self.cboPaymetM = ttk.Combobox(LeftFrame1, textvariable=PaymetM, state='readonly',
                                       font=('arial', 18, 'bold'), width=10)
        self.cboPaymetM['value'] = ('', 'Select An Option', 'Cash', 'Vis Card',"Master Card")
        self.cboPaymetM.current(0)
        self.cboPaymetM.grid(row=3, column=3, pady=2)





        #=========================================================LeftFrame2===================================================#
        LeftFrame2LL= Frame(LeftFrame2, bd=5, width=300, height=160, padx=5,bg="gainsboro", relief=RIDGE)
        LeftFrame2LL.grid(row=0, column=0)

        LeftFrame2LR = Frame(LeftFrame2, bd=5, width=300, height=160, padx=5, bg="black", relief=RIDGE)
        LeftFrame2LR.grid(row=0, column=1)
        # =========================================================LeftFrame2LL===================================================#

        self.chkCheckCredit = Checkbutton(LeftFrame2LL, text="check Cridit ",variable=Var1, onvalue=1,offvalue=0,
                                          font=('arial', 16, 'bold'), bg="gainsboro",command=checkCredit).grid(row=0, sticky=W)

        self.chkTermAgreed = Checkbutton(LeftFrame2LL, text="Term Agreed ", variable=Var2, onvalue=1, offvalue=0,
                                          font=('arial', 16, 'bold'), bg="gainsboro", command=TermAgreed).grid(row=1, sticky=W)

        self.chkAccountOnHold = Checkbutton(LeftFrame2LL, text="AccountOnHold", variable=Var3, onvalue=1, offvalue=0,
                                          font=('arial', 16, 'bold'), bg="gainsboro", command=AcctOnHold).grid(row=2, sticky=W)

        self.chkRestrictMailing = Checkbutton(LeftFrame2LL, text="Restrict Mailing ", variable=Var4, onvalue=1, offvalue=0,
                                          font=('arial', 16, 'bold'), bg="gainsboro", command=RestrictedMails).grid(row=3, sticky=W)
        # =========================================================LeftFrame2LR===================================================#
        self.txtInfo0 = Text(LeftFrame2LR, height=2, width=63, font=('arial', 9, 'bold'))
        self.txtInfo0.grid(row=0, column=0, pady=2)

        self.txtInfo1 = Text(LeftFrame2LR, height=2, width=63, font=('arial', 9, 'bold'))
        self.txtInfo1.grid(row=1, column=0, pady=2)

        self.txtInfo2 = Text(LeftFrame2LR, height=2, width=63, font=('arial', 9, 'bold'))
        self.txtInfo2.grid(row=2, column=0, pady=2)

        self.txtInfo3 = Text(LeftFrame2LR, height=2, width=63, font=('arial', 9, 'bold'))
        self.txtInfo3.grid(row=3, column=0, pady=2)

        # ========================================================LeftFrame3===================================================#
        self.btnTotal = Button(LeftFrame3, padx=33, pady=2,bd=4, fg="black", font=('arial', 20, 'bold'), width=9, height=2,
                             bg="gainsboro", text="Total", command=TotalCost).grid(row=0,column=0)

        self.btnReset = Button(LeftFrame3, padx=33, pady=2, bd=4, fg="black", font=('arial', 20, 'bold'), width=9,
                               height=2,
                               bg="gainsboro", text="Reset", command=Reset).grid(row=0, column=1)

        self.btnExit = Button(LeftFrame3, padx=33, pady=2, bd=4, fg="black", font=('arial', 20, 'bold'), width=9,
                               height=2,
                               bg="gainsboro", text="Exit", command=iExit).grid(row=0, column=2)



if __name__ == '__main__':
    root = Tk()
    application = Rental_Inventory(root)
    root.mainloop()
