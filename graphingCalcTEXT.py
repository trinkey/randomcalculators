equation = lambda x: x ** 2 - 5

widthandheight = 16

graph = []
for i in range(widthandheight + 1):
    graph.append(["--"] * (widthandheight + 1))

for i in range(widthandheight * 10):
    point = round(equation((i / 10) - widthandheight / 2))
    if point <= widthandheight / 2 and point >= -widthandheight / 2:
        graph[round(widthandheight / 2) - point][round(i / 10)] = "@@"

del(equation)

output = ""
for i in graph:
    for o in i:
        output += o
    output += "\n"

del(graph)
print(output)
del(output)
