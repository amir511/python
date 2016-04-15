#!/usr/bin/python3

''' this is a Notepad program, the purpose of this program is to make a simple GUI notepad which will be functional
'''

from easygui import*
def start_f(): #the first frame from which all other frames will be called
    input1= buttonbox(msg='Welcome to SimpleNote 1.0, Please make a choice: ',
                      title='SimpleNote 1.0',choices=['New','Open','Exit'],image='logo.png')
    if input1== None or input1=='Exit':
        quit()
    elif input1=='Open':
       open_f()
    elif input1=='New':
        new_f()
def open_f():#this function is for viewing AND also editing a file
    '''this is a list of the variables in this function and their description:
    input1: STRING : filename and its path inputed by user from the first fileopenbox
    output2: STRING: text read from the file opened by the user
    output1: STRING: text outputted from the simplenote textbox, contains old text in file+user new added test
    output3: INTEGER: representing the index number of the user choice of the filesave prompt
    output4: STRING: new filename with its new path inputed by user after pressing SAVE AS'''
    input1=fileopenbox(msg='Choose a file to open: ',title='Open file',default='*',filetypes=['*.txt'],multiple=False)
    try:
        fr=open(input1,'r')
        output2=fr.readlines()
        fr.close()
        output1=textbox(msg='When you finish editing or viewing, Press Ok and you will be prompted to save',
                        title=input1,text=output2,codebox=0)
        output3=indexbox(msg='How do you want to save?', title='Save file',
                         choices=('Save changes','Save a copy as', 'Discard changes'), image=None,
                 default_choice='Save changes', cancel_choice='Discard changes')
        if output3== 0: #if user pressed save changes
            fw=open(input1,'w')
            fw.write(output1)
            fw.close()
        elif output3==1: #if user pressed Save a copy
            output4=filesavebox(msg='Save file as',title='Save',default=input1,filetypes=['*.txt'])
            fw=open(output4,'w')
            fw.write(output1)
            fw.close()
    except:
        start_f()
def new_f():
    output1=''
    while True:
        try:
            output1=textbox(msg='When you finish editing, Press Ok and you will be prompted to save',
                            title='Untitled',text=output1,codebox=0)
            output2=filesavebox(msg='Save file as',title='Save',default='Untitled.txt',filetypes=['*.txt'])
            fw=open(output2,'w')
            fw.write(output1)
            fw.close()
            break
        except:
            ynchoice=ynbox(msg='Do you want to discard this file?')
            if ynchoice == True:
                start_f()
            else:
                continue
while True:
    start_f()


