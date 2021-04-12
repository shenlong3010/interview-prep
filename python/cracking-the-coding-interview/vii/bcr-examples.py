a = [13,27,35,40,49,55,59] # sorted
b = [17,35,39,40,55,58,60] # sorted

# brute force O(N^2)
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
print(binary_search(b, 60))

found_value = []
for i in a:
    found_value.append(binary_search(b, i))
print(found_value) 

