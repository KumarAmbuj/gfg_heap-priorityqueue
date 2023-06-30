import math


def height(N):
    return math.ceil(math.log2(N + 1)) - 1



N = 6
print(height(8))