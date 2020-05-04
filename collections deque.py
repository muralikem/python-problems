from collections import deque

d = deque()

for _ in range(int(input())):
    a = input()

    #c = map(int, b)
    if(a == 'pop'):
        d.pop()
    elif(a == 'popleft'):
        d.popleft()
    else:
        l = a.split()
        if(l[0] == 'append'):
            d.append(l[1])
        else:
            d.appendleft(l[1])

print(' '.join(d))