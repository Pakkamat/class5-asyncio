# ผลที่ได้จากการ Run

# Task A: Computing 0+1
# Time: 0.01
# Task B: Computing 0+1
# Time: 0.01
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.02
# Task B: Sum = 6

# Time: 3.01 sec

import asyncio
import time

# ใช้ฟังก์ชั่นของ async และใช้ฟังก์ชั่นการรอแบบ async ทำให้โปรแกรมเร็วขึ้น
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

# asyncio สร้างฟังก์ชั่นรับค่าตัวแปร 2 ตัว เป็นชื่อ และ เลข
# สร้างตัวแปรมาเก็บค่า คือ total
# ทำการบวกเลข เก็บในตัวแปร total โดยวนลูปจาก ตัวแปร numbers 
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    # Print ชื่อ Task, ผล Sum ที่ได้ (และ enter บรรทัด)
    print(f'Task {name}: Sum = {total}\n')

# สร้างฟังก์ชั่นมาทำการสร้างลิสโดยใช้ asyncio.gather 
async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))

# ทำการ Run ฟังก์ชั่น main(), จับเวลา, print เวลา
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')