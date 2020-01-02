import sys
sys.stdin = open("11279_new_input.txt")


class MaxHeap:
    def __init__(self, size):
        self.__heapsize = 0
        # 배열을 사용한 힙 구현
        self.__container = [None for _ in range(size + 1)]
        self.MAX = size

    def resizing(self):
        self.__container.append([None for _ in range(20)])
        self.MAX += 20

    def __get_parent_idx(self, current):
        return current // 2

    def __get_left_child_idx(self, current):
        return current * 2

    def __get_right_child_idx(self, current):
        return current * 2 + 1

    def is_empty(self):
        if self.__heapsize == 0:
            return True
        return False

    def is_full(self):
        if self.__heapsize == self.MAX-1:
            return True
        return False

    def push(self, key):
        if self.is_full():
            self.resizing()

        self.__heapsize += 1
        self.__container[self.__heapsize] = key
        current = self.__heapsize
        parent = self.__get_parent_idx(current)

        while current != 1:
            if self.__container[parent] >= self.__container[current]:
                break
            self.__container[parent], self.__container[current] = self.__container[current], self.__container[parent]
            current = parent
            parent = self.__get_parent_idx(current)

    def __get_bigger_child_idx(self, current):
        if current * 2 > self.__heapsize:
            return None
        elif current * 2 == self.__heapsize:
            return current * 2
        else:
            if self.__container[current * 2] > self.__container[current * 2 + 1]:
                return current * 2
            return current * 2 + 1

    def pop(self):
        if self.is_empty():
            return 0

        # 삭제할 원소의 값 기억
        ret = self.__container[1]
        # 마지막 원소를 루트로
        temp = self.__container[self.__heapsize]
        self.__container[1] = temp
        # 마지막 원소 삭제처리
        self.__container[self.__heapsize] = None
        # heap 개수 1 줄임
        self.__heapsize -= 1

        if not self.__heapsize:
            return ret

        cur_idx = 1
        bigger_child_idx = self.__get_bigger_child_idx(cur_idx)
        while bigger_child_idx and temp < self.__container[bigger_child_idx]:
            self.__container[cur_idx], self.__container[bigger_child_idx] = self.__container[bigger_child_idx], self.__container[cur_idx]
            cur_idx = bigger_child_idx
            bigger_child_idx = self.__get_bigger_child_idx(cur_idx)

        return ret

    def display(self):
        print("display", end=" ")
        for i in range(self.__heapsize):
            print(self.__container[i + 1], end=" ")
        print()

n = int(input())
maxheap = MaxHeap(n)
for i in range(n):
    x = int(sys.stdin.readline())
    if not x:
        print(maxheap.pop())
    else:
        maxheap.push(x)
