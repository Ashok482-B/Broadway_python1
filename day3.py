#if else case
num=11
if (num!=10):
    print("the number is equal!")
else:
    print("the number is not equal!")

    #if and elif case
marks=30
if(marks>50):
    print("second division")

elif(marks>60 and marks<80):
    print("first position")

else:
    print("fail")

#nested if
marks=90
if(marks>80):
    print("congo")
    if(marks==80):
     print("lucky")
elif(marks==100):
    print("topper")
else:
    print("fail") 


#e.g of nested if 
purchase=1000
is_member="True"
is_coupon="True"

if(purchase>=1000):
    if(is_member):
        print("member!")
    if(is_coupon):
        print(" you get 20% off")
    else:
         print("you get 10% off")


#next question for nested loop
#to check positive number if it is positive than find it is odd or even!
num=-1
if(num>0):
    print("positive number")
    
    if(num%2==0):
        print("even number")
    else:
        print("odd number")
else:
     print("negative number")

#new if case in one line
gender="M"
data="male" if gender=="M" else "female"
print(data)

Data="broadway"
print(data.upper())
print(data.lower())
print(data.title())

data="1234"
print(data.isdigit())
print(data.isalpha())
