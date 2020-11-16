from  tkinter import *
from PIL import Image,ImageTk
def fun1():
    class first:
        print("THIS PROJECT IS OUR FIRST PROJECT ON GUI TKINTER PYTHON ",'\n',"THIS IS BASED ON BANKING SYSTEM ",'\n',"USER HAVE OPEN ACCOUNT,DEPOSIT ,WITHDRAWL AMOUNT ")
        def __init__(self, a, b, c, d, e, f, g, x):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f
            self.g = g
            self.x = x

        def fun1(self):
            f = open("BANK.txt", "w")
            print("ENTER ACCOUNT HOLDER NAME:")
            self.a = str(input())
            f.write(str(self.a) + '\n')
            print("ENTER IFSC CODE")
            self.b = str(input())
            f.write(str(self.b) + '\n')
            print("ENTER ACCOUNT NUMBER")
            self.c = int(input())
            f.write(str(self.c) + '\n')
            print("ENTER CITY")
            self.d = str(input())
            f.write(str(self.d) + '\n')
            print("ENTER ACCOUNT BALANCE")
            self.e = int(input())
            f.write(str(self.e) + '\n')
            print(self.a)
            print(self.b)
            print(self.c)
            print(self.d)
            print(self.e)
            f.close()

        def fun2(self):
            print("ENTER DEPOSIT AMOUNT ")
            self.f = int(input())
            print(self.f)
            self.e = int(self.e) + int(self.f)
            print("AFTER DEPOSIT BALANCE IS ", self.e)


        def fun3(self):
            print("ENTER WITHDRAWL AMOUNT")
            self.g = int(input())
            print(self.g)

            self.e = int(self.e) - int(self.g)
            print("AFTER WITHDRAWL AMOUNT", self.e)


    f1 = first(a=print(), b=print(), c=print(), d=print(), e=print(), f=print(), g=print(), x=print())

    while (1):
        print("ENTER 1 FOR OPEN ACCOUNT")
        print("ENTER 2 FOR DEPOSIT AMOUNT")
        print("ENTER 3 FOR WITHDRWAL AMOUNT")
        print("ENTET 4 FOR EXIT")
        var1 = int(input())
        if (var1 == 1):
            f1.fun1()
        elif (var1 == 2):
            f1.fun2()
        elif (var1 == 3):
            f1.fun3()
        else:
            print("THX FOR THE SHOW OUR SMALL PROJECT BANKING RELETED")
            exit()


root=Tk()
root.geometry("735x435")
root.maxsize(700,500)
root.title("REGESTRATION FORM")
root.wm_iconbitmap("77.ico")
root.config(background="black")
image=Image.open("logo.jpg")
image = image.resize((150, 150), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
#image = image.resize((350, 350), Image.ANTIALIAS)
var1=Label(image=photo)
var1.pack()

label_0 =Label(root,text="Log-IN form", width=15,font=("bold",15))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=265,y=170)

label_1 =Label(root,text="FullName", width=15,font=("bold",10))
label_1.place(x=265,y=215)

#this will accept the input string text from the user.
entry_1=Entry(root)
entry_1.place(x=420 ,y=215)

label_2 =Label(root,text="MOBILE NO", width=15,font=("bold",10))
label_2.place(x=265,y=260)

#this will accept the input string text from the user.
entry_2=Entry(root)
entry_2.place(x=420 ,y=260)

label_3 =Label(root,text="PASSWORD", width=15,font=("bold",10))
label_3.place(x=265,y=305)

#this will accept the input string text from the user.
entry_3=Entry(root)
entry_3.place(x=420 ,y=305)

Button(root, text='Log-In' , width=15,bg="white",fg='black',font=("bold",10),command=fun1).place(x=335,y=350)
root.mainloop()
