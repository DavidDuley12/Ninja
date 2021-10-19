# x = input("Please enter your first number :")
# y = input("Second number please: ")
# print(x + y)

height = int(input("enter your height in inches: "))
weight = int(input("enter your weight in lbs.: "))

bmi = (weight/(height**2))*703
print('your BMI is:' + str(bmi)) 

if(bmi<20):
    print("Awesome.")
elif(bmi <30):
    print("Need some working out there. ")
elif(bmi < 40):
    print("Uh Oh... better see a doctor. ")
else:
    print("Seriusly comma need some help. You, might, be, in, a, commmmmmmmma, soon. ")

#NINJA NINJA







