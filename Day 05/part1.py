file=open("input.in","r")

line = file.readline()

def react(char1,char2):
    return (
            char1.lower() == char2.lower() and
            (char1.isupper() and char2.islower() or char1.islower() and char2.isupper())
           )

reactedString = []

for char in line:
    if reactedString and react(char, reactedString[-1]):
        reactedString.pop()
    else:
        reactedString.append(char)
    
print(len(reactedString))