# ผลที่ได้จากการ Run 

# Computing factorial(2), currently i=2...
# Computing factorial(3), currently i=2...
# Computing factorial(4), currently i=2...
# Computing factorial(3), currently i=3...
# Computing factorial(4), currently i=3...
# Computing factorial(4), currently i=4...
# [2, 6, 24]
# Time: 3.04 sec

import asyncio
import time 

# สร้างฟังก์ชั่น factorial เพื่อการคำนวน  factorial โดยการวนลูป
# และ Print ค่าออกมา
async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i

    return f

# เริ่มฟังก์ชั่น factorial ทั้ง 3 ค่าแบบพร้อมกัน 
# แต่ที่โปร 2 ออกมาช้า เพราะว่า asyncio.gather ต้องรอให้วนครบก่อนถึงจะ return ค่า L ออกมา
async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L) # [2, 6, 24]

if __name__ =='__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')