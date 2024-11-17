number=int(input("Enter Number to be checked"))
print("Number to be checked : ",number)
if number%2==0:
   print("This number is even")

else:
   print( "This number is odd")



height=float(input("Enter height in cm:" ))
weight=float(input("Enter weight in kg:" ))
BMI=weight/ (height/100)**2
print("Your BMI is", BMI)

if BMI <=18.4:
   print("You are under weight.")
elif BMI <=24.9:
   print("You are healty.")
elif BMI <=29.9:
   print("You are overweight.")
elif BMI <=34.9:
   print("You are severly overweight.")
elif BMI <=39.9:
   print("You are obese.")
else:
   print("You are severly obese.")



import datetime

#using now() to get current time
current_time=datetime.datetime.now()
print("current time is", current_time)

import calendar

print(calendar.calendar(2024))