import sys
sys.stdin = open("11286_input.txt")

class Node:
    def __init__(self, pri, key):
        self.pri = pri
        self.key = key


class Heap:
    def __init__(self, n):
        self.__heapsize = 0
        self.__container = [None for _ in range(n + 1)]

    def __get_parent(self, node):
        return node // 2

    def push(self, pri, key):
        self.__heapsize += 1
        cur = self.__heapsize
        new = Node(pri, key)
        self.__container[cur] = new
        par = self.__get_parent(cur)
        while cur != 1:
            if self.__container[par].pri < self.__container[cur].pri:
                break
            if self.__container[par].pri == self.__container[cur].pri:
                if self.__container[par].key < self.__container[cur].key:
                    break
            self.__container[par], self.__container[cur] = self.__container[cur], self.__container[par]
            cur = par
            par = self.__get_parent(cur)

    def is_empty(self):
        if not self.__heapsize:
            return True
        return False

    def __get_smaller(self, node):
        if node * 2 > self.__heapsize:
            return None
        if node * 2 == self.__heapsize:
            return node * 2
        if self.__container[node * 2].pri == self.__container[node * 2 + 1].pri:
            if self.__container[node * 2].key < self.__container[node * 2 + 1].key:
                return node * 2
            return node * 2 + 1
        if self.__container[node * 2].pri < self.__container[node * 2 + 1].pri:
            return node * 2
        return node * 2 + 1


    def pop(self):
        if self.is_empty():
            return 0

        return_n = self.__container[1]
        self.__container[1] = self.__container[self.__heapsize]
        self.__container[self.__heapsize] = None
        self.__heapsize -= 1

        if not self.__heapsize:
            return return_n.key

        cur = 1
        child = self.__get_smaller(cur)
        while child and self.__container[cur].pri >= self.__container[child].pri:
            if self.__container[cur].pri == self.__container[child].pri:
                if self.__container[cur].key <= self.__container[child].key:
                    break
            self.__container[cur], self.__container[child] = self.__container[child], self.__container[cur]
            cur = child
            child = self.__get_smaller(cur)

        return return_n.key

    def display(self):
        for i in self.__container:
            if not i:
                print("none", end=" ")
            else:
                print(i.pri, end= " ")
        print()

        for i in self.__container:
            if not i:
                print("none", end=" ")
            else:
                print(i.key, end= " ")
        print()

n = int(input())
heap = Heap(n)
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heap.push(abs(x), x)
    else:
        print(heap.pop())