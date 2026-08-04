import random

# ใช้ัวพิมพ์ใหPjมักใช้กับค่าคงที่ constant
HEADS = 1
TAILS = 2
TOSSESS = 10

def tosses_coin():
    for toss in range(TOSSESS):
        if random.randint(HEADS,TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')


tosses_coin()