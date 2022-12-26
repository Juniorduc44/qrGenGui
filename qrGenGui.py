from tkinter import *
import pyqrcode
import PIL.Image, PIL.ImageTk
from customtkinter import *
import customtkinter


#create the theme for the app
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
#other modes: system(default), light.
#Other Themes: blue(default), dark-blue.



#variable for creating the initial window(frame) and title for the app
app = customtkinter.CTk()
app.geometry("400x300")
app.title("Qr Code Generator")




def create_code():
    global label2
    # getting the text
    qr1 = entry1.get()
    #create code from entry
    qr2 = pyqrcode.create(qr1)
    #Create name for image
    img = "qr-codify2.png"
    #saving name by setting png file designation
    qr2.png(img, scale=5)
    #opening the qrcode in app
    get_image = PIL.ImageTk.PhotoImage(PIL.Image.open(img))
    
    #Labels
    label2 = Label(app, image=get_image)
    label2.image = get_image
    label2.pack(pady=5, padx=10)


def clear_all():
    entry1.delete(0, -1)
    label2.destroy()



# Create Gui 
#entry box for the input to be generated as qr code
entry1 = customtkinter.CTkEntry(app, placeholder_text = "Enter Data Here", font=("Comic Sans", 12))
entry1.pack(padx=3, pady=10)

#button creation
button1 = customtkinter.CTkButton(app, text="Create QR Code", command=create_code).pack(pady=5)
button2 = customtkinter.CTkButton(app, text="Clear", command=clear_all).pack(pady=5)

#result of the QR Code
label1 = customtkinter.CTkLabel(app, text='')
label1.pack(pady=10)

app.mainloop()