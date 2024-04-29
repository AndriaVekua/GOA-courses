def check_voting_age(age):
    if age >= 18:
        print("თქვენ გაქვთ ხმის მიცემის უფლება")
    else:
        print("თქვენ არ გაქვთ ხმის მიცემის უფლება")

# შეყვანა
age = int(input("შემოიტანეთ ასაკი: "))

# ფუნქციის გამოძახება
check_voting_age(age)
