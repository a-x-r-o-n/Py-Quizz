from module import *
isNewGame = True
cont = "y"
name = input("enter your name: ")

question_number = 1


while (isNewGame or cont == 'y') and question_number <= totalNumberOfQuestions:
    isNewGame = False


    result(checkAnswer(loadGame(question_number),question_number))
    
    cont = input("\n\nwant to continue?\nY or N\n\nenter choice:").lower()

    question_number += 1

    if question_number > totalNumberOfQuestions:

        print("\n\nQuestions not avalable at this moment, Try again after sometime!!\n\n")


scoreBoard(name)