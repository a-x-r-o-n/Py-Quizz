from module import *
startTime = time.time()
isNewGame = True
questionNoAttempted = []
cont = "y"
name = input("enter your name: ")
studentLog("NEW",name,None)
question_number = 0

while (isNewGame or cont == 'y') and question_number <= totalNumberOfQuestions:
    isNewGame = False

    question_number = random.randint(1,totalNumberOfQuestions)


    if (question_number not in questionNoAttempted) and len(questionNoAttempted)<=totalNumberOfQuestions:

        result(checkAnswer(loadGame(question_number),question_number))
        
        cont = input("\n\nwant to continue?\nY or N\n\nenter choice:").lower()

    questionNoAttempted.append(question_number)

    


scoreBoard(name)
endTime = time.time()