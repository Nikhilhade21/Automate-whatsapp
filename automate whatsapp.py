# import pywhatkit

# def value(num1,num2,num3,num4):
#     t=[num3,num4]
#     p=t[0]
#     k=t[1]
#     j='+91'
#     pywhatkit.sendwhatmsg(j+(num1),num2,p,k)

# mob=input("Enter Number to Send Message:")
# mes=input("Enter Your Message:")
# tim=int(input("Enter Time(in HOUR):"))
# tim1=int(input("Enter Time(in MINUTE):"))

# value(mob,mes,tim,tim1)
import pywhatkit
from datetime import datetime, timedelta
import time  # Add this import statement

def send_message_with_delay(num1, num2, delay_seconds):
    j = '+91'
    
    # Calculate the time to send the message (current time + delay)
    send_time = datetime.now() + timedelta(seconds=delay_seconds)
    time_hour, time_min = send_time.hour, send_time.minute
    
    # Wait for the specified delay
    time.sleep(delay_seconds)
    
    # Send the message
    pywhatkit.sendwhatmsg(j + num1, num2, time_hour, time_min)

mob = input("Enter Number to Send Message: ")
mes = input("Enter Your Message: ")

# Set delay to 10 seconds
delay_seconds = 10

send_message_with_delay(mob, mes, delay_seconds)

#7030503537