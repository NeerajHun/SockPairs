from collections import defaultdict

def PairCount(ar):
    d=defaultdict(int)
    for i in ar:
        d[i]+=1

    sum=0
    for color,pair in d.items():
        if d[color]>=2:
            sum+=pair//2
    return sum
N=int(input())
ar=list(map(int,input().split()))
print(f"Total pair of shocks is {PairCount(ar)}")