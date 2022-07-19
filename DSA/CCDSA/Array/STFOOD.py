for t in range(int(input())):
    N = int(input())
    max_prof = -1
    for n in range(N):
        S, P, V = map(int, input().strip().split())
        curr_prof = int(P/(S+1)) * V
        if(curr_prof>max_prof):
            max_prof = int(curr_prof)
    print(max_prof)
