s = input()

flag = True

while(flag):
    flag = False
    # print(s)
    for i in range(len(s)-1):
        if abs(ord(s[i]) - ord(s[i+1])) == 32:
            flag = True
            s = s[:i] + s[i+2:]
            break
print(-1 if s=='' else s)