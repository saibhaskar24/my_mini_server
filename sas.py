n,k = map(int,input().split())
ss = "1"
fs = "9"
ans = 0
for i in range(n-1):
    ss+="0"
    fs+="9"
ss = int(ss)
fs = int(fs)
if k < fs:
    fs = k
for i in range(ss,fs):
    j = str(i)
    c = 1
    for k in j:
        if c<0:
            break
        if k == "0":
            c -= 1
        else:
            c=1
    if c>=0:
        ans+=1
        print(j)

print(ans)
