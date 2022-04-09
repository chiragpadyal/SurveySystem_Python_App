from multiprocessing import parent_process
import re
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql_conn

import mysql.connector
from mysql.connector import Error
# import login

class Register:
	def __init__(self,root):
		self.root=root
		self.root.title("Registration Window")
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="white")

		#===Bg Image===
		self.bg=ImageTk.PhotoImage(file="b3.jpg")
		bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

		#===LEFT Image===
		self.left=ImageTk.PhotoImage(file="side2.jpg")
		left=Label(self.root,image=self.left).place(x=80,y=80,width=400,height=500)

		#===Register Frame===
		frame1=Frame(self.root,bg="white")
		frame1.place(x=480,y=80,width=700,height=500)

		title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

		#---------------Row1
		
		f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
		self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_fname.place(x=50,y=130,width=250)

		l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
		self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_lname.place(x=370,y=130,width=250)

		#---------------Row2

		contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
		self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_contact.place(x=50,y=200,width=250)

		email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
		self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_email.place(x=370,y=200,width=250)



		#---------------Row3

		question=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)

		self.gender=StringVar()
		self.g1=Radiobutton(frame1,text="Male",variable=self.gender,value="Male",font=("times new roman",15))
		self.g1.select()
		self.g1.place(x=50,y=270)

		self.g2=Radiobutton(frame1,text="Female",variable=self.gender,value="Female",font=("times new roman",15))
		self.g2.deselect()
		self.g2.place(x=210,y=270)


		#cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
		#cmb_quest['values']=("Select","Male","Female")
		#cmb_quest.place(x=50,y=270,width=250)
		#cmb_quest.current(0)




		#answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
		#txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=270,width=250)





		#---------------Row4

		password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
		self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
		self.txt_password.place(x=50,y=340,width=250)

		cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
		self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
		self.txt_cpassword.place(x=370,y=340,width=250)

		#------Terms------
		self.var_chk=IntVar()
		chk=Checkbutton(frame1,text="I Agree The Terms & Conditions.",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

		self.btn_img=ImageTk.PhotoImage(file="register.png")
		Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

		# Button(self.root,text="Sign In",font=("times new roman",20),bg="black",fg="white",bd=0,cursor="hand2").place(x=200,y=460,width=180)
	

	def validEmail(self, email):
		regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
		if(re.fullmatch(regex, email)):
			return False
		else:
			return True

	def validNumber(self, phone_nuber):
		pattern = re.compile("^[\d1-9]{10}$", re.IGNORECASE)
		if pattern.match(phone_nuber) is not None :
			return False
		else :
			return True

	def register_data(self):
		if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="":
			messagebox.showerror("Error","All Fields Are Required",parent=self.root)
		elif self.txt_password.get()!=self.txt_cpassword.get():
			messagebox.showerror("Error","Password & Confirm password should be same",parent=self.root)
		elif self.validEmail(self.txt_email.get()):
			messagebox.showerror("Error","Check Email",parent=self.root)
		elif self.validNumber(self.txt_contact.get()):
			messagebox.showerror("Error","Check Phone Number",parent=self.root)
		elif self.var_chk.get()==0:
			messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)
		else:
			messagebox.showinfo("Success","Register Successful",parent=self.root)
			self.mysql_add()


	def mysql_add(self):
		FirstName = self.txt_fname.get()
		LastName = self.txt_lname.get()
		Contact = self.txt_contact.get()
		Email = self.txt_email.get()
		Gender = self.gender.get()
		Password = self.txt_password.get()

		try:
			mydb = mysql_conn.mydb
			mycursor = mydb.cursor()
			sql = "INSERT INTO `regTable` ( `Firstname`, `lastname`, `Contact`, `Email`, `Gender`, `Password`) VALUES ( %s, %s, %s, %s, %s, %s ) "
			val_arr = (FirstName, LastName, Contact, Email, Gender, Password)
			mycursor.execute(sql, val_arr)
			mydb.commit()
			mycursor.close()
			mydb.close()
			self.root.destroy()
			import login
		except Error as err:
			print(err)




root=Tk()
root.geometry("500x650")
obj=Register(root)
root.mainloop()
