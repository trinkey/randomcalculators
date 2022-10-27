equation = lambda x: math.sin(x / 10) * 50 # MAKE SURE EQUATION STARTS WITH "lambda x: " and treat it as if it was "y = "
width = 100
height = 100
linechar = "@" # Char for when there is a line
nolinechar = " " # Char for when there isnt a line
startline = "​" # Zero width space to start/end line
endline = "​" # Helps with alignment problems if nolinechar is whitespace

printStatus = True

if printStatus: from time import sleep as s; from time import time as t; starttime = t()
graph = []
import math
for i in range(height + 1):
    graph.append([nolinechar * 2] * (width + 1))
if printStatus:
    x = width * 10
    for i in range(width * 10):
        point = math.floor(equation((i / 10) - width / 2))
        if point <= height / 2 and point >= -height / 2:
            graph[math.floor(height / 2) - point][math.floor(i / 10)] = linechar * 2
        x -= 1
        if not x % 100:
            print(str(x) + " maths left")
            s(0.01)
    del(x)
else:
    for i in range(width * 10):
        point = math.floor(equation((i / 10) - width / 2))
        if point <= height / 2 and point >= -height / 2:
            graph[math.floor(height / 2) - point][math.floor(i / 10)] = linechar * 2

del(width, height, equation, point)

if printStatus: print("finished writing, time to start prepping to print"); print("Time elapsed: " + str(t() - starttime)); s(0.01)
output = startline
if printStatus:
    x = len(graph)
    for i in graph:
        for o in i:
            output += o
        output += endline + "\n" + startline
        x -= 1
        if not x % 25:
            print(str(x) + " lines left to parse")
            print("Time elapsed: " + str(t() - starttime))
            s(0.01)
else:
    for i in graph:
        for o in i:
            output += o
        output += endline + "\n" + startline
if printStatus: print("printing"); print("Time elapsed: " + str(t() - starttime)); s(0.01)
del(graph)
print(output)
del(output)
print("complete")
print("Time elapsed: " + str(t() - starttime))
