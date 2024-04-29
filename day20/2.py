# რიცხვის შეყვანა
number = int(input("შეიყვანეთ რიცხვი: "))

# რიცხვების ჯამი და საშუალო არითმეტიკული
total = 0
for i in range(1, number + 1):
    total += i

average = total / number

# შედეგის დაბეჭდვა
print("რიცხვების ჯამი:", total)
print("საშუალო არითმეტიკული:", average)
