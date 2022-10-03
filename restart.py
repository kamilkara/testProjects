#1 Input: Number
# Ouput: Check whether the number is even or odd

# number = int(input("Please enter the number: "))
# if (number % 2 == 0):
#     print("Number is even");
# else:
#     print("Number is odd")

##########################
#2 Input: Name
# Output: Find the length of the number

# name = input("Please enter the name: ");
# print(len(name))

#########################
#3 Input: DOB
# Output: Age in year and in months

# import datetime
#
# birthYear = int(input("Please enter your year of birth: "))
# birthMonth = int(input("Please enter month (0-12)"))
#
# while birthMonth < 0 or birthMonth > 12:
#     birthMonth = int(input("Please type a correct month value: "))
#
# birthDay = int(input("Please enter your day of birth: "))
#
# calcYear = datetime.date.today().year - birthYear
# calcMonth = datetime.date.today().month - birthMonth
#
# print(str(calcYear) + " years " + str(calcMonth) + " months")

################
#4 Create a list , add 5 element (of any data type)

# list = [1, 2, 3, 4, 5]
# print(list)
# print(len(list))
# list.append([7,8,9,10])
# print(list)
# print(len(list))

#################
#3 alternative solution
# import datetime
#
# name = input("Hello! Let me know your name please: ")
# date = input("Hi {}! Please type your date of birth (dd/mm/yyyy): ".format(name))
#
# def calculate(date):
#     dateDay = int(date[0:2])
#     dateMonth = int(date[3:5])
#     dateYear = int(date[6:])
#     calcYear = datetime.date.today().year - dateYear
#     calcMonth = datetime.date.today().month - dateMonth
#     calcDay = datetime.date.today().day - dateDay
#     print("{}, you are {} years {} months and {} days old. Memento Mori!!!".format(name, calcYear, calcMonth, calcDay))
# calculate(date)

##################
#6 Maximum of two numbers in Python

# num1 = int(input("Please enter number 1: "));
# num2 = int(input("Please enter number 2: "));
#
# def greater(num1, num2):
#     if num1 < num2:
#         print("{} is the max value of the list.".format(num2));
#     elif num1 > num2:
#         print("{} is the max value of the list.".format(num1));
#     else:
#         print("Nice try! The numbers are equal :)");
#
# greater(num1, num2);

##################
#9 Python Program for Program to find area of a circle

# import math
#
# radius = int(input("Please enter the radius of circle: "));
#
# def circleArea(x):
#     area = round(math.pi * x ** 2, 4)
#     print(area)
#
# circleArea(radius)

##################
#11 Python Program for Sum of squares of first n natural numbers

# number = int(input("Please enter the number: "))
# total = 0;
# for i in range(0, number+1):
#     total += i**2
# print(total)

##################
#12 Python Program for cube sum of first n natural numbers

# number = int(input("Please enter the number: "))
# totalNum = 0
# for i in range(0, number+1):
#     totalNum += i
# print(totalNum**3)

##################
#15 Print the sum of the current number and the previous number

# number = int(input("Please enter the number: "));
# print(number*2-1)

##################
#16 Print characters from a string that are present at an even index number

# word = input("Please enter the word: ");
# list = []
# for i in range(0, len(word), 2):
#     list += word[i]
#     continue
# print(list)

##################
#17 Check if the first and last number of a list is the same
#
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 35]
#
# def compare(x, y):
#     resultX = False;
#     resultY = False;
#     if x[0] == x[-1]:
#         resultX = True;
#         print(resultX)
#     else:
#         print(resultX)
#
#     if y[0] == y[-1]:
#         resultY = True;
#         print(resultY)
#     else:
#         print(resultY)
#
# compare(numbers_x, numbers_y)

##################
#18 Display numbers divisible by 5 from a list
#
# list = [10, 20, 33, 46, 55]
#
# for i in list:
#     if i % 5 == 0:
#         print(i)

#19
#
# number = int(input("Please enter a number: "))
#
# for i in range(1, number+1):
#     print(str(i)*i)

##################
#20
#
# import operator
# operators ={
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv}
#
# calc = input("Please enter an operator ( + - * / ): ")
#
# num1 = int(input("Please enter num1: "));
# num2 = int(input("Please enter num2: "));
# stop = "n";
#
# total = operators[calc](num1, num2);
# print(total)
#
#
# while stop != "S":
#     decideInput = input("What do you want to do? Add numbers (a), change operator (c), stop program (s): ")
#     if decideInput.lower() == "a":
#         newInput = int(input("New number: "));
#         total = operators[calc](total, newInput)
#         print(total)
#     elif decideInput.lower() == "c":
#         calc = input("New operator ( + - * / ): ")
#         newInput = int(input("New number: "));
#         total = operators[calc](total, newInput)
#         print(total)
#     elif decideInput.lower() == "s":
#         stop = "S";

text = "kamil kara"

def reverse(word):
    # count = 0
    # newText = ""
    # for i in word:
    #     count -= 1
    #     newText += word[count]
    #
    # print(newText)
    word = word[::-1]
    print(word)

reverse("kamil")

