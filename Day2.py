f = open("input2.txt", 'r')

content = f.readlines() 
n_safe = 0
unsafe_reports = list()
for c in content:
    levels = list(map(int, c.strip().split()))
    is_safe = True
    has_increased = None

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]

        if abs(diff) > 3 or diff == 0:
            is_safe = False
            unsafe_reports.append(levels)
            break

        is_increasing = diff > 0

        if has_increased is not None and is_increasing != has_increased:
            is_safe = False
            unsafe_reports.append(levels)
            break

        has_increased = is_increasing

    if is_safe:
        n_safe += 1

print(n_safe) #463

# Part 2

for report in unsafe_reports:

    # Testing every possible combinations until finding a safe combination
    for i in range (len(report)):
        new_report = report[:i] + report[i+1:]
        is_safe = True
        has_increased = None

        for j in range(1, len(new_report)):
            diff = new_report[j] - new_report[j - 1]

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
            break


print(n_safe) #514