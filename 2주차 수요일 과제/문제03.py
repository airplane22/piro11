h = []

for i in range(9):
    h.append(int(input()))

breaking = ''
for i in range(9):
    for j in range(9):
        if i != j :
            if sum(h)-h[i]-h[j] == 100 :
                h[i] = 'x'
                h[j] = 'x'
                breaking = 1
                break
            else :
                pass

        else :
            continue
    if breaking == 1 :
        break
    else :
        continue

h.remove('x')
h.remove('x')

h.sort()

for i in h:
    print(i)





