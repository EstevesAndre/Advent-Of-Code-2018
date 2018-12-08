file=open("input.in", "r")

content = [list(map(int, i.split(', '))) for i in file.readlines()]

file.close()

matrix = {}
regions = {}
for x in range(len(content)):
    regions[x] = 0

maxX = max([point[0] for point in content])
maxY = max([point[1] for point in content])

for y in range(maxY):
    for x in range(maxX):
        best = maxX + maxY
        bestnum = -1
        for iPoint in range(len(content)):
            p = content[iPoint]
            dist = abs(x - p[0]) + abs(y - p[1])
            if dist < best:
                best = dist
                bestnum = iPoint
            elif dist == best:
                bestnum = -1
        matrix[y,x] = bestnum
        if bestnum != -1:
            regions[bestnum] = regions[bestnum] + 1

# remove infinite left right
for x in range(maxX):
    infinite = matrix[0,x]
    regions.pop(infinite, None)
    infinite = matrix[maxY - 1,x]
    regions.pop(infinite, None)

    
# remove infinite up down
for y in range(maxY):
    infinite = matrix[y,0]
    regions.pop(infinite, None)
    infinite = matrix[y, maxX-1]
    regions.pop(infinite, None)

inArea = 0

for y in range(maxY):
    for x in range(maxX):
        size = 0
        for iPoint in range(len(content)):
            p = content[iPoint]
            dist = abs(x - p[0]) + abs(y - p[1])
            size += dist
        if size < 10000:
            inArea += 1

print(inArea)