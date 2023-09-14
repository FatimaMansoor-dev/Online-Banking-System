import os
import random
import time
import tkinter
from captcha.image import ImageCaptcha
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from abc import ABC, abstractmethod

'''class Bank in composition with class Accounts and Customer '''
class Bank(Tk):
    class Customer:
        '''inititalizing empty list that will store user credentials'''
        list = []
        loggedin = False
        class Account(ABC):
            def __init__(self, balance=0):
                self.balance = balance
                for frame in window.mainframe.winfo_children():
                    frame.destroy()

                '''Making buttons to display when logged in'''
                self.lb = Button(window.mainframe,text="LOG OUT", command=self.logout, bg="black", highlightbackground="white",
                                 fg="white", font="Bold 16", highlightthickness=3)
                self.lb.grid(row=0,column=1,pady=400)
                '''button for delete account'''
                self.db = Button(window.mainframe, text="Delete Account", command=self.delete_acc, bg="black",
                                 highlightbackground="white", fg="white", font="Bold 16", highlightthickness=3)
                self.db.grid(row=0,column=0,padx=30,pady=400)
                ''' button to change password'''
                self.cp= Button(window.mainframe,text="CHANGE PASSWORD", command=self.changePass, bg="black", highlightbackground="white",
                                 fg="white", font="Bold 16", highlightthickness=3)
                self.cp.grid(row=0,column=2,pady=400,padx=30)



                ''' frame for options of transactions'''
                self.optionsFrame = Frame(window.mainframe)
                self.optionsFrame.config(bg="black")
                self.optionsFrame.place(x=50, y=50)
                '''buttons for transaction options'''
                Label(self.optionsFrame, text="SELECT YOUR CHOICE   ☻", font="Bold 20", bg="black", fg="white").place(
                    x=10, y=0)
                self.depositButton = Button(self.optionsFrame)
                self.depositButton.config(bg="white",
                                          fg="purple",
                                          font="bold 20",
                                          relief="groove",
                                          text="DEPOSIT",
                                          command=self.deposit
                                          )
                self.depositButton.grid(row=2, column=2, padx=20, pady=50)

                self.withdrawButton = Button(self.optionsFrame)
                self.withdrawButton.config(bg="#ffffff",
                                           fg="purple",
                                           font="bold 20",
                                           relief="groove",
                                           command=self.withdraw
                                           )
                if Bank.Customer.list[3] != "loan":
                    self.withdrawButton.config(text="withdraw")
                else:
                    self.withdrawButton.config(text="Apply for loan")
                self.withdrawButton.grid(row=2, column=3, pady=50)
                '''balance enquiry'''
                self.enquiryButton = Button(self.optionsFrame)
                self.enquiryButton.config(bg="white",
                                          fg="purple",
                                          font="bold 20",
                                          relief="groove",
                                          text="Balance Enquiry",
                                          command=self.balanceEnquiry
                                          )
                self.enquiryButton.grid(row=2, column=4, padx=20, pady=50)

            def deposit(self):
                self.optionsFrame.destroy()
                '''making new frame for depositing'''
                self.transactionFrame = Frame()
                self.transactionFrame.config(bg="black")
                self.transactionFrame.place(x=520, y=250)


                self.entry = Entry(width=20, font=("Adobe Gothic Std", 15))
                self.entry.place(x=460, y=190)
                Button(self.transactionFrame, text="1", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(1)).grid(row=2, column=0, padx=2, pady=2)
                Button(self.transactionFrame, text="2", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(2)).grid(row=2, column=1, padx=2, pady=2)
                Button(self.transactionFrame, text="3", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(3)).grid(row=2, column=2, padx=2, pady=2)
                Button(self.transactionFrame, text="4", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(4)).grid(row=3, column=0, padx=2, pady=2)
                Button(self.transactionFrame, text="5", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(5)).grid(row=3, column=1, padx=2, pady=2)
                Button(self.transactionFrame, text="6", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(6)).grid(row=3, column=2, padx=2, pady=2)
                Button(self.transactionFrame, text="7", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(7)).grid(row=4, column=0, padx=2, pady=2)
                Button(self.transactionFrame, text="8", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(8)).grid(row=4, column=1, padx=2, pady=2)
                Button(self.transactionFrame, text="9", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(9)).grid(row=4, column=2, padx=2, pady=2)
                Button(self.transactionFrame, text="0", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(0)).grid(row=5, column=1, padx=2, pady=2)
                '''button for clear text'''
                Button(self.transactionFrame, text="CLEAR", font="arial 10", height=3, relief="sunken", bg="black",
                       fg="white",
                       command=self.delete).grid(row=5, column=0, padx=2, pady=2)
                '''done button'''
                Button(self.transactionFrame, text="DONE", height=2, font="arial 15", relief="sunken", bg="black",
                       fg="white",
                       command=self.getDepositionAmount).grid(row=5, column=2, padx=2, pady=2)

            def getDepositionAmount(self):

                self.amountToDeposit = int(self.entry.get())
                '''datetime'''
                self.localtime = time.asctime((time.localtime(time.time())))
                '''depositing amount and appending the balance and time in list that is to be written in file'''
                if Bank.Customer.list[3] != "loan":
                    self.balance=Bank.Customer.list[-1][-1]
                    self.balance += self.amountToDeposit
                    Bank.Customer.list.append([self.localtime, self.balance])
                    messagebox.showinfo("deposition",
                                        f"You successfully deposited RS. {int(self.entry.get())}."
                                        f" your current balance is RS. {int(self.balance)}")

                self.transactionFrame.destroy()
                self.entry.destroy()

            ''' withdraw '''
            def withdraw(self):
                self.optionsFrame.destroy()
                '''making new frame for withdrawal'''
                self.transactionFrame = Frame()
                self.transactionFrame.config(bg="black")
                self.transactionFrame.place(x=520, y=240)
                '''cal'''
                self.entry = Entry(width=20, font=("Adobe Gothic Std", 17))
                self.entry.place(x=470, y=190)
                Button(self.transactionFrame, text="1", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(1)).grid(row=2, column=0, padx=2, pady=2)
                Button(self.transactionFrame, text="2", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(2)).grid(row=2, column=1, padx=2, pady=2)
                Button(self.transactionFrame, text="3", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(3)).grid(row=2, column=2, padx=2, pady=2)
                Button(self.transactionFrame, text="4", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(4)).grid(row=3, column=0, padx=2, pady=2)
                Button(self.transactionFrame, text="5", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(5)).grid(row=3, column=1, padx=2, pady=2)
                Button(self.transactionFrame, text="6", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(6)).grid(row=3, column=2, padx=2, pady=2)
                Button(self.transactionFrame, text="7", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(7)).grid(row=4, column=0, padx=2, pady=2)
                Button(self.transactionFrame, text="8", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(8)).grid(row=4, column=1, padx=2, pady=2)
                Button(self.transactionFrame, text="9", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(9)).grid(row=4, column=2, padx=2, pady=2)
                Button(self.transactionFrame, text="0", font="arial 20", relief="sunken", bg="orange",
                       command=lambda: self.display(0)).grid(row=5, column=1, padx=2, pady=2)
                '''button for clear text'''
                Button(self.transactionFrame, text="CLEAR", font="arial 10", height=3, relief="sunken", bg="black",
                       fg="white",
                       command=self.delete).grid(row=5, column=0, padx=2, pady=2)
                '''done button'''
                Button(self.transactionFrame, text="DONE", height=2, font="arial 15", relief="sunken", bg="black",
                       fg="white",
                       command=self.getWithdrawalAmount).grid(row=5, column=2, padx=2, pady=2)

            def getWithdrawalAmount(self):

                self.amountToWithdraw = int(self.entry.get())
                '''datetime'''
                self.localtime = time.asctime((time.localtime(time.time())))

                if Bank.Customer.list[3] != "loan":
                    ''' checking if the amount is smaller than current balance for checking and savings account'''
                    if self.amountToWithdraw > Bank.Customer.list[-1][-1] and Bank.Customer.list[3] == "saving":
                        messagebox.showerror("invalid", "Amount larger than current balance.")
                        self.transactionFrame.destroy()
                        self.entry.destroy()
                        return
                    elif self.amountToWithdraw > self.balance and Bank.Customer.list[3] == "checking":
                        self.transactionFrame.destroy()
                        self.entry.destroy()

                    else:
                        '''if not, append it to the list'''
                        self.balance =Bank.Customer.list[-1][-1]
                        self.balance-=int(self.entry.get())
                        Bank.Customer.list.append([self.localtime, self.balance])

                        for widget in window.mainframe.winfo_children():
                            widget.destroy()

                else:
                    self.principleAmount = 0 - self.amountToWithdraw

                self.transactionFrame.destroy()
                self.entry.destroy()


            '''methods'''
            def continuetransaction(self):
                self.__init__()
            def delete(self):
                self.entry.delete(0, END)

            def display(self, text):
                self.leng = len(self.entry.get())
                self.entry.insert(self.leng, text)

            def balanceEnquiry(self):
                for frame in window.mainframe.winfo_children():
                    frame.destroy()
                self.enquiryframe = Frame(window.mainframe)
                self.enquiryframe.config(bg="#000000")
                self.enquiryframe.place(x=10, y=10)
                self.balancephoto = PhotoImage(file="./icons/balance.png")
                Label(self.enquiryframe, image=self.balancephoto).grid(row=2, column=1)
                if Bank.Customer.list[3]!="loan":

                    Label(self.enquiryframe, text=f"YOUR CURRENT BALANCE IS RS. {self.balance}/-", font="Bold 20",
                          bg="#000000", fg="#ffffff").grid(pady=2)
                Button(self.enquiryframe, text="Back", command=self.back).grid(row=4, column=2)
            def back(self):
                self.enquiryframe.destroy() 
                self.optionsFrame = Frame(window.mainframe)
                self.optionsFrame = Frame(window.mainframe)
                self.optionsFrame.config(bg="black")
                self.optionsFrame.place(x=50, y=50)

                Label(self.optionsFrame, text="SELECT YOUR CHOICE   ☻", font="Bold 20", bg="black", fg="white").place(
                    x=10, y=0)
                self.depositButton = Button(self.optionsFrame)
                self.depositButton.config(bg="white",
                                          fg="purple",
                                          font="bold 20",
                                          relief="groove",
                                          text="DEPOSIT",
                                          command=self.deposit
                                          )
                self.depositButton.grid(row=2, column=2, padx=20, pady=50)

                ''' similarly withdraw aur balance enquiry k buttons'''
                self.withdrawButton = Button(self.optionsFrame)
                self.withdrawButton.config(bg="#ffffff",
                                           fg="purple",
                                           font="bold 20",
                                           relief="groove",
                                           # text="Withdraw",
                                           command=self.withdraw
                                           )
                if Bank.Customer.list[3] != "loan":
                    self.withdrawButton.config(text="withdraw")
                else:
                    self.withdrawButton.config(text="Apply for loan")
                self.withdrawButton.grid(row=2, column=3, pady=50)
                '''balance enquiry'''
                self.enquiryButton = Button(self.optionsFrame)
                self.enquiryButton.config(bg="white",
                                          fg="purple",
                                          font="bold 20",
                                          relief="groove",
                                          text="Balance Enquiry",
                                          command=self.balanceEnquiry
                                          )
                self.enquiryButton.grid(row=2, column=4, padx=20, pady=50)
            '''making an abstract method of calcpayment which will be inherited in subclasses '''
            @abstractmethod
            def calcpayment(self):
                pass

            def logout(self):
                Bank.Customer.loggedin = False
                messagebox.showinfo("Log Out",
                                    "You've been logged out successfully")
                self.lb.destroy()
                self.optionsFrame.destroy()
                self.db.destroy()
                try:
                    self.transactionFrame.destroy()
                except AttributeError:
                    pass
                finally:
                    window.home_page()

            def delete_acc(self):
                if Bank.Customer.list[3] == "checking":
                    self.fl = open("Checkingclients.txt", "r")
                    self.list = self.fl.readlines()
                    self.fl.close()
                    self.writetofile = open("Checkingclients.txt", "w")
                elif Bank.Customer.list[3] == "saving":
                    self.fl = open("Savingsclients.txt", "r")
                    self.list = self.fl.readlines()
                    self.fl.close()
                    self.writetofile = open("Savingsclients.txt", "w")
                else:
                    self.fl = open("Loanclients.txt", "r")
                    self.list = self.fl.readlines()
                    self.fl.close()
                    self.writetofile = open("Loanclients.txt", "w")
                self.writetofile.truncate(0)
                for item in self.list:
                    self.transac = eval(item)
                    print(self.transac)
                    if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1] and \
                            self.transac[2] == Bank.Customer.list[2]:
                        print("acc deleted")
                        print(Bank.Customer.list)
                        print(self.transac)
                    else:
                        self.writetofile.write(f"{self.transac}\n")
                self.writetofile.close()
            def changePass(self):
                for widget in window.mainframe.winfo_children():
                    widget.destroy()
                Label(window.mainframe,text="TYPE IN YOUR NEW PASSWORD : ",font="Bold 16",bg="#000000",fg="#ffffff").grid(padx=30,pady=50)
                self.newpass=Entry(window.mainframe)
                self.newpass.grid(row=1,padx=5,pady=50)
                Button(window.mainframe,text="CHANGE ",command=self.implementpass,font="Bold 16",bg="#000000",fg="#ffffff").grid(row=2)
            def implementpass(self):
                if len(self.newpass.get())>=7 :
                    if Bank.Customer.list[3] == "checking":
                        self.fl = open("Checkingclients.txt", "r")
                        self.list = self.ch.readlines()
                        self.fl.close()
                        self.writetofile = open("Checkingclients.txt", "w")
                    elif Bank.Customer.list[3] == "saving":
                        self.fl = open("Savingsclients.txt", "r")
                        self.list = self.fl.readlines()
                        self.fl.close()
                        self.writetofile = open("Savingsclients.txt", "w")
                    else:
                        self.fl = open("Loanclients.txt", "r")
                        self.list = self.fl.readlines()
                        self.fl.close()
                        self.writetofile = open("Loanclients.txt", "w")
                    self.writetofile.truncate(0)
                    for item in self.list:
                        self.transac = eval(item)
                        if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1] and self.transac[2] == Bank.Customer.list[2]:
                            Bank.Customer.list[2]=self.newpass.get()
                            self.writetofile.write((f"{Bank.Customer.list}\n"))
                        else:
                            self.writetofile.write(f"{self.transac}\n")
                    self.writetofile.close()
                    messagebox.showerror("Pass changed","Your password has been changed. returning to main window.")
                else:
                    messagebox.showerror("weak pass","Your password is too weak, Kindly reconsider")
                    self.changePass()
        '''Customer Class'''
        def __init__(self):
            self.loginFrame = LabelFrame(window.mainframe)
            self.loginFrame.config(highlightbackground="black", border=0, bg="beige")
            self.loginFrame.config(bg="#000000", height=400, width=800)
            self.loginFrame.place(x=10, y=10)

            # asking to login or ceate an account
            '''login label'''
            self.loginLabel = Label(self.loginFrame)
            self.loginLabel.config(bg="#000000",
                                   fg="#ffffff",
                                   text="Already Have An Account?",
                                   font=("Copperplate Gothic", 25))
            self.loginLabel.place(x=50, y=50)
            '''button for login'''
            self.loginButton = Button(self.loginFrame)
            self.loginButton.config(font="bold 18", relief=SUNKEN,
                                    bg="#A07200",
                                    fg="white",
                                    text="LOGIN",
                                    command=self.login)
            self.loginButton.place(x=200, y=100)

            '''register label'''
            self.regLabel = Label(self.loginFrame)
            self.regLabel.config(bg="#000000",
                                 fg="#ffffff",
                                 text=" OR \n Create Your Account Now.",
                                 font=("Copperplate Gothic", 25))
            self.regLabel.place(x=50, y=150)
            '''button for create account'''
            self.create_accountButton = Button(self.loginFrame)
            self.create_accountButton.config(font="bold 18", relief=SUNKEN,
                                             bg="#A07200",
                                             fg="white",
                                             text="CREATE ACCOUNT",
                                             command=self.createAcc)
            self.create_accountButton.place(x=150, y=250)

        '''login form'''
        def login(self):
            self.login_window = Tk()
            self.login_window.title("Bank")
            self.login_window.configure(bg="#EBE8FC")
            self.login_window.geometry("900x700")

            self.login_frame = Frame(self.login_window, bg="#EBE8FC")
            self.login_frame.pack(pady=50)

            self.loginlabel = Label(self.login_frame, background="#EBE8FC", font=("Goudy Stout", 20),
                                    foreground="#8C11BE", text='L O G I N')
            self.loginlabel.grid(row=0, column=0, columnspan=2, pady=30)

            self.form_frame = Frame(self.login_window, bg="#EBE8FC")
            self.form_frame.pack(pady=50)

            self.namelb = Label(self.form_frame, text="ENTER YOUR FULL NAME", fg="#8C11BE", bg="#EBE8FC", font=("bold", 12))
            self.namelb.grid(row=0, column=0, sticky="e", padx=10, pady=10)
            self.client_name = Entry(self.form_frame, width=40)
            self.client_name.grid(row=0, column=1, padx=10, pady=10)

            self.cniclb = Label(self.form_frame, text="ENTER CNIC NO (without -)", fg="#8C11BE",
                                bg="#EBE8FC", font=("bold", 12))
            self.cniclb.grid(row=1, column=0, sticky="e", padx=10, pady=10)
            self.cnic = Entry(self.form_frame, width=40)
            self.cnic.grid(row=1, column=1, padx=10, pady=10)

            self.password = Label(self.form_frame, text="ENTER PASSWORD:", fg="#8C11BE",
                                bg="#EBE8FC", font=("bold", 12))
            self.password.grid(row=2, column=0, sticky="e", padx=10, pady=10)
            self.passw = Entry(self.form_frame, width=20)
            self.passw.grid(row=2, column=1, padx=10, pady=10)

            self.cap_lb = Label(self.form_frame, text="WRITE THE CAPTCHA TEXT HERE", fg="#8C11BE",
                                bg="#EBE8FC", font=("bold", 12))
            self.cap_lb.grid(row=4, column=0, sticky="e", padx=10, pady=10)
            self.cap_ent = Entry(self.form_frame)
            self.cap_ent.grid(row=4, column=1, padx=10, pady=10)

            self.captcha_obj = ImageCaptcha(height=150, width=250)
            self.lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "s", "u", "v", "w", "x", "y", "z",
                        "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            options = ["saving", "checking", "loan"]
            self.selectedoptions=StringVar(self.form_frame, value = "loan")
            self.selectedoptions.set(options[0])
            Label(self.form_frame, text="TYPE OF ACCOUNT:", fg="#8C11BE",
                                bg="#EBE8FC", font=("bold", 12)).grid(row = 3, column=0)
            self.dd=OptionMenu(self.form_frame,self.selectedoptions,*options,command=self.disp)
            self.dd.grid(row=3,column=1)
            self.word = ""
            for _ in range(5):
                self.word += random.choice(self.lst)
            print(self.word)
            self.captcha_obj.write(chars=self.word, output='img.png')
            self.p1 = PhotoImage(master=self.form_frame, file='img.png')
            self.img_lb = Label(self.form_frame, image=self.p1)
            self.img_lb.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

            Button(self.form_frame, text="Submit", bg="#A682FF", fg="white", font=("bold", 12), command=self.submitLogin).grid(row=6, column=0, columnspan=2, pady=10)


        def disp(self,event):
            Label(self.dd,text=self.selectedoptions.get()).grid()

        def submitLogin(self):
            ''' getting values and checking if entries are correct'''
            self.acc = self.selectedoptions.get()
            self.custname=self.client_name.get()
            self.custpass=self.passw.get()

            self.custcnic=self.cnic.get()
            if not self.custname:
                messagebox.showwarning("Empty Field", "Please enter your name.")
                return
            if not self.custpass :
                messagebox.showwarning("Empty Field", "Please enter your password.")
                return
            if not self.custcnic or len(self.custcnic)!=11 or (not int(self.custcnic)):
                messagebox.showwarning("Invalid", "Please enter valid CNIC number.")
            if not self.acc:
                messagebox.showwarning("Empty Field", "select an option too.")
                return
            if (self.cap_ent.get())!=self.word:
                messagebox.showwarning("Incorrect", "Incorrect Captcha entry.")

            else:
                '''if no errors, finding the account in files'''
                count=0

                if self.acc=="checking":
                    self.logCheckingFile = open("Checkingclients.txt", "r")
                    self.filecontents2 = self.logCheckingFile.readlines()  # gives a list as: ["['12365478985', 'fatima', 'fghjkllsssss', 'checking', ['Sat Jul 15 19:31:15 2023', 0], ['Sat Jul 15 19:31:21 2023', 100000]]","['74125896321', 'mansoor', '1kjlasd', 'checking', ['Sat Jul 15 19:38:02 2023', 0], ['Sat Jul 15 19:38:17 2023', 100000]]"]
                    self.logCheckingFile.close()

                    for line in self.filecontents2:
                        self.line = eval(line.strip())
                        if self.line[1] == self.custname and self.line[0] == self.custcnic and self.line[2]==self.custpass:
                            '''checking if user is on overdraft'''
                            if int(self.line[-1][-1]) >= 0:
                                self.bal=self.line[-1][-1]    # taking value of balance from list
                            else:
                                self.bal=abs(int(self.line[-1][-1]))
                            Bank.Customer.loggedin = True
                            Bank.Customer.list = self.line
                            self.login_window.destroy()
                        else:
                            count += 1
                            if count == len(self.filecontents):
                                messagebox.showerror("Account Not found", "Invalid Details")
                elif self.acc=="saving":
                    self.logSavingFile = open("Savingsclients.txt", "r")
                    self.filecontents= self.logSavingFile.readlines()
                    self.logSavingFile.close()

                    for line in self.filecontents:
                        self.line = eval(line.strip())
                        if self.line[1] == self.custname and self.line[0] == self.custcnic and self.line[2]==self.custpass:
                            self.bal = self.line[-1][-1]
                            Bank.Customer.loggedin = True
                            Bank.Customer.list = self.line
                            self.login_window.destroy()
                            self.savelogin=SavingAccount(self.bal)
                        else:
                            count += 1
                            if count == len(self.filecontents):
                                messagebox.showerror("Account Not found", "Invalid Details")
                            
                else:
                    self.logLoanFile=open("Loanclients.txt","r")
                    self.filecontents = self.logLoanFile.readlines()
                    self.logLoanFile.close()

                    for line in self.filecontents:
                        self.line = eval(line.strip())
                        if self.line[1] == self.custname and self.line[0] == self.custcnic and self.line[2] == self.custpass:
                            self.debittedamount = self.line[-1][-2]
                            Bank.Customer.loggedin = True
                            Bank.Customer.list = self.line
                            self.login_window.destroy()
                            self.loanlogin = LoanAccount(self.debittedamount)
                        else:
                            count+=1
                            if count==len(self.filecontents):
                                messagebox.showerror("Account Not found", "Invalid Details")
        def createAcc(self):
            self.register_window = Tk()
            self.register_window.title("Bank Registration")
            self.register_window.configure(bg="#EBE8FC")
            self.register_window.geometry("900x800")

            self.register_frame = Frame(self.register_window, bg="#EBE8FC")
            self.register_frame.pack(pady=50)

            self.register_label = Label(self.register_frame, background="#EBE8FC", font=("Goudy Stout", 20),
                                        foreground="#8C11BE", text='R E G I S T E R')
            self.register_label.grid(row=0, column=0, columnspan=3, pady=15)

            self.form_frame = Frame(self.register_window, bg="#EBE8FC")
            self.form_frame.pack(pady=20)

            self.namelb = Label(self.form_frame, text="ENTER YOUR FULL NAME", fg="#8C11BE", bg="#EBE8FC", font=("bold", 12))
            self.namelb.grid(row=0, column=0, sticky="e", padx=10, pady=10)
            self.client_name = Entry(self.form_frame, width=40)
            self.client_name.grid(row=0, column=1, padx=10, pady=10)

            self.cniclb = Label(self.form_frame, text="ENTER CNIC NO (without -)", fg="#8C11BE",
                                bg="#EBE8FC", font=("bold", 12))
            self.cniclb.grid(row=1, column=0, sticky="e", padx=10, pady=10)
            self.cnic = Entry(self.form_frame, width=40)
            self.cnic.grid(row=1, column=1, padx=10, pady=10)

            self.password = Label(self.form_frame, text="ENTER PASSWORD:", fg="#8C11BE",
                                bg="#EBE8FC", font=("bold", 12))
            self.password.grid(row=2, column=0, sticky="e", padx=10, pady=10)
            self.passw = Entry(self.form_frame, width=20)
            self.passw.grid(row=2, column=1, padx=10, pady=10)

            self.gender_lb = Label(self.form_frame, text="SELECT GENDER", fg="#8C11BE", bg="#EBE8FC", font=("bold", 12))
            self.gender_lb.grid(row=3, column=0, sticky="e", padx=10, pady=10)
            self.gender = StringVar(self.form_frame, "M")
            r1 = Radiobutton(self.form_frame, text="MALE", fg="#8C11BE", bg="#EBE8FC",
                            variable=self.gender, value="M")
            r1.grid(row=3, column=1, sticky="w")
            r2 = Radiobutton(self.form_frame, text="FEMALE", fg="#8C11BE", bg="#EBE8FC",
                            variable=self.gender, value="F")
            r2.grid(row=3, column=2, sticky="w")

            self.doblabel = Label(self.form_frame, text="DATE OF BIRTH", fg="#8C11BE", bg="#EBE8FC", font=("bold", 12))
            self.doblabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

            self.menu = StringVar()
            self.menu = StringVar(self.form_frame, value="1")
            self.drop = OptionMenu(self.form_frame, self.menu, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
                                "28", "29", "30", "31" )
            self.drop.config(width=5)
            self.drop.grid(row=4, column=1, padx=10, pady=10)

            self.menu2 = StringVar()
            self.menu2 = StringVar(self.form_frame, value="January")
            self.drop2 = OptionMenu(self.form_frame, self.menu2, "January", "February", "March", "April", "May", "June",
                                    "July", "August", "September", "October", "November", "December")
            self.drop2.config(width=15)
            self.drop2.grid(row=4, column=2, padx=10, pady=10)

            self.menu3 = StringVar()
            self.menu = StringVar(self.form_frame, value="1990")
            self.drop3 = OptionMenu(self.form_frame, self.menu3,"2002","2001", "2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990")
            self.drop3.config(width=5)
            self.drop3.grid(row=4, column=3, padx=10, pady=10)

            self.cap_lb = Label(self.form_frame, text="WRITE THE CAPTCHA TEXT HERE", fg="#8C11BE",
                                bg="#EBE8FC", font=("bold", 12))
            self.cap_lb.grid(row=5, column=0, sticky="e", padx=10, pady=10)
            self.cap_ent = Entry(self.form_frame)
            self.cap_ent.grid(row=5, column=1, padx=10, pady=10)

            self.captcha_obj = ImageCaptcha(height=150, width=250)
            self.lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "s", "u", "v", "w", "x", "y", "z",
                        "1", "2", "3", "4", "5", "6", "7", "8", "9"]

            self.word = ""
            for rn in range(5):
                self.word += random.choice(self.lst)

            self.captcha_obj.write(chars=self.word, output='img.png')
            self.p1 = PhotoImage(master=self.form_frame, file='img.png')
            self.img_lb = Label(self.form_frame, image=self.p1)
            self.img_lb.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
            print(self.word)

            Button(self.form_frame, text="Submit", bg="#A682FF", fg="white", font=("bold", 12), command=self.done).grid(row=7, column=0, columnspan=3, pady=10)


        def done(self):

            self.nic = self.cnic.get()
            self.name = self.client_name.get()
            self.pasword = self.passw.get()
                # Check if any field is empty
            if not self.name:
                messagebox.showwarning("Empty Field", "Please enter your name.")
            elif not self.nic or len(self.nic)!=11:
                messagebox.showwarning("Invalid", "Please correct CNIC number.")
            elif not self.pasword or len(self.pasword)<=6:
                messagebox.showwarning("Incompetent", "Your password is too weak")
            elif self.cap_ent.get() != self.word:
                messagebox.showwarning("Incorrect", "Incorrect Captcha entering.")
            else:

                Bank.Customer.list.append(self.nic)
                Bank.Customer.list.append(self.name)
                Bank.Customer.list.append((self.pasword))

                Bank.Customer.loggedin = True
                self.loginFrame.destroy()
                self.register_window.destroy()



                # -----------------------------------------------------------------#
                # -----------------------------------------------------------------#
                messagebox.showinfo("WELCOME TO ROYAL Bank",
                                    "Select the type of account")
                self.optionsframe = Frame()
                self.optionsframe.place(x=250, y=150, height=500, width=900)

                self.p1 = PhotoImage(master=self.optionsframe, file="./icons/s.PNG")
                Button(master=self.optionsframe, image=self.p1, width=300, height=200, command=self.saving).place(relx=0.02,
                                                                                                                  rely=0.25)
                Label(self.optionsframe, text="Savings Account ", fg="white", bg="black").place(relx=0.15, rely=0.7)

                self.p2 = PhotoImage(master=self.optionsframe, file="./icons/checking.PNG")
                Button(self.optionsframe, image=self.p2,padx=10, width=300, height=300, command=self.checking).place(relx=0.36,
                                                                                                             rely=0.08)
                Label(self.optionsframe, text="Checking Account ", fg="white", bg="black").place(relx=0.5, rely=0.7)

                self.p3 = PhotoImage(master=self.optionsframe, file="./icons/loan.png")
                Button(self.optionsframe, image=self.p3, width=300, height=300, command=self.loan).place(relx=0.7,
                                                                                                         rely=0.08)
                Label(self.optionsframe, text="Loan Account ", fg="white", bg="black").place(relx=0.9, rely=0.7)

        ''' to make obj of savings class'''

        def saving(self):
            '''adding user and his credentials in the file'''
            self.optionsframe.destroy()

            messagebox.showinfo("New Account",
                                "You successfully made a new Savings Account")
            Bank.Customer.list.append(SavingAccount.acc_type)
            '''datetime'''
            self.localtime = time.asctime((time.localtime(time.time())))
            '''.'''
            Bank.Customer.list.append([self.localtime, 0])
            '''registration savings ka kaam'''
            with open("Savingsclients.txt", "a+") as file:
                file.write(f"{Bank.Customer.list}\n")
                file.flush()

            self.savelogin = SavingAccount()

        def checking(self):
            self.optionsframe.destroy()
            messagebox.showinfo("New Account",
                                "You successfully made a new checking Account")
            Bank.Customer.list.append(CheckingAccount.acc_type)
            '''datetime'''
            self.localtime = time.asctime((time.localtime(time.time())))
            '''.'''
            Bank.Customer.list.append([self.localtime, 0])
            '''registration checking a kaam'''
            self.regcheck = open("Checkingclients.txt", "a+")
            self.regcheck.write(f"{Bank.Customer.list}\n")
            self.regcheck.close()
            print(Bank.Customer.list)

            self.check = CheckingAccount()

        def loan(self):
            self.optionsframe.destroy()
            messagebox.showinfo("New Account",
                                "You successfully made a new Loan Account")
            Bank.Customer.list.append(LoanAccount.acc_type)
            '''datetime'''
            self.localtime = time.asctime((time.localtime(time.time())))
            '''.'''
            Bank.Customer.list.append([self.localtime, 0, 0])
            '''registration checking a kaam'''
            with open("Loanclients.txt", "a+") as file:
                file.write(f"{Bank.Customer.list}\n")

            print(Bank.Customer.list)

            self.loan = LoanAccount()

    '''Bank start horhi ab'''
    def __init__(self):
        super().__init__()
        self.geometry("3000x5000")
        # head frame
        self.topfm = LabelFrame(bg="#710193",
                                highlightthickness=1,
                                bd=0)
        self.topfm.place(x=50,
                         y=0,
                         width=10000,
                         height=100)

        # title
        self.head = Label(self.topfm)
        self.head.configure(text="                  THE ROYAL BANK", bg='#710193', fg='white',
                            font=('Bold', 20))
        self.head.grid(row=0, column=0, pady=35)

        # main frame
        self.mainframe = Frame()
        '''assigning title and icon to main window'''
        self.title("BANK")
        self.mainframe.config(highlightthickness=5)
        self.mainframe["background"] = "black"
        self.mainframe.place(x=250, y=150, height=500, width=900)
        '''admin or customer'''
        self.frame = Frame(self, borderwidth=6, bg="white", relief=SUNKEN)
        self.frame.place(x=250, y=150, height=500, width=900)
        self.b1 = Button(self.frame, fg="black", bg="yellow", text="ADMINISTRATOR", font="Bold 25",
                         command=self.administrator, highlightbackground="black")
        self.b1.place(relx=0.38, rely=0.3)
        self.b2 = Button(self.frame, fg="black", bg="pink", text="CUSTOMER", font="Bold 25", command=self.customer,
                         highlightbackground="black")
        self.b2.place(relx=0.4, rely=0.5)

    def administrator(self):
        self.loggedin = False
        self.frame.destroy()
        '''adding image0'''
        self.img = PhotoImage(file="./icons/login.png")
        Label(self.mainframe, image=self.img, bg="#000000").grid()
        Label(self.mainframe, text="SIGN IN", bg="#000000", font="Bold 30", fg="#57a1f8").place(x=520, y=50)
        '''entries'''
        self.username = Entry(self.mainframe, width=15, fg="#000000", bg="#ffffff", border=0,
                              font=('Microsoft YaHei UI Light', 19, 'bold'))
        self.username.insert(0, 'username')
        self.username.grid(row=0, column=1, padx=10)
        self.password = Entry(self.mainframe, width=12, fg="#000000", bg="#ffffff", border=0,
                              font=('Microsoft YaHei UI Light', 19, 'bold'))
        self.password.insert(0, 'password')
        self.password.grid(row=0, column=2)
        '''done'''
        Button(self.mainframe, text="SIGN IN", width=16, pady=7, bg="#57a1f8", fg="#ffffff", border=0, font="Bold 15",
               command=self.adminSignin).grid(row=1, column=1, padx=50)

    def adminSignin(self):
        if self.loggedin == False:
            self.adminname = self.username.get()
            self.adminpass = self.password.get()
            '''checking username and pass'''
            self.admins = {"Fatima Mansoor": "fm2004*", "Zobia Naseem": "zobee8520^", "Hafsa Ahmed": "hafsa9090%%"}
            try:
                self.admins[self.adminname]
            except KeyError:
                messagebox.showerror("error login", "Please enter correct username.")

            else:
                if self.admins[self.adminname] == self.adminpass:
                    messagebox.showinfo("succesfull", "you are logged in!")
                    self.loggedin = True
                    for widget in self.mainframe.winfo_children():
                        widget.destroy()
                    Button(self.mainframe, text="view checking clients", font="Bold 25", bg="purple", fg="#ffffff",
                           command=self.displayChecking).place(relx=0.3, rely=0.3)
                    Button(self.mainframe, text="view saving clients", font="Bold 25", bg="purple", fg="#ffffff",
                           command=self.displaySaving).place(relx=0.3, rely=0.45)
                    Button(self.mainframe, text="view loan clients",command=self.displayLoan, font="Bold 25", bg="purple", fg="#ffffff").place(
                        relx=0.3, rely=0.6)
                    Button(self.mainframe, text="logout", font="Bold 16", bg="#000000", fg="#ffffff",
                           command=self.logout).place(relx=0.7, rely=0.7)
                else:
                    messagebox.showerror("error", "Please enter correct password")
            Button(self.mainframe, text="BACK", command=self.goback, fg="#ffffff", bg="#000000",
                   highlightbackground="#ffffff",font="Bold 18").place(relx=0.2, rely=0.7)
        else:
            for widget in self.mainframe.winfo_children():
                widget.destroy()
            Button(self.mainframe, text="view checking clients", font="Bold 25", bg="purple", fg="#ffffff",
                   command=self.displayChecking).place(relx=0.3, rely=0.3)
            Button(self.mainframe, text="view saving clients", font="Bold 25", bg="purple", fg="#ffffff",
                   command=self.displaySaving).place(relx=0.3, rely=0.45)
            Button(self.mainframe, text="view loan clients",command=self.displayLoan, font="Bold 25", bg="purple", fg="#ffffff").place(relx=0.3,
                                                                                                              rely=0.6)
            Button(self.mainframe, text="BACK", command=self.goback, fg="#ffffff", bg="#000000",font="Bold 16",
               highlightbackground="#ffffff").grid(row=3, column=1)

    def logout(self):
        messagebox.showinfo("logout", "you are logged out")
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        self.administrator()

    def goback(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        self.administrator()

    def displayChecking(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        Label(self.mainframe, text="Select clients to generate their reports :", bg="#000000", fg="#ffffff",
              font="Bold 20").grid(padx=50, pady=30)
        self.checkfile = open("Checkingclients.txt", "r")
        self.checklist = self.checkfile.readlines()
        self.checkfile.close()
        self.variables = []
        for ind in range(0, len(self.checklist)):
            self.var = BooleanVar()
            self.variables.append(self.var)
            self.info = eval(self.checklist[ind])
            self.acctype = "checking"
            self.choice = Checkbutton(self.mainframe, text=self.info[1], bg="#000000", fg="purple", font="Bold 16",
                                      variable=self.var)
            self.choice.grid(row=ind + 1, column=0, pady=10)
        Button(self.mainframe, text="generate report", command=self.report,fg="#ffffff", bg="#000000").grid(row=len(self.checklist) + 1, column=0)
        Button(self.mainframe, text="BACK", command=self.back, fg="#ffffff", bg="#000000",
               highlightbackground="#ffffff", font="Bold 18").grid(row=len(self.checklist) + 1, column=1)

    def displaySaving(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        Label(self.mainframe, text="Select clients to generate their reports :", bg="#000000", fg="#ffffff",
              font="Bold 20").grid(padx=50, pady=30)
        self.savefile = open("Savingsclients.txt", "r")
        self.savelist = self.savefile.readlines()
        self.savefile.close()
        self.variables = []
        for ind in range(0, len(self.savelist)):
            self.var = BooleanVar()
            self.variables.append(self.var)
            self.info = eval(self.savelist[ind])
            self.acctype = "saving"
            self.choice = Checkbutton(self.mainframe, text=self.info[1], bg="#000000", fg="purple", font="Bold 16",
                                      variable=self.var)
            self.choice.grid(row=ind + 1, column=0, pady=10)
        Button(self.mainframe, text="generate report", command=self.report).grid(row=len(self.savelist) + 1, column=0)
        Button(self.mainframe, text="BACK", command=self.back, fg="#ffffff", bg="#000000",
               highlightbackground="#ffffff", font="Bold 18").grid(row=len(self.savelist) + 1, column=1)
    def displayLoan(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        Label(self.mainframe, text="Select clients to generate their reports :", bg="#000000", fg="#ffffff",
              font="Bold 20").grid(padx=50, pady=30)
        self.loan = open("Loanclients.txt", "r")
        self.transactiolist = self.loan.readlines()
        self.loan.close()
        self.variables = []
        for ind in range(0, len(self.transactiolist)):
            self.var = BooleanVar()
            self.variables.append(self.var)
            self.info = eval(self.transactiolist[ind])
            self.acctype = "loan"
            self.choice = Checkbutton(self.mainframe, text=self.info[1], bg="#000000", fg="purple", font="Bold 16",
                                      variable=self.var)
            self.choice.grid(row=ind + 1, column=0, pady=10)
        Button(self.mainframe, text="generate report", command=self.report,fg="#ffffff", bg="#000000").grid(row=1,column=3)
        Button(self.mainframe, text="BACK", command=self.back, fg="#ffffff", bg="#000000",
               highlightbackground="#ffffff", font="Bold 18").grid(row=0, column=3)

    def report(self):
        for i in range(0, len(self.variables)):
            if self.variables[i].get():
                if self.acctype!="loan":

                    if self.acctype == "checking":
                        Bank.Customer.list = eval(self.checklist[i])
                    #     print(self.info)
                    elif self.acctype == "saving":
                        Bank.Customer.list = eval(self.savelist[i])

                    print(Bank.Customer.list)
                    '''report ka mandatory kaam'''
                    self.head = f'''CNIC : {Bank.Customer.list[0]}                    NAME : {Bank.Customer.list[1]}'''
                    ''' creating instance of the custom class and adding content to pdf'''
                    self.page = FPDF()
                    self.page.add_page()
                    self.page.set_font("Arial")
                    self.page.cell(0, 10, self.head, ln=True)
                    self.page.cell(10, 3, ln=True)
                    self.page.cell(40, 7, 'Date', 1, 0, 'C')
                    self.page.cell(70, 7, 'Transaction Type', 1, 0, 'C')
                    self.page.cell(40, 7, 'Amount', 1, 1, 'C')

                    for index in range(5, len(Bank.Customer.list)):
                        print(Bank.Customer.list[index])
                        self.info = ''
                        self.date = Bank.Customer.list[index][0]
                        if Bank.Customer.list[index][1] > Bank.Customer.list[index - 1][1]:
                            self.type = "deposit"
                            self.amount = Bank.Customer.list[index][1] - Bank.Customer.list[index - 1][1]
                            self.page.cell(70, 7, self.date, 1, 0, 'C')
                            self.page.cell(40, 7, self.type, 1, 0, 'C')
                            self.page.cell(40, 7, str(self.amount), 1, 1, 'C')
                        else:
                            self.type = "withdraw"
                            self.amount = Bank.Customer.list[index - 1][1] - Bank.Customer.list[index][1]
                            self.page.cell(70, 7, self.date, 1, 0, 'C')
                            self.page.cell(40, 7, self.type, 1, 0, 'C')
                            self.page.cell(40, 7, str(self.amount), 1, 1, 'C')
                    self.bal = Bank.Customer.list[-1][-1]
                    self.page.cell(0, 10, f"", ln=True)
                    if self.bal < 0:
                        self.page.cell(0, 10, "    CURRENT BALANCE : Rs. 0")
                    else:
                        self.page.cell(0, 10, f"    CURRENT BALANCE : Rs.{self.bal}")

                    self.page.output(f"Reportfor{Bank.Customer.list[1]}.pdf", "F")
                    self.path = f"Reportfor{Bank.Customer.list[1]}.pdf"
                    os.system(self.path)
                else:
                    Bank.Customer.list = eval(self.transactiolist[i])
                    '''report ka mandatory kaam'''
                    self.head = f'''CNIC : {Bank.Customer.list[0]}                    NAME : {Bank.Customer.list[1]}'''
                    ''' creating instance of the custom class and adding content to pdf'''
                    self.page = FPDF()
                    self.page.add_page()
                    self.page.set_font("Arial")
                    self.page.cell(0, 10, self.head, ln=True)
                    self.page.cell(10, 3, ln=True)
                    self.page.cell(40, 7, 'Date', 1, 0, 'C')
                    self.page.cell(70, 7, 'Transaction Type', 1, 0, 'C')
                    self.page.cell(40, 7, 'Amount', 1, 1, 'C')

                    self.ln = open("Loanclients.txt", "r")
                    self.list = self.ln.readlines()
                    self.ln.close()
                    for transac in self.list:
                        print(transac)
                        self.transac = eval(transac.strip())
                        if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1]:
                            for index in range(5, len(self.transac)):
                                self.info = ''
                                self.date = self.transac[index][0]
                                if index == 5:
                                    self.type = "loan"
                                    self.amount = abs(self.transac[5][1])
                                    print("loan amount is: ", self.amount)
                                    self.page.cell(0, 10, f"", ln=True)
                                    self.page.cell(70, 7, self.date, 1, 0, 'C')
                                    print("date written")
                                    self.page.cell(40, 7, self.type, 1, 0, 'C')
                                    self.page.cell(40, 7, str(self.amount), 1, 1, 'C')
                                else:
                                    self.type = "deposit"
                                    self.amount = self.transac[index][1]
                                    self.page.cell(70, 7, self.date, 1, 0, 'C')
                                    self.page.cell(40, 7, self.type, 1, 0, 'C')
                                    self.page.cell(40, 7, str(self.amount), 1, 1, 'C')
                    self.page.cell(0, 10, f"", ln=True)
                    self.page.cell(0, 10, f"    Repayments Remaining : {abs(Bank.Customer.list[-1][-1])}")
                    self.page.output(f"Reportfor{Bank.Customer.list[1]}.pdf", "F")
                    self.path = f"Reportfor{Bank.Customer.list[1]}.pdf"
                    os.system(self.path)

    def back(self):
        self.adminSignin()

    def customer(self):
        # toggle button

        self.toggle_btn = Button(text='☰',
                                 bg='#710193',
                                 fg='white',
                                 font=('Bold', 20),
                                 bd=0,
                                 activebackground='#710193',
                                 activeforeground='white')
        self.toggle_btn.configure(command=self.toggle_menu)
        self.toggle_btn.place(x=0, y=0, height=100, width=90)
        self.frame.destroy()
        self.home_page()

    def toggle_menu(self):

        # toggle menu frame
        self.toggle_menuFrame = Frame(bg="#710193",
                                      highlightthickness=1)
        self.window_height = self.winfo_height()  # winfo height matlab screen ki height
        self.toggle_menuFrame.place(x=0,
                                    y=95,
                                    height=self.window_height,
                                    width=200)

        # changing toggle button into x

        self.toggle_btn.config(text="X", bg="#710193")  # button change krega
        self.toggle_btn.config(command=self.collapse_toggle_menu)  # neeche wala function call horha
        # ab butons lagaiygay menu frame me

        self.home_btn = Button(self.toggle_menuFrame)  # home button
        self.home_btn.config(text="HOME",
                             font="arial 15",
                             bd=6,
                             fg="#ffffff",
                             width=8,
                             bg="purple",
                             command=self.home_page)
        self.home_btn.place(relx=0.1, rely=0.1)
        # savings account button
        self.accounts_btn = Button(self.toggle_menuFrame)
        self.accounts_btn.config(text=" ACCOUNTS",
                                 font="bold 13",
                                 bd=6,
                                 bg='purple',
                                 fg="#ffffff",
                                 command=self.accounts_page)
        self.accounts_btn.place(relx=0.1, rely=0.2)
        # LOAN account button
        self.loan_btn = Button(self.toggle_menuFrame)
        self.loan_btn.config(text="LOANS",
                             font="bold 13",
                             bd=6,
                             bg='purple',
                             fg="#ffffff",
                             command=self.loans_page)
        self.loan_btn.place(relx=0.1, rely=0.3)
        # TRANSACTIONS button
        self.transaction_btn = Button(self.toggle_menuFrame)
        self.transaction_btn.config(text="MY TRANSACTIONS",
                                    font="arial 13",
                                    bd=6,
                                    bg='purple',
                                    fg="#ffffff",
                                    command=self.myTransactions)
        self.transaction_btn.place(relx=0.08, rely=0.4)
        # CONTACT US button
        self.contact_btn = Button(self.toggle_menuFrame)
        self.contact_btn.config(text="CONTACT US",
                                font="arial 13",
                                bd=6,
                                bg='purple',
                                fg="#ffffff",
                                command=self.contact)
        self.contact_btn.place(relx=0.1, rely=0.5)

    def collapse_toggle_menu(self):
        self.toggle_menuFrame.destroy()
        self.toggle_btn.config(text="☰")
        self.toggle_btn.config(command=self.toggle_menu)

    def home_page(self):
        for frame in self.mainframe.winfo_children():
            frame.destroy()
        self.photo1 = PhotoImage(file="./icons/The_Royal_Bank_logo.png")
        Label(self.mainframe, image=self.photo1).place(x=180, y=100)

        self.features = Label(self.mainframe,
                              text="FEATURES:\n*ENSURE TO SAVE YOUR MONEY\n*LOANS WOULD BE GUARENTED\n*AVAIL EASY REPAYMENT OPTIONS\n*ATTRACTIVE INTEREST RATES\n*HASSLE FREE WAYS TO FULFILL YOUR FINANCIAL NEEDS"
                              , font="comicsansms 15 italic bold", bg="black", fg="purple")
        self.features.place(x=20, y=300)
        self.photo2 = PhotoImage(file="./icons/bank.png")
        Label(master=self.mainframe, image=self.photo2).place(x=670, y=30)

        self.photo3 = PhotoImage(file="./icons/bank_work (1).png")
        Label(self.mainframe, image=self.photo3).place(x=650, y=250)

    def accounts_page(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

        if Bank.Customer.loggedin == True:
            if Bank.Customer.list[3] == "saving":
                self.savingacc = SavingAccount(Bank.Customer.list[-1][-1])
            elif Bank.Customer.list[3] == "checking":
                self.checkingacc = CheckingAccount(Bank.Customer.list[-1][-2])
            else:
                self.loanac=LoanAccount()
        elif Bank.Customer.loggedin == False:
            self.custom = Bank.Customer()



    def loans_page(self):
        for frame in self.mainframe.winfo_children():
            frame.destroy()
        if Bank.Customer.loggedin == True:
            pass
        else:
            self.custom = Bank.Customer()

    def myTransactions(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        if Bank.Customer.loggedin == True:
            '''report ka mandatory kaam'''
            self.head = f'''CNIC : {Bank.Customer.list[0]}                    NAME : {Bank.Customer.list[1]}'''
            ''' creating instance of the custom class and adding content to pdf'''
            self.page = FPDF()
            self.page.add_page()
            self.page.set_font("Arial")
            self.page.cell(0, 10, self.head, ln=True)
            self.page.cell(0, 10, f"", ln=True)

            self.page.cell(150,7,"      DATE                                          TRANSACTION                                  AMOUNT ")
            '''checking the type of account'''
            if Bank.Customer.list[3] == "checking":
                self.ch = open("Checkingclients.txt", "r")
                self.transactiolist = self.ch.readlines()
                self.ch.close()
            elif Bank.Customer.list[3] == "saving":
                self.sav = open("Savingsclients.txt", "r")
                self.transactiolist = self.sav.readlines()
                self.sav.close()
            else:
                self.loan = open("Loanclients.txt", "r")
                self.transactiolist = self.loan.readlines()
                self.loan.close()

            for transac in self.transactiolist:
                self.transac = eval(transac.strip())
                if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1] and self.transac[2] == Bank.Customer.list[2]:
                    if Bank.Customer.list[3]=="saving" or Bank.Customer.list[3]=="checking":
                        self.page.cell(0, 10, f"", ln=True)
                        print("report list",Bank.Customer.list)
                        for index in range(5, len(self.transac)):
                            self.date = Bank.Customer.list[index][0]
                            if Bank.Customer.list[index][1] > Bank.Customer.list[index - 1][1]:
                                self.type = "deposit"
                                self.amount = Bank.Customer.list[index][1] - Bank.Customer.list[index - 1][1]
                                self.page.cell(70, 7, self.date, 1, 0, 'C')
                                self.page.cell(40, 7, self.type, 1, 0, 'C')
                                self.page.cell(40, 7, str(self.amount), 1, 1, 'C')
                            else:
                                self.type = "withdraw"
                                self.amount = Bank.Customer.list[index - 1][1] - Bank.Customer.list[index][1]
                                self.page.cell(70, 7, self.date, 1, 0, 'C')
                                self.page.cell(40, 7, self.type, 1, 0, 'C')
                                self.page.cell(40, 7, str(self.amount), 1, 1, 'C')

                        self.bal = Bank.Customer.list[-1][1]
                        self.page.cell(0, 10, f"", ln=True)
                        self.page.cell(0, 10, f"    CURRENT BALANCE : Rs.{self.bal}")

                    if  Bank.Customer.list[3] == "loan":
                        self.ln = open("Loanclients.txt", "r")
                        self.list = self.ln.readlines()
                        for transac in self.list:
                            self.transac = eval(transac.strip())
                            if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1]:
                                for index in range(5, len(self.transac)):
                                    self.info = ''
                                    self.date = self.transac[index][0]
                                    if index == 5:
                                        self.type = "loan"
                                        self.amount = abs(self.transac[5][1])
                                        print("loan amount is: ",self.amount)
                                        # self.page.cell(0, 10, f"", ln=True)
                                        self.page.cell(0, 10, f"", ln=True)
                                        self.page.cell(70, 7, self.date, 1, 0, 'C')
                                        print("date written")
                                        self.page.cell(40, 7, self.type, 1, 0, 'C')
                                        self.page.cell(40, 7, str(self.amount), 1, 1, 'C')
                                    else:
                                        self.type="deposit"
                                        self.amount=self.transac[index][1]
                                        self.page.cell(70, 7, self.date, 1, 0, 'C')
                                        self.page.cell(40, 7, self.type, 1, 0, 'C')
                                        self.page.cell(40, 7, str(self.amount), 1, 1, 'C')
                        self.page.cell(0, 10, f"", ln=True)
                        self.page.cell(0, 10, f"    Repayments Remaining : {abs(Bank.Customer.list[-1][-1])}")

            self.page.output("myTransac.pdf", "F")

            Button(self.mainframe, text="Download My Report", font="Bold 20", command=self.generateReport,
                       bg="red").place(x=10, y=10)


        else:
            try:
                self.custom.login()
            except AttributeError:
                self.customer1 = Bank.Customer()

    def generateReport(self):
        self.path = "myTransac.pdf"
        os.system(self.path)

    def contact(self):
        for frame in self.mainframe.winfo_children():
            frame.destroy()

        self.contact_icon_1 = PhotoImage(file="./icons/images.png")
        self.contact_icon_1_label = Label(self.mainframe, image=self.contact_icon_1)
        self.contact_icon_1_label.place(rely=0.1, relx=0.35)
        self.email = Label(self.mainframe, text='''You can reach us with your feedback and suggestions using any of these channels: 
        Email : complaints.Pakistan@Rb.com
        Call us : 042 111 002 002
        Vist : Our Nearest Branch
        Write to us : Head Complaints Management Unit,
        SCBPL Client Care Unit, 1st Floor, Jubilee,
        Insurance Building, I.I. Chundrigar Road, Karachi''', font="comicsansms 15 italic bold", bg="#000000",
                           fg="purple")
        self.email.place(rely=0.5,relx=0.08)


class SavingAccount(Bank.Customer.Account):
    acc_type = "saving"

    def __init__(self, balance=0):
        self.interestRate = 0.20
        super().__init__(balance)
    '''overriding methods'''
    def getDepositionAmount(self):
        super().getDepositionAmount()
        self.sav = open("Savingsclients.txt", "r")
        self.savinglist = self.sav.readlines()
        self.sav.close()
        self.writetofile = open("Savingsclients.txt", "w")
        for transac in self.savinglist:
            self.transac = eval(transac.strip())
            if (self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1] and self.transac[2] == Bank.Customer.list[2]):
                self.writetofile.write(f"{Bank.Customer.list}\n")
            else:
                self.writetofile.write(f"{self.transac}\n")
        self.writetofile.close()
        self.calcpayment()
        self.img = PhotoImage(file="./icons/Capture.PNG")
        Label(window.mainframe, image=self.img).place(x=280, y=50)
        Label(window.mainframe, text="SUCCESFULL TRANSACTION ☻ !", font="Bold 22", bg="#000000", fg="green").place(
            x=250, y=320)
        Button(window.mainframe, text="Continue Transactions", font="Bold 15", command=self.continuetransaction,
               bg="#000000", fg="#ffffff").place(x=250, y=450)

    '''overriding get withdrawal amount method'''

    def getWithdrawalAmount(self):
        super().getWithdrawalAmount()
        self.sav = open("Savingsclients.txt", "r")
        self.savinglist = self.sav.readlines()
        self.sav.close()
        self.writetofile = open("Savingsclients.txt", "w")
        for transac in self.savinglist:
            self.transac = eval(transac.strip())
            if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1]:
                self.writetofile.write(f"{Bank.Customer.list}\n")
            else:
                self.writetofile.write(f"{self.transac}\n")
        self.writetofile.close()
        self.calcpayment()
        self.img = PhotoImage(file="./icons/Capture.PNG")
        Label(window.mainframe, image=self.img).place(x=280, y=50)
        Label(window.mainframe, text="SUCCESFULL TRANSACTION ☻ !", font="Bold 22", bg="#000000", fg="green").place(
            x=250, y=320)
        Button(window.mainframe, text="Continue Transactions", font="Bold 15", command=self.continuetransaction,
               bg="#000000", fg="#ffffff").place(x=250, y=450)

    def calcpayment(self):
        self.amaountToBePayed = ((Bank.Customer.list[-1][-1] * self.interestRate) / 365)
        messagebox.showinfo("interest amount",
                            f"The bank will pay you Rs.{round(self.amaountToBePayed, 2)} daily as per 20% interest rate.")


class CheckingAccount(Bank.Customer.Account):
    acc_type = "checking"

    def __init__(self,balance=0):
        ''' checking if user is on overdraft'''
        if Bank.Customer.list[-1][1] < 0:
            self.isoverdraft=True
            self.withdrawal_amount = Bank.Customer.list[-1][1]
        else:
            self.isoverdraft = False
            self.withdrawal_amount = 0

        self.creditLimit = 50000 - (abs(self.withdrawal_amount))
        self.interest_rate = 0.27
        super().__init__(Bank.Customer.list[-1][1])

    def getDepositionAmount(self):
        super().getDepositionAmount()
        self.ch = open("Checkingclients.txt", "r")
        self.ch.seek(0)
        self.checkinglist = self.ch.readlines()
        self.ch.close()
        self.writetofile = open("Checkingclients.txt", "w")
        self.writetofile.seek(0)
        for transac in self.checkinglist:
            self.transac = eval(transac.strip())
            if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1]:
                self.writetofile.write(f"{Bank.Customer.list}\n")
            else:
                self.writetofile.write(f"{self.transac}\n")
        self.writetofile.close()
        self.img = PhotoImage(file="./icons/Capture.PNG")
        Label(window.mainframe, image=self.img).place(x=280, y=50)
        Label(window.mainframe, text="SUCCESFULL TRANSACTION ☻ !", font="Bold 22", bg="#000000", fg="green").place(
            x=250, y=320)
        Button(window.mainframe, text="Continue Transactions", font="Bold 15", command=self.continuetransaction,
               bg="#000000", fg="#ffffff").place(x=250, y=450)

    '''overriding get withdrawal amount method'''
    def getWithdrawalAmount(self):
        super().getWithdrawalAmount()
        '''overdraft'''
        if self.amountToWithdraw > Bank.Customer.list[-1][1] and self.amountToWithdraw <= self.creditLimit+Bank.Customer.list[-1][1]:
            self.showOverdraftConfirmation()
        elif self.amountToWithdraw > Bank.Customer.list[-1][1] and self.amountToWithdraw> self.creditLimit:
            messagebox.showwarning("oops","The amount is greater than your crdeit limit")
            self.withdraw()
        else:
            self.updateBalance()

    def showOverdraftConfirmation(self):
        self.optionsFrame.destroy()
        self.entry.destroy()

        Label(window.mainframe, text="Continue with overdraft?", font="Bold 16", bg="#000000", fg="#ffffff").place(x=10,
                                                                                                                   y=150)
        Label(window.mainframe, text=f"You currently have Rs.{self.creditLimit} as your overdraft credit limit",
              font="Bold 16", bg="#000000", fg="#ffffff").place(x=10, y=30)
        Button(window.mainframe, text="Yes", command=self.handleOverdraft, bg="#ffffff", fg="#000000",
               font="Bold 16").place(x=50, y=230)

    def handleOverdraft(self):
        self.withdrawal_amount = self.amountToWithdraw - self.balance
        self.creditLimit -= self.withdrawal_amount
        Bank.Customer.list.append([self.localtime, self.balance-self.amountToWithdraw])
        self.calcpayment()
        self.updateBalance()

    def updateBalance(self):
        self.ch = open("Checkingclients.txt", "r+")
        self.checkinglist = self.ch.readlines()
        self.writeToFile = open("Checkingclients.txt", "w")
        self.writeToFile.truncate(0)
        for transac in self.checkinglist:
            self.transac = eval(transac)
            if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1] and self.transac[2] == Bank.Customer.list[2]:
                self.writeToFile.write(f"{Bank.Customer.list}\n")
            else:
                self.writeToFile.write(f"{self.transac}\n")
        self.ch.close()
        self.writeToFile.close()
        self.img = PhotoImage(file="./icons/Capture.PNG")
        Label(window.mainframe, image=self.img).place(x=280, y=50)
        Label(window.mainframe, text="SUCCESFULL TRANSACTION ☻ !", font="Bold 22", bg="#000000", fg="green").place(
            x=250, y=320)
        Button(window.mainframe, text="Continue Transactions", font="Bold 15", command=self.continuetransaction,
               bg="#000000", fg="#ffffff").place(x=250, y=450)

    def calcpayment(self):
        self.interestamount = (self.withdrawal_amount * self.interest_rate)
        self.amountToBePayed = ((self.withdrawal_amount + self.interestamount))
        messagebox.showinfo("", f" you have to pay RS.{self.amountToBePayed} monthly as per 27% interest.")
    def balanceEnquiry(self):
        super().balanceEnquiry()
        Label(self.enquiryframe, text="Total OverDraft limit: RS. 50,000/-", font="Bold 20",
              bg="#000000", fg="#ffffff").grid(row=1)
        Label(self.enquiryframe, text=f"Remaining Overdraft Amount: Rs.{self.creditLimit}", font="Bold 20",
              bg="#000000", fg="#ffffff").grid(row=2)
        Button(self.enquiryframe, text="Back", command=self.back).grid(row=4, column=2)
class LoanAccount(Bank.Customer.Account):
    acc_type = "loan"
    def __init__(self, bal=0):
        if len(Bank.Customer.list)>=6:
            self.principleAmount = Bank.Customer.list[5][1]
            self.loanDuration = Bank.Customer.list[5][-1]
        self.interestRate = 0.27
        super().__init__(bal)

    def deposit(self):
        if len(Bank.Customer.list)>=6:
            super().deposit()
        else:
            messagebox.showinfo("cannot deposit", "You have not taken any loan yet!")

    def getDepositionAmount(self):
        super().getDepositionAmount()
        if self.amountToDeposit == int(self.calcpayment()):
            Bank.Customer.list.append([self.localtime, self.balance + self.amountToDeposit, Bank.Customer.list[-1][-1]-1])
            self.balance += self.amountToDeposit
            self.ln = open("Loanclients.txt", "r")
            self.loanlist = self.ln.readlines()
            self.ln.close()
            self.writetofile=open("Loanclients.txt","w")
            for transac in self.loanlist:
                self.transac = eval(transac.strip())
                if (self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1] and self.transac[2] == Bank.Customer.list[2]):
                    self.writetofile.write(f"{Bank.Customer.list}\n")
                else:
                    self.writetofile.write(f"{self.transac}\n")
            messagebox.showinfo("deposition",
                                    f"You successfully deposited RS. {int(self.amountToDeposit)}."
                                    f"your next repayment will be after 30 days")

            if len(Bank.Customer.list) >= 6 and Bank.Customer.list[-1][-1] == 0:
                Bank.Customer.list=[Bank.Customer.list[0],Bank.Customer.list[1],Bank.Customer.list[2],"loan",[self.localtime,0,0]]
                self.writetofile.truncate(0)
                self.writetofile.seek(0)
                for item in self.loanlist:
                        item = eval(item)
                        if item[0] == Bank.Customer.list[0] and item[1] == Bank.Customer.list[1] and item[2] ==  Bank.Customer.list[2]:
                            self.writetofile.write(f"{Bank.Customer.list}\n")
                        else:
                            self.writetofile.write(f"{item}\n")


                messagebox.showinfo("repayment completed",
                                    "You completed your loan repayment, you are now eligible for taking a loan again")
            self.writetofile.close()
            self.__init__()

        else:
            messagebox.showerror("error", f"Kindly deposity RS.{self.calcpayment()} as per 27% interest rate")
            self.__init__()

    def withdraw(self):
        try:
            Bank.Customer.list[5]
        except IndexError:
            super().withdraw()
            Label(window.mainframe, text="Month Duration",font="Bold 18",bg="#000000",fg="#ffffff").place(x=550, y=150)
            self.scale = Scale(window.mainframe, from_=1, to=12, orient=HORIZONTAL,width=18)
            self.scale.place(x=550, y=190)
        else:
            messagebox.showerror("-", "You are already on Loan")

    def getWithdrawalAmount(self):
        self.loanDuration = self.scale.get()
        super().getWithdrawalAmount()
        Bank.Customer.list.append([self.localtime, self.principleAmount, self.loanDuration])
        self.ln = open("Loanclients.txt", "r")
        self.lnlist = self.ln.readlines()
        self.writetofile = open("Loanclients.txt", "w")
        # self.writetofile.truncate(0)
        for transac in self.lnlist:
            self.transac = eval(transac.strip())
            if self.transac[0] == Bank.Customer.list[0] and self.transac[1] == Bank.Customer.list[1] and self.transac[2] == Bank.Customer.list[2]:
                self.writetofile.write(f"{Bank.Customer.list}\n")
            else:
                self.writetofile.write(f"{self.transac}\n")
        messagebox.showinfo("loan update",
                            f"You took a loan of {abs(self.principleAmount)} for {self.loanDuration} months."
                            f"\n you have to pay RS.{self.calcpayment()} monthly as per 27% interest rate")
        self.__init__(Bank.Customer.list[-1][2])

    def calcpayment(self):
        self.principleAmount = abs(Bank.Customer.list[5][1])
        self.repaymentAmount = (self.principleAmount + (self.principleAmount * self.interestRate)) / self.loanDuration
        return int(self.repaymentAmount)

    def balanceEnquiry(self):
        super().balanceEnquiry()
        Label(self.enquiryframe, text=f"Principle Loan Amount : Rs. {abs(self.principleAmount)}/- ", font="Bold 20",
              bg="#000000", fg="#ffffff").grid(row=1)
        Label(self.enquiryframe, text=f"Monthly Repayment : Rs.{self.calcpayment()}/-", font="Bold 20",
              bg="#000000", fg="#ffffff").grid(row=2)
        Label(self.enquiryframe, text=f"Repayments Remaining : {Bank.Customer.list[-1][-1]}", font="Bold 20",
              bg="#000000", fg="#ffffff").grid(row=3)
        Button(self.enquiryframe, text="Back", command=self.back).grid(row=4, column=2)

window = Bank()
window.mainloop()