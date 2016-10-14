'''
print 'hello world!'


a = 1
if a ==1:
	print '1'
else:
	print '2'

while a == 'hellp':
	print 'hello'
else:
	print "not hello, its"

for i in xrange(1,10):
	print i
	if i==3:
		break
print i

#while i == 3:
#	s = raw_input('enter something:')
#	if s=='1':
#		break
#	if len(s)>2:
#		continue
#	print len(s)

def say():
	print "hello"

say()
def maxanb(a,b):
	if a>b:
		print "a>b",b
	else:
		print "a<b",a

def printMax(x, y):

	x = int(x) # convert to integers, if possible
	y = int(y)
	if x > y:
		print x, 'is maximum'
	else:
		print y, 'is maximum'

printMax(3, 5)
print printMax.__doc__

import sys
print "the some some"
for i in sys.argv:
	print i
print '\n\nThe PYTHONPATH is', sys.path, '\n'
if __name__ == '__main__':
	print "this program is being run by itself"
else:
	print 'I am being XXXXXX'

shoplist = ['apple', 'mango', 'carrot', 'banana']
for item in shoplist:
	print len(shoplist),item,len(item)
for item in shoplist[1]:
	print len(shoplist[1]),item,len(item),item.split()
shoplist.append("hello")
print shoplist[len(shoplist)-1]

class Person(object):
	"""docstring for Person"""
	def __init__(self,name):
		self.name = name
	def sayHi(self):
		print 'Hello,how are you?' , self.name
p = Person('lizhaojian')
p.sayHi()

class Person:
	population = 0
	def __init__(self,name):
		self.name = name
		print ('Initalizing %s') %self.name
		#when the person is created he/she
		#addto the population
		Person.population += 1
	def __del__(self):
		print '%s says bye'%self.name
		Person.population -= 1

		if Person.population == 0:
			print 'i am the only one left '
		else:
			print 'There are still %d people left'%Person.population

	def sayHi(self):
		print 'Hi my name is %s'%self.name
	def howMany(self):
		if Person.population == 1:
			print 'I am the only one left here'
		else:
			print 'We have %d person here'%Person.population

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('lizhaojian')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

'''

class choolMember:
	def __init__(self,name,age):
		self.name = name 
		self.age = age 
		print '(initialized Sc)'
