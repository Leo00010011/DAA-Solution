
def dp_solver(S, T):
    n = len(S)
    m = len(T)
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        dp[i][0] = 1
        
        for j in range(1, m+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][m] * 2

def count_paths(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]


print(count_paths('abracadabra','abra'))

#s: abdbaedadb
#t: abda 