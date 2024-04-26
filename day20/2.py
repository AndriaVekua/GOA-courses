
# მომხმარებელს შევყვანით რიცხვი
number = int(input("შეიყვანეთ რიცხვი: "))

# საშუალო რიცხვის გათვლა
sum_of_numbers = 0

# for loop-ით დავბეჭდოთ რიცხვები 1-დან number-მდე და დავამატოთ მათი ჯამი
for i in range(1, number + 1):
    print(i)
    sum_of_numbers += i

# რიცხვების ჯამის და საშუალო არითმეტიკულის გამოტანა
print("რიცხვების ჯამი:", sum_of_numbers)
print("საშუალო არითმეტიკული:", sum_of_numbers / number)
