file=open("input.in","r")

content=file.readlines()
content = [i.strip() for i in content]
content = list(map(int,content))
file.close()

#content = [-6, +3, +8, +5, -6]
sum = 0
freq = set()

# run across content as much times as needed till find a duplicate on the current sum
while True:
    for i in content:
        sum += i
        if sum in freq:
            print(sum)
            quit()
        freq.add(sum)