import random
c=0
while True:
    print("Enter a number between 1 to 6 :")
    num = int(input())
    dice_num = random.randint(1, 6)
    print("Random number come on DICE :", dice_num)
    if(num == dice_num):
        c+=1
    print("Your Score :", c)
    print("Enter q to EXIT the game and p to CONTINUE the game :")
    run=str(input())
    if(run=="q"):
        break


