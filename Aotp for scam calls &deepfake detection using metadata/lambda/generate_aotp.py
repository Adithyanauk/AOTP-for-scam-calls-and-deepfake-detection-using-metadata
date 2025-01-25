import random
import string

def generate_aotp(length=6):
    characters = string.ascii_letters
    aotp = ''.join(random.choice(characters) for _ in range(length))
    return aotp

if __name__ == "__main__":
    print(f"Generated AOTP: {generate_aotp()}")
