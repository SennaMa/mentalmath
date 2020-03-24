#Addition tool - Print random numbers to improve my mental math

#pulling random numbers and defining them
import random
numberOfGoods = 0
numberOfBads = 0

#use a for loop if you only want this to run X times. Then you can count how many



for _ in range(10):   #change to always loop
    userNum = 0
    answer = -9999

    topNum = random.randint(1, 100)
    botNum = random.randint(1, 100)
    answer = topNum + botNum

    print(topNum)
    print(botNum)
    ##print(answer)


    userinput = input("What is the answer?\n") or 0
    # /n will put your code
    # by writing "or 0" this means you either write an answer or it defaults to 0
    # same as:
    # if userinput == None:
    #     userinput = 0


#checking the answer
    if int(userinput) == answer:
        print("good")
        numberOfGoods += 1
    elif int(userinput) != answer:
        print("bad")
        numberOfBads += 1


#after 10 entries, print and total your score
print("Correct = {}\nIncorrect = {}".format(numberOfGoods, numberOfBads))
    #/n is a new line
    #prints the number of correct and incorrects
    #{} will put the numbers in the format in the brackets





