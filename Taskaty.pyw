#!/usr/bin/python3
from easygui import*
import re
import os
#function for making a new account
def new_user():
    inp1 = multpasswordbox(msg='Welcome to Taskaty!\n Please create your user ID to continue',title='Welcome!',
                           fields=['User Name','Password'])
    f=open('UserID','w')
    f.write(inp1[0]+'\n'+inp1[1])
    f.close()
    enter_pass()
#function for accessing the already existent account
def enter_pass():
    f=open('UserID','r')
    user_data=f.readlines()
    f.close()
    inp_pass=passwordbox(msg='Welcome ' + user_data[0] + ' to Taskaty! \nPlease enter your passowrd:', title='Welcome!') #TODO: need to add logo to this box
    if inp_pass == user_data[1]:
        first_choice()
    elif inp_pass == None:
        quit()
    else:
        msgbox(msg='WRONG PASSWORD!\n Please Try again')
        enter_pass()
#first prompt frame after user login that leads to other frames
def first_choice():
    ch=indexbox('What do you want to do?',choices=('Work with existing categories','Create a new category','Exit'))
    if ch == 0:
        categories()
    elif ch == 1:
        new_category()
    elif ch == 3:
        quit()
#function for adding new categories
def new_category():
    try:
        cat_name=enterbox('Enter the name of the new category: ', 'New Category')
        os.mkdir('categories/'+cat_name)
    except FileExistsError:
        msgbox('Category already exists!, Please choose a different name.')
        new_category()
    except:
        first_choice()
    ch=ynbox('Do you want to add more?', default_choice='No')
    if ch == True:
        new_category()
    else:
        first_choice()
#function for working with existing categories
def categories():
    cats=os.listdir('categories')
    ch_cat=choicebox('Please select a category: ','Categories available',cats)
    if ch_cat == None:
        first_choice()
    else:
    #first_choice() if ch_cat == None else None
        ch=indexbox('What do you want to do?',choices=('Work with existing tasks','Create a new task','Return'))
        if ch == 0:
            tasks(ch_cat)
        elif ch == 1:
            new_task(ch_cat)
        elif ch == 3:
            categories()
def tasks(a):
    tasks=os.listdir('categories/'+a)
    if tasks == []:
        msgbox('There are no tasks yet in this category, Please add tasks first!.')
        categories()
    else:
        ch_task=choicebox('Please select a task: ','tasks available',tasks)
    if ch_task == None:
        categories()
    else:
        f=open('categories/'+a+'/'+ch_task,'r')
        text_old=f.readlines()
        f.close()
        text_new=textbox(ch_task+'\nEdit your task',text=text_old)
        ff=open('categories/'+a+'/'+ch_task,'w')
        ff.write(text_new)
        ff.close()
        categories()
def new_task(ch_cat):
    try:
        task_name=enterbox('Enter the name of the new Task: ', 'New Task')
        f=open('categories/'+ch_cat+'/'+task_name,'w')
        f.close()
    except FileExistsError:
        msgbox('Task already exists!, Please choose a different name.')
        new_task(ch_cat)
    except:
        categories()
    ch=ynbox('Do you want to add more?', default_choice='No')
    if ch == True:
        new_task(ch_cat)
    else:
        tasks(ch_cat)




#program initiated here
f=open('UserID','r')
user_data=f.readlines()
f.close()
if user_data == []:
    new_user()
else:
    enter_pass() 

