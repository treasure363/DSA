T =int(input())
for t in range(T):
    A,B,C,P,Q,R = map(int, input().strip().split())
    pair = {
        "1":[A,P],
        "2":[B,Q],
        "3":[C,R]
    }
    if P>Q and P>R:
        pair["1"]=[P,A]
    elif Q>P and Q>R:
        pair["2"]=[Q,B]
    else:
        pair["3"]=[R<C]
    for i in pair.keys():
        print(i, pair[i])
    chef = list(pair[i][0] for i in pair.keys())
    total = list(pair[i][1] for i in pair.keys())
    print(chef, total)
    if(int(sum(chef)))>=(int(sum(total))):
        print("YES")
    else:
        print("NO")