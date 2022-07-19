for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    top = []
    ct, r_ct = 0, 0
    ele = arr[0]
    for i in range(1, n):
        if arr[i] >= ele and r_ct < ct:
            ele = arr[i]
            ct += 1
        else:
            r_ct += 1















'''
Brute Force method
    for i in range(n):
        if len(top)!=0:
            flag = True
            for j in range(len(top)):
                if arr[i]<top[j][-1]:
                    flag = False
                    top[j].append(arr[i])
                    break
            if flag:
                top.append([arr[i]])
        else:
            top.append([arr[i]])
    print(len(top), end=" ")
    for i in top:
        print(i[-1], end= " ")
    print()

Brute Force updated
    while(len(arr)>0):
        ele = arr[0]
        rem = [ele]
        for i in range(1, len(arr)):
            if arr[i] < ele:
                rem.append(arr[i])
                ele = arr[i]
        top.append(rem[-1])
        for i in rem:
            arr.remove(i)
    print(len(top), end = " ")
    for i in top:
        print(i, end = " ")
    print()
'''


