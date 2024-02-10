import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiation(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def modulus(x, y):
    return x % y

def permutations(n, r):
    return math.perm(n, r)

def combinations(n, r):
    return math.comb(n, r)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base):
    return math.log(x, base)

def main():
    print("Welcome to Complex Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Modulus")
    print("9. Permutations")
    print("10. Combinations")
    print("11. Sin")
    print("12. Cos")
    print("13. Tan")
    print("14. Logarithm")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

        if choice in ('1', '2', '3', '4', '5', '8', '9', '10'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", exponentiation(num1, num2))
            elif choice == '8':
                print("Result:", modulus(num1, num2))
            elif choice == '9':
                print("Result:", permutations(num1, num2))
            elif choice == '10':
                print("Result:", combinations(num1, num2))

        elif choice in ('6', '7', '11', '12', '13', '14'):
            num = float(input("Enter number: "))

            if choice == '6':
                print("Result:", square_root(num))
            elif choice == '7':
                print("Result:", factorial(num))
            elif choice == '11':
                print("Result:", sin(num))
            elif choice == '12':
                print("Result:", cos(num))
            elif choice == '13':
                print("Result:", tan(num))
            elif choice == '14':
                base = float(input("Enter base: "))
                print("Result:", log(num, base))
        
        else:
            print("Invalid input")

        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
