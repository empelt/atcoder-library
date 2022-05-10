# 再帰上限解放
import sys
sys.setrecursionlimit(10**6)

MOD = 10**9+7
N = 1

# mod累乗
def powmod(x,y):
    res=1
    for _ in range(y):
      res=res*x%MOD
    return res

# bit全探索
for i in range(2 ** N):
    for j in range(N):
        if ((i >> j) & 1):
            print('hello')

# dfs
edge = [[] for _ in range(N)]
visited = [False] * N
def dfs(now):
    if visited[now]:
        return 0
    cnt = 1
    visited[now] = True
    for i in edge[now]:
        cnt += dfs(i)
    return cnt