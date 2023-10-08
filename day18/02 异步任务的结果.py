import asyncio
import time

async def foo(i):
    print(f"任务{i}启动")
    await asyncio.sleep(i)
    print(f"任务{i} {i}秒结束")
    return i * i

def task2callback(ret):
    print("异步任务2的结果：", ret.result())

start = time.time()

# 创建事件循环对象
loop = asyncio.get_event_loop()
# 构建任务对象列表
tasks = [
    asyncio.ensure_future(foo(1)),
    asyncio.ensure_future(foo(2)),
    asyncio.ensure_future(foo(3)),
] # foo(1):asyncio.Task
tasks[1].add_done_callback(task2callback)

# 启动运行
loop.run_until_complete(asyncio.wait(tasks)) # 阻塞等待所有的协程结束
# print(tasks[0])
# print(tasks[0].done())
# print(tasks[0].result())
for task in tasks:
    print(task.done(), task.result())
print("cost timer:", time.time() - start)