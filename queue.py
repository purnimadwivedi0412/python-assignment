class Queue:
    def __init__(self):
        self.queue = [] 
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        return self.queue.pop(0)

    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        print("Queue:", self.queue)



q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element (peek):", q.peek())

print("Dequeued element:", q.dequeue())

q.display()