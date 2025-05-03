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
