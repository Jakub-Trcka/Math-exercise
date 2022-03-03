import random

def squered(x):
    return (x * x)

def cubed(x):
    return (x * x * x)

num_list3 = [2, 2, 2, 3, 3]
num_list4 = [1, 2, 2]

print("lets start")

while True:
    try:
        number_of_wrong_answers = 0
        for _ in range(5):


            random_choice1 = random.choice(num_list4)

            random_choice2 = random.choice(num_list3)

            if float(random_choice1) == 1:
                if float(random_choice2) == 2:

                    num1 = random.randint(2, 20)
                    print("What is square root of " + str(squered(float(num1))) + "?")
                    choice2 = input(":")

                    if float(choice2) == float(num1):                  
                        print("correct")

                    else:
                        print("incorrect")
                        print("it's " + str(num1))
                        number_of_wrong_answers += 1

                elif float(random_choice2) == 3:
                    num1 = random.randint(2, 5)
                    print("What is cube root of " + str(cubed(float(num1))) + "?")
                    choice2 = input(":")

                    if float(choice2) == float(num1):
                        print("correct")

                    else:
                        print("incorrect")
                        print("it's " + str(num1))
                        number_of_wrong_answers += 1

            elif float(random_choice1) == 2:

                if float(random_choice2) == 2:
                    num1 = random.randint(2, 20)
                    print("What is " + str(num1) + " squered?")
                    choice2 = input(":")

                    if float(choice2) == squered(float(num1)):
                        print("correct")

                    else:
                        print("incorrect")
                        print("it's " + str(squered(num1)))
                        number_of_wrong_answers += 1

                elif float(random_choice2) == 3:
                    num1 = random.randint(2, 5)
                    print("What is " + str(num1) + " cubed?")
                    choice2 = input(":")

                    if float(choice2) == cubed(float(num1)):
                        print("correct")

                    else:
                        print("incorrect")
                        print("it's " + str(cubed(num1)))
                        number_of_wrong_answers += 1

        print("You got " + str(number_of_wrong_answers) + " wrong")
    except ValueError:
        print("Invalid input")