i = 0
arr = []
while i < 5000:
    arr.append(i*i*i)
    i += 1

print(f" {arr[0]} {arr[1]} {arr[2]}")