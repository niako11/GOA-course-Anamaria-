
score = int(input("შეიყვანე შენი ქულა: "))

if score > 80:
    grade = "A"
elif score > 60:
    grade = "B"
elif score > 40:
    grade = "C"
elif score > 20:
    grade = "D"
else:
    grade = "F"

print("შენი შეფასებაა:", grade)
