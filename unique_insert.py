list = [13,12,15,14,12,19,13,18,18,16,16,12,13]
unique = []
for i in range(len(list)):
    if list[i] not in unique:
        unique.append(list[i])
unique.sort()
print(unique)