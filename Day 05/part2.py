file=open("input.in","r")

line = file.readline()

def react(char1,char2):
    return (
            char1.lower() == char2.lower() and
            (char1.isupper() and char2.islower() or char1.islower() and char2.isupper())
           )

def reactedString(line):
    string = []
    for char in line:
        if string and react(char, string[-1]):
            string.pop()
        else:
            string.append(char)
    return string
        

charsLines = set([c.lower() for c in line])
minValue = min([reactedString(line.replace(char, '').replace(char.upper(),'')) for char in charsLines])

print (minValue)


def are_opp(a, b):
    return (a.lower() == b.lower() and
            ((a.isupper() and b.islower()) or
             (a.islower() and b.isupper())))


def react(line):
    buf = []
    for c in line:
        if buf and are_opp(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)


agents = set([c.lower() for c in line])

# part 1
print(react(line))

# part 2
print(min([react(line.replace(a, '').replace(a.upper(), ''))
           for a in agents]))