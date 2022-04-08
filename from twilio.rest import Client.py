from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(True,True)
        self.n = random.randint(1000,9999)
        self.client=Client("ACeae2cdfa44a9d923e0e70d78c3d8d4be","26b0436edbf1194ce08c66db69949a84")
        self.client.messages.create(to =["+919967104460"],
                                   from_ = "+14302340637",
                                   body=self.n)

    
    def Labels(self):
        self.c = Canvas(self,bg = "white",width=400, height=450)
        self.c.place(x=100,y=60)

        self.Login_Title=Label(self,text="OTP Verification",font="bold, 20",bg="white")
        self.Login_Title.place(x=210,y=90)

        self.q = Label(self,text="Enter The mobile no.",font="arial, 10",bg="white")
        self.q.place(x=230,y=140)

        self.p = Label(self,text="Enter the OTP",font="arial, 10",bg="white")
        self.p.place(x=230,y=220)



    def Entry(self):
        self.User_Name=Text(self, borderwidth=2, wrap="word",width=29,height=2)
        self.User_Name.place(x=190,y=250)

        self.number=Text(self, borderwidth=2, wrap="word",width=29,height=2)
        self.number.place(x=190,y=160)


    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="submit .png")
        self.submitButton=Button(self,image=self.submitButtonImage,command=self.checkOTP,border=0)
        self.submitButton.place(x=180,y=300)

        self.resendOTPImage=PhotoImage(file="resendotp.png")
        self.resendOTP=Button(self,image=self.resendOTPImage,command=self.resendOTP,border=0)
        self.resendOTP.place(x=180,y=400)
        

    
    def checkOTP(self):
        try:
            self.userInput=int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo", "OTP verified")
                self.n="done"

            elif self.n=="done":
                messagebox.showinfo("showinfo", "already Login")
            else:
                messagebox.showinfo("showinfo", "wrong OTP")
        except:
            messagebox.showinfo("showinfo", "Invalid OTP")


    def resendOTP(self):
        self.n = random.randint(1000,9999)
        self.client=Client("ACeae2cdfa44a9d923e0e70d78c3d8d4be","26b0436edbf1194ce08c66db69949a84")
        self.client.messages.create(to =["+919967104460"],
                                   from_ = "+14302340637",
                                   body=self.n)
        
    
    


if __name__=="__main__":
    window=otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()
