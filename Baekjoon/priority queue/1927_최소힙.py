import sys
sys.stdin = open("1927_input.txt")


class Heap:
    def __init__(self, n):
        self.__heapsize = 0
        self.__container = [None for _ in range(n + 1)]

    def __get_parent(self, node):
        return node // 2

    def push(self, pri):
        self.__heapsize += 1
        current = self.__heapsize
        self.__container[current] = pri
        parent = self.__get_parent(current)

        while current != 1:
            if self.__container[parent] <= self.__container[current]:
                break
            self.__container[parent], self.__container[current] = self.__container[current], self.__container[parent]
            current = parent
            parent = self.__get_parent(current)

    def is_empty(self):
        if not self.__heapsize:
            return True
        return False

    def __get_small_child(self, node):
        if node * 2 > self.__heapsize:
            return None
        if node * 2 == self.__heapsize:
            return node * 2
        if self.__container[node * 2] < self.__container[node * 2 + 1]:
            return node * 2
        return node * 2 + 1

    def pop(self):
        if self.is_empty():
            return 0

        return_num = self.__container[1]
        self.__container[1] = self.__container[self.__heapsize]
        self.__container[self.__heapsize] = None
        self.__heapsize -= 1

        if not self.__heapsize:
            return return_num

        current = 1
        small_child = self.__get_small_child(current)

        while small_child and self.__container[current] > self.__container[small_child]:
            self.__container[current], self.__container[small_child] = self.__container[small_child], self.__container[current]
            current = small_child
            small_child = self.__get_small_child(current)

        return return_num

    def display(self):
        print(self.__container)


size = int(input())
heap = Heap(size)

for n in range(size):
    x = int(sys.stdin.readline())
    if x:
        heap.push(x)
    else:
        print(heap.pop())