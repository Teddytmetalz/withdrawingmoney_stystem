#Creating a class of the clients in the Queue.
class Queue:
		def __init__(self):
			self.items = []
		
		def isEmpty(self):
			return self.items == []
		
		def enqueue(self, item):
			self.items.insert(0,item)
			
		def dequeue(self):
			return self.items.pop()
		
		def size(self):
			return len(self.items)
		
		def peek(self):
			return self.items[len(self.items)-1]
#The part of the code will have the names in the loop fiiling up the q=Queue() , hence the name is filled in the empty parentheses.
q=Queue()
q.enqueue("Teddy")
q.enqueue("Peter")
q.enqueue("Andy")
q.enqueue("Camilla")
q.enqueue("Eugene")
q.enqueue("Tyno")

start = time.time()
#A "for loop" in most, if not all, programming languages is a mechanism to run a piece of code more than once. This is as below:
for i in range(6):
	
	time.sleep(5.0)
	print("person on queue", q.dequeue ())
	end = time.time()
	print(end - start)
#When the queue is empty then 	
if q.isEmpty():
	for i in range (1):
		s = str(input("ATM FREE \n"))
 elif if q.isActive():
    s = str(input("CHECK SUFFICIENT FUNDS \n"))
		s = str(input("CHECK NETWORK AVILABILITY \n"))
		s = str(input("CHECK TECHNICAL FAULTS \n"))
		q.enqueue(s)
