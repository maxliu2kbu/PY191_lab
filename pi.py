import random

def point():
    return (random.uniform(-1, 1), random.uniform(-1, 1))

def inside(x,y):
    return x**2 + y**2 <= 1

times = 10000000
count = 0
for i in range(times):
    if inside(*point()):
        count += 1

print(4 * count / times)