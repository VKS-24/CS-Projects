
def add(num1, num2):
    result = num1 + num2
    print(result)
    

def sub(num1, num2):
    result = num1-num2
    print(result)
    

def mult(num1, num2):
    result = num1*num2
    print(result)
    

def div(num1, num2):
    ## do not divide by zero
    if num2 == 0:
        print("Syntax Error")
    else:   
        result = num1/num2 
        print(result)

def calculate(num1, num2, operator):
    
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return sub(num1, num2)
    elif operator == "*":
        return mult(num1, num2)
    elif operator == "/":
        return div(num1, num2)
    else:
        print("Pls give a valid operator")
        return "error"

if __name__ == "__main__":
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    operator = input("Enter the operator(+,-,*,/): ")

    calculate(add, sub, mult, div, num1, num2, operator)

    