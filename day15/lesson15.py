def finance_study(score):
    if score > 90 and score <= 100:
        print("თქვენ დაგიფინანსდებათ სწავლა სრულიად.")
    elif score > 70 and score <= 80:
        print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით.")
    elif score > 40 and score <= 70:
        print("თქვენ დაგიფინანსდებათ სწავლა 500 ლარით.")
    else:
        print("თქვენ არ დაგიფინანსდებათ სწავლის პროცესი.")
score = float(input("შემოიტანეთ თქვენი ტესტის ქულა: "))
finance_study(score)
