
# input is a sorted (array, list, or matrix), use binary search or two pointer
# strategy
def findMax(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if (arr[mid] < arr[mid + 1]):
            start = mid + 1;
        else:
            end = mid;
    return end;

def main():
    print(findMax([1, 3, 8, 12, 4, 2]))

def test1():
    assert findMax([1, 3, 8, 12, 4, 2]) == 3 
    assert findMax([1, 2, 3, 1]) == 2 
