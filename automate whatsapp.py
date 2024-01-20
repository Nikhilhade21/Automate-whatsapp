import pywhatkit

def value(num1,num2,num3,num4):
    t=[num3,num4]
    p=t[0]
    k=t[1]
    j='+91'
    pywhatkit.sendwhatmsg(j+(num1),num2,p,k)

mob=input("Enter Number to Send Message:")
mes=input("Enter Your Message:")
tim=int(input("Enter Time(in HOUR):"))
tim1=int(input("Enter Time(in MINUTE):"))

value(mob,mes,tim,tim1)

