class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        head_node = Node('head')
        self.head = head_node
        self.tail = head_node
        self.num_of_data = 0

    def insert(self, data):
        insert_node = Node(data)
        self.tail.next = insert_node
        self.next = insert_node
        self.num_of_data += 1

    def delete(self):
        if self.num_of_data == 0:
            print('empty')
            return False
        elif self.num_of_data == 1:
            delete_node = self.head.next
            self.head.next = None
            self.tail = self.head
            self.num_of_data -= 1
            print(delete_node, '삭제')
            return delete_node.data
        else:
            delete_node =
