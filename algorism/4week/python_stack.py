def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("stack is empty!")
        return
    else:
        return s.pop()
s = []

push(1)
push(2)
push(3)
print(s)
print(pop())
print(pop())
print(pop())
print(s)