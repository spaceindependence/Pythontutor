from math import *

Students1Class = int(input())
Students2Class = int(input())
Students3Class = int(input())
TotalDesks = ceil((Students1Class / 2)) + ceil((Students2Class / 2)) + ceil((Students3Class / 2))
print(TotalDesks)