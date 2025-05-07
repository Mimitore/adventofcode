import re

f = open("input3.txt", 'r')

txt = f.read() 
res = 0
res2 = 0


pattern = re.compile(r"mul\((\d*),(\d*)\)")
matches = re.finditer(pattern, txt)

for match in matches:

    res+= int(match.group(1))*int(match.group(2))

print(res) #162813399

enabled_pattern = re.compile(r"do\(\)(.*?)don\'t\(\)", re.DOTALL)
enabled_matches = re.finditer(enabled_pattern, txt)

# Capturing texts between do() and don't()
for emat in enabled_matches:
    enabled_mul = re.finditer(pattern, emat.group(1)) 

    # Capturing the pattern mul(x,x) between do() and don't()
    for emul in enabled_mul:
        res2+= int(emul.group(1))*int(emul.group(2))

# Also capturing the text before the first do() of the input
first_enabled_matches = re.search(r"(.*?)do\(\)", txt).group(1)
# Capturing the pattern mul(x,x) in this text
first_enabled_mul = re.finditer(pattern, first_enabled_matches) 
for fmul in first_enabled_mul:
        res2+= int(fmul.group(1))*int(fmul.group(2))

print(res2)