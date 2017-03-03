#turtle 2.0
import turtle, math, random, time

seledyn = '#c1f0f0'
#turtle.bgcolor("red")
turtle.bgcolor(seledyn)

t = turtle.Turtle()
t.color("violet", "blue")

def sign1(size):
	turtle.speed(0.1)
	for x in range(10):
		for y in range(10):
			turtle.goto(x*size,y*size)
			turtle.goto(y*size, x*size)
			turtle.goto(x+y, x+y)
	
def sign2(size1, size2):
	turtle.speed(0.1)
	for x in range(15):
		for y in range(10):
			turtle.goto((x+y)*size1,(y+x)*size1)
			turtle.goto((x-y)*(size2), (y-x)*(size2))		
			#turtle.goto(x+y, x+y)
def sign3(size1, size2):
	turtle.speed(0.1)
	for x in range(10):
		for y in range(10):
			turtle.goto((x**2)*(y+size1),(y**2)*(x+size1))
			turtle.goto((x**2)*(size2-y), (y**2)*(size2-x))			
			
def sign4(size1, size2):
	turtle.speed(0.1)
	for x in range(15):
		for y in range(15):
			turtle.goto((math.sin(x))*y+size1, math.sin(y)*x*size1)
			turtle.goto(math.cos(x)*y*size2, math.cos(y)*x+size2)
					
def sign5(size1, size2):
	turtle.speed(0.1)
	for x in range(15):
		for y in range(15):
			turtle.goto((math.sin(x))*y+size1, math.sin(y)*x*size1)
			turtle.goto(math.cos(x)*y*size2, math.cos(y)*x+size2)
			
def sign6(dist1,dist2):
	turtle.speed(0.1)
	turtle.bgcolor("black")
	t.color('white', 'green')
	#t.begin_fill()
	for x in range(dist1):
		for y in range(dist2):
			t.forward(x**1.1)
			t.right(y**0.98)
			
def sign7(dist1,dist2):
	turtle.speed(0.1)
	turtle.bgcolor("black")
	t.color('white', 'green')
	#t.begin_fill()
	time.sleep(2)
	for x in range(dist1):
		for y in range(dist2):
			t.forward(x**1.1)
			t.right(y**0.98)	
			
def sign8(dist1,dist2):
	turtle.speed(0.1)
	turtle.bgcolor("black")
	t.color('white', 'green')
	#t.begin_fill()
	for x in range(dist1):
		for y in range(dist2):
			direction = random.randrange(-10,10)
			t.forward(x**1.1)
			t.right(y*direction)
			
def sign9(dist1,dist2):
	turtle.speed(0.1)
	turtle.bgcolor("black")
	t.color('white', 'green')
	#t.begin_fill()
	for x in range(dist1):
		for y in range(dist2):
			xpos = random.randrange(-10*(x+1),10)
			ypos = random.randrange(-5*(y+1),5)
			t.goto(xpos, -2**ypos)

			
#uncommend some section and run the program!				
#sign1(20)
#sign1(-20)

#sign2(10, 20)
#sign2(-10, -20)

#sign3(1, 1)
#sign3(0.1, 0.1)

#sign4(15,15)
#sign4(15,-15)

sign7(20,20)

#sign7(20,30)

'''
for x in range(5,10):
	#turtle.bgcolor("red")
	turtle.bgcolor(seledyn)
	sign4(x*4,x*4)
	#sign2(x*2,x*2)
'''
