import asyncio
import time
# สร้างฟังก์ชั่น hello ขึ้นมาเพื่อ Print วัน เดือน ปี เวลา
# Start รอ และ done
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# สร้างฟังก์ชั่น main สร้าง task 1, task2 ให้ทำงานพร้อมกัน โดยใช้ syncio.gather จะได้ไม่ต้องใช้หลายบรรทัด
async def main():
    task1 = asyncio.create_task(hello(1)) # returns immediately, the task is created 
    # await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1,task2)

# ทำการ Run ฟังก์ชั่น main(), จับเวลา, print เวลา
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')