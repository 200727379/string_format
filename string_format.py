#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#28 April 2021

"""To concatenate, or combine, two strings you can use the + operator. But to concatenate or
    to combine a string and a number we can use one of the following formats:

"""
name = "Lesley " #string 1
surname = "Mothapo" # string 2
age = 33 # integer/number

#First format
message = f"Hi my name is {name} {surname} and I am {age} years of age this year 2021" # use parameters
print(message)

#Second format
msg = "Hi my name is {} {} and I am {} years of age this year 2021" #pick values from the format function below
print(msg.format(name, surname, age))

#Third format
msg2 = "Hi my name is {0} {2} and I am {1} years of age this year 2021" #use index
print(msg2.format(name, age, surname))