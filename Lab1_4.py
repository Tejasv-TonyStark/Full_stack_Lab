class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return None

c = Calculator()

while True:
    print("\n1.Add  2.Sub  3.Mul  4.Div  5.Exit")
    ch = input("Choose option: ")

    if ch == "5":
        print("Bye")
        break

    a = input("Enter first number: ")
    b = input("Enter second number: ")

    try:
        a = float(a)
        b = float(b)
    except:
        print("Invalid numbers")
        continue

    if ch == "1":
        print("Result =", c.add(a, b))
    elif ch == "2":
        print("Result =", c.sub(a, b))
    elif ch == "3":
        print("Result =", c.mul(a, b))
    elif ch == "4":
        ans = c.div(a, b)
        if ans is not None:
            print("Result =", ans)
    else:
        print("Wrong choice")
        