# O(n^2) time | O(1) space
def pairWithTargetSum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return []


# O(n) time | O(n) space
def pairWithTargetSumHashing(arr, target):
    mymap = {}
    for i,v in enumerate(arr):
        if target-v in mymap.keys():
            return (i, mymap[target-v])
        mymap[v] = i
    return []


def binarySearch(arr, target):
    pass

# O(nlogn) time | O(logn) space
def pairWithTargetSumBinarySearch(arr, target):
    pass

def pairWithTargetSumTwoPointers(arr, target):
    arr.sort()
    leftPtr = 0
    rightPtr = len(arr) - 1
    while leftPtr < rightPtr:
        sum = arr[leftPtr] + arr[rightPtr]
        if sum == target: return (leftPtr, rightPtr)
        elif sum < target: leftPtr += 1;
        else: rightPtr -= 1;
    return []


def main():
    print(pairWithTargetSum([1,2,3,4,6], 6))
    print(pairWithTargetSumHashing([1,2,3,4,6], 6)) 
    print(pairWithTargetSumTwoPointers([1,2,3,4,6], 6))

main()

def test1():
    pass
