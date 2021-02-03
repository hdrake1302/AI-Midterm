class Queue:
    """Represent a queue"""
    def __init__(self):
        self.st = []

    def enqueue(self, el):
        """add element to the end of the queue"""
        self.st.append(el)

    def dequeue(self):
        """pop first element out of the queue"""
        return self.st.pop(0)

    def front(self):
        """return first element of the queue"""
        return self.st[0]

    def rear(self):
        """return last element of the queue"""
        return self.st[-1]

    def size(self):
        """return size of the queue"""
        return len(self.st)

    def empty(self):
        """return true if the queue is empty else false"""
        return len(self.st) == 0


