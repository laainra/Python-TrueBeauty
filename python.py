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
        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.namkeen = IntVar()
        self.atta = IntVar()
        self.pasta = IntVar()
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.dal = IntVar()
        self.tea = IntVar()
        self.soap = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.sanitizer = IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
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

        snacks = LabelFrame(self.root, text="Snacks", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483", relief=GROOVE, bd=10)
        snacks.place(x=5, y=180, height=380, width=325)

        item1 = Label(snacks, text="Nutella Choco Spread", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item1.grid(row=0, column=0, pady=11)
        item1_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.nutella)
        item1_entry.grid(row=0, column=1, padx=10)

        item2 = Label(snacks, text="Noodles (1 Pack)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item2.grid(row=1, column=0, pady=11)
        item2_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.noodles)
        item2_entry.grid(row=1, column=1, padx=10)

        item3 = Label(snacks, text="Lays (10Rs)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item3.grid(row=2, column=0, pady=11)
        item3_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.lays)
        item3_entry.grid(row=2, column=1, padx=10)

        item4 = Label(snacks, text="Oreo (20Rs)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item4.grid(row=3, column=0, pady=11)
        item4_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.oreo)
        item4_entry.grid(row=3, column=1, padx=10)

        item5 = Label(snacks, text="Chocolate Muffin", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item5.grid(row=4, column=0, pady=11)
        item5_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.muffin)
        item5_entry.grid(row=4, column=1, padx=10)

        item6 = Label(snacks, text="Dairy Milk Silk (60Rs)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item6.grid(row=5, column=0, pady=11)
        item6_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.silk)
        item6_entry.grid(row=5, column=1, padx=10)

        item7 = Label(snacks, text="Namkeen (15Rs)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item7.grid(row=6, column=0, pady=11)
        item7_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.namkeen)
        item7_entry.grid(row=6, column=1, padx=10)


#MONAAA
        # ===============================GROCERY===============
        grocery = LabelFrame(self.root, text="Grocery", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3", fg="#6C3483")
        grocery.place(x=340, y=180, height=380, width=325)

        item8_label = Label(grocery, text="Aashirvaad Atta (1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item8_label.grid(row=0, column=0, pady=11)
        item8_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.atta)
        item8_entry.grid(row=0, column=1, padx=10)

        item9_label = Label(grocery, text="Pasta (1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item9_label.grid(row=1, column=0, pady=11)
        item9_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.pasta)
        item9_entry.grid(row=1, column=1, padx=10)

        item10_label = Label(grocery, text="Basmati Rice (1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item10_label.grid(row=2, column=0, pady=11)
        item10_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.rice)
        item10_entry.grid(row=2, column=1, padx=10)

        item11_label = Label(grocery, text="Sunflower Oil (1ltr)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item11_label.grid(row=3, column=0, pady=11)
        item11_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.oil)
        item11_entry.grid(row=3, column=1, padx=10)

        item12_label = Label(grocery, text="Refined Sugar (1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item12_label.grid(row=4, column=0, pady=11)
        item12_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.sugar)
        item12_entry.grid(row=4, column=1, padx=10)

        item13_label = Label(grocery, text="Daal (1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#603483")
        item13_label.grid(row=5, column=0, pady=11)
        item13_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.dal)
        item13_entry.grid(row=5, column=1, padx=10)

        item14_label = Label(grocery, text="Tea Powder (1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item14_label.grid(row=6, column=0, pady=11)
        item14_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.tea)
        item14_entry.grid(row=6, column=1, padx=10)


        #-------------------------beauty and hygine-----------------
        hygiene = LabelFrame(self.root, text="Beauty & Hygiene", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3", fg="#6C3483")
        hygiene.place(x=677, y=180, height=380, width=325)

        item15_label = Label(hygiene, text="Bathing Soap", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item15_label.grid(row=0, column=0, pady=11)
        item15_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.soap)
        item15_entry.grid(row=0, column=1, padx=10)

        item16_label = Label(hygiene, text="Shampoo (1ltr)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item16_label.grid(row=1, column=0, pady=11)
        item16_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.shampoo)
        item16_entry.grid(row=1, column=1, padx=10)

        item17_label = Label(hygiene, text="Body Lotion (1ltr)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item17_label.grid(row=2, column=0, pady=11)
        item17_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.lotion)
        item17_entry.grid(row=2, column=1, padx=10)

        item18_label = Label(hygiene, text="Face Cream", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item18_label.grid(row=3, column=0, pady=11)
        item18_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.cream)
        item18_entry.grid(row=3, column=1, padx=10)

        item19_label = Label(hygiene, text="Shaving Foam", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item19_label.grid(row=4, column=0, pady=11)
        item19_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.foam)
        item19_entry.grid(row=4, column=1, padx=10)

        item20_label = Label(hygiene, text="Face Mask (1piece)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item20_label.grid(row=5, column=0, pady=11)
        item20_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.mask)
        item20_entry.grid(row=5, column=1, padx=10)

        item21_label = Label(hygiene, text="Hand Sanitizer (50ml)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item21_label.grid(row=6, column=0, pady=11)
        item21_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.sanitizer)
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

        total_snacks = Label(billing_menu, text="Total Snacks Price", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_snacks.grid(row=0, column=0)
        self.total_sna = StringVar()
        total_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_sna)
        total_snacks_entry.grid(row=0, column=1, padx=10, pady=7)

        total_grocery = Label(billing_menu, text="Total Grocery Price", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_grocery.grid(row=1, column=0)
        self.total_gro = StringVar()
        total_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_gro)
        total_grocery_entry.grid(row=1, column=1, padx=10, pady=7)

        total_hygiene = Label(billing_menu, text="Total Beauty & Hygiene Price", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_hygiene.grid(row=2, column=0)
        self.total_hyg = StringVar()
        total_hygiene_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_hyg)
        total_hygiene_entry.grid(row=2, column=1, padx=10, pady=7)

        tax_snacks = Label(billing_menu, text="Snacks Tax", font=("Arial Black", 11), bg="#A569BD", fg="white")
        tax_snacks.grid(row=0, column=2)
        self.a = StringVar()
        tax_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a)
        tax_snacks_entry.grid(row=0, column=3, padx=10, pady=7)

        tax_grocery = Label(billing_menu, text="Grocery Tax", font=("Arial Black", 11), bg="#A569BD", fg="white")
        tax_grocery.grid(row=1, column=2)
        self.b = StringVar()
        tax_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b)
        tax_grocery_entry.grid(row=1, column=3, padx=10, pady=7)
        
        tax_hygiene = Label(billing_menu, text="Beauty & Hygiene Tax", font=("Arial Black", 11), bg="#A569BD", fg="white")
        
        tax_hygiene.grid(row=2, column=2)

        tax_hygiene_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c)
        tax_hygiene_entry.grid(row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)

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
    self.nu = self.nutella.get() * 120
    self.no = self.noodles.get() * 40
    self.la = self.lays.get() * 10
    self.ore = self.oreo.get() * 20
    self.mu = self.muffin.get() * 30
    self.si = self.silk.get() * 60
    self.na = self.namkeen.get() * 15
    total_snacks_price = (self.nu + self.no + self.la + self.ore + self.mu + self.si + self.na)
    self.total_sna.set(str(total_snacks_price) + " Rs")
    self.a.set(str(round(total_snacks_price * 0.05, 3)) + " Rs")
    self.at = self.atta.get() * 42
    self.pa = self.pasta.get() * 120
    self.oi = self.oil.get() * 113
    self.ri = self.rice.get() * 160
    self.su = self.sugar.get() * 55
    self.te = self.tea.get() * 480
    self.da = self.dal.get() * 76
    total_grocery_price = (self.at + self.pa + self.oi + self.ri + self.su + self.te + self.da)
    self.total_gro.set(str(total_grocery_price) + " Rs")
    self.b.set(str(round(total_grocery_price * 0.01, 3)) + " Rs")

    self.soap_price = self.soap.get() * 30
    self.shampoo_price = self.shampoo.get() * 180
    self.cream_price = self.cream.get() * 130
    self.lotion_price = self.lotion.get() * 500
    self.foam_price = self.foam.get() * 85
    self.mask_price = self.mask.get() * 100
    self.sanitizer_price = self.sanitizer.get() * 20
    total_hygiene_price = (
        self.soap_price +
        self.shampoo_price +
        self.cream_price +
        self.lotion_price +
        self.foam_price +
        self.mask_price +
        self.sanitizer_price
    )
    self.total_hyg.set(str(total_hygiene_price) + " Rs")
    self.c.set(str(round(total_hygiene_price * 0.10, 3)) + " Rs")
    
    total_bill = (
        total_snacks_price +
        total_grocery_price +
        total_hygiene_price +
        round(total_grocery_price * 0.01, 3) +
        round(total_hygiene_price * 0.10, 3) +
        round(total_snacks_price * 0.05, 3)
    )
    
    self.total_all_bill = str(total_bill) + " Rs"
    billarea(self)
    
def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(END, "\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txtarea.insert(END, f"\n\nBill no.: {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
    self.txtarea.insert(END, f"\nPhone No.: {self.phone.get()}")
    self.txtarea.insert(END, "\n====================\n")
    self.txtarea.insert(END, "Product\t\tQty\tPrice\n")
    self.txtarea.insert(END, "====================\n")

def billarea(self):
    intro(self)
    if self.nutella.get() != 0:
        self.txtarea.insert(END, f"Nutella\t\t{self.nutella.get()}\t{self.nu}\n")
    if self.noodles.get() != 0:
        self.txtarea.insert(END, f"Noodles\t\t{self.noodles.get()}\t{self.no}\n")
    if self.lays.get() != 0:
        self.txtarea.insert(END, f"Lays\t\t{self.lays.get()}\t{self.la}\n")
    if self.oreo.get() != 0:
        self.txtarea.insert(END, f"Oreo\t\t{self.oreo.get()}\t{self.ore}\n")
    if self.muffin.get() != 0:
        self.txtarea.insert(END, f"Muffins\t\t{self.muffin.get()}\t{self.mu}\n")
    if self.silk.get() != 0:
        self.txtarea.insert(END, f"Silk\t\t{self.silk.get()}\t{self.si}\n")
    if self.namkeen.get() != 0:
        self.txtarea.insert(END, f"Namkeen\t\t{self.namkeen.get()}\t{self.na}\n")
    if self.atta.get() != 0:
        self.txtarea.insert(END, f"Atta\t\t{self.atta.get()}\t{self.at}\n")
    if self.pasta.get() != 0:
        self.txtarea.insert(END, f"Pasta\t\t{self.pasta.get()}\t{self.pa}\n")
    if self.rice.get() != 0:
        self.txtarea.insert(END, f"Rice\t\t{self.rice.get()}\t{self.ri}\n")
    if self.oil.get() != 0:
        self.txtarea.insert(END, f"Oil\t\t{self.oil.get()}\t{self.oi}\n")
    if self.sugar.get() != 0:
        self.txtarea.insert(END, f"Sugar\t\t{self.sugar.get()}\t{self.su}\n")
    if self.dal.get() != 0:
        self.txtarea.insert(END, f"Daal\t\t{self.dal.get()}\t{self.da}\n")
    if self.tea.get() != 0:
        self.txtarea.insert(END, f"Tea\t\t{self.tea.get()}\t{self.te}\n")
    if self.soap.get() != 0:
        self.txtarea.insert(END, f"Soap\t\t{self.soap.get()}\t{self.so}\n")
    if self.shampoo.get() != 0:
        self.txtarea.insert(END, f"Shampoo\t\t{self.shampoo.get()}\t{self.sh}\n")
    if self.lotion.get() != 0:
        self.txtarea.insert(END, f"Lotion\t\t{self.lotion.get()}\t{self.lo}\n")
    if self.cream.get() != 0:
        self.txtarea.insert(END, f"Cream\t\t{self.cream.get()}\t{self.cr}\n")
    if self.foam.get() != 0:
        self.txtarea.insert(END, f"Foam\t\t{self.foam.get()}\t{self.fo}\n")
    if self.mask.get() != 0:
        self.txtarea.insert(END, f"Mask\t\t{self.mask.get()}\t{self.mask_price} Rs\n")
    if self.sanitizer.get() != 0:
        self.txtarea.insert(END, f"Sanitizer\t\t{self.sanitizer.get()}\t{self.sanitizer_price} Rs\n")

    self.txtarea.insert(END, f"....................")
    if self.a.get() != '0.0 Rs':
        self.txtarea.insert(END, f"Total Snacks Tax: {self.a.get()}\n")
    if self.b.get() != '0.0 Rs':
        self.txtarea.insert(END, f"Total Grocery Tax {self.b.get()}\n")
    if self.c.get() != '0.0 Rs':
        self.txtarea.insert(END, f"Total Beauty&Hygiene Tax {self.c.get()}\n")
    self.txtarea.insert(END, f"Total Bill Amount {self.total_all_bill.get()}\n")
    self.txtarea.insert(END, "---\n")

def clear(self):
    self.txtarea.delete(1.0, END)
    self.nutella.set(0)
    self.noodles.set(0)
    self.lays.set(0)
    self.oreo.set(0)
    self.muffin.set(0)
    self.silk.set(0)
    self.namkeen.set(0)
    self.atta.set(0)
    self.pasta.set(0)
    self.rice.set(0)
    self.oil.set(0)
    self.sugar.set(0)
    self.dal.set(0)
    self.tea.set(0)
    self.soap.set(0)
    self.shampoo.set(0)
    self.lotion.set(0)
    self.cream.set(0)
    self.foam.set(0)
    self.mask.set(0)
    self.sanitizer.set(0)
    self.total_sna.set('0.0 Rs')
    self.total_gro.set('0.0 Rs')
    self.total_hyg.set('0.0 Rs')
    self.a.set('0.0 Rs')
    self.b.set('0.0 Rs')
    self.c.set('0.0 Rs')
    self.c_name.set('')
    self.bill_no.set('')
    self.phone.set('')

def exit1(self):
    self.root.destroy()

# copas diatas ini yakkk....
root = Tk()
bill_app = true_beauty(root)
root.mainloop()
