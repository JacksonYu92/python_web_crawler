import time
import threading

def foo(t):
    print("foo 开始")
    time.sleep(t)
    print("foo 结束")

def bar(t):
    print("bar 开始")
    time.sleep(t)
    print("bar 结束")

start = time.time()
# 串行任务
# foo()
# bar()

# 基于多线程的并发
# t1 = threading.Thread(target=foo, args=(2,))
# t1.start() # 调度线程对象
#
# t2 = threading.Thread(target=bar, args=(3,))
# t2.start() # 调度线程对象
#
# t1.join() # t1线程没有结束，阻塞
# t2.join()
t_list = []
for i in range(100):
    t = threading.Thread(target=foo, args=(2,))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print(f"耗时{time.time()-start}秒")