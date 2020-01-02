# 시간초과
import sys
sys.stdin = open("11279_input.txt")


class Node():
    def __init__(self, data, pri):
        self.data = data
        self.next = None
        self.pri = pri

class priority_queue():
    def __init__(self, data, pri):
        self.head = Node(data, pri)

    def enqueue(self, data, pri):
        node = self.head
        flag = False
        while node.next:
            if node.next.pri > pri:
                new = Node(data, pri)
                new.next = node.next
                node.next = new
                del new
                flag = True
            if flag:
                break
            node = node.next
        if not flag and node.pri <= pri:
            node.next = Node(data, pri)


    def dequeue(self):
        node = self.head
        if not node.next:
            print(0)
        while node.next:
            if not node.next.next:
                print(node.next.pri)
                node.next = None
                break
            node = node.next

    def display(self):
        node = self.head
        print("dis", end=" ")
        while node:
            print(node.data, end=" ")
            node = node.next
        print()

n = int(input())
x = int(input())
q = priority_queue(x, x)
if not x:
    q.dequeue()

for i in range(n-1):
    x = int(sys.stdin.readline())
    if x:
        q.enqueue(x, x)
    else:
        q.dequeue()
