def check_number_sign(num):
    if num > 0:
        print("რიცხვი დადებითია")
    elif num < 0:
        print("რიცხვი უარყოფითია")
    else:
        print("რიცხვი ნულია")

# შემოყვანა
number = int(input("შემოიტანეთ რიცხვი: "))

# ფუნქციის გამოძახება
check_number_sign(number)
