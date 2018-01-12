import time
def producer():
    n = 1
    while True:
        print("生产了" + str(n))
        yield n
        n = n +1

def comsumer(p):
    while True:
        n = next(p)
        print("消费了" + str(n))
        # time.sleep(1)

p = producer()
comsumer(p)