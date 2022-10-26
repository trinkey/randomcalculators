subscript = [i for i in "₀₁₂₃₄₅₆₇₈₉"]

from turtle import Turtle, Screen
from math import log
scr = Screen()
scr.setup(600, 300)
scr.bgcolor("#333333")
scr.tracer(0)

turt = Turtle()
turt.color("white")
turt.hideturtle()
turt.pu()

while True:
    try:
        bval = "b"
        turt.clear()
        turt.write("y = A logₓb", align = "center", font = ["Arial", 24, "normal"])
        scr.update()
        Aval = input("Enter the A value: ")
        Avallit = Aval
        if Aval == "1": Aval = ""
        turt.clear()
        turt.write("y = " + Aval + " logₓb", align = "center", font = ["Arial", 24, "normal"])
        scr.update()
        xval = input("Enter the root: ")
        xvalsubscript = ""
        if xval == "10":
            xvalsubscript = ""
        else:
            for i in xval:
                if i == ".":
                    xvalsubscript += "."
                else:
                    xvalsubscript += subscript[int(i)]
        turt.clear()
        turt.write("y = " + Aval + " log" + xvalsubscript + "b", align = "center", font = ["Arial", 24, "normal"])
        scr.update()
        bval = input("Enter the b value: ")
        turt.clear()
        output = float(Avallit) * (log(float(bval)) / log(float(xval)))
        turt.write(str(output) + " = " + Aval + " log" + xvalsubscript + bval, align = "center", font = ["Arial", 24, "normal"])
        scr.update()
        print(output)
        input("Press enter to continue\n")
    except:
        turt.clear()
        turt.write("nan = " + Aval + " log" + xvalsubscript + bval, align = "center", font = ["Arial", 24, "normal"])
        scr.update()
        print("Bad input")
        input("Press enter to continue\n")