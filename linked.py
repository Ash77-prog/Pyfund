class Node:
    def __init__(self,element):
        self.element= element
        self.next= None


    class Stack:
        def __init__(self):
            self.head = None
        
        def is_empty(self, size):
            return self.size == 0


        def push(self,element):
            if self.head = None :
                self.head = Node(element)
            else:
                new_node = Node(element)
                new_node.next = self.head
                self.head = new_node

         def peek(self, element):
        if self.is_empty:
            raise Exception("Empty stack")
        else:
            return self.head.element

        def pop(self):
            if self.head = None:
                return None
            else:
                popped = self.head.element
                self.head = self.head.next
                return popped

lstack = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        lstack.push(int(do[1]))
    elif operation == 'pop':
        popped = lstack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break


