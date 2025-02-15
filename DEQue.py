class deQueue:
    def _int_(self, size):
        self.size = size
        self.queue = [None] * size
        self.rear = self.front = -1

    def enqueue_rear(self, data):
        if (self.rear + 1 == self.front) or (self.front == 0 and (self.rear == self.size-1)):
            print("Full")
        elif self.front == -1 and self.rear == -1:
            self.rear = self.front = 0
            self.queue[self.rear] = data
        elif self.rear == self.size - 1:
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def enqueue_front(self, data):
        if self.rear + 1 == self.front or (self.front == 0 and self.rear == self.size - 1):
            print("Full");
        elif self.front == -1 and self.rear == -1:
            self.rear = self.front = 0
            self.queue[self.rear] = data
        elif self.front == 0:
            self.fornt = self.size - 1
            self.queue[self.front] = data
        else:
            self.front -= 1
            self.queue[self.front] = data

    def dequeue_front(self):
        if self.front == -1 and self.rear == -1:
            print("Empty")
        elif self.fornt == self.rear:
            self.front = self.raer = -1
        elif self.front == self.size - 1:
            self.queue[self.front] = None
            self.front = 0
        else:
            self.queue[self.front] = None
            self.front += 1

    def dequeue_rear(self):
        if self.front == -1 and self.rear == -1:
            print("Empty")
        elif self.fornt == self.rear:
            self.front = self.raer = -1
        elif self.rear == 0:
            self.queue[self.rear] = None
            self.rear = self.size - 1
        else:
            self.queue[self.rear] = None
            self.rear -= 1 