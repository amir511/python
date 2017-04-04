# a script made to get the difference between two dates, with giving the option to exclude days, like e.g. fridays and saturdays to get the working days only
# np.busday_count('2017-01-01', '2018-01-01', weekmask="Sun Mon Tue Wed Thu Fri Sat")

import numpy as np
import colorama
from termcolor import cprint

colorama.init()

#default values for working and weekend days
weekendDefault="Fri Sat"
workingDaysDefault = "Sun Mon Tue Wed Thu"
allDays = "Sun Mon Tue Wed Thu Fri Sat"

workingDaysString = workingDaysDefault #initial value for this variable which migh be changed after that

#Strings written alone to avoid cluttering code
welcomeString = "This is a script to calculate the difference between two dates in WORKING days, written by E. Amir Anwar on 9-Mar-2017"
beginningDateString = "Please enter The beginning date in the following format: YYYY-MM-DD\n"
endingDateString = "Please enter The ending date in the following format: YYYY-MM-DD\n"
weekendString = '''Default weekend is Friday and Saturday
                   Press Enter to accept, or enter the weekend days separated by space in the following format:
                   Fri for Friday, Sat for Saturday, Sun for Sunday, Mon for Monday, Tue for Tuesday, Wed for Wednesday, Thu for Thursday
                   Example: "Sat Sun" \n'''



def main():
    beginningDate = input(beginningDateString)
    endingDate = input(endingDateString) 
    difference = np.busday_count(beginningDate, endingDate, weekmask= workingDaysString)
    print("Excluding weekend days,and NOT counting last day, the difference in working days is :")
    cprint(str(difference) + " working days", 'green' )
    
# this function calculates the working days based on the weekend
def getWorkingDays(weekend):
    if weekend == "" or weekend == weekendDefault:
        return workingDaysDefault
    else:
        allDaysArray = allDays.split()
        weekendArray = weekend.split()
        workingDaysArray = []
        for i in range(0,len(allDaysArray)):
            if allDaysArray[i] != weekendArray[0] and allDaysArray[i] != weekendArray[1]:
                workingDaysArray.append(allDaysArray[i])
        workingDays = ""
        for i in range(0,len(workingDaysArray)):
            workingDays += workingDaysArray[i]+" "
        return workingDays

#The following lines will run once only
def programStart():
    cprint(welcomeString,'blue')
    weekend = input(weekendString)
    workingDaysString = getWorkingDays(weekend)
    cprint("The working days are:"+ workingDaysString,'blue')



#Execution of the programs:
try:
    programStart()
except:
    cprint("Error, Restarting program",'red')
    programStart()

while(True):
    try:
        main()
    except:
        cprint("Something wrong, please make sure that all entered values are correct and in the right format",'red')
        main()
