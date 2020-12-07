import random
lines = open('raffle_nn.txt').read().splitlines()
win = random.choice(lines)
print("winner: " + win)
