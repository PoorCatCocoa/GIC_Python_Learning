#Q1
import random
rolls = [0] * 13                                                        #make list roll 13 unit
for i in range(1000):                                                   #for loop for 1000times circle from 1 to 1000
    dice_sum = random.randint(1,6) +random.randint(1,6)     #make dice_sum random from 2-12
    rolls[dice_sum] += 1                                                #every circle +1 in unit of roll
for sum_value in range(2,13):                                           #for loop for sum_value circle in range 2-13
    print(f"Sum {sum_value}: {rolls[sum_value]} times")                 #print the result by 2-13: rolls[2-13]

#Q2
x = int(input("Enter a integer: "))
for i in range(x):
    if x /1 and x /i == 0:
        print(x)