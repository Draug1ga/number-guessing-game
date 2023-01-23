import random

def generateNum():
    num = random.randrange(1,10)
    num = int(num)
    print(num)
    return num

def playerGuess():
    try:
        guess = input("Please guess a number between 1 & 10...")
        gnum = int(guess)
        
    except ValueError:
        print("Oops that is not a valid entry")
 
    else:
        return gnum

def welcome():
    print("NUMBER GUESSING GAME")
    player = input("What is your name? ")
    print("Hello {}. Welcome to the number guessing game!".format(player))

    if scoreList == []:
        print("There is no current highscore. Let's make one!")
    else:
        print("The current Highscore is {}".format(max(scoreList)))

def guessLoop():

    try:
        count = 1
        num = generateNum()
        gnum = playerGuess()

        while gnum != num:
            if gnum < num:
                print("Your guess is too low")
            elif gnum > num:
                print("Your guess is too High")
            gnum = playerGuess()
            count = count + 1
            currentScore = int(100 / count)
        else:
            if count == 1:
                currentScore = int(100 / count)
                print("Thats correct!")
                print("It took you {} guess".format(count))
                print("Great Job your score is {}".format(currentScore))
                highScore(currentScore)

            elif count != 1:
                print("Thats correct!")
                print("It took you {} guesses".format(count))
                print("Great Job your score is {}".format(currentScore))
                highScore(currentScore)
    except TypeError:
        pass

def playAgain():
    repeatgame = input("Type YES, if you'd like to play again?...")
    if repeatgame == "YES":
        main()
    elif repeatgame == "yes":
        main()
    else:
        print("Thank you for playing the number guessing game!")

def highScore(currentScore):
    scoreList.append(currentScore)
        
def main():
    welcome()
    guessLoop()
    playAgain()


scoreList = []
main()