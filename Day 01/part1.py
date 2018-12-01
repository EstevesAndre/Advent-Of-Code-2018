file=open("input.in","r")

# read all lines
content = file.readlines()
file.close()
# remove all whitespaces and \n at the beginning and at the end of each string
content = [i.strip() for i in content]
# transforming the list of strings into a list of integers
content = list(map(int,content))

print(sum(content))