print("Welcome to Power Calculator")
num = int(input("Enter a number: "))
n = int(input("How many powers you want? "))
for i in range(1, n + 1):
    power = num ** i
    print(num, "power", i, "=", power)
