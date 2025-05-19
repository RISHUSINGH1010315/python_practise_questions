import re
name = "Hello pyhton Rishu 231010315"

digitCount = re.sub("[^0-9]", "", name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall(r"\s", name)

print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))