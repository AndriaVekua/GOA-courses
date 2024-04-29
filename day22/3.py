def calculate_rectangle_perimeter(side1, side2, side3, side4):
    perimeter = side1 + side2 + side3 + side4
    return perimeter

# მართკუთხედის ოთხ გვერდის შეტანა
side1 = float(input("შემოიტანეთ პირველი გვერდი: "))
side2 = float(input("შემოიტანეთ მეორე გვერდი: "))
side3 = float(input("შემოიტანეთ მესამე გვერდი: "))
side4 = float(input("შემოიტანეთ მეოთხე გვერდი: "))

# პერიმეტრის გამოთვლა და შედეგის დაბეჭდვა
perimeter = calculate_rectangle_perimeter(side1, side2, side3, side4)
print("მართკუთხედის პერიმეტრი:", perimeter)
