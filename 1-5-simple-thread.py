# ผลที่ได้จากการ Run

# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task B: Computing 1+2
# Task A: Computing 1+2
# Time: 1.01
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.02
# Task B: Sum = 6

# Time: 3.03 sec

import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor
# ใช้ฟังก์ชั่นของ async แต่ไปใช้ time.sleep ทำให้การทำงานต้องรอ โปรแกรมจึงช้า
# แต่ทำการใช้ฟังก์ชั่นของ ThreadPoolExecutor ทำให้เปลี่ยนจาก sync เป็น async เหมือนกันทำให้โปรแกรมเร็วขึ้น
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# asyncio สร้างฟังก์ชั่นรับค่าตัวแปร 2 ตัว เป็นชื่อ และ เลข
# สร้างตัวแปรมาเก็บค่า คือ total
# สร้างตัวแปร มาใช้ฟังก์ชั่นของ ThreadPoolExecutor
# ทำการบวกเลข เก็บในตัวแปร total โดยวนลูปจาก ตัวแปร numbers 
async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
    # Print ชื่อ Task, ผล Sum ที่ได้ (และ enter บรรทัด)
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
# asyncio สร้างฟังก์ชั่นมาเก็บค่า และสร้าง task ขึ้นมา แต่ยังไม่ให้รัน 
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
# ทำการรัน task และทำจนเสร็จ
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')