f = open("input4.txt", 'r')
lines = f.read().splitlines()
res = 0
res2 = 0
for line_index in range(len(lines)):
    line = lines[line_index]

    for letter_index in range (len(line)):
        #Part 1
        if line[letter_index] == 'X':
            # North XMAS Verification => Need the preceding 3 lines, with same letter index
            if line_index >= 3:
                l2 = lines[line_index-1][letter_index]
                l3 = lines[line_index-2][letter_index]
                l4 = lines[line_index-3][letter_index]

                if l2 == 'M' and l3 == 'A' and l4 == 'S':
                    res+=1

            # South XMAS Verification => Need the following 3 lines, with same letter index
            if len(lines) - line_index > 3:
                l2 = lines[line_index+1][letter_index]
                l3 = lines[line_index+2][letter_index]
                l4 = lines[line_index+3][letter_index]

                if l2 == 'M' and l3 == 'A' and l4 == 'S':
                    res+=1

            # East XMAS Verification => Need the following 3 letters, with same line
            if len(line) - letter_index > 3:
                l2 = lines[line_index][letter_index+1]
                l3 = lines[line_index][letter_index+2]
                l4 = lines[line_index][letter_index+3]

                if l2 == 'M' and l3 == 'A' and l4 == 'S':
                    res+=1
            
            # West XMAS Verification => Need the preceding 3 letters, with same line
            if letter_index >= 3:
                l2 = lines[line_index][letter_index-1]
                l3 = lines[line_index][letter_index-2]
                l4 = lines[line_index][letter_index-3]

                if l2 == 'M' and l3 == 'A' and l4 == 'S':
                    res+=1
            
            # North-East XMAS Verification => Need the following 3 letters on the 3 preceding lines
            if len(line) - letter_index > 3 and line_index >= 3:
                l2 = lines[line_index-1][letter_index+1]
                l3 = lines[line_index-2][letter_index+2]
                l4 = lines[line_index-3][letter_index+3]

                if l2 == 'M' and l3 == 'A' and l4 == 'S':
                    res+=1
            
            # North-West XMAS Verification => Need the preceding 3 letters on the 3 preceding lines
            if letter_index >= 3 and line_index >= 3:
                l2 = lines[line_index-1][letter_index-1]
                l3 = lines[line_index-2][letter_index-2]
                l4 = lines[line_index-3][letter_index-3]

                if l2 == 'M' and l3 == 'A' and l4 == 'S':
                    res+=1

            # South-West XMAS Verification => Need the preceding 3 letters on the 3 following lines
            if letter_index >= 3 and len(lines) - line_index > 3:
                l2 = lines[line_index+1][letter_index-1]
                l3 = lines[line_index+2][letter_index-2]
                l4 = lines[line_index+3][letter_index-3]

                if l2 == 'M' and l3 == 'A' and l4 == 'S':
                    res+=1

            # South-East XMAS Verification => Need the following 3 letters on the 3 following lines
            if len(line) - letter_index > 3 and len(lines) - line_index > 3:
                l2 = lines[line_index+1][letter_index+1]
                l3 = lines[line_index+2][letter_index+2]
                l4 = lines[line_index+3][letter_index+3]

                if l2 == 'M' and l3 == 'A' and l4 == 'S':
            
                    res+=1
        #Part 2
        elif line[letter_index] == 'A':
            # If we have room for the cross 
            if letter_index > 0 and letter_index < len(line)-1 and line_index > 0 and line_index < len(lines)-1:
                
                nw = lines[line_index-1][letter_index-1]
                ne = lines[line_index-1][letter_index+1]
                sw = lines[line_index+1][letter_index-1]
                se = lines[line_index+1][letter_index+1]
                
                if nw in ('M', 'S') and ne in ('M', 'S') and sw in ('M', 'S') and se in ('M', 'S'):
                    if nw != se and sw!=ne:
                        res2+=1


print(res) #Part1: 2662
print(res2) #Part2: 2034