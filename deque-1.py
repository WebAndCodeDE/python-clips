from collections import deque
d = deque()

command_dict = {
    "append":d.append, 
    "appendleft": d.appendleft,
    "pop": d.pop,
    "popleft": d.popleft
}

for i in range(int(input())):
    iterations = input().split()
    if len(iterations)>1:
        x,y = iterations
        command_dict[x](int(y))
    else:
        command_dict[iterations[0]]()

print(*d)