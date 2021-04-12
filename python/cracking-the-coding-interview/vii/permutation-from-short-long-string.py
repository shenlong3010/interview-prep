from itertools import permutations
s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"

permutation = [''.join(p) for p in permutations(s)]
print(permutation)

