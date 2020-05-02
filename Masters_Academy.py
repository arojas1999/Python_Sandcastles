"""
File: khansole_academy.py
-------------------------
A gift from Dad to you. Remember that you can learn and strive no matter your age. I love you.
"""

import random

SUCCESS = 2
MIN_RANDOM = 1
MAX_RANDOM = 9

def main():
    """
    random additions
    """
    print("This program will help you become The King of Addition. With all my love for Simon and Sylvia.")
    start()

def start():
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    print("What is " + (str(num1)) + " + " + (str(num2)) + "?")
    right_answer = num1 + num2
    user_answer = int(input("Your answer: "))
    while (right_answer != user_answer):
        print("Incorrect. The expected answer is: " + str(right_answer))
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        print("What is " + (str(num1)) + " + " + (str(num2)) + "?")
        right_answer = num1 + num2
        user_answer = int(input("Your answer: "))
    else:
        if (right_answer == user_answer):
            print("Correct! You have gotten " + (str(1)) + " correct in a row")
            num3 = random.randint(MIN_RANDOM, MAX_RANDOM)
            num4 = random.randint(MIN_RANDOM, MAX_RANDOM)
            print("What is " + (str(num3)) + " + " + (str(num4)) + "?")
            right_answer_1 = num3 + num4
            user_answer_1 = int(input("Your answer: "))
            i = 1
            while i < SUCCESS and right_answer_1 == user_answer_1:
                i = i + 1
                print("Correct! You have gotten " + (str(i)) + " correct in a row")
                num3 = random.randint(MIN_RANDOM, MAX_RANDOM)
                num4 = random.randint(MIN_RANDOM, MAX_RANDOM)
                print("What is " + (str(num3)) + " + " + (str(num4)) + "?")
                right_answer_1 = num3 + num4
                user_answer_1 = int(input("Your answer: "))
            else:
                if right_answer_1 != user_answer_1:
                    print("Incorrect. The expected answer is: " + str(right_answer_1))
                    start()
                else:
                    print("Correct! You have gotten " + (str(i + 1)) + " correct in a row")
                    print("Congratulations!! You are The King of Addition.")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
