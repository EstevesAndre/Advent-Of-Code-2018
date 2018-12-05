file=open("input.in","r")

Initialline = file.readline()

def react(char1,char2):
    if char1.isupper() and char2.islower() or char2.isupper() and char1.islower():
        if char1.upper() == char2.upper():
            return True
    return False

lengths = list()

for char in range(ord('a'), ord('z') + 1):        
    findsReact = True
    line = Initialline.replace(chr(char), '')
    line = line.replace(chr(char).upper(),'')
    print(chr(char))
    while findsReact == True:
        findsReact = False
        index = 0
        reactedLine = ""
        while index < len(line) - 1:
            if react(line[index], line[index+1]):
                index += 2
                findsReact = True
            else:
                reactedLine += line[index:index+1]
                index += 1
        reactedLine += line[index:]
        line = reactedLine
    
    lengths.append(len(line))

print(min(lengths))