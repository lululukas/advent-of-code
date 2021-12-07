from advent.utils import read_data


measurements = read_data(1)
#measurements = [
#    199,
#    200,
#    208,
#    210,
#    200,
#    207,
#    240,
#    269,
#    260,
#    263,
#]

totals = []
for i, measurement in enumerate(measurements):
    s, e = i, i + 3
    if e > len(measurements):
        break
    totals.append(sum(measurements[s:e]))

results = []
for i, total in enumerate(totals):
    if i == 0:
        change = None
    else:
        prev_sum = totals[i-1]
        if total == prev_sum:
            change = "no change"
        else:
            change = "increase" if total > prev_sum else "decrease"
    results.append(change)

print(results.count("increase"))
