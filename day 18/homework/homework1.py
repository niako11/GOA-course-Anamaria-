
my_name = "Anamaria"

user_name = input("please enter your name: ")
user_age = int(input("please enter your age: "))

if user_age >= 18:
    print("You are of age:", True)
else:
    print("you aren't of age:", False)

if user_name == my_name:
    print("Your name matches mine:", True)
else:
    print("Your name doesn't match mine.:", False)
