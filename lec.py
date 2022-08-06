s = input()
n = len(s)
res = ""
for i in range(1, n // 2 + 1):
    prefix = s[0:i]
    new_s = prefix * (n // len(prefix))
    if res == "" and s == new_s:
        res = prefix
if res == "":
    print(s)
else:
    print(res)