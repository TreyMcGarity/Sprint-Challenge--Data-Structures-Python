class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.index = 0 #needed to maintain position in list

    def append(self, item):
        # if size of storage is within capacity
        if len(self.storage) < self.capacity:
            # append value at end of current storage
            self.storage.append(item)
        else:
            # if index hits capacity (handles proper indexing)
            if self.index == self.capacity:
                # set index back to zero 
                self.index = 0
            # pop storage at index (to maintain rest of list order)
            self.storage.pop(self.index)
            # then insert value at index
            self.storage.insert(self.index, item)
            # increment index
            self.index += 1

    def get(self):
        return self.storage