a = int(input()) # Distance between rows
b = int(input()) # Distance between holes
l = int(input()) # The length of the free end of the lace
N = int(input()) # Number of holes in each row

LenthOfTheLace = (2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)
print(LenthOfTheLace)
