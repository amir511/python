''' This script is for sending the sunday emails
outlook should be opened first then the script should be initiated
the script will work automatically when the following key combinateion is pressed:
ctrl+Alt+x
Created by Amir Anwar 29/1/2017
'''
import random
import pyautogui as p
import easygui as e
#Constants:
NPD_subject = "NPD sheet update"
NPD_body1 = '''Dear All
Kindly make sure that the online NPD sheet is up-to-date before tomorrow's meeting
Thanks for your support'''
NPD_body2='''Dear all 
It is important to update the NPD online sheet today before tomorrow's meeting
Many thanks for your support completing any missing info'''
NPD_body3='''Good Morning All
Please make sure that the info in NPD online sheet is up-to-date
We need to be able to discuss the latest info in tomorrow's NPD meeting
Thanks for your support'''
NPD_body4='''Dear all
Kindly make sure that the NPD sheet is up to date so that we can have a complete info to use in tomorrow's meeting
Thank you'''
Transportation_subject="Tomorrow's meeting in M"
Transportation_body='''Dear Mr. X
Kindly arrange a means for transportation to deliver us  tomorrow to M and back to E
We should be at M on 10:30 am 
And We should come back to E before 4:00 pm to catch the company's bus lines
Many thanks
'''
TransportationRecipient="X@E.com.eg"
TransportationCC="Z@E.com.eg;K@M-eg.com;H@E.com.eg"

NPD_body_list=[NPD_body1,NPD_body2,NPD_body3,NPD_body4]
R = random.randint(0, 3)
p.PAUSE = 1
p.FAILSAFE = True
def newBlankEmail():
    p.click()
    p.keyDown("ctrl")
    p.press("n")
    p.keyUp("ctrl")

def newNPDEmail():
    p.moveTo(487,85)
    p.click()
    p.click()

def addRecipient(recipientEmail):
    p.click(184, 166)
    p.typewrite(recipientEmail)

def addCC(CCEmails):
    p.click(184, 197)
    p.click()
    p.typewrite(CCEmails)

def addSubject(subjectText):
    p.click(185, 227)
    p.typewrite(subjectText)

def addBody(bodyText):
    p.click(90, 269)
    p.typewrite(bodyText)

def sendEmail():
    p.click(29, 188)
    
def getRandomNPDBody():
    randomNPDBody = NPD_body_list[R]
    return randomNPDBody

def generateNPDEmail():
    newNPDEmail()
    addSubject(NPD_subject)
    addBody(getRandomNPDBody())
    sendEmail()

def generateTransportationEmail():
    newBlankEmail()
    addRecipient(TransportationRecipient)
    addCC(TransportationCC)
    addSubject(Transportation_subject)
    addBody(Transportation_body)
    sendEmail()

def startDiaolg():
    choice = e.choicebox("What do you want to do?", "Make a choice", ["NPD email","Transportation email"])
    if choice == "NPD email":
        generateNPDEmail()
        startDiaolg()
    elif choice == "Transportation email":
        generateTransportationEmail()
        startDiaolg()

try:
    startDiaolg()
except:
    e.msgbox("Something Wrong happened!", "Error")

