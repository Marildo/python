from tkinter import *

app = Tk()
app.title("Tk Inter")
app.geometry("500x400")
app.config(background="#007")

txt1 = Label(app, text="Verify files", background="#ff0", foreground="#000")
txt1.place(x=10, y=10, width=100, height=20)

txt2 = Label(app, text="Segundo label", bg="#ffb", fg="#aad")
txt2.pack(ipadx=1, ipady=1, padx=2, pady=3, side="top")
app.mainloop()