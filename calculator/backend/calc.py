
def add(num1, num2):
    result = num1 + num2
    print(result)
    return result
    

def sub(num1, num2):
    result = num1-num2
    print(result)
    return result
    

def mult(num1, num2):
    result = num1*num2
    print(result)
    return result
    

def div(num1, num2):
    ## do not divide by zero
    if num2 == 0:
        print("Syntax Error")
        return float('inf')
    else:   
        result = num1/num2 
        print(result)
        return result   

def calculate(num1, num2, operator):
    print(num1,num2, operator)
    print(type(num1), type(num2), type(operator))
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

#if __name__ == "__main__":
  # num1=float(input("Enter first number: "))
   # num2=float(input("Enter second number: "))
   # operator = input("Enter the operator(+,-,*,/): ")

   # calculate(add, sub, mult, div, num1, num2, operator)

    