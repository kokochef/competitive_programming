#https://www.codechef.com/problems/SEAVOTE/
itr = int(raw_input())
for i in xrange(itr):
    b = int(raw_input())
    a = raw_input().split()
    a = [int(s) for s in a]
    for s in a:
        if s==0:
            b-=1
    d = sum(a)
    if d<=(99+b) and d>=100:
        print "YES"
    else:
        print "NO"
