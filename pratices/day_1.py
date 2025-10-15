# basic calculator 
def add_numbers(a,b):
    return a + b
for i in range (0,2):
    num1 = float(input("Enter first number :"))
    num2 = float(input("Enter second number :"))
    result = add_numbers(num1,num2)
    print(f"{num1} + {num2} = {result:0.2f}")