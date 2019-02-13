
# C 스타일로 짜기
size = 100
stack = [0] * size
top = -1

def push(item):
    # top은 int. int는 def 등 함수 속에서 변경이 되어도 실제 int 값이 변화하지 않는다.
    # 때문에 그렇게 사용하기 위해서는 global top으로 사용한다.
    global top
    if top > size -1:
        return
    else:
        top += 1
        # stack은 list. python에서  list는 def등 함수 속에서 변경이 되어도 실제 list가 변화한다.
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("stack is empty!")
        return 0
    else:
        result = stack[top]
        top -= 1
        return result

push(1)
push(2)
push(3)

print(top, stack)



print("pop item => %d " % pop())
print(pop())
print(pop())
print(top, stack)