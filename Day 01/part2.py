file=open("input.in","r")

content=file.readlines()

content = [i.strip() for i in content]
content = list(map(int,content))
file.close()

#content = [-6, +3, +8, +5, -6]
sum = 0
freq = set()
i = 0

# run across content as much times as needed till find a duplicate on the current sum
while True:
    sum += content[i]
    if(sum in freq):
        break
    freq.add(sum)
    i += 1
    if(i == len(content)):
        i = 0

print(sum)