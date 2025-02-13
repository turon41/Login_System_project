from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1067x600+100+50")
        self.root.resizable(False,False)


        #BACKGROUND IMAGE
        self.bg = ImageTk.PhotoImage(file="images/desktop-wallpaper-login2.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight = 1)


        #LOGIN FRAME
        Frame_Login =  Frame(self.root, bg="white")
        Frame_Login.place(x=330, y=150, width=500, height = 400)

        #TITLE AND SUBTITLE
        title = Label(Frame_Login, text="Login Here", font=("Impact",35, "bold"), fg="blue", bg="white").place(x=90,y=30)
        subtitle = Label(Frame_Login, text="Members Login Area", font=("Goudy old style",15, "bold"), fg="black", bg="white").place(x=90,y=100)


        #USERNAME

        lbl_user= Label(Frame_Login, text="Username", font=("Goudy old style",15, "bold"), fg="grey", bg="white").place(x=90,y=140)
        self.username = Entry(Frame_Login,  font=("Goudy old style",15), bg="white")
        self.username.place(x=90,y=170,width = 320, height = 35)



        #PASSWORD

        lbl_password= Label(Frame_Login, text="Password", font=("Goudy old style",15, "bold"), fg="grey", bg="white").place(x=90,y=210)
        self.password = Entry(Frame_Login, font=("Goudy old style",15), bg="white")
        self.password.place(x=90,y=240,width = 320, height = 35)


        #BUTTON

        forget = Button(Frame_Login, cursor = "hand2", text="Forgot Password", bd=0, font=("Goudy old style",12), fg="blue", bg="white").place(x=90,y=280)
        submit = Button(Frame_Login, command= self.check_function, cursor = "hand2", text="Login?", bd=0, font=("Goudy old style",15, "bold"), bg="blue", fg="white").place(x=90,y=320, width = 180, height =40)

    def check_function(self):
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("Error", "All fields are required",parent = self.root)

            elif self.username.get()!="turon41" or self.password.get()!="123456":
                messagebox.showerror("Error", "Invalid Username or Password",parent = self.root)

            else:
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")



root = Tk()
obj = Login(root)
root.mainloop()