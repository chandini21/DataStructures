class Node:
    
    # default constructor
    def __init__(self):
        self.data = None
        self.next = None
    
    # method to set value to node 
    def set_data(self, data):
        self.data = data
    
    # method to get value of node 
    def get_data(self):
        return self.data
        
    # method to set next node of the present node    
    def set_next(self, next):
        self.next = next
        
    # method to get next node of the current node
    def get_next(self):
        return self.next
        
    # check if the node has next node
    def has_next(self):
        # if get_next(self) is None:
            # return False
        # return True
        return self.next != None
