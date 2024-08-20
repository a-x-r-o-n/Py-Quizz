from module import *
import random
isNewGame = True
questionNoAttempted = []
cont = "y"

name = input("enter your name: ")

question_number = random.randint(1,totalNumberOfQuestions)



while (isNewGame or cont == 'y') and question_number <= totalNumberOfQuestions:
    isNewGame = False

    question_number = random.randint(1,totalNumberOfQuestions)


    if (question_number not in questionNoAttempted) and len(questionNoAttempted)<=totalNumberOfQuestions:

        result(checkAnswer(loadGame(question_number),question_number))
        
        cont = input("\n\nwant to continue?\nY or N\n\nenter choice:").lower()

    questionNoAttempted.append(question_number)

    


scoreBoard(name)