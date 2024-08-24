class Calculator:
    def __init__(self):
        self.ans = 0

    def add(self, num1, num2):
        self.ans = num1 + num2
        return self.ans

    def subtract(self, num1, num2):
        self.ans = num1 - num2
        return self.ans

    def multiply(self, num1, num2):
        self.ans = num1 * num2
        return self.ans

    def divide(self, num1, num2):
        if num2 == 0:
            print("Not divisible by zero")
        self.ans = num1 / num2
        return self.ans

    def clear(self):  # Empty the value of self.ans
        self.ans = 0
        return self.ans

calc = Calculator()
while True:
    print("Welcome to CodSoft Calculator!")
    print("Which operation you want to perform?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Go Back")
    choice = input("Choose an operation (1-5): ")
        
    if choice == '5':
        print("Calculator stopped running")
        break
        
    if choice in ['1', '2', '3', '4']:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
    if choice == '1':
        print("Result of ADDITION is ", calc.add(number1, number2))
        break
    elif choice == '2':
        print("Result of SUBTRACTION is ", calc.subtract(number1, number2))
        break
    elif choice == '3':
        print("Result of MULTIPLICATION is ", calc.multiply(number1, number2))
        break
    elif choice == '4':
        if(number2 != 0):
            print("Result of DIVISION is ", calc.divide(number1, number2))
            break
        else: 
            print("Not Defined!! Try another number")
            break
    else:
        print("Invalid choice, please choose again.")
        break