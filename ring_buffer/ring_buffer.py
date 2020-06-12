class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.counter = 0
    def append(self, item):
        
        if len(self.data) == self.capacity:
            self.data.pop(self.counter%self.capacity)
            self.data.insert(self.counter%self.capacity,item)
            self.counter += 1
        else:
            self.data.append(item)

    def get(self):
        return self.data

'''
buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.append('d')
buffer.append('e')
buffer.append('f')

buffer.append('h')
buffer.get()
'''