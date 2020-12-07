import random

class Ticket:

    lLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ti = []
    name = ""
    entries = 0

def Main():

    t = Ticket()
    t.name = input("Character Name: ")
    t.entries = int(input("# of Entries: "))

    for i in range (t.entries):
        for i in range(6):
            lorn = random.choice(range(1,3))
            if lorn == 1:
                t.ti += random.choice(t.numbers)
            if lorn == 2:
                t.ti += random.choice(t.lLetters)
            t.ti = ''.join(t.ti)

        with open("raffle_nn.txt", "a") as f:
            if f.ti not in "raffle_nn.txt":
                f.write(t.ti + " | " + t.name + "\n")
                t.ti = []
            else:
                print("Duplicate Found")

if __name__ == '__main__':
    Main()
