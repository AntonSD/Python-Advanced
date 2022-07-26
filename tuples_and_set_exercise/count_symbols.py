text = input()
occurrences = {}

for ch in text:
    if ch not in occurrences:
        occurrences[ch] = 1
    else:
        occurrences[ch] += 1

sorted_occurrences = sorted(occurrences)

for key, value in sorted(occurrences.items()):
    print(f"{key}: {value} time/s")