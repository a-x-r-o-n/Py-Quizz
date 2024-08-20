from db import *

# ---------- | Methoda | ---------------

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

        return True

    else:
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
