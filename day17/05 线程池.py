import time
from concurrent.futures import ThreadPoolExecutor

def task(i):
    print(f'任务{i}开始！')
    time.sleep(i)
    print(f'任务{i}结束！')
    return i

start = time.time()
pool = ThreadPoolExecutor(3)
# pool.submit(task,1) # 1s
# pool.submit(task,2) # 2s
# pool.submit(task,3) # 3s

future_list = []
for i in range(1, 4):

    # （1）串行
    # print(task(i))

    # （2）线程池技术异步实现，完成并发
    future = pool.submit(task, i) # future对象
    future_list.append(future)
    # future.done()  # 返回布尔值
    # future.result() # 1



pool.shutdown() # 阻塞
print(f"耗时{time.time() - start}秒")
print(future_list)
print([future.result() for future in future_list])