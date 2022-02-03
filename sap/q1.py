def nonRepeatingCharacter(s):
    lst = []
    for i in s:
        count = 0
        for j in s:
            if i == j:
                count += 1
            if count > 1:
                break
        if count == 1:
            lst.append(i)
    return lst

if __name__ == "__main__":
    # string = input()
    print(nonRepeatingCharacter("ChampakChacha")) # m p k c 
