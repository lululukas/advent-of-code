from advent.utils import read_data


measurements = read_data(1)

results = []
for i, measurement in enumerate(measurements):
    if not results:
        results.append(None)
        continue
    prev_measurement = measurements[i - 1]
    if measurement == prev_measurement:
        change = "no change"
    else:
        change = "increase" if measurement > prev_measurement else "decrease"
    results.append(change)

print(results.count("increase"))
