for t in range(int(input())):
    N = int(input())
    S = input()
    A, B = [], []
    for i in range(0, len(S), 2):
        A.append(int(S[i]))
        B.append(int(S[i+1]))
    ct = N
    for i in range(N-1):
        if A[:i].count("1") > B[:i+1].count("1") + B[i+1:].count("1") or B[:i].count("1") > A[:i+1].count("1") + A[i+1:].count("1"):
            ct = i+1
            break
    print(ct*2)