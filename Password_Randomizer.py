import string #To get the letter and symbol list
import random #Very useful randomizer functions

print("This programme will generate a randomized password")
Letter = int(input("Enter the number of letter you want: "))
Number = int(input("Enter the number of number you want: "))
Symbol = int(input("Enter the number of symbol you want: "))

print("The length of your password is: ", Letter + Number + Symbol)

Password = [] #Defining the Password "set" beforehand

x = range(Letter)
for n in x:
    Password.append(random.choice(string.ascii_letters))

x = range(Number)
for n in x:
    Password.append(str(random.randint(0, 9)))  #I use the function str() to convert randomized numbers into string for later

x = range(Symbol)
for n in x:
    Password.append(random.choice(string.punctuation))

random.shuffle(Password) #I was thinking of combining this with the below command, but it turns out random.shuffle() returns None rather than a list

print("".join(Password))
