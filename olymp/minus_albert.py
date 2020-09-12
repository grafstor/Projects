
input()
a = input().split()

bx = []
bn = []

sm = 0

for num in a:
    sm += abs(num)

dean = sm/len(a)


for num in a:
    if num >= dean:
        bx.append(num)
        continue

    if abs(num) >= dean:
        bn.append(num)
        
mins = 109

comb = None

bx = sorted(bx)
bn = sorted(bn)



for i in range(len(bn)-1):
    for j in range(len(bx)):
        rex = bx[j]+bn[i]+bn[i+1]

        if rex == 0:
            print(bx[j], bn[i], bn[i+1])
            exit()

        if rex < mins:
            comb = (bx[j], bn[i], bn[i+1])
            mins = rex

for i in range(len(bx)-1):
    for j in range(len(bn)):
        rex = bn[j]+bx[i]+bx[i+1]

        if rex == 0:
            print( bn[j]+bx[i]+bx[i+1])
            exit()

        if rex < mins:
            comb = (bn[j],bx[i],bx[i+1])
            mins = rex


print(comb)
