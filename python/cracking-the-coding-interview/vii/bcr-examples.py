a = [13,27,35,40,49,55,59] # sorted
b = [17,35,39,40,55,58,60] # sorted

# brute force O(N^2)
print("Brute force solution O(n^2)")
for i in a:
    for j in b:
        if i == j:
            print(i)


"""
Rather, we want to look for BCR in this case,
The BCR in this case is O(N), because we know we will have to look at each
element at least once and there are 2N total elements
"""
# we can use binary search to reduce to O(NlogN) since the array is sorted
# O(nlogn) t | O(n) space
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return arr[mid]
    return 0

print("Binary search solution O(nlogn)")
for i in a:
    if binary_search(b, i):
        #breakpoint()
        print(i)

# now, in order to reduce this to O(n), 
# we have to find a way to reduce O(logn) to O(1)

mydict = {i:False for i in b}

for i in a:
    if i in mydict:
        mydict[i] = True

print("Hashtable solution O(n)")
filter_keys = [key for key, value in mydict.items() if value == True]
print("\n".join(str(v) for v in filter_keys))
print("\n".join(map(str, filter_keys)))
