### Andrew Bomer
-----
### Question 1
-----
```
class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		Pet.__init__(self, name, owner)
		self.lives = lives
	def talk(self):
		print('meow!')
	def lose_life(self):
		if (self.lives > 0):
			self.live = (self.lives - 1)
			if (self.lives == 0):
				self.is_alive = False
```
-----

### Question 2
-----

```
f = Foo(4)
b = Bar(3)
print(f.a)
# prints 4

print(b.a)
# prints 3

print(f.garply())
# Errors

print(b.garply())
# prints 3

b.a = 9
print(b.garply())
# prints 9

f.baz = lambda val: val * val
print(f.garply())
# prints 16
```
