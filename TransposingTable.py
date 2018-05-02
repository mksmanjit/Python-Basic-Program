sunday = [20, 22, 25, 28]
monday = [15, 20, 16, 18]
tuesday = [25, 28, 12]

for item in zip(sunday, monday, tuesday):
    print(item)

daily = [sunday, monday, tuesday]

for item in zip(daily[0], daily[1], daily[2]):
    print(item)

for item in zip(*daily):
    print(item)


transposed = list(zip(*daily))
print(transposed)