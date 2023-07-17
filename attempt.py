import random

print "Content-Type: text/plain"
print 

value = 1883
valid = False
while valid == False: 
  random_num = value * random.randint(1, 999999)
  if len(str(random_num)) >= 5 or len(str(random_num)) <= 8:
    valid = True
print "Random value is " + str(random_num);
