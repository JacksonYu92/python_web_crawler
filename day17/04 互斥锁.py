import threading
import time

lock = threading.Lock()



x = 100

def sub():
    # 加锁
    lock.acquire()
    global x
    temp = x -1
    time.sleep(0.001)
    x = temp
    # 释放锁
    lock.release()

# 串行版本
# for i in range(100):
#     sub()
# print(x)

# 并发版本
t_list = []
for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    t_list.append(t)

for i in t_list:
    t.join()

print(x)

