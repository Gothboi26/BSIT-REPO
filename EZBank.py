from tkinter import *
import os

root = Tk()
root.geometry("515x600")
root.title("ATM")
mainFrame = Frame(root, bg= "blue",height=700, width=600)
mainFrame.place(x=0,y=0)
labelIntro = Label(mainFrame, text='EZ BANK',width=17,height=2,bg="#ffd60c",font='arial 10 bold')
labelIntro.place(x=200,y=30)


def custWin():
	custFrame = Frame(root, bg= "blue",height=700, width=600)
	custFrame.place(x=0,y=0)

	labelIntro = Label(custFrame, text='TRANSACT',width=17,height=2,bg="#ffd60c",font='arial 10 bold')
	labelIntro.place(x=200,y=30)

	logButton= Button(text="Withdraw",width=10,font="arial 10 bold",command=witWin)
	logButton.place(x=225,y=150)

	logButton= Button(text="Deposit",width=10,font="arial 10 bold",command=depWin)
	logButton.place(x=225,y=250)

	logButton= Button(text="Balance",width=10,font="arial 10 bold",command=bal)
	logButton.place(x=225,y=350)   
    

def bank():
	global logAcc
	accountList = os.listdir()
	logAcc = logNum.get()

	for account in accountList:
		if account == logAcc:
			file = open(account,"r")
			file_data = file.read()
			file_data = file_data.split('\n')
			print(file_data)
			custWin()
			return
		else:
			root.geometry("515x600")
			root.title("ATM")
			mainFrame = Frame(root, bg= "blue",height=700, width=600)
			mainFrame.place(x=0,y=0)
			label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
			label.place (x=150, y=150)
			label.config(fg="red" ,text="Invalid Account Please Register!")
			logButton= Button(text="Register",width=10,font="arial 10 bold",command=regWin)
			logButton.place(x=225,y=300)

	
def deposit():
	global updatedbal
	file = open(logAcc,"r")
	file_data = file.read()
	if amount.get() == "":
		root.geometry("515x600")
		root.title("ATM")
		mainFrame = Frame(root, bg= "blue",height=700, width=600)
		mainFrame.place(x=0,y=0)
		label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
		label.place (x=225, y=150)
		label.config(text="Amount is Req")
		return
	if float(amount.get())<=0:
		root.geometry("515x600")
		root.title("ATM")
		mainFrame = Frame(root, bg= "blue",height=700, width=600)
		mainFrame.place(x=0,y=0)
		label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
		label.place (x=225, y=150)
		label.config(text="Negative",fg="red")
		logButton= Button(text="Return",width=10,font="arial 10 bold",command=custWin)
		logButton.place(x=225,y=200)
		return

	file = open(logAcc,'r+')
	file_data = file.read()
	details = file_data.split('\n')
	currentbal = details[1]
	updatedbal = currentbal
	updatedbal= float(updatedbal) + float(amount.get())
	file_data = file_data.replace(currentbal,str(updatedbal))
	file.seek(0)
	file.truncate(0)
	file.write(file_data)
	file.close

	root.geometry("515x600")
	root.title("ATM")
	mainFrame = Frame(root, bg= "blue",height=700, width=600)
	mainFrame.place(x=0,y=0)
	label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
	label.place (x=200, y=150)
	logButton= Button(text="Return",width=10,font="arial 10 bold",command=custWin)
	logButton.place(x=225,y=200)
	label.config(text=("Net Balance:", str (updatedbal)))
	
def withdrawn():
	global updatedbal
	file = open(logAcc,"r")
	file_data = file.read()
	if withd.get()=="":
		mainFrame = Frame(root, bg= "blue",height=700, width=600)
		mainFrame.place(x=0,y=0)
		label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
		label.place (x=200, y=150)
		label.config(text='Amount is required!',fg="red")
		logButton= Button(text="Return",width=10,font="arial 10 bold",command=custWin)
		logButton.place(x=225,y=200)
		return
	if float(withd.get()) <=0:
		mainFrame = Frame(root, bg= "blue",height=700, width=600)
		mainFrame.place(x=0,y=0)
		label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
		label.place (x=150, y=150)
		label.config(text='Negative currency is not accepted', fg='red')
		logButton= Button(text="Return",width=10,font="arial 10 bold",command=custWin)
		logButton.place(x=225,y=200)
		return

	file = open(logAcc,'r+')
	file_data = file.read()
	details = file_data.split('\n')
	currentbal = details[1]
	if float(withd.get()) >float(currentbal):
		mainFrame = Frame(root, bg= "blue",height=700, width=600)
		mainFrame.place(x=0,y=0)
		label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
		label.place (x=200, y=150)
		label.config(text='Insufficient Funds!', fg='red')	
		logButton= Button(text="Return",width=10,font="arial 10 bold",command=custWin)
		logButton.place(x=225,y=200)	
		return
	updatedbal = currentbal
	updatedbal= float(updatedbal) - float(withd.get())
	file_data = file_data.replace(currentbal,str(updatedbal))
	file.seek(0)
	file.truncate(0)
	file.write(file_data)
	file.close

	root.geometry("515x600")
	root.title("ATM")
	mainFrame = Frame(root, bg= "blue",height=700, width=600)
	mainFrame.place(x=0,y=0)
	label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
	label.place (x=200, y=150)
	logButton= Button(text="Return",width=10,font="arial 10 bold",command=custWin)
	logButton.place(x=225,y=200)
	label.config(text=("Net Balance:", str (updatedbal)))

def bal():

	root.geometry("515x600")
	root.title("ATM")
	mainFrame = Frame(root, bg= "blue",height=700, width=600)
	mainFrame.place(x=0,y=0)
	label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
	label.place (x=200, y=150)
	logButton= Button(text="Return",width=10,font="arial 10 bold",command=custWin)
	logButton.place(x=225,y=200)
	label.config(text=("Net Balance", str (updatedbal)))
	

def depWin():
    depFrame = Frame(root, bg= "blue",height=700, width=600)
    depFrame.place(x=0,y=0)
    labelAccNo = Label(depFrame, text='Enter Amount',width=15,font='Times 12')
    labelAccNo.place(x=200,y=150)
    intUser = Entry(textvariable=amount,width=17,font='times 12',bd=3)
    intUser.place(x=200,y=200)
    logButton= Button(text="Enter",width=10,font="arial 10 bold",command=deposit)
    logButton.place(x=225,y=350)

def witWin():
	global withd
	withd = StringVar()
	witFrame = Frame(root, bg= "blue",height=700, width=600)
	witFrame.place(x=0,y=0)
	labelAccNo = Label(witFrame, text='Enter Amount',width=15,font='Times 12')
	labelAccNo.place(x=200,y=150)
	intUser = Entry(textvariable=withd,width=17,font='times 12',bd=3)
	intUser.place(x=200,y=200)
	logButton= Button(text="Enter",width=10,font="arial 10 bold",command=withdrawn)
	logButton.place(x=225,y=350)

def balWin():
	balFrame = Frame(root, bg= "blue",height=700, width=600)
	balFrame.place(x=0,y=0)
	logButton= Button(text="Enter",width=10,font="arial 10 bold",command=bal)
	logButton.place(x=225,y=350)

def finReg ():
	accountNum = accNum.get()
	accountList = os.listdir()
	if accountList == "":
		root.geometry("515x600")
		root.title("ATM")
		mainFrame = Frame(root, bg= "blue",height=700, width=600)
		mainFrame.place(x=0,y=0)
		label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
		label.place (x=225, y=200)
		label.config(fg="red",text="Required * ")
		return
	
	for checkAcc in accountList:
		if accountNum == checkAcc:
			root.geometry("515x600")
			root.title("ATM")
			mainFrame = Frame(root, bg= "blue",height=700, width=600)
			mainFrame.place(x=0,y=0)
			label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
			label.place (x=225, y=200)
			label.config(fg="red",text="Already* ")
			return
		else:
			root.geometry("515x600")
			root.title("ATM")
			mainFrame = Frame(root, bg= "blue",height=700, width=600)
			mainFrame.place(x=0,y=0)
			newAcc = open(accountNum,"w")
			newAcc.write(accountNum+'\n')
			newAcc.write('0')
			newAcc.close()
			label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
			label.place (x=225, y=200)
			label.config(fg="red",text="done* ")
			logButton= Button(text="Proceed",width=10,font="arial 10 bold",command=logWin)
			logButton.place(x=225,y=300)
			return


def regWin():
	global accNum
	accNum=StringVar()

	regFrame = Frame(root, bg= "blue",height=700, width=600)
	regFrame.place(x=0,y=0)

	labelIntro = Label(regFrame, text='REGISTER',width=17,height=2,bg="#ffd60c",font='arial 10 bold')
	labelIntro.place(x=200,y=30)

	labelAccNo = Label(regFrame, text='Input Account Number',width=15,font='Times 12')
	labelAccNo.place(x=200,y=150)

	intUser = Entry(textvariable=accNum,width=17,font='times 12',bd=3)
	intUser.place(x=200,y=200)

	logButton= Button(text="Register",width=10,font="arial 10 bold",command=finReg)
	logButton.place(x=225,y=350)




def logWin():

	global logNum
	logNum = StringVar()
	root.geometry("515x600")
	root.title("ATM")
	mainFrame = Frame(root, bg= "blue",height=700, width=600)
	mainFrame.place(x=0,y=0)
	labelIntro = Label(mainFrame, text='EZ BANK',width=17,height=2,bg="#ffd60c",font='arial 10 bold')
	labelIntro.place(x=200,y=30)
	logButton= Button(text="Login",width=10,font="arial 10 bold",command=bank)
	logButton.place(x=225,y=250)    
    
	label = Label (mainFrame, font=('arial', 12, 'bold'), fg="white", bg="blue", bd=5, anchor='w')
	label.place (x=190, y=380)

	labelAccNo = Label(mainFrame, text='Account Number',width=15,font='Times 12')
	labelAccNo.place(x=200,y=150)

	intUser = Entry(textvariable=logNum,width=17,font='times 12',show="*",bd=3)
	intUser.place(x=200,y=200)

logButton= Button(text="Login",width=10,font="arial 10 bold",command=logWin)
logButton.place(x=225,y=250)
logButton= Button(text="Register",width=10,font="arial 10 bold",command=regWin)
logButton.place(x=225,y=300)	 


amount = StringVar()
root.mainloop()