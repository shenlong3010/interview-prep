def sumSubArray(array):
	total = sum(array)
	avg = total // 3
	subArray = []
	totalSub = 0
	subArray.append(0)

	for i in range(len(array) - 1):
		totalSub += array[i]
		if totalSub == avg:
			subArray.append(i + 1)
			totalSub = 0
	return subArray

def test1():
	assert sumSubArray([2,2,1,3,4]) == [0,2,4]

def test2():
	assert sumSubArray([1,1,1,1,1,5,5]) == [0,5,6]
