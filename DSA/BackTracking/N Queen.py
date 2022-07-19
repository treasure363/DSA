n = int(input("Enter N: "))
safe_space = [[0]*n]*n
queens = [[i,0,0] for i in range(n)]

def display(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], '\t',  end="")
        print()

def update(arr, i, j, v):
    print(i,j)
    for l in range(n):                  #marking unsafe vertical and horizontal square
        print(i, l, j)
        arr[i][l] = arr[i][l] + v
        arr[l][j] = arr[l][j] + v
        display(arr, len(arr))
    
    #columns formula: (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)
    for l in range(n):
        print(l)
        if i-1>=0 and j-1>=0:           #upper left diagonal
            arr[i-1][j-1] += v
        if i-1>=0 and j+1<n:            #upper right diagonal
            arr[i-1][j+1] += v
        if i+1<n and j-1>=0:            #bottom left diagonal
            arr[q+1][j-1] += v
        if i+1<n and j+1<n:             #bottom right diagonal
            arr[i+1][j+1] += v
        display(arr, len(arr))
    return arr


def rec(q, safe_space, queens, n):
    print("Q:", q)
    display(safe_space, n)
    print(queens)
    if q==-1:                               #if all the queens are located then return to where the function was called from
        return queens
    flag = 1                                        #assume that the queen is not placed correctly
    for i in range(queens[q][1], n):                #check which column to place the current Queen
        #print(safe_space[q][i], safe_space[q][i]==0)
        if safe_space[q][i]==0:                        #if the square is safe then place the queen
            print("I'm in at", i)
            if queens[q][2]==0:
                safe_space = update(safe_space, q, i, 1)#updating spaces which are attacked now by the queen
                queens[q] = [q,i,1]                       #updating the queens position
            else:
                safe_space = update(safe_space, q, queens[q][1], -1)#updating spaces which were attacked before to safe
                queens[q] = [q,i,1]                       #updating the queens position
                safe_space = update(safe_space, q, i, 1)#updating spaces which are attacked now by the queen
            flag = 0                                #updating flag which indicates the queen is placed
            break
    print("Updated:", "YES" if flag==0 else "NO")
    display(safe_space, n)
    print(queens)
    if flag:
        #safe_space = update(safe_space, q, queens[q][1], 1)#updating spaces which were attacked before to safe
        queens[q] = [q, 0]                          #restting the queen, basically not placing it on the board yet
        rec(q-1, safe_space, queens, n)
    else:
        rec(q+1, safe_space, queens, n)

print(rec(0, safe_space, queens, n))

for i in range(n):
    Q = queens[i]
    for j in range(n):
        if i==Q[0] and j==Q[1]:
            print("Q\t", end="")
        else:
            print("0\t", end="")
    print()