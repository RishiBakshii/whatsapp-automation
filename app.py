import pywhatkit
import time
import random

msg="""
IMS DIA -  Interior  Architecture and design  💯 Free 💯
Online  WEBINAR by AR. ROHIT BHARTI
Time: Tue, 25 July, 2023, 11:00 AM

Webinar Registers Form
https://forms.gle/Mx9smG8oLfQeEJgHA 

Please click this Zoom meeting URL 
https://zoom.us/j/91262708218?pwd=UGVjZ0w4V2kzaEFOQkh6RzB4RVg1Zz09 
"""

def generateRandomNumber(): 
    random_number=random.randint(10,20)
    return random_number

def sendWhatsAppMessage(phoneNumber,Message):
    pywhatkit.sendwhats_image(f'+91{phoneNumber}', "posterImage.jpg",caption=msg)
    print(f"Message Forwarded to {phoneNumber}")

def main():
    NumberCount=1
    with open("contacts.txt",'r') as fileObj:
        for number in fileObj.readlines():
            print(f'{NumberCount} : {number}')
            time.sleep(generateRandomNumber())
            
            sendWhatsAppMessage('9971205564',Message=msg)
            print(f"sended to {number}")
            
            NumberCount+=1
            
            if(NumberCount==10):
                break
            
main()