count = 0
for hours in range(24):
    for min in range(60):
        for sec in range(60):
            print(f"{hours}:{min}:{sec}")
            if (hours == 16 and ((min == 16 or min == 37) or (sec == 16 or sec == 37))) or (
                    (min == 16 or min == 37) and (sec == 16 or sec == 37)):
                count += 1
                print(True)
print(count)
print(count/(24*60*60))
print(4/60/60)
