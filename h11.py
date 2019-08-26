n = int(input())
t1 = tuple(map(int, input().split()))
if len(t1) == n:
    print(hash(t1))
