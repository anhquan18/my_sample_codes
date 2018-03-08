l = [x for x in range(10)]
print l

a = 10
l = [x*a for x in range(10) if (x % 2 == 0) and (x > 5)]
print l

for x in l:
    print x

for x in l[1:-1]:
    print x

for x in range(len(l)):
    print l[x]
