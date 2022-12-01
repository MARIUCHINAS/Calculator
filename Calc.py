from time import sleep

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

while True:
 def main():
     print("Select operation.")
     print("1. Add")
     print("2. Subtract")
     print("3. Multiply")
     print("4. Divide")
     print("5. Modulus")
     print("6. Power")

     choice = input("Enter choice(1/2/3/4/5/6): ")

     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))

     if choice == '1':
         print(num1, "+", num2, "=", add(num1, num2))
         sleep(1)

     elif choice == '2':
         print(num1, "-", num2, "=", subtract(num1, num2))
         sleep(1)

     elif choice == '3':
         print(num1, "*", num2, "=", multiply(num1, num2))
         sleep(1)

     elif choice == '4':
         print(num1, "/", num2, "=", divide(num1, num2))
         sleep(1)

     elif choice == '5':
         print(num1, "%", num2, "=", modulus(num1, num2))
         sleep(1)

     elif choice == '6':
         print(num1, "**", num2, "=", power(num1, num2))
         sleep(1)

     else:
         print("Invalid input")
         sleep(1)

 if __name__ == '__main__':
     main()