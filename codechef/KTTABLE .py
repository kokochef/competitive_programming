#https://www.codechef.com/problems/KTTABLE/
itr = int(raw_input())
for i in xrange(itr):
    n = int(raw_input())
    a = raw_input().split()
    a = [int(s) for s in a]
    b = raw_input().split()
    b = [int(s) for s in b]
    time = 0
    nos =0
    for j in xrange(n):
        t = a[j]-time
        if t>=b[j]:
            nos+=1
        time = a[j]
    print nos
