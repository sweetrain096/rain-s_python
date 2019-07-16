import sys
sys.stdin = open("1158_input.txt")

# 기본 노드 생성. 우선 다음것만 만들기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



n, m = map(int, input().split())

node1 = Node(1)
node2 = Node(2)
node1.next = node2

node3 = Node(3)
node2.next = node3

node4 = Node(4)
node3.next = node4



# delete
# delete_node = node3
delete_node = node3
pre_node = node3
next_node = pre_node
node2.next


node = node1
while node:
    print(node.data)
    node = node.next