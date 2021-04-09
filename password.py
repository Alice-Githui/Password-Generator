import random 
#password generator

#define the characters that will be used to generate random passwords
tokens = 'abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#%&*'

while True:
    password_length = int(input("What length do you want your password to be?: "))
    password_count = int(input("How many passwords do you want to generate?: "))

    for i in range(0, password_count):
        # print(i)
        password = ""
        for x in range(0, password_length):
            password_generated = random.choice(tokens)
            password           = password + password_generated
        print("Random password generated is:", password)

