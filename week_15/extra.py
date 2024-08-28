class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def bubble_sort(self):
        if self.head is None:
            return

        has_made_changes = True
        
        while has_made_changes:
            
            has_made_changes = False
            current = self.head

            while current.next is not None:
                next_node = current.next

                if current.data > next_node.data:
                    
                    current.data, next_node.data = next_node.data, current.data
                    has_made_changes = True

                current = next_node


node1 = Node("64")
node2 = Node("34")
node3 = Node("25")
node4 = Node("12")
node5 = Node("22")
node6 = Node("11")
node7 = Node("90")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

ll = LinkedList(node1)

print("Lista original:")
ll.print_structure()

ll.bubble_sort()

print("Lista ordenada:")
ll.print_structure()




