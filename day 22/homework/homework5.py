number = int(input("შეიტანეთ რიცხვი: "))
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
