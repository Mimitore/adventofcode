#Part 1
f = open("input.txt", 'r')

content = f.readlines() 
res = 0 # result for part 2
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
print(sum(diff_list)) # result part 1: 2031679


#Part 2 
left_index = 0
while left_index!=len(left_list):
    for i in range (len(left_list)):
        l = left_list[left_index] 
        r = right_list[i]

        # Increasing similarity score
        if (l == r):
            res+=l

        # There is no number on the right, less than l
        elif (l < r):
            left_index+=1
            break

        # If the last number on the right, go to the next number on the left
        if (i == len(left_list) - 1):
            left_index+=1

print(res) # result part 2: 19678534


