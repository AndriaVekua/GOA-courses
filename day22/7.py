def check_age(age):
    if age < 13:
        print("ბავშვი ხარ")
    elif 13 <= age <= 19:
        print("შენ ხარ მოზარდი")
    else:
        print("სრულწლოვანი ხარ")

# ასაკის შეყვანა
age = int(input("შემოიტანეთ ასაკი: "))

# პირობითი განცხადების გაშვება
check_age(age)
