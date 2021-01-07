import random
import time
capital=[]
for k in range(65,(65+26)):
    capital.append(chr(k))
small=[]
for k in capital:
    small.append(k.lower())
num=[]
for k in range(1,11):
    num.append(str(k))
special=["!","@","#","$","%","&","*","(",")","_","-","+","=","[","]",":",";","<",">","?","/"]
characters=capital+small+num+special
pass1=[]
size=int(input("Enter length of password:"))
while size<8:
    print("Password length should be greater than 8")
    size=int(input("Enter length of password:"))

def save():
    PATH=r"C:\Users\GJ\Desktop\password.txt"  #CHANGE THIS PATH ACCORDINGLY
    fh=open(PATH,'w')
    fh.writelines(pass1)
    fh.close()
    print(r"Successfully Saved at ",PATH)
    time.sleep(1)

def loop(pass1):


    if (cap == 1) and (sma == 1) and (n == 1) and (sp == 1):

        print("Generating Strong Password..")
        time.sleep(1)
        for letter in pass1:
            print(letter, end="")

        choice=input(" \n Do You Want to save Password in Notedpad (Yes or No) \n 1.Yes \n 2.No \n")
        if choice==("yes" or "YES" or "1" or "Yes") :
            save()
        elif choice==("no" or "NO" or "2" ):
            print("Exited Without Saving")
            time.sleep(1)

    else:
        pass1.clear()

        generate()
def chk():


    global cap,sma,n,sp
    cap,sma,n,sp=0,0,0,0
    for k in pass1:
        if k in capital:
            cap=1
        elif k in small:
            sma=1
        elif k in num:
            n=1
        elif k in special:
            sp=1

    loop(pass1)
def generate():

    for k in range(size):
        pass1.append(random.choice(characters))
    chk()

generate()

