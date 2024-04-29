def calculate_rectangle_area(length, width):
    # ფართობის გამოთვლა
    area = length * width
    return area

# მართკუთხედის სიგრძე და სიმაღლე
length = float(input("მართკუთხედის სიგრძე: "))
width = float(input("მართკუთხედის სიმაღლე: "))

# ფართობის გამოთვლა და შედეგის დაბეჭდვა
area = calculate_rectangle_area(length, width)
print("მართკუთხედის ფართობი:", area)
