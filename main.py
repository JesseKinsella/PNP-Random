import random #random module (a chunk of code)

print(random.randint(1, 10)) #between min, max inclusive

print(random.random()) #random float between 0,1

#method 1
magic_8_ball = ['Yes', 'No', 'Maybe']
print(random.choice(magic_8_ball))

#alt method
answer = random.randint(1,3)
if answer == 1:
  print("Yes")
if answer == 2:
  print("No")
if answer == 3:
  print("Maybe")