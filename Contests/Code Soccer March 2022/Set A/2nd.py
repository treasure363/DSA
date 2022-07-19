X, Y, Z = map(int, input().strip().split())
if Z==5:
    slices = 0
    left = X - Y
elif Z>0 and Z<5:
    slices = 5 - Z
    left = X - Y - 1
else:
    slices = 0
    left = X - Y
print(left, slices)