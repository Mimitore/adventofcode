f = open("input.txt", 'r')

content = f.readlines() 
res = 0
left_list = list()
right_list = list()

# Extracting left and right IDs
for c in content:
    left_list.append(int(c[0:5]))
    right_list.append(int(c[8:13]))

left_list.sort()
right_list.sort()

# Pairing up the numbers, showing the total distance
diff_list = [abs(left_list[i] - right_list[i]) for i in range (len(left_list))]
print(sum(diff_list))





