import re

file=open("input.in","r")

content=file.readlines()
content=[list(map(int,re.findall(r'-?\d+', line))) for line in content]

Matrix = [[0 for x in range(1000)] for y in range(1000)]

for line in content:
    for x in range(line[1], line[1]+line[3]):
        for y in range(line[2], line[2]+line[4]):
            if Matrix[x][y] == 0:
                Matrix[x][y] = line[0]
            elif Matrix[x][y] != -1:
                Matrix[x][y] = -1

sum = 0

for x in range(1000):
    for y in range(1000):
        if Matrix[x][y] == -1:
            sum += 1
            
print(sum)