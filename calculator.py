#Python Calculator
#nkle 50346820

ans = 0 
choice = 0
action = ""

print("Python Calculator\n")

#Calculate and print the equation
def calculate():
    global action
    match choice:
        case "1":
            ans = num1 + num2
            print(f"{num1} + {num2} = {ans}")
            action = input("Let's do the next calculation? ")

        case "2":
            ans = num1 - num2
            print(f"{num1} - {num2} = {ans}")
            action = input("Let's do the next calculation? ")

    
        case "3":
            ans = num1 * num2
            print(f"{num1} * {num2} = {ans}")
            action = input("Let's do the next calculation? ")
    
        case "4": 
            ans = num1 / num2
            print(f"{num1} / {num2} = {ans}")
            action = input("Let's do the next calculation? ")
    
        case "5":
            ans = num1 % num2
            print(f"{num1} % {num2} = {ans}")
            action = input("Let's do the next calculation? ")
    
        case "6":
            ans = num1 ** num2
            print(f"{num1} ** {num2} = {ans}")
            action = input("Let's do the next calculation? ")


#Repeats the process 
while action != "no":
    print("--------------------------------------")
    print("\nSelect operation\n")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Exponent\n")
    choice = input("\nEnter choice 1/2/3/4/5/6\n")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    calculate()

print("\nExiting the calculator. Goodbye!")


