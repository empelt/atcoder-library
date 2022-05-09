MOD = 10**9+7
def powmod(x,y):
    res=1
    for _ in range(y):
      res=res*x%MOD
    return res

