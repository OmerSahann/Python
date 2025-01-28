import tkinter
import base64
from tkinter import messagebox, END

window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(height=500, width=250)
window.config(pady=10)

# Resim Yeri
image = tkinter.PhotoImage(file="topsecret.png")
image_label = tkinter.Label(image=image)
image_label.pack()

# Title Yerleri
title_label = tkinter.Label(text="Enter your title")
title_label.pack()

title_entry = tkinter.Entry()
title_entry.pack()

# Secret Yerleri
secret_label = tkinter.Label(text="Enter your secret")
secret_label.pack()

secret_text = tkinter.Text(height=10, width=20)
secret_text.pack()

# Key Yerleri
key_label = tkinter.Label(text="Enter master key")
key_label.pack()

key_entry = tkinter.Entry()
key_entry.pack()


def encode(key, clear):
    try:
        if not key or not clear:
            raise ValueError("Anahtar veya metin boş olamaz!")

        enc = []
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
            enc.append(enc_c)

        encoded_string = "".join(enc).encode('utf-8')
        return base64.urlsafe_b64encode(encoded_string).decode('utf-8')

    except Exception as e:
        messagebox.showerror("Hata", f"Şifreleme işlemi sırasında hata oluştu: {e}")
        return None


def decode(key, enc):
    try:
        if not key or not enc:
            raise ValueError("Anahtar veya şifreli metin boş olamaz!")

        dec = []
        decoded_bytes = base64.urlsafe_b64decode(enc.encode('utf-8'))
        enc = decoded_bytes.decode('utf-8')

        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)

        return "".join(dec)

    except Exception as e:
        messagebox.showerror("Hata", f"Çözme işlemi sırasında hata oluştu: {e}")
        return None


def şifrele():
    mesaj = secret_text.get("1.0", END).strip()
    master_key = key_entry.get().strip()

    if not master_key or not mesaj:
        messagebox.showwarning("Eksik Bilgi", "Lütfen hem anahtar hem de şifreli metni girin!")
        return None

    return encode(master_key, mesaj)


def çöz():
    master_key = key_entry.get().strip()
    şifreli_metin = secret_text.get("1.0", END).strip()

    if not master_key or not şifreli_metin:
        messagebox.showwarning("Eksik Bilgi", "Lütfen hem anahtar hem de şifreli metni girin!")
        return None

    return decode(master_key, şifreli_metin)


def Encription_işlemleri():
    title = title_entry.get().strip()

    if not title:
        messagebox.showwarning("Eksik Bilgi", "Lütfen başlık girin!")
        return

    şifreli_metin = şifrele()
    if şifreli_metin:
        with open("mysecret.txt", "a", encoding="utf-8") as file:
            file.write(title)
            file.write("\n")
            file.write(şifreli_metin)
            file.write("\n")


def Decription_işlemleri():
    çözülecek_metin = çöz()
    if çözülecek_metin:
        secret_text.delete("1.0", END)
        secret_text.insert("1.0", çözülecek_metin)


# Butonlar
save_button = tkinter.Button(text="Save & Encrypt", command=Encription_işlemleri)
save_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", command=Decription_işlemleri)
decrypt_button.pack()

window.mainloop()
