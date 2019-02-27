'''
큐를 구현하여 다음 동작을 확인해봅시다
세 개의 데이터 1, 2, 3 을 차례로 큐에 삽입하고
큐에서 세 개의 데이터를 차례로 꺼내서 출력한다.
1, 2, 3이 출력되어야함
'''

size = 100
Q = [0] * size
front, rear = -1, -1

def enQueue(item):
    global front, rear
    if isFull():
        print("Queue Full")
    rear += 1
    Q[rear] = item

def Qpeek():
    global front
    return Q[front + 1]

def deQueue():
    global front
    if isEmpty():print("Queue Empty")
    front += 1
    return Q[front]

def isFull():
    global front, rear
    if rear == 100 - 1:
        return True
    return False

def isEmpty():
    global front, rear
    if front == rear and rear == -1:
        return True
    return False


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())

print(Q)
print(front, rear)