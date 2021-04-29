arr=[1,7,5,9,2,12,3]
k = 2
c = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] - arr[i] == k or arr[i] - arr[j] == k:
            print(arr[i], arr[j])
            c += 1
print(c)
myhash = dict()
for i in arr:
    myhash[i] = 0
for key,value in myhash.items():
    if key + value == k or key - value == k:
        myhash[key] += 1

print(myhash)
