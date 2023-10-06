import multiprocessing
# multiprocessing.Process拥有和threading.Thread()同样的API

import time

def foo(t):
    print(f"任务{t} 开始")
    time.sleep(t)
    print(f"任务{t} 结束")

if __name__ == '__main__':
    start = time.time()

    t_list = []
    for i in range(1,6):
        t = multiprocessing.Process(target=foo, args=(i,))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    print(f"耗时{time.time()-start}秒")
