count = 0
for h in range(24):
    for m in range(60):
        for s in range(60):
            print(f"{h}:{m}:{s}")
            if (h == 16 and (m == 37 or s == 37)):
                count += 1
                print(True)
            elif ((m == 37 and s == 16) or (m == 16 and s == 37)):
                count += 1
                print(True)
print(count)
print(count / (24 * 60 * 60))
# print(4/60/60)
print((23 * 4 + 58 * 2 + 2 * 60) / (24 * 60 * 60))
