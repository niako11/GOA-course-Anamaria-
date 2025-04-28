even_sum = 0
even_count = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
        even_count += 1
average = even_sum / even_count
print("ლუწი რიცხვების საშუალო არითმეტიკული:", average)
