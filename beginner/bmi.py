print("BMI Calculator")
weight = int(input("What is your weight in kg: "))
height = float(input("What is your height in m: "))
hsquare = height ** 2

bmi = weight / hsquare
bmi = round(bmi, 2)
print(f"Your BMI score is {bmi} ")

if bmi <= 5:
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You have healthy weight")
elif bmi >=25 and bmi <=29.9:
    print("You are overweight")
elif bmi >=30 and bmi <= 34.9:
    print("You have Obese Type 1")
elif bmi >= 35 and bmi <= 39.9:
    print("You have Obese Type 2")
else:
    print("You have Obese Type 3")



