n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = "YES"
for i in range(n):
    if a[i] in b:
        ans = "YES"
        break
    else:
        ans = "NO"
print(ans)