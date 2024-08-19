from db import *

# ---------- | Methoda | ---------------

def loadGame(qi):
    global questionsAttempted


    questionsAttempted += 1
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
        print("Correct Answer!!")

    elif not isCorrect:
        wrongAnswers += 1
        print("Wrong Answer!!")

    pass

def scoreBoard(name):

    print(f"\n\n---------- | SCORE BOARD | ---------------\n\nName: {name}\nNumber of Questions Attempted: {questionsAttempted}\nNumber of correct Answers: {correctAnswers}\nNumber of Wrong Answers: {wrongAnswers}\n\nAccuracy: {int((correctAnswers/questionsAttempted)*100)}%")



def totitms(t):
    for tot in chs:
        t += 1

    return t


# ---------- | Admin |----------------------




# ---------- | Attributes | ---------------


totalNumberOfQuestions = totitms(0)
questionsAttempted = 0
correctAnswers = 0
wrongAnswers = 0
