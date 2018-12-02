file=open("input.in","r")

content = file.readlines()
file.close()
content = [i.strip() for i in content]

sum2 = 0
sum3 = 0

for line in content:
    inc2 = 1
    inc3 = 1
    while line != '':
        count = line.count(line[0])
        if count == 2:
            sum2 += inc2
            inc2 = 0
        elif count == 3:
            sum3 += inc3
            inc3 = 0
        line = line.replace(line[0],'')

print(sum2 * sum3)    