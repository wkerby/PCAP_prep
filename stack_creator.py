#create a stack using OOP method
class Stack:
	def __init__(self):
		self.__stack_list = []
	def push(self,value):
		self.__stack_list.append(value) #can't pop anything unless something has been pushed
	def pop(self):
		value = self.__stack_list[-1]
		del self.__stack_list[-1]
		return value
class CountingStack(Stack):
	def __init__(self):
		Stack.__init__(self)
		self.push_count = 0
		self.pop_count = 0
	def push(self,value):
		self.push_count += 1
		Stack.push(self,value)
	def pop(self):
		self.pop_count += 1
		Stack.pop(self)
	def get_num_pops(self):
		return self.pop_count
	def get_num_pushes(self):
		return self.push_count

examplestack = CountingStack()
for i in range(5):
	examplestack.push(i)
	examplestack.pop()

#create a queue class that behaves in a FIFO manner
class Queue:
	def __init__(self):
		self.queue_list = []
	def put(self,value):
		return self.queue_list.append(value)
	def get(self):
		print(self.queue_list[0])
		return self.queue_list.pop(0)
		
#now test the class 
examplequeue = Queue()
for customer in ["Customer3","Customer4","Customer5","Customer6"]:
	examplequeue.put(customer)

for customer in list(range(len(examplequeue.queue_list)+1)):
	try:
		examplequeue.get()
	except IndexError:
		print("There are no longer any items in the queue.")

#now create a queue subclass that has true/false capabilities
class TrueQueue(Queue):
	def __init__(self):
		Queue.__init__(self)
	def isqueue(self):
		if len(self.queue_list) > 0:
			return True
		else:
			return False

exampletrue = TrueQueue()
for i in range(10):
	exampletrue.put("Customer " + str(i+1))

print(exampletrue.isqueue())

for customer in list(range(len(exampletrue.queue_list))):
	exampletrue.get()

print(exampletrue.isqueue())

#create a cat class
class Cat:
	def __init__(self,name,age,sex,furcolor,weight,lifespan = '15 years'):
		self.name = name
		self.age = age
		self.sex = sex
		self.furcolor = furcolor
		self.weight = weight
		self.lifespan = lifespan

buddy = Cat("Buddy",11,"M","Orange/White","13 lbs.")
print(buddy.__dict__)










	

