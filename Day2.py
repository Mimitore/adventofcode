f = open("input2.txt", 'r')

content = f.readlines() 
n_safe = 0

for c in content:
    levels = list(map(int, c.strip().split()))
    is_safe = True
    has_increased = None

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]

        if abs(diff) > 3 or diff == 0:
            is_safe = False
            break

        is_increasing = diff > 0

        if has_increased is not None and is_increasing != has_increased:
            is_safe = False
            break

        has_increased = is_increasing

    if is_safe:
        n_safe += 1

print(n_safe)