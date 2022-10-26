from math import log
while True:
    mode = input("Mode 1-2")
    if mode == "1":
        print("(a * log(num)) / (b * log(root))")
        try: print((int(input("a value: ")) * log(float(input("Enter the number: ")))) / (int(input("b value: ")) * log(int(input("Enter the root: ")))))
        except ValueError: print("Bad input, try again.")
        except ZeroDivisionError: print("Root can't be one")
    elif mode == "2":
        print("log\\n/ ^m sqrt(a)")
        print(log(int(input("a")) ** int(input("m"))) / log(int(input("n"))))