weight = 72.0
height = 1.75
bmi = weight/(height * height)
if (bmi < 18):
    status = "Underweight"
elif bmi < 25:
    status = "Ideal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("You are %s and your bmi is %.1f"%(status,bmi))
