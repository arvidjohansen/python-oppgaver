
import random

#print(random.random()) #random float between 0.0 and 1.0
#print(random.randint(1,100)) #random int between a and b

candidates = ['Joe Biden', 'Donald Trump']


file = open('votes.txt','w')

for i in range(10000):
    file.write(random.choice(candidates) + '\n')

file.close()

