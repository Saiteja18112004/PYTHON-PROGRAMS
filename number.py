n = int(input("Enter a number: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    for i in range(n, 0, -1):
        print(i)
