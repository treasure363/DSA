s = set()
N = int(input())
for n in range(N):
    a, b = map(int, input().strip().split())
    s.add((a,b))
p = list(s)
p.sort()
s = p

start, end = s[0][0], s[0][1]
for i in range(1, len(s)):
    if s[i][0] < s[i-1][1]:                             #starting of new meeting is overlapping with previous meeting
        end = s[i][1]
    elif s[i][0] == end:
        end = s[i][1]
        if i==N-1:
            print(start, end)
            break
    else:
        print(start, end)
        start = s[i][0]                                 #update start and end
        end = s[i][1]
        if i==N-1:
            print(start, end)
            break

