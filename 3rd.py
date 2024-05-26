class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
        

    def enqueue(self, value):
        if self.isFull():
            print("Circular queue is full. .")
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Circular queue is empty. Cannot dequeue.")
            return None
        removed_value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed_value

    def front(self):
        if self.isEmpty():
            print("Circular queue is empty.")
            return None
        return self.queue[self.front]

    def rear(self):
        if self.isEmpty():
            print("Circular queue is empty.")
            return None
        return self.queue[self.rear]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
       
        return (self.rear + 1) % self.size == self.front


if __name__ == "__main__":
    q = CircularQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Dequeued:", q.dequeue())  
    q.enqueue(4)
    print("Front:",q.front())  
    print("Rear:", q.rear())  
