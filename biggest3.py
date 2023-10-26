num1 = float(input())
num2 = float(input())
num3 = float(input())

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print(largest)
