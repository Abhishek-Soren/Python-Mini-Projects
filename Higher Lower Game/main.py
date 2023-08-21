
from game_data import data
import random
from art import logo, vs
# from replit import clear


def compare(celeb_A, celeb_B):
    '''To Compare the follower count of the two celebrities'''
    if celeb_A['follower_count'] > celeb_B['follower_count']:
        return "a"
    else:
        return "b"


def game():
    ans = True
    score = 0

    B = random.choice(data)
    print(logo)

    while (ans):
        temp = data
        A = B
        temp.remove(A)
        B = random.choice(temp)

        print(
            f"Compare A:{A['name']},a {A['description']},from {A['country']}.")
        print(A['follower_count'])
        print(vs)
        print(
            f"Compare B:{B['name']},a {B['description']},from {B['country']}.")
        print(B['follower_count'])
        your_answer = input("Who has more followers? 'A' or 'B' : ").lower()

        actual_answer = compare(A, B)
        # clear()
        if your_answer == actual_answer:
            score += 1
            print(logo)

            print(f"You're right. Current Score : {score}")

        else:
            ans = False
            print(logo)
            print(f"Sorry! That's wrong. Final Score : {score}")


game()
