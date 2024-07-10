class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

class Stack:
    
    def __init__(self, head=None):
        self.head = head
        
    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        pop_data = self.head.data
        self.head = self.head.next
        return pop_data


my_stack =  Stack()

my_stack.push('First')
my_stack.push('Second')
my_stack.push('Third')

print('Stack after push')
my_stack.print_structure()


print('POP')
print(my_stack.pop())

print('Stack after POP')
my_stack.print_structure()

print('POP')
print(my_stack.pop())

print('Stack after POP')
my_stack.print_structure()



