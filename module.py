from db import *
import time
import random
import datetime

# ---------- | Methoda | ---------------
def writeFile(logpath,msg):
    with open(logpath,'a') as file:
        
        file.write(msg)

def studentLog(logType,secondParam,thirdParam):
    if logType == "NEW":
        writeFile("D:\\scraps\\PY\\P R O J E C T S\\Quiz\\logFiles\\studentProgress.txt",f"|==============================================================================|\n\nStudent Name: {secondParam}\nDate of attempt: {(datetime.datetime.now()).day}/{(datetime.datetime.now()).month}/{(datetime.datetime.now()).year}\nTime: {(datetime.datetime.now()).hour}:{(datetime.datetime.now()).minute}")
    elif logType == "STATS":
        writeFile("D:\\scraps\\PY\\P R O J E C T S\\Quiz\\logFiles\\studentProgress.txt",f"\n\nQuestion Number: {secondParam}\nAnswer Status: {thirdParam}")

    elif logType == "FINAL":
        writeFile("D:\\scraps\\PY\\P R O J E C T S\\Quiz\\logFiles\\studentProgress.txt",f"\n\n__________________\n\nTotal questions attempted: {secondParam}\nTotal Correct Answers: {thirdParam}\nTotal Wrong Answers: {secondParam-thirdParam}\n\n|==============================================================================|")
    pass
def loadGame(qi):
    global totalQuestionsAnswered


    totalQuestionsAnswered += 1
    localCount = 0

    for traverse in qNa:

        localCount += 1
        if localCount == qi:

            print(f"\n\nQuestion {localCount}\n____________\n\n{traverse}")
            for chi in chs[localCount-1]:
                print(f"{chi}")

            ch = input("\n\nEnter Choice: ")

            return ch

def checkAnswer(ch,qi):
    localCount = 0
    for i in qNa:
        localCount += 1
        if localCount == qi:
            ans = qNa[i]

    if ch.lower() == ans.lower():
        studentLog("STATS",qi,True)
        return True

    else:
        studentLog("STATS",qi,False)
        return False

def result(isCorrect):
    global correctAnswers,wrongAnswers

    if isCorrect:

        correctAnswers += 1
    elif not isCorrect:
        wrongAnswers += 1
    
    print("Moving on to the next Question....\n\n")

def scoreBoard(name):

    print(f"\n\n---------- | SCORE BOARD | ---------------\n\nName: {name}\nNumber of Questions Attempted: {totalQuestionsAnswered}\nNumber of correct Answers: {correctAnswers}\nNumber of Wrong Answers: {wrongAnswers}\n\nAccuracy: {int((correctAnswers/totalQuestionsAnswered)*100)}%")
    studentLog("FINAL",totalQuestionsAnswered,correctAnswers)



def totitms(t):
    for tot in chs:
        t += 1

    return t


# ---------- | Admin |----------------------




# ---------- | Attributes | ---------------


totalNumberOfQuestions = totitms(0)
totalQuestionsAnswered = 0
correctAnswers = 0
wrongAnswers = 0
