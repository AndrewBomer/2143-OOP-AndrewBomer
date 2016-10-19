### Andrew Bomer

### Answer 1
-----

johns_bag = Bag()
johns_bag.print_bag()
# []

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# ['blue', 'red', 'green', 'red']

s = johns_bag.take_skittle()
print(s.color)
# blue

print(johns_bag.number_sold)
# 1

print(Bag.number_sold)
# 1

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# ['red', 'green', 'red']

print(Bag.number_sold)
# 2

print(soumyas_bag.number_sold)
# 2
-----

### Answer 2
-----
def take_color(self, color):
    	self.color = color
    	if color in self.skittles:
    		self.skittles.remove(color)
    		return self.skittles
    	else:
    		return None

-----

### Answer 3
-----
def take_all(self):
    	for i in self.skittles:
    		print ("%s"%(i))
-----

