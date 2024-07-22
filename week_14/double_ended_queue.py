class Node: 
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class double_ended_queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def print_structure(self):
        current_node = self.front

        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.next
    
    def push_left(self, data):
        new_node = Node(data, next=self.front)
        
        if self.front is not None:
            self.front.prev = new_node
        else:
            self.rear = new_node
        
        self.front = new_node
    
    def push_right(self, data):
        new_node = Node(data, prev=self.rear)
        
        if self.rear is not None:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node
    
    def pop_left(self):
        if self.front is None:
            return None
        
        pop_data = self.front.data
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None  
        return pop_data
    
    def pop_right(self):
        if self.rear is None:
            return None
        pop_data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is not None:
            self.rear.next = None
        else:
            self.front = None  
        return pop_data
    
    

my_deque = double_ended_queue()

my_deque.push_left('Left1')
my_deque.push_right('Right1')
my_deque.push_left('Left2')
my_deque.push_right('Right2')
my_deque.push_left('Left3')
my_deque.push_right('Right3')
my_deque.push_right('Right4')
my_deque.push_right('Right5')
my_deque.push_left('Left4')
my_deque.push_left('Left5')
print('Before pop left')
my_deque.print_structure()

print(f'\nAfter pop left')
my_deque.pop_left()
my_deque.print_structure()

print(f'\nAfter pop right')
my_deque.pop_right()
my_deque.print_structure()

print(f'\nAfter pop right')
my_deque.pop_right()
my_deque.print_structure()

print(f'\nAfter pop left')
my_deque.pop_left()
my_deque.print_structure()



