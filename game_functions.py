from art import vs
import random


def display_info(_a, _b):
    print(f'Compare A: {_a["name"]}, a {_a["description"]}, from {_a["country"]}'
          f'{vs}\n'
          f'Aganist B: {_b["name"]}, a {_b["description"]}, from {_b["country"]}')


def ask():
    return input("Who has more followers? Type 'A' or 'B': ").lower()


def determine_real_answer(_a, _b):
    if _a["follower_count"] > _b["follower_count"]:
        return "a"
    else:
        return "b"


def get_random_b(_a):
    random_b = random.randint(0, 50)
    while _a == random_b:
        random_b = random.randint(0, 50)
    return random_b

