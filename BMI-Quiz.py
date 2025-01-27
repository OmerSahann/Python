import tkinter

from scipy.integrate import lebedev_rule

window=tkinter.Tk()
window.title("BMI Calculator")
window.minsize(height=250,width=250)
window.config(pady=10)

label1=tkinter.Label(text="Enter Your Weight(kg)")
label1.pack()

enter1=tkinter.Entry()
enter1.pack()

label2=tkinter.Label(text="Enter Your Height(cm)")
label2.pack()

enter2=tkinter.Entry()
enter2.pack()

label3=tkinter.Label()
label3.pack()

def hesapla():
    try:
        kilo = int(enter1.get())
        boy = int(enter2.get()) / 100
        bmı = kilo / (boy ** 2)
    except ZeroDivisionError:
        label3.config(text="Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")
    except ValueError:
        label3.config(text="Geçerli bir sayı girmelisiniz.")
    else:
        if(bmı<=0):
            label3.config(text="Hatalı giriş yaptınız")
        else:
            text=""
            if(bmı<18.5):
                text="Underweight."
            elif(bmı<=24.9):
                text="Healty."
            elif(bmı<=29.9):
                text="Overweight"
            elif(bmı<=39.9):
                text="Obese"
            elif(bmı>=40):
                text="Externaly Obese"
            label3.config(text=f'Your BMI is {round(bmı,2)}. You are {text}')


buton=tkinter.Button(text="Calculate",command=hesapla)
buton.pack()




window.mainloop()