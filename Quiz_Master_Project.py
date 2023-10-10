'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("Have you ever wondered what the best drink in the world is?\nWell, no need to look further,"
      " I'll quench your thirst for the answer.\nObviously it's", "\033[1;31m" + 'Dr.Pepper!' + "\033[0m")
print("\033[1;31m" + 'Dr.Pepper' + "\033[0m", "is without a doubt the most amazing drink and through this short quiz, "
      "we'll find out \nif you can call yourself a, \033[1;31m" + 'Dr.Pepper' + "\033[0m", "know it all.\n")

number_correct = 0


def wrong_q():
    print("\nSorry that wasn't the correct answer, better luck next time!")


def correct_q():
    print("\n\033[1;32m" + "That's right!" + "\033[0m", "You're a \033[1;31m" + 'Dr.Pepper' + "\033[0m", "genius")
    print("Your current score is ", number_correct, "out of 7")


def question_set():
    global number_correct

    def question1():
        global number_correct
        print("Starting things off a bit simple;\nWhen was \033[1;31m" + 'Dr.Pepper' + "\033[0m", "released to the "
              "public?")
        print("A) 1904\nB) 1880\nC) 1885\nD) 1776")
        q_input = str(input(":"))
        if q_input.lower() == "a" or q_input == "1904":
            wrong_q()
            print("The correct answer was C, 1885")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "b" or q_input == "1880":
            wrong_q()
            print("The correct answer was C, 1885")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "c" or q_input == "1885":
            number_correct += 1
            correct_q()
        elif q_input.lower() == "d" or q_input == "1776":
            wrong_q()
            print("The correct answer was C, 1885")
            print("Your current score is ", number_correct, "out of 7")
        else:
            print("That isn't an option, try again")
            question1()
    question1()

    def question2():
        global number_correct
        print("\nNext we'll go to a true of false question")
        print("The release of \033[1;31m" + 'Dr.Pepper' + "\033[0m", "preceded(came before) Coca-Cola")
        q_input = str(input("True or False: "))
        if q_input.lower() == "true" or q_input.lower() == "t":
            number_correct += 1
            correct_q()
        elif q_input.lower() == "false" or q_input.lower() == "f":
            wrong_q()
            print("The correct answer was true! \033[1;31m" + 'Dr.Pepper' + "\033[0m",
                  "predates Coca Cola by one year.")
            print("Your current score is ", number_correct, "out of 7")
        else:
            print("That isn't an option, try again")
            question2()
    question2()

    def question3():
        global number_correct
        print("\nFollowing this, let's delve into the origins of the \x1B[3m" + 'most amazing drink.' + "\x1B[0m")
        print("\nWho was the amazing inventor of \033[1;31m" + 'Dr.Pepper' + "\033[0m")
        print("A) John Stith Pemberton\nB) Charles T Pepper\nC) Caleb Bradham\nD) Charles Alderton\nE) "
              "Dr. William Alexander Reed Pepper")
        q_input = str(input(":"))
        if q_input.lower() == "a" or q_input.lower() == "john stith pemberton":
            wrong_q()
            print("The correct answer was D, Charles Alderton")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "b" or q_input.lower() == "charles t pepper":
            wrong_q()
            print("The correct answer was D, Charles Alderton")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "c" or q_input.lower() == "caleb bradham":
            wrong_q()
            print("The correct answer was D, Charles Alderton")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "d" or q_input == "charles alderton":
            number_correct += 1
            correct_q()
        elif q_input.lower() == "e" or q_input.lower() == "dr. william alexander reed pepper":
            wrong_q()
            print("The correct answer was D, Charles Alderton")
            print("Your current score is ", number_correct, "out of 7")
        else:
            print("That isn't an option, try again")
            question3()
    question3()

    def question4():
        global number_correct
        print("\nSo we all know that \033[1;31m" + 'Dr.Pepper' + "\033[0m", "tastes amazing, but what "
              "does it taste like?")
        print("How many flavors are in \033[1;31m" + 'Dr.Pepper?' + "\033[0m")
        while True:
            try:
                q_input = int(input("Type your answer here:"))
            except ValueError:
                print("Type in a number and try again")
            else:
                break
        if q_input == 23:
            number_correct += 1
            correct_q()
        else:
            wrong_q()
            print("\nThe correct answer was 23!")
            print("The complex flavor profile of \033[1;31m" + 'Dr.Pepper' + "\033[0m", "has 23 unique flavors!")
            print("Your current score is ", number_correct, "out of 7")
    question4()

    def question5():
        global number_correct
        print("\nThe secret of \033[1;31m" + 'Dr.Pepper' + "\033[0m", "must be kept.")
        print("How many banks is the recipe of \033[1;31m" + 'Dr.Pepper' + "\033[0m", "split between?")
        print("A) 17\nB) 10\nC) 4\nD) 2")
        q_input = input(":")
        if q_input.lower() == "a" or q_input == "17":
            wrong_q()
            print("The correct answer was D, 2")
            print("\033[1;31m" + 'Dr.Pepper\'s' + "\033[0m", "recipe is split between two banks in Dallas")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "b" or q_input == "10":
            wrong_q()
            print("The correct answer was D, 2")
            print("\033[1;31m" + 'Dr.Pepper\'s' + "\033[0m", "recipe is split between two banks in Dallas")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "c" or q_input == "4":
            wrong_q()
            print("The correct answer was D, 2")
            print("\033[1;31m" + 'Dr.Pepper\'s' + "\033[0m", "recipe is split between two banks in Dallas")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "d" or q_input == "2":
            number_correct += 1
            correct_q()
        else:
            print("That isn't an option, try again")
            question1()
    question5()

    def question6():
        global number_correct
        print("\nHopefully you've developed some appreciation "
              "for \033[1;31m" + 'Dr.Pepper' + "\033[0m", "through this quiz.\n"
              "Here's the next question:")
        print("All across the world, how many total varieties of \033[1;31m" + 'Dr.Pepper' + "\033[0m", "are there?")
        print("A) 26\nB) 47\nC) 32\nD) 17")
        q_input = input(":")
        if q_input.lower() == "a" or q_input == "26":
            number_correct += 1
            correct_q()
        elif q_input.lower() == "b" or q_input == "47":
            wrong_q()
            print("The correct answer was A, 26")
            print("There are 26 different varieties of \033[1;31m" + 'Dr.Pepper\'s' + "\033[0m",
                  "all across the world!")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "c" or q_input == "32":
            wrong_q()
            print("The correct answer was A, 26")
            print("There are 26 different varieties of \033[1;31m" + 'Dr.Pepper\'s' + "\033[0m",
                  "all across the world!")
            print("Your current score is ", number_correct, "out of 7")
        elif q_input.lower() == "d" or q_input == "17":
            wrong_q()
            print("The correct answer was A, 26")
            print("There are 26 different varieties of \033[1;31m" + 'Dr.Pepper\'s' + "\033[0m",
                  "all across the world!")
            print("Your current score is ", number_correct, "out of 7")
        else:
            print("That isn't an option, try again")
            question1()
    question6()

    def question7():
        global number_correct
        print("\nAnd for the final question, the most important one of all!")
        print("What is the most amazing drink in the world?")
        q_input = input(":")
        if q_input.lower() == "dr.pepper" or q_input == "dr pepper":
            number_correct += 1
        else:
            print("Have you learned nothing from this quiz??")
            print("\033[1;31m" + 'Dr.Pepper' + "\033[0m", "is obviously the best drink, "
                  "and I disagree with any other opinion. :)")

    question7()

    percentage = (number_correct/7)*100
    percentage = round(percentage, 2)
    if percentage >= 93:
        lg = "A"
    elif 90 <= percentage <= 92:
        lg = "A-"
    elif 87 <= percentage <= 89:
        lg = "B+"
    elif 83 <= percentage <= 86:
        lg = "B"
    elif 80 <= percentage <= 82:
        lg = "B-"
    elif 77 <= percentage <= 79:
        lg = "C+"
    elif 73 <= percentage <= 76:
        lg = "C"
    elif 70 <= percentage <= 72:
        lg = "C-"
    elif 67 <= percentage <= 69:
        lg = "D+"
    elif 63 <= percentage <= 66:
        lg = "D"
    elif 60 <= percentage <= 62:
        lg = "D-"
    else:
        lg = "F"

    print("Your final grade for this quiz is:", percentage, "that's a(n):", lg)
    print("Thanks for playing my quiz!\nHopefully you learned something interesting about"
          " \033[1;31m" + 'Dr.Pepper!' + "\033[0m")


question_set()

