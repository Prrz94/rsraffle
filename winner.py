import random
with open('raffle_nn.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('raffle_shuffled.txt','w') as target:
    for _, line in data:
        target.write( line )
lines = open('raffle_shuffled.txt').read().splitlines()
win = random.choice(lines)
print("winner: " + win)
