file=open("input.in","r")

content = file.readlines()
file.close()

# \n erased
content = [i.strip() for i in content] 


countOf2 = 0
countOf3 = 0

for line in content:
    # initializing variables to increment per line if found
    inc2 = 1
    inc3 = 1
    while line != '' and not(inc2 == 0 and inc3 == 0):
        count = line.count(line[0])
        if count == 2:
            # line contains two line[0]
            countOf2 += inc2 
            inc2 = 0
        elif count == 3:
            # line contains three line[0]
            countOf3 += inc3
            inc3 = 0
        # erases all chars (line[0]) of the line
        line = line.replace(line[0],'')

print(countOf2 * countOf3)