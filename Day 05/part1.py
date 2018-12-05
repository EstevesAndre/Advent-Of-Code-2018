file=open("input.in","r")

line = file.readline()

def react(char1,char2):
    if char1.isupper() and char2.islower() or char2.isupper() and char1.islower():
        if char1.upper() == char2.upper():
            return True
    return False

findsReact = True

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

print(len(line))