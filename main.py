import string
import random

print("This programme will generate a randomized password")
Letter = int(input("Enter the number of letter you want: "))
Number = int(input("Enter the number of number you want: "))
Symbol = int(input("Enter the number of symbol you want: "))

print("The length of your password is: ", Letter + Number + Symbol)

Password = []

x = range(Letter)
for n in x:
    Password.append(random.choice(string.ascii_letters))

x = range(Number)
for n in x:
    Password.append(str(random.randint(0, 9)))

x = range(Symbol)
for n in x:
    Password.append(random.choice(string.punctuation))

random.shuffle(Password)

print("".join(Password))