from tkinter import *
from PIL import ImageTk  # pip install p

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Survey Creation And Analytics")
        self.root.geometry("3264x1633+100+50")
        self.root.resizable(True, True)
        # ====BG Image=====
        self.bg = ImageTk.PhotoImage(file="logo.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Exp_btn = Button(self.root, text="Real Life Experience With SUZUKi", fg="white", bg="#d77337",
                         font=("times new roman", 15)).place(x=260, y=350)

        Exp_btn = Button(self.root, text="Real Life Experience With TATA", fg="white", bg="#d77337",
                         font=("times new roman", 15)).place(x=1000, y=350)

        Exp_btn = Button(self.root, text="Real Life Experience With HONDA", fg="white", bg="#d77337",
                         font=("times new roman", 15)).place(x=260, y=718)

        Exp_btn = Button(self.root, text="Real Life Experience With TOYOTA", fg="white", bg="#d77337",
                         font=("times new roman", 15)).place(x=1000, y=720)


root = Tk()
obj = Login(root)
root.mainloop()
