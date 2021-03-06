import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
	n, b = list(map(int, input().split()))
	prices = list(map(int, input().split()))
	prices = sorted(prices)
	res = 0
	total = 0
	for i in range(n):
		if total + prices[i] <= b:
			res += 1
			total += prices[i]
		else:
			break
	print(res)


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()

