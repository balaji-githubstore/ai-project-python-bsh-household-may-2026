"""understanding async await methods in python"""
import asyncio



async def m1():
    print("start")
    for i in range(1,11):
        print(i)
        await asyncio.sleep(1)
    print("End")
    return "code done"

async def m1_run():
    # will run the async method in the background
    call_mtd=asyncio.create_task(m1())
    await asyncio.sleep(5)
    print("do another activity 1")
    print("do another activity 2")
    print("do another activity 3")
    print("do another activity 4")

    result=await call_mtd
    print(result)




# await for m1() to complete and then return
# result=asyncio.run(m1())

# print(result)

asyncio.run(m1_run())
