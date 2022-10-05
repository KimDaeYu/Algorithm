import sys

input = sys.stdin.readline
N = int(input().rstrip())
Map = [['0']*N]

for _ in range(N):
    Map.append(input().split())

dp = [[[0,0,0] for _ in range(N)] for __ in range(N+1)]
dp[1][1][0] = 1


for i in range(1,N+1):
    for j in range(1,N):
        if i==1 and j==1:
            continue
        if(Map[i][j] == '0'):
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][1]
            if(Map[i][j-1] == '0' and Map[i-1][j] == '0'):
                dp[i][j][1] = sum(dp[i-1][j-1])


# print(Map)
# print(dp)
print(sum(dp[N][N-1]))