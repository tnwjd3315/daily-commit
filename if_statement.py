# Control flow tools

# if statement
x = int(input("Please enter an integer: "))
if x < 0:
  x=0
  print("Negative changed to zero")
elif x == 0:
  print("Zero")
elif x == 1:
  print("Single")
else:
  print("More")

# for statement
# measure some strings
words = ['cat', 'window', 'defenestrate']
for word in words:
  print(word, len(word))

# sample collection
users = {'Hans':'active', 'Elena':'inactive','Sujeong':'active'}

# difficult to edit the collection -> either copy or create new collection
# stategy1: iterate over a copy
for user, status in users.copy().items():
  if status == 'inactive':
    del users[user]

# strategy2: create a new collection
active_users={}
for user, status in users.items():
  if status == 'active':
    active_users[user] = status

# range function
for i in range(5):
  print(i)

list(range(5,10))
list(range(0,10,3))
list(range(-10,-100,-30))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# instead, enumerate()

sum(range(4)) #0+1+2+3

# break and continue statement
for n in range(2,10):
  for x in range(2,n):
    if n % x==0:
      print(f"{n} equals {x} * {n//x}")
      break

for n in range(2,10):
  if n % 2 == 0:
    print(f"Found an even number {n}")
    continue
  print(f"Found an odd number {n}")

# break + else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# pass statement - functions nothing
while True:
   pass

# used for minimum functioned class
class MyEmptyClass:
   pass

def initlog(*args):
   pass

# match statement
def http_error(status):
   match status:
      case 400:
         return "Bad requiest"
      case 404:
         return "Not found"
      case 418:
         return "I'm a teapot"
      
      case 401 | 403 | 404:
         return "Not allowed"
      
      case _: # wildcard and never fails to match
         return "Something's wrong with the internet"
      
# point is an (x, y) tuple
def patterns(point):
  match point:
      case (0, 0):
          print("Origin")
      case (0, y):
          print(f"Y={y}")
      case (x, 0):
          print(f"X={x}")
      case (x, y):
          print(f"X={x}, Y={y}")
      case _:
          raise ValueError("Not a point")
     
# use classes to structure the data
class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y

def where_is(point):
   match point:
      case Point(x=0, y=0):
          print("Origin")
      case Point(x=0, y=y):
          print(f"Y={y}")
      case Point(x=x, y=0):
          print(f"X={x}")
      case Point():
          print("Somewhere else")
      case _:
          print("Not a point")
      
Point(1, 2)
Point(1, y=2)
Point(x=1, y=2)
Point(y=2, x=1)

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")