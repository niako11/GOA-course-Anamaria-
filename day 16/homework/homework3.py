#control flow - ნიშნავს იმ წესრიგს, რომლითაც პროგრამაში ირჩევა და სრულდება კოდის ბლოკები.

# მაგალითი N1
age = 18
if age >= 18:
    print("შენ ხარ სრულწლოვანი")
else:
    print("შენ ხარ არასრულწლოვანი")


# მაგალითი N2
number = -5
if number > 0:
    print("რიცხვი დადებითია")
elif number < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი ნულია")


# მაგალითი N3
score = 85
if score >= 90:
    print("შენ მიიღე A")
elif score >= 80:
    print("შენ მიიღო B")
elif score >= 70:
    print("შენ მიიღო C")
elif score >= 60:
    print("შენ მიიღო D")
else:
    print("შენ ჩაიჭერი")

