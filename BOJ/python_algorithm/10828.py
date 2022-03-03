n = int(input())

stack = []

def push(num):
    stack.append(num)

def pop():
    if len(stack) == 0:
        return -1 
    else: 
        return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1 
    else: 
        return 0 

def top():
    if len(stack) == 0:
        return -1 
    else: 
        return stack[-1]
ls = []
for _ in range(n):
    ls += list(input().split())

for i in range(len(ls)):
    if ls[i] == 'push':
        push(int(ls[i+1]))
    elif ls[i] == 'pop':
        print(pop())
    elif ls[i] == 'size':
        print(size())
    elif ls[i] == 'empty':
        print(empty())
    elif ls[i] == 'top':
        print(top())