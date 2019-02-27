'''
큐를 구현하여 다음 동작을 확인해봅시다
세 개의 데이터 1, 2, 3 을 차례로 큐에 삽입하고
큐에서 세 개의 데이터를 차례로 꺼내서 출력한다.
1, 2, 3이 출력되어야함
'''

size = 4
Q = [0] * size
front, rear = 0, 0

def enQueue(item):
    global front, rear
    rear += 1
    rear = rear % size
    Q[rear] = item

def Qpeek():
    global front
    return Q[front + 1]

def deQueue():
    global front
    front += 1
    front = front % size
    return Q[front]

def isFull():
    global front, rear
    if (rear + 1) % size == front:
        return True
    return False

def isEmpty():
    global front, rear
    if front == rear:
        return True
    return False


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(4)
enQueue(4)
print(deQueue())
print(deQueue())
print(Q)
print(front, rear)