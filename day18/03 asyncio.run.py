import asyncio
import time

async def foo(i):
    print(f"任务{i}启动")
    await asyncio.sleep(i)
    print(f"任务{i} {i}秒结束")
    return i * i

# def callback(obj):
#     print(obj.result())

async def main():

    # 构建任务对象列表
    tasks = [
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    ]

    # 方式1
    # tasks[0].add_done_callback(lambda ret: print(ret.result()))
    #
    # await asyncio.wait(tasks)
    #
    # for task in tasks:
    #     print(task.done(), task.result())

    # 方式2
    rets = await asyncio.gather(*tasks)
    print(rets)

# 简写
start = time.time()
asyncio.run(main())
print("cost timer:", time.time() - start)

