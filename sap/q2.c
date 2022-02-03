
def pizzaMeat(numOfOrders, size, ordersNum):
    mpizza = []

    for i in range(numOfOrders - size + 1):
        found = 0
        for j in range(i, i + size):
            if ordersNum[j] < 0:
                mpizza.append(ordersNum[j])
                found = 1
                break
        if found == 0:
            mpizza.append(0)

    return mpizza


if __name__ == "__main__":
    #numOfOrders, size = map(int, input().split())
    #ordersNum = list(map(int, input().split())
    lst = [-11, -2, 19, 37, 64, -18]
    print(pizzaMeat(6, 3, lst))
