height = float(input("Enter Your height in centimeters: "))  # Input height in cm
weight = int(input("Enter Your weight in kilograms: "))
height = height / 100  
bmi = weight / (height ** 2)
print(height)
print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
