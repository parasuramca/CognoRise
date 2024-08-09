import string
import random

def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length for the password: "))
    password = gen_pass(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
