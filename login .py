from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk 
import sqlite3
# pip install pymysql
class Login_Window:
	def __init__(self,root):
		self.root=root
		self.root.title("Login Window")
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="white")


                #===Bg Image===
		self.bg=ImageTk.PhotoImage(file="b4.jpg")
		bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

		#===Bg Colors===
		left_lbl=Label(self.root,bg="#08A3D2",bd=0)
		left_lbl.place(x=0,y=0,relheight=1,width=600)

		right_lbl=Label(self.root,bg="#031F3C",bd=0)
		right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

		#===Frames===
		login_frame=Frame(self.root,bg="white")
		login_frame.place(x=250,y=100,width=800,height=515)

		title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

		email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=250,y=150)
		self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgrey")
		self.txt_email.place(x=250,y=180,width=350,height=35)

		pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=250,y=250)
		self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgrey",show="*")
		self.txt_pass_.place(x=250,y=280,width=350,height=35)

		btn_reg=Button(login_frame,text="Register new Account?",command=self.login,font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)

		btn_login=Button(login_frame,text="Login",command=self.dashboard,font=("times new roman",20,"bold"),fg="white",bg="#B00857").place(x=250,y=360,width=180,height=40)

	def login(self):


	
		#===LEFT Image===
		self.bg=ImageTk.PhotoImage(file="loginside.png")
		left=Label(self.root,image=self.bg).place(x=80,y=120,width=350)

		#===Login Frame===
		#frame1=Frame(self.root,bg="white")
		#frame1.place(x=450,y=100,width=700,height=500)
		self.root.destroy()
		import registerpage

	def dashboard(self):
		if self.txt_email.get()=="" or self.txt_pass_.get()=="":
			messagebox.showerror("Error","All Fields Are Required",parent=self.root)
		else:
			messagebox.showinfo("You have logged in successfully")
			self.root.destroy()
			import newfile







root=Tk()
obj=Login_Window(root)
root.mainloop()
