
with open("day3/input.txt") as f:
    data = f.readlines()

diagnostics = [line.strip() for line in data]
#diagnostics = [
#    "00100",
#    "11110",
#    "10110",
#    "10111",
#    "10101",
#    "01111",
#    "00111",
#    "11100",
#    "10000",
#    "11001",
#    "00010",
#    "01010",
#]
print(diagnostics)
print(len(diagnostics))

res = ""
for i in range(len(diagnostics[0])):
    bits = "".join([diagnostic[i] for diagnostic in diagnostics])
    if bits.count("1") == bits.count("0"):
        raise ValueError("Both bits equally common")
    most_significant = "1" if bits.count("1") > bits.count("0") else "0"
    res += most_significant

mask = int("1" * len(diagnostics[0]), 2)
gamma = int(res, 2)
epsilon = ~gamma & mask
print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")
print(f"Product: {gamma * epsilon}")
