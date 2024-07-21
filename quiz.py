"""
Program: quiz.py
Author: Ava Flanigan
Last date modified: 3/8/24
The program is a 10 question quiz on beverage facts.
1. Welcome the user to the quiz.
2. Present the user with the question, allow them to respond, and tell them what value to respond with.
3. If the user gets the question wrong, allow them another attempt.
    a. If they get the question right on the second attempt, grant them half a point, and move onto the next question.
    b. If they get the question wrong again, grant them no points, tell them the correct answer, and move them onto the next question.
4. If the user gets the question wrong, grant them a point, give them another fact regarding the question's topic, and continue to the next question.
5. Repeat process for nine additional questions.
6. Once all questions are answered, find the percentage grade the user got on quiz.
7. Use the percentage grade to find the user's letter grade.
8. Output to the user their number and letter grade, and give them a message based on their performance on the quiz.
"""
points = 0
questions = 0
print("Welcome to the quiz!")

print("Question 1: Fill in the blank using an integer: There are more than ___ flavors of Fanta worldwide.")
question_1 = int(input("Answer: "))
questions += 1
if question_1 != 200:
    print("Wrong! You have one more try.")

    for question_1 in range(1):
        q1 = int(input("New answer: "))
        if q1 == 200:
            print("Correct! Onto the next question")
            points += 1/2
            break
        else:
            print("Wrong! The answer is 200.")
            continue
else:
    points += 1
    print("Correct! Fanta Orange is Fanta's most popular flavor out of the 200.")


print("Question 2: True or False- Coca-Cola is older than Spelman College.")
question_2 = bool(int(input("True or False, type '0' for False and '1' for True: ")))
questions += 1
if question_2 == 0:
    print("Correct! Spelman was founded in 1881, and the Coca-Cola brand was created in 1886.")
    points += 1
else:
    print("Wrong! You have one more try.")
    for q2 in range(1):
        q2 = bool(int(input("True or False: ")))
        if q2 == 0:
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is False.")
            continue

print("Question 3: Multiple choice- What are traditional Boba pearls made out of? \n A. Mochi \n B. Tapioca \n C. Coffee \n D. Gelatine")
question_3 = input("Type your letter answer: ")
quest3 = question_3.upper()
questions += 1
if quest3 != "B":
    print("Wrong! You have one more try.")
    for q3 in range(1):
        q3 = (input("Type your letter answer again: "))
        qu3 = q3.upper()
        if qu3 == "B":
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is B. Tapioca.")
            continue
else:
    points += 1
    print("Correct! Boba pearls are made out of Tapioca and are very high in sugar!")

print("Question 4: Type the answer: What is the chemical formula for water? \n A. CO  \n B. OH \n C. CO2 \n D. H2O")
question_4 = input("Type your letter answer: ")
quest4 = question_4.upper()
questions += 1
if quest4 != ("D"):
    print("Wrong! You have one more try.")
    for q4 in range(1):
        q4 = input("Type your new letter answer: ")
        qu4 = q4.upper()
        if qu4 == ("D"):
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is D. H2O.")
            continue
else:
    points += 1
    print("Correct! Water has two hydrogen atoms and one oxygen atom.")

print("Question 4: How many Pepsi logos have there been over the years?")
questions += 1
question_5 = int(input("Answer using an integer: "))
if question_5 != 20:
    print("Wrong! You have one more try.")
    for q5 in range(1):
        q5 = int(input("Type your new answer: "))
        if q5 == (20):
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is 20.")
            continue
else:
    points += 1
    print("Correct! PepsiCo has had 20 logos, and their first logo was of their original name \"Brad's Drink\"")

print("Question 6: What percent of Americans drink one glass of soda a day?")
question_6 = int(input("Type your answer as an integer: "))
questions += 1
if question_6 != 48:
    print("Wrong! You have one more try.")
    for q6 in range(1):
        q6 = int(input("Type your new answer: "))
        if q6 == (48):
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is 48%.")
            continue
else:
    points += 1
    print("Correct! 48% of Americans drink soda everyday, and the most popular soda is Coca-Cola.")

print("Question 7: True or False- Kombucha is fermented ginger ale.")
question_7 = bool(int(input("True or False, type '0' for False and '1' for True: ")))
questions += 1
if question_7 == 0:
    print("Correct! Kombucha is not fermented ginger ale. It's made out of fermented tea.")
    points += 1
else:
    print("Wrong! You have one more try.")
    for q7 in range(1):
        q7 = bool(int(input("True or False: ")))
        if q7 == 0:
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is False.")
            continue

print("Question 8: What is the most popular type of tea world wide? \n A. Black Tea \n B. Green Tea \n C. Honey Lemon Tea \n D. Jasmine Tea")
question_8 = input("Type your letter answer: ")
quest8 = question_8.upper()
questions += 1
if quest8 != "A":
    print("Wrong! You have one more try.")
    for q8 in range(1):
        q8 = input("Type your new letter answer: ")
        qu8 = q8.upper()
        if qu8 == ("A"):
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is A. Black Tea.")
            continue
else:
    points += 1
    print("Correct! Black tea is the most popular tea in the world and is used to make southern sweet tea.")

print("Question 9: True or False- Sprite is owned by PepsiCo.")
question_9 = bool(int(input("True or False, type '0' for False and '1' for True: ")))
questions += 1
if question_9 == 0:
    print("Correct! Sprite is not owned by PepsiCo. They are owned by Coca-Cola.")
    points += 1
else:
    print("Wrong! You have one more try.")
    for q9 in range(1):
        q9 = bool(int(input("True or False: ")))
        if q9 == 0:
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is False.")
            continue
print("Question 10: What year did boba tea originate?")
question_10 = int(input("Type in an integer value: "))
questions += 1
if question_10 != 1988:
    print("Wrong! You have one more try.")
    for q10 in range(1):
        q10 = int(input("Type your new answer: "))
        if q10 == (1988):
            print("Correct! Onto the next question.")
            points += 1/2
            break
        else:
            print("Wrong! The answer is 1988.")
            continue
else:
    points += 1
    print("Correct! Boba Tea origniated in 1988 in Taiwan!")


total = points/questions *100

if total >= 90:
    print("Impressive! You got a", total, "%, and your letter grade was A! You're a beverage fanatic!")
elif total >= 80:
    print("Wow! You got a", total, "%, and your letter grade was B! You really know your beverage facts!")
elif total >= 70:
    print("Nice! You got a", total, "%, and your letter grade was C! You may know some beverage facts!")
elif total >= 60:
    print("You got a", total, "%, and your letter grade was D! You know a little something about bevergaes!")
else:
    print("You got a", total, "%, and your letter grade was F! You may need to brush up on your beverage facts!")
