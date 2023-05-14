#Nama Kelompok
#1. Ahitsa Dawang Ransifa (V3922002)
#2. Diah Munica Nawang (V3922015)
#3. Fernando Djaka (V3922022)
#4. Herdina Fitri Desfiastuti (V3922023)
#5. Laila Ainur Rahma (V3922026)

from tkinter import *
import random
import os
import sys
from tkinter import messagebox


class true_beauty:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Kelompok 5")
        title = Label(self.root, text="TRUE BEAUTY STORE", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#A569BD", fg="white")
        title.pack(fill=X)

        # ===variables=====

        self.Liptint = IntVar()
        self.Highliter = IntVar()
        self.Concealer = IntVar()
        self.Eyeshadow = IntVar()
        self.Cushion = IntVar()
        self.Foundation = IntVar()
        self.Primer = IntVar()
        self.facewash = IntVar()
        self.toner = IntVar()
        self.essence = IntVar()
        self.serum = IntVar()
        self.moisturizer = IntVar()
        self.sunscreen= IntVar()
        self.masker= IntVar()
        self.body_scrub = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.handcream = IntVar()
        self.deodorant = IntVar()
        self.sunblock = IntVar()
        self.wax = IntVar()
        self.total_makeup = StringVar()
        self.total_skincare = StringVar()
        self.total_bodycare = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        self.phone = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.total_all_bill = StringVar()
        
# AHITSA
        # ----------COSTUMER DETAILS --------------------
        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#A569BD", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)

        cust_name = Label(details, text="Customer Name", font=("Arial Black", 14), bg="#A569BD", fg="white")
        cust_name.grid(row=0, column=0, padx=15)
        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.c_name)
        cust_entry.grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="Contact No.", font=("Arial Black", 14), bg="#A569BD", fg="white")
        contact_name.grid(row=0, column=2, padx=10)
        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.phone)
        contact_entry.grid(row=0, column=3, padx=8)

        bill_name = Label(details, text="Bill.No.", font=("Arial Black", 14), bg="#A569BD", fg="white")
        bill_name.grid(row=0, column=4, padx=10)
        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no)
        bill_entry.grid(row=0, column=5, padx=8)
        # -------------------------------Makeup------------------------
        MakeUp = LabelFrame(self.root, text="MakeUp", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483", relief=GROOVE, bd=10)
        MakeUp.place(x=5, y=180, height=380, width=325)

        item1 = Label(MakeUp, text="Liptint", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item1.grid(row=0, column=0, pady=11)
        item1_entry = Entry(MakeUp, borderwidth=2, width=15, textvariable=self.Liptint)
        item1_entry.grid(row=0, column=1, padx=10)

        item2 = Label(MakeUp, text="Highliter", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item2.grid(row=1, column=0, pady=11)
        item2_entry = Entry(MakeUp, borderwidth=2, width=15, textvariable=self.Highliter)
        item2_entry.grid(row=1, column=1, padx=10)

        item3 = Label(MakeUp, text="Concealer", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item3.grid(row=2, column=0, pady=11)
        item3_entry = Entry(MakeUp, borderwidth=2, width=15, textvariable=self.Concealer)
        item3_entry.grid(row=2, column=1, padx=10)

        item4 = Label(MakeUp, text="Eyeshadow", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item4.grid(row=3, column=0, pady=11)
        item4_entry = Entry(MakeUp, borderwidth=2, width=15, textvariable=self.Eyeshadow)
        item4_entry.grid(row=3, column=1, padx=10)

        item5 = Label(MakeUp, text="Cushion", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item5.grid(row=4, column=0, pady=11)
        item5_entry = Entry(MakeUp, borderwidth=2, width=15, textvariable=self.Cushion)
        item5_entry.grid(row=4, column=1, padx=10)

        item6 = Label(MakeUp, text="Foundation", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item6.grid(row=5, column=0, pady=11)
        item6_entry = Entry(MakeUp, borderwidth=2, width=15, textvariable=self.Foundation)
        item6_entry.grid(row=5, column=1, padx=10)

        item7 = Label(MakeUp, text="Primer ", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item7.grid(row=6, column=0, pady=11)
        item7_entry = Entry(MakeUp, borderwidth=2, width=15, textvariable=self.Primer)
        item7_entry.grid(row=6, column=1, padx=10)


#MONAAA
        # ===============================SKINCARE===============
        SkinCare = LabelFrame(self.root, text="SkinCare", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3", fg="#6C3483")
        SkinCare.place(x=340, y=180, height=380, width=325)

        item8_label = Label(SkinCare, text="Facewash", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item8_label.grid(row=0, column=0, pady=11)
        item8_entry = Entry(SkinCare, borderwidth=2, width=15, textvariable=self.facewash)
        item8_entry.grid(row=0, column=1, padx=10)

        item9_label = Label(SkinCare, text="Toner", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item9_label.grid(row=1, column=0, pady=11)
        item9_entry = Entry(SkinCare, borderwidth=2, width=15, textvariable=self.toner)
        item9_entry.grid(row=1, column=1, padx=10)

        item10_label = Label(SkinCare, text="Essence", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item10_label.grid(row=2, column=0, pady=11)
        item10_entry = Entry(SkinCare, borderwidth=2, width=15, textvariable=self.essence)
        item10_entry.grid(row=2, column=1, padx=10)

        item11_label = Label(SkinCare, text="Serum", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item11_label.grid(row=3, column=0, pady=11)
        item11_entry = Entry(SkinCare, borderwidth=2, width=15, textvariable=self.serum)
        item11_entry.grid(row=3, column=1, padx=10)

        item12_label = Label(SkinCare, text="Moisturizer", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item12_label.grid(row=4, column=0, pady=11)
        item12_entry = Entry(SkinCare, borderwidth=2, width=15, textvariable=self.moisturizer)
        item12_entry.grid(row=4, column=1, padx=10)

        item13_label = Label(SkinCare, text="Sunscreen", font=("Arial Black", 11), bg="#E5B4F3", fg="#603483")
        item13_label.grid(row=5, column=0, pady=11)
        item13_entry = Entry(SkinCare, borderwidth=2, width=15, textvariable=self.sunscreen)
        item13_entry.grid(row=5, column=1, padx=10)

        item14_label = Label(SkinCare, text="Masker", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item14_label.grid(row=6, column=0, pady=11)
        item14_entry = Entry(SkinCare, borderwidth=2, width=15, textvariable=self.masker)
        item14_entry.grid(row=6, column=1, padx=10)


        #-------------------------Body Care-----------------
        BodyCare = LabelFrame(self.root, text="BodyCare", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3", fg="#6C3483")
        BodyCare.place(x=677, y=180, height=380, width=325)

        item15_label = Label(BodyCare, text="Body Scrub", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item15_label.grid(row=0, column=0, pady=11)
        item15_entry = Entry(BodyCare, borderwidth=2, width=15, textvariable=self.body_scrub)
        item15_entry.grid(row=0, column=1, padx=10)

        item16_label = Label(BodyCare, text="Shampoo ", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item16_label.grid(row=1, column=0, pady=11)
        item16_entry = Entry(BodyCare, borderwidth=2, width=15, textvariable=self.shampoo)
        item16_entry.grid(row=1, column=1, padx=10)

        item17_label = Label(BodyCare, text="Body Lotion", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item17_label.grid(row=2, column=0, pady=11)
        item17_entry = Entry(BodyCare, borderwidth=2, width=15, textvariable=self.lotion)
        item17_entry.grid(row=2, column=1, padx=10)

        item18_label = Label(BodyCare, text="Hand Cream", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item18_label.grid(row=3, column=0, pady=11)
        item18_entry = Entry(BodyCare, borderwidth=2, width=15, textvariable=self.handcream)
        item18_entry.grid(row=3, column=1, padx=10)

        item19_label = Label(BodyCare, text="Deodorant", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item19_label.grid(row=4, column=0, pady=11)
        item19_entry = Entry(BodyCare, borderwidth=2, width=15, textvariable=self.deodorant)
        item19_entry.grid(row=4, column=1, padx=10)

        item20_label = Label(BodyCare, text="Sunblock", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item20_label.grid(row=5, column=0, pady=11)
        item20_entry = Entry(BodyCare, borderwidth=2, width=15, textvariable=self.sunblock)
        item20_entry.grid(row=5, column=1, padx=10)

        item21_label = Label(BodyCare, text="Wax", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item21_label.grid(row=6, column=0, pady=11)
        item21_entry = Entry(BodyCare, borderwidth=2, width=15, textvariable=self.wax)
        item21_entry.grid(row=6, column=1, padx=10)

        #------------------------------bill Area---------------------------

        billarea_Frame = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
        billarea_Frame.place(x=1010, y=188, width=330, height=372)
        bill_title = Label(billarea_Frame, text="Bill Area", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#E5B4F3", fg="#6C3483")
        bill_title.pack(fill=X)
        scrol_y = Scrollbar(billarea_Frame, orient=VERTICAL)
        self.txtarea = Text(billarea_Frame, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #==========================Bill menu=======================
        billing_menu = LabelFrame(self.root, text="Billing Summary", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_MakeUp = Label(billing_menu, text="Total MakeUp Price", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_MakeUp.grid(row=0, column=0)
        self.total_makeup = StringVar()
        total_MakeUp_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_makeup)
        total_MakeUp_entry.grid(row=0, column=1, padx=10, pady=7)

        total_SkinCare = Label(billing_menu, text="Total SkinCare Price", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_SkinCare.grid(row=1, column=0)
        self.total_skincare = StringVar()
        total_SkinCare_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_skincare)
        total_SkinCare_entry.grid(row=1, column=1, padx=10, pady=7)

        total_BodyCare = Label(billing_menu, text="Total Body Care Price", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_BodyCare.grid(row=2, column=0)
        self.total_bodycare = StringVar()
        total_BodyCare_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_bodycare)
        total_BodyCare_entry.grid(row=2, column=1, padx=10, pady=7)

        tax_MakeUp = Label(billing_menu, text="MakeUp Tax", font=("Arial Black", 11), bg="#A569BD", fg="white")
        tax_MakeUp.grid(row=0, column=2)
        self.a = StringVar()
        tax_MakeUp_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a)
        tax_MakeUp_entry.grid(row=0, column=3, padx=10, pady=7)

        tax_SkinCare = Label(billing_menu, text="SkinCare Tax", font=("Arial Black", 11), bg="#A569BD", fg="white")
        tax_SkinCare.grid(row=1, column=2)
        self.b = StringVar()
        tax_SkinCare_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b)
        tax_SkinCare_entry.grid(row=1, column=3, padx=10, pady=7)
        
        tax_BodyCare = Label(billing_menu, text="Body CareTax", font=("Arial Black", 11), bg="#A569BD", fg="white")
        
        tax_BodyCare.grid(row=2, column=2)

        tax_BodyCare_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c)
        tax_BodyCare_entry.grid(row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=850, width=480, height=95)

        button_total = Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=lambda: total(self))
        button_total.grid(row=0, column=0, padx=12)

        button_clear = Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=lambda: clear(self))
        button_clear.grid(row=0, column=1, padx=10, pady=6)

        button_exit = Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", width=8, command=lambda: exit1(self))
        button_exit.grid(row=0, column=2, padx=10, pady=6)

        intro(self)
        billarea(self)

# HERDINA
def total(self):
    if self.c_name.get() == "" or self.phone.get() == "":
        messagebox.showerror("Error", "Fill the complete Customer Detail")
        return
    self.nu = self.Liptint.get() * 50000
    self.no = self.Highliter.get() * 60000
    self.la = self.Concealer.get() * 55000
    self.ore = self.Eyeshadow.get() * 127000
    self.mu = self.Cushion.get() * 185000
    self.si = self.Foundation.get() * 150000
    self.na = self.Primer.get() * 50000
    total_MakeUp_price = (self.nu + self.no + self.la + self.ore + self.mu + self.si + self.na)
    self.total_makeup.set(str(total_MakeUp_price) + " Rp")
    self.a.set(str(round(total_MakeUp_price * 0.05, 3)) + " Rp")
    self.at = self.facewash.get() * 52000
    self.pa = self.toner.get() * 90000
    self.oi = self.serum.get() * 120000
    self.ri = self.essence.get() * 120000
    self.su = self.moisturizer.get() * 55000
    self.te = self.masker.get() * 48000
    self.da = self.sunscreen.get() * 76000
    total_SkinCare_price = (self.at + self.pa + self.oi + self.ri + self.su + self.te + self.da)
    self.total_skincare.set(str(total_SkinCare_price) + " Rp")
    self.b.set(str(round(total_SkinCare_price * 0.01, 3)) + " Rp")

    self.body_scrub_price = self.body_scrub.get() * 50000
    self.shampoo_price = self.shampoo.get() * 30000
    self.handcream_price = self.handcream.get() * 30000
    self.lotion_price = self.lotion.get() * 55000
    self.deodorant_price = self.deodorant.get() * 65000
    self.sunblock_price = self.sunblock.get() * 100000
    self.wax_price = self.wax.get() * 65000
    total_BodyCare_price = (
        self.body_scrub_price +
        self.shampoo_price +
        self.handcream_price +
        self.lotion_price +
        self.deodorant_price +
        self.sunblock_price +
        self.wax_price
    )
    self.total_bodycare.set(str(total_BodyCare_price) + " Rp")
    self.c.set(str(round(total_BodyCare_price * 0.10, 3)) + " Rp")
    
    total_bill = ( total_MakeUp_price + total_SkinCare_price + total_BodyCare_price + round(total_SkinCare_price * 0.01, 3) + round(total_BodyCare_price * 0.10, 3) +round(total_MakeUp_price * 0.05, 3) ) 
    
    self.total_all_bill = str(total_bill) + " Rp"
    billarea(self)
    
def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(END, "\tWELCOME TO TRUE BEAUTY STORE\n\tPhone-No.739275410")
    self.txtarea.insert(END, f"\n\nBill no.: {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
    self.txtarea.insert(END, f"\nPhone No.: {self.phone.get()}")
    self.txtarea.insert(END, "\n====================\n")
    self.txtarea.insert(END, "Product\t\tQty\tPrice\n")
    self.txtarea.insert(END, "====================\n")

def billarea(self):
    intro(self)
    if self.Liptint.get() != 0:
        self.txtarea.insert(END, f"Liptint\t\t{self.Liptint.get()}\t{self.nu}\n")
    if self.Highliter.get() != 0:
        self.txtarea.insert(END, f"Highliter\t\t{self.Highliter.get()}\t{self.no}\n")
    if self.Concealer.get() != 0:
        self.txtarea.insert(END, f"Concealer\t\t{self.Concealer.get()}\t{self.la}\n")
    if self.Eyeshadow.get() != 0:
        self.txtarea.insert(END, f"Eyeshadow\t\t{self.Eyeshadow.get()}\t{self.ore}\n")
    if self.Cushion.get() != 0:
        self.txtarea.insert(END, f"Cushion\t\t{self.Cushion.get()}\t{self.mu}\n")
    if self.Foundation.get() != 0:
        self.txtarea.insert(END, f"Foundation\t\t{self.Foundation.get()}\t{self.si}\n")
    if self.Primer.get() != 0:
        self.txtarea.insert(END, f"Primer\t\t{self.Primer.get()}\t{self.na}\n")
    if self.facewash.get() != 0:
        self.txtarea.insert(END, f"facewash\t\t{self.facewash.get()}\t{self.at}\n")
    if self.toner.get() != 0:
        self.txtarea.insert(END, f"toner\t\t{self.toner.get()}\t{self.pa}\n")
    if self.essence.get() != 0:
        self.txtarea.insert(END, f"essence\t\t{self.essence.get()}\t{self.ri}\n")
    if self.serum.get() != 0:
        self.txtarea.insert(END, f"serum\t\t{self.serum.get()}\t{self.oi}\n")
    if self.moisturizer.get() != 0:
        self.txtarea.insert(END, f"moisturizer\t\t{self.moisturizer.get()}\t{self.su}\n")
    if self.sunscreen.get() != 0:
        self.txtarea.insert(END, f"Sunscreen\t\t{self.sunscreen.get()}\t{self.da}\n")
    if self.masker.get() != 0:
        self.txtarea.insert(END, f"masker\t\t{self.masker.get()}\t{self.te}\n")
    if self.body_scrub.get() != 0:
        self.txtarea.insert(END, f"Body scrub\t\t{self.body_scrub.get()}\t{self.body_scrub_price}\n")
    if self.shampoo.get() != 0:
        self.txtarea.insert(END, f"Shampoo\t\t{self.shampoo.get()}\t{self.shampoo_price}\n")
    if self.lotion.get() != 0:
        self.txtarea.insert(END, f"Lotion\t\t{self.lotion.get()}\t{self.lotion_price}\n")
    if self.handcream.get() != 0:
        self.txtarea.insert(END, f"Hand Cream\t\t{self.handcream.get()}\t{self.handcream_price}\n")
    if self.deodorant.get() != 0:
        self.txtarea.insert(END, f"Deodorant\t\t{self.deodorant.get()}\t{self.deodorant_price}\n")
    if self.sunblock.get() != 0:
        self.txtarea.insert(END, f"Sunblock\t\t{self.sunblock.get()}\t{self.sunblock_price} Rp\n")
    if self.wax.get() != 0:
        self.txtarea.insert(END, f"Wax\t\t{self.wax.get()}\t{self.wax_price} Rp\n")
    self.txtarea.insert(END, f"\n--------------------------\n")
    if self.a.get() != '':
        self.txtarea.insert(END, f"Total MakeUp Tax: {self.a.get()}\n")
    if self.b.get() != '':
        self.txtarea.insert(END, f"Total SkinCare Tax {self.b.get()}\n")
    if self.c.get() != '':
        self.txtarea.insert(END, f"Total BodyCare Tax {self.c.get()}\n")

    self.txtarea.insert(END, f"\nTotal Bill Amount {self.total_all_bill}\n")
    self.txtarea.insert(END, "---\n")

def clear(self):
    self.txtarea.delete(1.0, END)
    self.Liptint.set(0)
    self.Highliter.set(0)
    self.Concealer.set(0)
    self.Eyeshadow.set(0)
    self.Cushion.set(0)
    self.Foundation.set(0)
    self.Primer.set(0)
    self.facewash.set(0)
    self.toner.set(0)
    self.essence.set(0)
    self.serum.set(0)
    self.moisturizer.set(0)
    self.sunscreen.set(0)
    self.masker.set(0)
    self.body_scrub.set(0)
    self.shampoo.set(0)
    self.lotion.set(0)
    self.handcream.set(0)
    self.deodorant.set(0)
    self.sunblock.set(0)
    self.wax.set(0)
    self.total_makeup.set('0.0 Rp')
    self.total_skincare.set('0.0 Rp')
    self.total_bodycare.set('0.0 Rp')
    self.a.set('0.0 Rp')
    self.b.set('0.0 Rp')
    self.c.set('0.0 Rp')
    self.c_name.set('')
    self.bill_no.set('')
    self.phone.set('')

def exit1(self):
    self.root.destroy()

# copas diatas ini yakkk....
root = Tk()
bill_app = true_beauty(root)
root.mainloop()
