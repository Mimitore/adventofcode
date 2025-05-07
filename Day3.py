import re

f = open("input3.txt", 'r')

txt = f.read() 
res = 0

pattern = re.compile(r"mul\((\d*),(\d*)\)")
matches = re.finditer(pattern, txt)

for match in matches:
    res+= int(match.group(1))*int(match.group(2))

print(res) #162813399