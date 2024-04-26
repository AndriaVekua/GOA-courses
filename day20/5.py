# ცარიელი სია
new_list = []

# ორი რიცხვის შემოტანა
a = int(input("შეიყვანეთ a: "))
b = int(input("შეიყვანეთ b: "))

# for loop-ით შევქმნათ სია რიცხვებით a-დან b-მდე
for number in range(a, b):
    new_list.append(number)

# შედეგის დაბეჭდვა
print("ახალი სია:", new_list)
