# basic calculator 
def add_numbers(a,b):
    return a + b
for i in range(0,2):
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter numeric values")
    result = add_numbers(num1,num2)
    print(f"{num1} + {num2} = {result:0.2f}")
