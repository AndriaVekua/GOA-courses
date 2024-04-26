# რიცხვის შემოტანა
number = int(input("შეიყვანეთ რიცხვი: "))

# მარტივობის შემოწმება
is_prime = True

# თუ რიცხვი ნაშთია 1-ზე, მაშინ არაა მარტივი
if number <= 1:
    is_prime = False
else:
    # შევამოწმოთ, რამდენი გამყოფი აქვს რიცხვს
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

# შედეგის დაბეჭდვა
if is_prime:
    print("თქვენი რიცხვი მარტივია")
else:
    print("თქვენი რიცხვი არ არის მარტივი")
