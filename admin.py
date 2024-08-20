from db import *
from module import *
adminLogin = lambda usr,pswd: {print("Logged inn Successfully!!"),True} if usr == adminUsername and pswd == adminPassword else False
def removeQuestionFromDirectory():
    print("This Module is under Development!\n\n\t\tStay tuned")
def addNewQuestionsToDirectory():
    global adminSessionStatus
    if adminSessionStatus:

        QuestionToBeAdded = input("Enter Question: ")
        addNewChoicesToList()
        CorrectChoice = input("Enter Correct Choice")

        qNa.update({QuestionToBeAdded:CorrectChoice})
def addNewChoicesToList():
    global adminSessionStatus

    if adminSessionStatus:

        option = ""
        newChoiceForQuiz = ""

        temporaryBufferList = []

        for i in range(4):
            if i == 0:
                option = 'A'
            elif i == 1:
                option = 'B'

            elif i == 2:
                option = 'C'

            else:
                option = 'D'

            
            newChoiceForQuiz = input(f"Enter Choice for {option}: ")
            temporaryBufferList.append(f"{option}) {newChoiceForQuiz}")

        chs.append(temporaryBufferList)

    else:

        print("Session Has Expired!!")


    pass
def sessionManagement(isAdminLoginVerified):
    global adminSessionStatus

    if isAdminLoginVerified:

        print("your Session has been created")
        adminSessionStatus = True

#-------Updated on 20-08-2024-------

'''def adminLogin(usr,pswd):

    if usr == adminUsername and pswd == adminPassword:

        print(" Logged inn Successfully!!")

        return True'''

def adminDashboard():

    global adminTask

    adminTask = input("\n\n| ======================================== DASHBOARD ======================================== |\n\nAdd Questions? or Remove Questions?\n\nEnter A or R: ")

    if adminTask.lower() in ['a', 'r']:
        return adminTask
    
    elif adminTask.lower() == "quit":

        return 0
    
    else:
        print("Wrong Choice")


adminSessionStatus = False

sessionManagement(adminLogin(input("ENTER USERNAME: "), input("ENTER PASSWORD: ")))
while adminSessionStatus:

    processStatus = adminDashboard()

    if processStatus == 0:
        print("\n\nSession Terminated!!!\n\n")
        adminSessionStatus = False

    elif processStatus == 'a':
        addNewQuestionsToDirectory()

    elif processStatus == 'r':

        removeQuestionFromDirectory()