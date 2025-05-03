import random
import string

def password():
    counter = 0
    pw = " "
    while counter <= 10:
        letters = list("@*#&abc") + list(string.ascii_letters)
        numbers = random.randint(1, 100)
        number = str(numbers)
        letter = random.choice(letters)
        pw += number + letter
        counter += 1
    print(pw) 
password()