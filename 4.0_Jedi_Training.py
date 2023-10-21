# 4.0 Jedi Training (40pts)  Name:________________
# Below each program list the mistakes found in comments.

# 1. Make the following program work. (3 mistakes)  (3pts)

# midichlorians = float(input("Enter midichlorian count: "))
# if midichlorians > 10000:
#     print("You have serious Jedi potential")
# else:
#     print("Jedi, you will never be.")

# indentation error(s) on first line
# parenthesis missing in variable declaration
# colon missing after first if statement
# change elif to else and add colon

# 2. Make the following program work. (3 mistakes)  (3pts)
     
# x = input("Enter a number: ")
# if x == 3:
#     print("You entered 3")

# indentation error on first line
# colon missing in if statement
# use == in comparison

# 3. Make the following program work. (4 mistakes)  (4pts)

# answer = input("What is the name of Poe Dameron's Droid? ")
# if answer == "BB8":
#     print("Correct!")
# else:
#     print("Incorrect! It is BB8.")

# indentation on first line
# if statement indentation
# change 'a' to answer
# == for comparison
# add : after else
# 4. Make the following program work. (4 mistakes) (4pts)
     
jedi = input("Name one of the top 3 greatest Jedi.\n:")
if jedi.lower() == "yoda" or jedi.lower() == "luke skywalker" or jedi.lower() == "obi-wan kenobi":
    print("That is correct!")
else:
    print("That person isn't one of the greatest jedi.")

# "" around yoda
# "" around luke skywalker
# "" around obi-wan- kenobi
# () around print statement
# change x to jedi

# 5. Make the following program work whether they enter 'a', A, Jedi Master or jedi master
#    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?: ")

if user_input.lower() == "a" or user_input.lower() == "jedi master":
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() == "sith lord":
    sensitivity = 900
elif user_input.lower() == "c" or user_input.lower() == "droid":
    sensitivity = 0
else:
    sensitivity = " "
    print("Not a choice!")

print("Sensitivity: ", sensitivity)

# indentations
# "" around A
# use == for comparison checks
# elif instead of else if
# lowercase 's' in sensitivity
# change to else at the end


'''
6. NUMBER ANALYSIS PROGRAM  (10pts)
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''


def number_report():
    num = int(input("Give a number and we'll read out the characteristics of that number:\n"))

    remainder = num % 2
    if remainder == 0:
        test_1 = "Even"
    else:
        test_1 = "Odd"
    if num < 0:
        test_2 = "Negative"
    elif num > 0:
        test_2 = "Positive"
    else:
        test_2 = "Zero"
    if num < -100 or num > 100:
        test_3 = "Exclusive"
    else:
        test_3 = "Inclusive"

    print("Test 1: ", test_1)
    print("Test 2: ", test_2)
    print("Test 3: ", test_3)


number_report()



'''
GRADING 2.0    (10pts)
-------------------
Copy your Grading 1.0 program below and then modify it to also print out the letter grade depending on the numerical 
grade.
If they fail, tell them to "Transfer to Johnston!"
'''


def grade_calc():
    sg = float(input("What was your semester grade?\n:"))
    fe = float(input("What was your final exam grade\n:"))
    ew = float(input("How much is the final exam worth?\n:"))
    fg = ((ew*fe) + (100-ew)*sg)/100

    if fg >= 93:
        lg = "A"
    elif 90 <= fg <= 92.9:
        lg = "A-"
    elif 87 <= fg <= 89.9:
        lg = "B+"
    elif 83 <= fg <= 86.9:
        lg = "B"
    elif 80 <= fg <= 82.9:
        lg = "B-"
    elif 77 <= fg <= 79.9:
        lg = "C+"
    elif 73 <= fg <= 76.9:
        lg = "C"
    elif 70 <= fg <= 72.9:
        lg = "C-"
    elif 67 <= fg <= 69.9:
        lg = "D+"
    elif 63 <= fg <= 66.9:
        lg = "D"
    elif 60 <= fg <= 62.9:
        lg = "D-"
    else:
        lg = "F"
    print("Your overall grade for the class is:", fg, "\nThis is a(n):", lg)
    if lg == "F":
        print("Transfer to Johnston!")


grade_calc()

