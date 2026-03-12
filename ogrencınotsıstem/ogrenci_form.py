import tkinter as tk
from tkinter import messagebox
import mysql.connector

def kaydet():
    adi = entry_adi.get()
    soyadi = entry_soyadi.get()
    sifre = entry_sifre.get()
    vize = int(entry_vize.get())
    final = int(entry_final.get())
    ort = (vize+final)/2
    gectiMi = "EVET" if ort >= 50 else "HAYIR"
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kitrvm231229069",  # MySQL şifren
        database="okuldb"
    )
    cursor = conn.cursor()
    sql = "INSERT INTO ogrenciler (adi, soyadi, sifre, vize, final, ort, gectiMi) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (adi, soyadi, sifre, vize, final, ort, gectiMi)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Başarılı", f"Öğrenci kaydedildi!\nOrtalama: {ort}\nGeçti Mi: {gectiMi}")

root = tk.Tk()
root.title("Öğrenci Bilgi Formu")

tk.Label(root, text="Ad:").grid(row=0, column=0)
entry_adi = tk.Entry(root)
entry_adi.grid(row=0, column=1)

tk.Label(root, text="Soyad:").grid(row=1, column=0)
entry_soyadi = tk.Entry(root)
entry_soyadi.grid(row=1, column=1)

tk.Label(root, text="Şifre:").grid(row=2, column=0)
entry_sifre = tk.Entry(root, show="*")
entry_sifre.grid(row=2, column=1)

tk.Label(root, text="Vize:").grid(row=3, column=0)
entry_vize = tk.Entry(root)
entry_vize.grid(row=3, column=1)

tk.Label(root, text="Final:").grid(row=4, column=0)
entry_final = tk.Entry(root)
entry_final.grid(row=4, column=1)

tk.Button(root, text="Kaydet", command=kaydet).grid(row=5, column=0, columnspan=2)

root.mainloop()