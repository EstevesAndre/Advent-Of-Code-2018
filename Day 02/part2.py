file=open("input.in","r")

content=file.readlines()
content=[i.strip() for i in content]

sizeLine = len(content[0])

key = []
bestValue = sizeLine

for i in range(0, len(content)):
    for j in range(i + 1, len(content)):
        similarity = [ord(a) ^ ord(b) for a,b in zip(content[i],content[j])]
        similarity = list(map(int,similarity))
        equalValue = sizeLine - similarity.count(0)
        if bestValue > equalValue:
            key = []
            bestValue = equalValue
            key.append(content[i])
            key.append(content[j])
            key.append(similarity)

mostCommon = key[0]

for i in range(0,len(key[0])):
    if(key[2][i] != 0):
        mostCommon = mostCommon.replace(key[0][i],'')

print(mostCommon)
