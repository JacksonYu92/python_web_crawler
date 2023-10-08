import asyncio
import time

async def task(i):
    print(f"任务{i}启动")
    await asyncio.sleep(i)
    print(f"任务{i}结束")

start = time.time()

# 创建事件循环对象
loop = asyncio.get_event_loop()
# 构建协程任务列表
tasks = [task(1), task(2), task(3)] # task(1):协程对象  coroutine object
print(tasks[0])
# 启动运行
loop.run_until_complete(asyncio.wait(tasks)) # 阻塞等待所有的协程结束

print("cost timer:", time.time() - start)