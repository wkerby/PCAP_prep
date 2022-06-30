#create the triangle class
import sys
sys.path.append(r'Z:\Shared\Users\WKerby\\My Computer\Documents\Python')

import testmodule as t
import math as m
exampleobject = t.Point(0,3)
class Triangle():
	def __init__(self, vertice1, vertice2, vertice3):
		self.vertice1 = vertice1
		self.vertice2 = vertice2
		self.vertice3 = vertice3
		self.points = [vertice1,vertice2,vertice3]
	def perimeter(self):
		return round(m.sqrt((self.vertice1._Point__x - self.vertice2._Point__x)**2 + (self.vertice1._Point__y - self.vertice2._Point__y)**2) + m.sqrt((self.vertice2._Point__x - self.vertice3._Point__x)**2 + (self.vertice2._Point__y - self.vertice3._Point__y)**2) + m.sqrt((self.vertice1._Point__x - self.vertice3._Point__x)**2 + (self.vertice1._Point__y - self.vertice3._Point__y)**2),2)


triangle = Triangle(t.Point(),t.Point(0,3),t.Point(3,0))
print(triangle.vertice1._Point__y)
print(triangle.perimeter())

