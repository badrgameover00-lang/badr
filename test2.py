import random
print("hey this is a guessing game u have only three trys or u will die \n guess a number between 1-100 \n u have chances based on the ur diffuclty \n have fun")
number = random.randrange(1,101)
lifes = 0
end_game = 0

difficulty = int(input("choose u difficulty (put the number next to the dificulty \n 1_easy \n 2_mediam \n 3_hard \n"))
if difficulty ==1:
    end_game = 20
elif difficulty == 2:
    end_game =10
elif difficulty == 3:
    end_game=5

while True :
    guess = int(input("your guess : "))
    if guess == number :
        lifes += 1
        print(f"groncratiolation u have guesses the coreect number wich was {number} u did it in ur {lifes}'th guess")
        break
    elif guess != number :
        print ("wrong guess !!!")
        lifes += 1
    if lifes == end_game:
        print(f"u have used all ur 3 lifes and the correct number was {number} ur going to die now byeee")
        break
    
    if guess > number:
        print("ur number is bigger than the goal")
    elif guess < number:
        print("ur number is smaller than the goal")