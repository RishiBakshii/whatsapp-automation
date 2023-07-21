import pywhatkit
import time
import random
from contacts import contact
from html import escape

registrationFormLink='https://forms.gle/Mx9smG8oLfQeEJgHA'
zoomLink='https://zoom.us/j/91262708218?pwd=UGVjZ0w4V2kzaEFOQkh6RzB4RVg1Zz09'


def create_clickable_link(url, link_text):
    # Escape special characters in the URL and link text
    escaped_url = escape(url)
    escaped_text = escape(link_text)
    
    # Construct the HTML anchor tag
    link = f'<a href="{escaped_url}" target="_blank">{escaped_text}</a>'
    
    return link

msg=f"""
IMS DIA -  Interior  Architecture and design  💯 Free 💯
Online WEBINAR by AR. ROHIT BHARTI
Time: Tue, 25 July, 2023, 11:00 AM

Webinar Registration Form
{registrationFormLink}

Please click this Zoom meeting URL 
{zoomLink}
"""

def generateRandomNumber(): 
    random_number=random.randint(10,20)
    return random_number

def sendWhatsAppMessage(phoneNumber,Message):
    pywhatkit.sendwhats_image(f'+91{phoneNumber}', "posterImage.jpg",caption=msg,close_time=10,tab_close=True,wait_time=15)
    print(f"Message Forwarded to {phoneNumber}")

def main():
    NumberCount=1
    with open("contacts.txt",'r') as fileObj:
        for number in fileObj.readlines():
            print(f'{NumberCount} : {number}')
            time.sleep(generateRandomNumber())
            
            sendWhatsAppMessage(contact['krrishOffice'],Message=msg)
            print(f"sended to {number}")
            
            NumberCount+=1
            
            if(NumberCount==10):
                break
main()