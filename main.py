from game_data import data
from art import logo
from game_functions import *
import random


# Prereqs
print(logo)

random_a = random.randint(0,50)
random_b = get_random_b(random_a)

USER_SCORE = 0


# Main
game_continue = True
while game_continue:
    display_info(data[random_a], data[random_b])
    real_answer = determine_real_answer(data[random_a], data[random_b])
    user_answer = ask()
    if user_answer != real_answer:
        game_continue = False
        break
    else:
        USER_SCORE += 1
        print(f"You're right! Current score: {USER_SCORE}.")
        random_a = random_b
        random_b = get_random_b(random_a)


print(f"Sorry that's wrong. Final score: {USER_SCORE}")
