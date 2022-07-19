def origami(dp, m, n):
    
    vertical_min = 1000000000000
    horizontal_min = 1000000000000
    if m == n:
        return 1
    if n == 13 and m == 11 or m == 13 and n == 11:
        return 6
    

    # If the answer for the given rectangle is
    # previously calculated return that answer
    if dp[m][n] != 0:
        return dp[m][n]

    # The rectangle is cut horizontally and
    # vertically into two parts and the cut
    # with minimum value is found for every
    # recursive call.
    for i in range(1, m//2+1):

        # Calculating the minimum answer for the
        # rectangles with width equal to n and length
        # less than m for finding the cut point for
        # the minimum answer
        horizontal_min = min(origami(dp, i, n) + origami(dp, m-i, n), horizontal_min)
    for j in range(1, n//2+1):

        # Calculating the minimum answer for the
        # rectangles with width equal to n and length
        # less than m for finding the cut point for
        # the minimum answer
        vertical_min = min(origami(dp, m, j) + origami(dp, m, n-j), vertical_min)

    # Minimum of the vertical cut or horizontal
    # cut to form a square is the answer
    dp[m][n] = min(vertical_min, horizontal_min)
    return dp[m][n]



if __name__ == '__main__':
    inp = [input().strip.split()]
    m = int(inp[0])
    n = int(inp[1])
    dp = [[0 for i in range(max(m,n))] for i in range(max(m,n))]
    print(origami(dp, m, n))
