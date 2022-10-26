while True:
 w=input("Mode?\nContinuous - 1\nCompounding - 2\n");s=float(input("Enter the starting amount: "));l=float(input("Enter the amount of time passed: "));p=float(input("Enter the percentage amount as a decimal: "))
 if w=="1":print(s*2.71828182846**(l*p))
 if w=="2":t=float(input("Enter the amount of times per year that the intrest happens: "));print(s*(1+p/t)**(l*t))