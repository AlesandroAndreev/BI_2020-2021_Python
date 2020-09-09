for i in range(1000):
    print("Hello! This is calculator. To exit write exit")
#Operator input
    b = input("Write operator: ")
#Check exit condition
    if b == "exit":
        print("Bye!")
        break
#Entering numbers
    a = float(input("Write first number: "))
    c = float(input("Write second number: "))

#Basic operations of the calculator.
    # Before division, it is checked that
    # the denominator is not zero.

    if b == "+" :
        print(a + c)
    elif b == "-":
        print(a - c)
    elif b == "*":
        print(a * c)
    elif b == "/":
        if c == 0:
            print("Zero!")
            continue
        print(a / c)
    elif b == "**":
        print(a ** c)
    elif b == "%":
        if c == 0:
            print("Zero!")
            continue
        print(a % c)
    elif b == "//":
        if c == 0:
            print("Zero!")
            continue
        print(a // c)
    else:
        print("Error, wrong operator")
        continue


