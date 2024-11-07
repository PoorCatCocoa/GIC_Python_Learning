import time
age = input("Please enter your age for the discount: ")
if age <= "12":
    print("\nYou are a child.")
    print("\nThe price is 2$")
elif age <= "18":
    print("\nYou are a teenager.")
    print("\nThe price is 3$")
elif age <= "25":
    print("\nYou are a adult.")
    print("\nThe price is 4$")

i =1
while i < 21:
    print(i)
    i +=1
e = 2
while e <= 21:
    print(e)
    e +=2
c = 0
for c in range (c, int(input("Enter an number: \nEnter 'E' to stop\n"))):
    print(c)
    c +=1
    time.sleep(0.1)
    if input() == 'E' or 'e':
        break