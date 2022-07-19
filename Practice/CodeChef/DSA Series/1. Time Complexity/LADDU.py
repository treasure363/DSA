T = int(input())
for t in range(T):
    inp = list(input().split().strip())
    laddus = 0
    for _ in range(inp[0]):
        activity = list(input().strip().split())
        if activity[0]=="CONTEST_WON":
            if activity[1]<=20:
                laddus += 300 + (20-activity[1])
            else:
                laddus += 300
        elif activity[0]=="TOP_CONTRIBUTOR":
            laddus += 300
        elif activity[0]=="BUG_FOUND":
            laddus += activity[1]
        else:
            laddus += 50
    if inp[1]=="INDIAN":
        print(laddus//200)
    else:
        print(laddus//400)
