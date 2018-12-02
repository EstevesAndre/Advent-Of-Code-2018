file=open("input.in","r")

content=file.readlines()
content=[i.strip() for i in content]

# size of each box ID
sizeLine = len(content[0])

# key [box ID1, box ID2, similarity]
# similarity <- array with the diference of each char of the two IDs
    # Ex: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0]
    # Which means that both string are equal with exception of character index 20 that differ in 6 ordinary numbers    
key = []

# bestValue, if 0 means that the two strings are equal.
# so it starts with sizeLine, which means that are completely different
bestValue = sizeLine

for i in range(0, len(content)): # Each ID1 
    for j in range(i + 1, len(content)): # ID2 to be compared with ID1
        # returns an array with all OR EXCLUSIVE values between the two BOX IDs
        similarity = [ord(a) ^ ord(b) for a,b in zip(content[i],content[j])] 
        # equalValue is the value of comparation [0,sizeLine]:
            # 0 means both strings are equal;
            # 1 means that just one character is different between the two Box IDs
            # and so on...
        equalValue = sizeLine - similarity.count(0)
        # if equalValue is lower than bestValue means that the two IDs are more similar than the previous two IDs
        # so key array with the stored values are updated with the new IDs and similarity
        if equalValue < bestValue:
            key = []
            bestValue = equalValue
            key.append(content[i])
            key.append(similarity)

# return Value with common letters between two most equal Box IDs
mostCommon = key[0]

# if a value of index of the similarity is != 0 means that index value of the box ID is different,
# so is erased of the string mostCommon
for i in range(0,len(key[0])):
    if(key[1][i] != 0):
        mostCommon = mostCommon.replace(key[0][i],'')

print(mostCommon)