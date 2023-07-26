# ผลที่ได้จากการ Run

# Wed Jul 26 14:44:59 2023 hello 1 started
# Wed Jul 26 14:44:59 2023 hello 2 started
# Wed Jul 26 14:45:03 2023 hello 1 done
# Wed Jul 26 14:45:03 2023 hello 2 done
# Time: 4.01 sec

import asyncio
import time
# สร้างฟังก์ชั่น hello ขึ้นมาเพื่อ Print วัน เดือน ปี เวลา
# Start รอ และ done
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# สร้างฟังก์ชั่น main สร้าง task 1, task2 และ ให้ทำงานพร้อมกัน
async def main():
    task1 = asyncio.create_task(hello(1)) # returns immediately, the task is created 
    # await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

# ทำการ Run ฟังก์ชั่น main(), จับเวลา, print เวลา
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')