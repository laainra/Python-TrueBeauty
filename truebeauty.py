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
import win32print
from datetime import datetime
from tkinter import filedialog
import webbrowser
import urllib.parse



class true_beauty:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
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
        self.date = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.total_all_bill = StringVar()
        self.txtarea = StringVar()
        
# AHITSA
        # ----------COSTUMER DETAILS --------------------
        details = LabelFrame(self.root, text="Detail Customer", font=("Arial Black", 12), bg="#A569BD", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)

        cust_name = Label(details, text="Nama Customer", font=("Arial Black", 14), bg="#A569BD", fg="white")
        cust_name.grid(row=0, column=0, padx=15)
        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.c_name)
        cust_entry.grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="No. Hp", font=("Arial Black", 14), bg="#A569BD", fg="white")
        contact_name.grid(row=0, column=2, padx=10)
        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.phone)
        contact_entry.grid(row=0, column=3, padx=8)

        bill_name = Label(details, text="No. Bill.", font=("Arial Black", 14), bg="#A569BD", fg="white")
        bill_name.grid(row=0, column=4, padx=10)
        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no)
        bill_entry.grid(row=0, column=5, padx=8)

        date_name = Label(details, text="Tanggal", font=("Arial Black", 14), bg="#A569BD", fg="white")
        date_name.grid(row=0, column=6, padx=10)

        date_entry = Entry(details, borderwidth=4, width=30, textvariable=self.date)
        date_entry.grid(row=0, column=7, padx=8)

        # Set the current date and time
        date_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        # -------------------------------Makeup-------------------
        MakeUp = LabelFrame(self.root, text="MakeUp", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483", relief=GROOVE, bd=10)
        MakeUp.place(x=5, y=180, height=380, width=325)

        item1 = Label(MakeUp, text="Liptint", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item1.grid(row=0, column=0, pady=15)
        item1_entry = Entry(MakeUp, borderwidth=10, width=15, textvariable=self.Liptint)
        item1_entry.grid(row=0, column=1, padx=10)
        item1_button = Button(MakeUp, text="+", font=("Arial Black", 15), height=0, width=3,bg="#FFFFFF", command=lambda: plusbutton(self.Liptint))
        item1_button.grid(row=0, column=2, padx=10)

        item2 = Label(MakeUp, text="Highliter", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item2.grid(row=1, column=0, pady=15)
        item2_entry = Entry(MakeUp, borderwidth=10, width=15, textvariable=self.Highliter)
        item2_entry.grid(row=1, column=1, padx=10)
        item2_button = Button(MakeUp, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.Highliter))
        item2_button.grid(row=1, column=2, padx=10)

        item3 = Label(MakeUp, text="Concealer", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item3.grid(row=2, column=0, pady=15)
        item3_entry = Entry(MakeUp, borderwidth=10, width=15, textvariable=self.Concealer)
        item3_entry.grid(row=2, column=1, padx=10)
        item3_button = Button(MakeUp, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.Concealer))
        item3_button.grid(row=2, column=2, padx=10)

        item4 = Label(MakeUp, text="Eyeshadow", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item4.grid(row=3, column=0, pady=15)
        item4_entry = Entry(MakeUp, borderwidth=10, width=15, textvariable=self.Eyeshadow)
        item4_entry.grid(row=3, column=1, padx=10)
        item4_button = Button(MakeUp, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.Eyeshadow))
        item4_button.grid(row=3, column=2, padx=10)

        item5 = Label(MakeUp, text="Cushion", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item5.grid(row=4, column=0, pady=15)
        item5_entry = Entry(MakeUp, borderwidth=10, width=15, textvariable=self.Cushion)
        item5_entry.grid(row=4, column=1, padx=10)
        item5_button = Button(MakeUp, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.Cushion))
        item5_button.grid(row=4, column=2, padx=10)     

        item6 = Label(MakeUp, text="Foundation", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item6.grid(row=5, column=0, pady=15)
        item6_entry = Entry(MakeUp, borderwidth=10, width=15, textvariable=self.Foundation)
        item6_entry.grid(row=5, column=1, padx=10)
        item6_button = Button(MakeUp, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.Foundation))
        item6_button.grid(row=5, column=2, padx=10) 

        item7 = Label(MakeUp, text="Primer ", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item7.grid(row=6, column=0, pady=15)
        item7_entry = Entry(MakeUp, borderwidth=10, width=15, textvariable=self.Primer)
        item7_entry.grid(row=6, column=1, padx=10)
        item7_button = Button(MakeUp, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.Primer))
        item7_button.grid(row=6, column=2, padx=10) 


        # ===============================SKINCARE===============
        SkinCare = LabelFrame(self.root, text="SkinCare", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3", fg="#6C3483")
        SkinCare.place(x=400, y=180, height=380, width=325)

        item8_label = Label(SkinCare, text="Facewash", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item8_label.grid(row=0, column=0, pady=15)
        item8_entry = Entry(SkinCare, borderwidth=10, width=15, textvariable=self.facewash)
        item8_entry.grid(row=0, column=1, padx=10)
        item8_button = Button(SkinCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.facewash))
        item8_button.grid(row=0, column=2, padx=10)

        item9_label = Label(SkinCare, text="Toner", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item9_label.grid(row=1, column=0, pady=15)
        item9_entry = Entry(SkinCare, borderwidth=10, width=15, textvariable=self.toner)
        item9_entry.grid(row=1, column=1, padx=10)
        item9_button = Button(SkinCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.toner))
        item9_button.grid(row=1, column=2, padx=10)

        item10_label = Label(SkinCare, text="Essence", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item10_label.grid(row=2, column=0, pady=15)
        item10_entry = Entry(SkinCare, borderwidth=10, width=15, textvariable=self.essence)
        item10_entry.grid(row=2, column=1, padx=10)
        item10_button = Button(SkinCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.essence))
        item10_button.grid(row=2, column=2, padx=10)    

        item11_label = Label(SkinCare, text="Serum", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item11_label.grid(row=3, column=0, pady=15)
        item11_entry = Entry(SkinCare, borderwidth=10, width=15, textvariable=self.serum)
        item11_entry.grid(row=3, column=1, padx=10)
        item11_button = Button(SkinCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.serum))
        item11_button.grid(row=3, column=2, padx=10)

        item12_label = Label(SkinCare, text="Moisturizer", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item12_label.grid(row=4, column=0, pady=15)
        item12_entry = Entry(SkinCare, borderwidth=10, width=15, textvariable=self.moisturizer)
        item12_entry.grid(row=4, column=1, padx=10)
        item12_button = Button(SkinCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.moisturizer))
        item12_button.grid(row=4, column=2, padx=10)

        item13_label = Label(SkinCare, text="Sunscreen", font=("Arial Black", 11), bg="#E5B4F3", fg="#603483")
        item13_label.grid(row=5, column=0, pady=15)
        item13_entry = Entry(SkinCare, borderwidth=10, width=15, textvariable=self.sunscreen)
        item13_entry.grid(row=5, column=1, padx=10)
        item13_button = Button(SkinCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.sunscreen))
        item13_button.grid(row=5, column=2, padx=10)

        item14_label = Label(SkinCare, text="Masker", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item14_label.grid(row=6, column=0, pady=15)
        item14_entry = Entry(SkinCare, borderwidth=10, width=15, textvariable=self.masker)
        item14_entry.grid(row=6, column=1, padx=10)
        item14_button = Button(SkinCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.masker))
        item14_button.grid(row=6, column=2, padx=10)



        #-------------------------Body Care-----------------
        BodyCare = LabelFrame(self.root, text="BodyCare", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3", fg="#6C3483")
        BodyCare.place(x=800, y=180, height=380, width=325)

        item15_label = Label(BodyCare, text="Body Scrub", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item15_label.grid(row=0, column=0, pady=15)
        item15_entry = Entry(BodyCare, borderwidth=10, width=15, textvariable=self.body_scrub)
        item15_entry.grid(row=0, column=1, padx=10)
        item15_button = Button(BodyCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.body_scrub))
        item15_button.grid(row=0, column=2, padx=10)

        item16_label = Label(BodyCare, text="Shampoo ", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item16_label.grid(row=1, column=0, pady=15)
        item16_entry = Entry(BodyCare, borderwidth=10, width=15, textvariable=self.shampoo)
        item16_entry.grid(row=1, column=1, padx=10)
        item16_button = Button(BodyCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.shampoo))
        item16_button.grid(row=1, column=2, padx=10)

        item17_label = Label(BodyCare, text="Body Lotion", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item17_label.grid(row=2, column=0, pady=15)
        item17_entry = Entry(BodyCare, borderwidth=10, width=15, textvariable=self.lotion)
        item17_entry.grid(row=2, column=1, padx=10)
        item17_button = Button(BodyCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.lotion))
        item17_button.grid(row=2, column=2, padx=10)

        item18_label = Label(BodyCare, text="Hand Cream", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item18_label.grid(row=3, column=0, pady=15)
        item18_entry = Entry(BodyCare, borderwidth=10, width=15, textvariable=self.handcream)
        item18_entry.grid(row=3, column=1, padx=10)
        item18_button = Button(BodyCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.handcream))
        item18_button.grid(row=3, column=2, padx=10)

        item19_label = Label(BodyCare, text="Deodorant", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item19_label.grid(row=4, column=0, pady=15)
        item19_entry = Entry(BodyCare, borderwidth=10, width=15, textvariable=self.deodorant)
        item19_entry.grid(row=4, column=1, padx=10)
        item19_button = Button(BodyCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.deodorant))
        item19_button.grid(row=4, column=2, padx=10)

        item20_label = Label(BodyCare, text="Sunblock", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item20_label.grid(row=5, column=0, pady=15)
        item20_entry = Entry(BodyCare, borderwidth=10, width=15, textvariable=self.sunblock)
        item20_entry.grid(row=5, column=1, padx=10)
        item20_button = Button(BodyCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.sunblock))
        item20_button.grid(row=5, column=2, padx=10)

        item21_label = Label(BodyCare, text="Wax", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483")
        item21_label.grid(row=6, column=0, pady=15)
        item21_entry = Entry(BodyCare, borderwidth=10, width=15, textvariable=self.wax)
        item21_entry.grid(row=6, column=1, padx=10)
        item21_button = Button(BodyCare, text="+", font=("Arial Black", 15), height=0, width=3, bg="#FFFFFF", command=lambda: plusbutton(self.wax))
        item21_button.grid(row=6, column=2, padx=10)

        #------------------------------bill Area---------------------------

        billarea_Frame = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
        billarea_Frame.place(x=1190, y=182, width=330, height=375)
        bill_title = Label(billarea_Frame, text="Struk", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#E5B4F3", fg="#6C3483")
        bill_title.pack(fill=X)
        scrol_y = Scrollbar(billarea_Frame, orient=VERTICAL)
        self.txtarea = Text(billarea_Frame, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #==========================Bill menu=======================
        billing_menu = LabelFrame(self.root, text="Billing", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=620, relwidth=1, height=137)

        total_MakeUp = Label(billing_menu, text="Total Harga MakeUp ", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_MakeUp.grid(row=0, column=0)
        self.total_makeup = StringVar()
        total_MakeUp_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_makeup)
        total_MakeUp_entry.grid(row=0, column=1, padx=10, pady=7)

        total_SkinCare = Label(billing_menu, text="Total Harga SkinCare", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_SkinCare.grid(row=1, column=0)
        self.total_skincare = StringVar()
        total_SkinCare_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_skincare)
        total_SkinCare_entry.grid(row=1, column=1, padx=10, pady=7)

        total_BodyCare = Label(billing_menu, text="Total Harga Body Care ", font=("Arial Black", 11), bg="#A569BD", fg="white")
        total_BodyCare.grid(row=2, column=0)
        self.total_bodycare = StringVar()
        total_BodyCare_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_bodycare)
        total_BodyCare_entry.grid(row=2, column=1, padx=10, pady=7)

        tax_MakeUp = Label(billing_menu, text="Pajak MakeUp", font=("Arial Black", 11), bg="#A569BD", fg="white")
        tax_MakeUp.grid(row=0, column=2)
        self.a = StringVar()
        tax_MakeUp_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a)
        tax_MakeUp_entry.grid(row=0, column=3, padx=10, pady=7)

        tax_SkinCare = Label(billing_menu, text="Pajak SkinCare", font=("Arial Black", 11), bg="#A569BD", fg="white")
        tax_SkinCare.grid(row=1, column=2)
        self.b = StringVar()
        tax_SkinCare_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b)
        tax_SkinCare_entry.grid(row=1, column=3, padx=10, pady=7)
        
        tax_BodyCare = Label(billing_menu, text="Pajak Body Care", font=("Arial Black", 11), bg="#A569BD", fg="white")
        
        tax_BodyCare.grid(row=2, column=2)

        tax_BodyCare_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c)
        tax_BodyCare_entry.grid(row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=750, width=750, height=95)

        button_total = Button(button_frame, text="Hitung Total", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=lambda: total(self))
        button_total.grid(row=0, column=0, padx=12)

        button_clear = Button(button_frame, text="Bersihkan", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=lambda: clear(self))
        button_clear.grid(row=0, column=1, padx=10, pady=6)

        print_button = Button(button_frame, text="Cetak", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", width=8, command=lambda: on_print_button_click(self))
        print_button.grid(row=0, column=2, padx=10, pady=6)

        button_exit = Button(button_frame, text="Keluar", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", width=8, command=lambda: exit1(self))
        button_exit.grid(row=0, column=3, padx=10, pady=6)
        
        button_send = Button(button_frame, text="Kirim", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", width=8, command=lambda: send(self))
        button_send.grid(row=0, column=4, padx=10, pady=6)

        intro(self)
        billarea(self)
        
    def save_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.txtarea.get("1.0", "end"))
        
def plusbutton(item):
    current_value = int(item.get())
    new_value = current_value + 1
    item.set(str(new_value))

def send(self):
    phone_number = self.phone.get() # Replace with the input phone number
    
    # Get the text from the text area
    text = self.txtarea.get("1.0", "end")
    
    # Encode the text for the URL
    encoded_text = urllib.parse.quote(text)
    
    # Create the WhatsApp URL with the phone number and encoded text
    url = f"https://wa.me/{phone_number}?text={encoded_text}"
    
    # Open the URL in a web browser
    webbrowser.open(url)

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
    self.total_makeup.set(" Rp " + str(total_MakeUp_price))
    self.a.set(" Rp " + str(round(total_MakeUp_price * 0.05, 3)))
    self.at = self.facewash.get() * 52000
    self.pa = self.toner.get() * 90000
    self.oi = self.serum.get() * 120000
    self.ri = self.essence.get() * 120000
    self.su = self.moisturizer.get() * 55000
    self.te = self.masker.get() * 48000
    self.da = self.sunscreen.get() * 76000
    total_SkinCare_price = (self.at + self.pa + self.oi + self.ri + self.su + self.te + self.da)
    self.total_skincare.set(" Rp " + str(total_SkinCare_price))
    self.b.set(" Rp " + str(round(total_SkinCare_price * 0.01, 3)))

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
    self.total_bodycare.set(" Rp " + str(total_BodyCare_price))
    self.c.set(" Rp " + str(round(total_BodyCare_price * 0.10, 3)))
    
    total_bill = ( total_MakeUp_price + total_SkinCare_price + total_BodyCare_price + round(total_SkinCare_price * 0.01, 3) + round(total_BodyCare_price * 0.10, 3) +round(total_MakeUp_price * 0.05, 3) ) 
    
    self.total_all_bill =" Rp " +  str(total_bill)
    billarea(self)
    
def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(END, "WELCOME TO TRUE BEAUTY STORE\n\tPhone-No.08132428974")
    self.txtarea.insert(END, f"\n\nBill no.: {self.bill_no.get()}")

    self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
    self.txtarea.insert(END, f"\nPhone No.: {self.phone.get()}")
    self.txtarea.insert(END, "\n================================\n")
    self.txtarea.insert(END, "Product\t\tQty\tPrice\n")
    self.txtarea.insert(END, "\n================================\n")

def billarea(self):


    intro(self)
    if self.Liptint.get() != 0:
        self.txtarea.insert(END, f"Liptint\t\t{self.Liptint.get()}\tRp {self.nu}\n")
    if self.Highliter.get() != 0:
        self.txtarea.insert(END, f"Highliter\t\t{self.Highliter.get()}\tRp {self.no}\n")
    if self.Concealer.get() != 0:
        self.txtarea.insert(END, f"Concealer\t\t{self.Concealer.get()}\tRp {self.la}\n")
    if self.Eyeshadow.get() != 0:
        self.txtarea.insert(END, f"Eyeshadow\t\t{self.Eyeshadow.get()}\tRp {self.ore}\n")
    if self.Cushion.get() != 0:
        self.txtarea.insert(END, f"Cushion\t\t{self.Cushion.get()}\tRp {self.mu}\n")
    if self.Foundation.get() != 0:
        self.txtarea.insert(END, f"Foundation\t\t{self.Foundation.get()}\tRp {self.si}\n")
    if self.Primer.get() != 0:
        self.txtarea.insert(END, f"Primer\t\t{self.Primer.get()}\tRp {self.na}\n")
    if self.facewash.get() != 0:
        self.txtarea.insert(END, f"facewash\t\t{self.facewash.get()}\tRp {self.at}\n")
    if self.toner.get() != 0:
        self.txtarea.insert(END, f"toner\t\t{self.toner.get()}\tRp {self.pa}\n")
    if self.essence.get() != 0:
        self.txtarea.insert(END, f"essence\t\t{self.essence.get()}\tRp {self.ri}\n")
    if self.serum.get() != 0:
        self.txtarea.insert(END, f"serum\t\t{self.serum.get()}\tRp {self.oi}\n")
    if self.moisturizer.get() != 0:
        self.txtarea.insert(END, f"moisturizer\t\t{self.moisturizer.get()}\tRp {self.su}\n")
    if self.sunscreen.get() != 0:
        self.txtarea.insert(END, f"Sunscreen\t\t{self.sunscreen.get()}\tRp {self.da}\n")
    if self.masker.get() != 0:
        self.txtarea.insert(END, f"masker\t\t{self.masker.get()}\tRp {self.te}\n")
    if self.body_scrub.get() != 0:
        self.txtarea.insert(END, f"Body scrub\t\t{self.body_scrub.get()}\tRp {self.body_scrub_price}\n")
    if self.shampoo.get() != 0:
        self.txtarea.insert(END, f"Shampoo\t\t{self.shampoo.get()}\tRp {self.shampoo_price}\n")
    if self.lotion.get() != 0:
        self.txtarea.insert(END, f"Lotion\t\t{self.lotion.get()}\tRp {self.lotion_price}\n")
    if self.handcream.get() != 0:
        self.txtarea.insert(END, f"Hand Cream\t\t{self.handcream.get()}\tRp {self.handcream_price}\n")
    if self.deodorant.get() != 0:
        self.txtarea.insert(END, f"Deodorant\t\t{self.deodorant.get()}\tRp {self.deodorant_price}\n")
    if self.sunblock.get() != 0:
        self.txtarea.insert(END, f"Sunblock\t\t{self.sunblock.get()}\tRp {self.sunblock_price} \n")
    if self.wax.get() != 0:
        self.txtarea.insert(END, f"Wax\t\t{self.wax.get()}\tRp {self.wax_price} \n")
    self.txtarea.insert(END, f"\n--------------------------------\n")
    if self.a.get() != '':
        self.txtarea.insert(END, f"Total MakeUp Tax: {self.a.get()}\n")
    if self.b.get() != '':
        self.txtarea.insert(END, f"Total SkinCare Tax {self.b.get()}\n")
    if self.c.get() != '':
        self.txtarea.insert(END, f"Total BodyCare Tax {self.c.get()}\n")

    self.txtarea.insert(END, "\n---------------------------------\n")
    self.txtarea.insert(END, f"\nTotal Bill Amount {self.total_all_bill}\n")
    
    self.txtarea.insert(END, f"\n\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    self.txtarea.insert(END, "\nTerima Kasih dan Sampai Jumpa\n")

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
    self.total_makeup.set('0.0')
    self.total_skincare.set('0.0')
    self.total_bodycare.set('0.0')
    self.a.set('0.0')
    self.b.set('0.0')
    self.c.set('0.0')
    self.c_name.set('')
    self.bill_no.set('')
    self.phone.set('')

def exit1(self):
    self.root.destroy()
    
def on_print_button_click(self):
    result = messagebox.askyesno("Cetak", "Cetak billing?")
    if result:
        self.save_to_file()
    
def save_to_file(self):
    file_path = "bill.txt"  # Path/lokasi file untuk menyimpan teks
    text_content = self.txtarea.get("1.0", "end-1c")  # Mendapatkan isi teks dari Text area

    with open(file_path, "w") as file:
        file.write(text_content)





# copas diatas ini yakkk....
root = Tk()
bill_app = true_beauty(root)
root.mainloop()
