
h = float(input("enter your height in m: "))
w = float(input("enter your weight in kg: "))

'''- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.'''

bmi=(w/h**2)
bm=round(bmi,1)
if bmi<18.5:
  print(f"your BMI is {bm} You are underweight")
elif (bmi<25):
  print(f"Your BMI is {bm} You are in correct weight")
elif bmi<30:
  print(f"Your BMI is {bm} you are slightly overweight no probs you have great chances")
elif bmi>30 and bmi<35:
  print("your BMI is",bm,"you are OBESE")
else:
  print("Your BMI :",bm,"clinically OBESEE..")






