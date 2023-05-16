age = float(input("Enter age: "))

# думаю уместен контроль граничных значений
if 0 > age < 0.1:
    print("You haven't been born yet")
elif age < 2:
    print("Baby")
elif 2 <= age < 4:
    print("Kid")
elif 4 <= age < 13:
    print("Child")
elif 13 <= age < 20:
    print("Teenager")
elif 20 <= age < 65:
    print("Grown-up")
else:
    print("Senior")
