# ผลที่ได้จากการ Run 

# Wed Jul 26 15:01:06 2023 hello 0 started
# Wed Jul 26 15:01:06 2023 hello 1 started
# Wed Jul 26 15:01:06 2023 hello 2 started
# Wed Jul 26 15:01:06 2023 hello 3 started
# Wed Jul 26 15:01:06 2023 hello 4 started
# Wed Jul 26 15:01:06 2023 hello 5 started
# Wed Jul 26 15:01:06 2023 hello 6 started
# Wed Jul 26 15:01:06 2023 hello 7 started
# Wed Jul 26 15:01:06 2023 hello 8 started
# Wed Jul 26 15:01:06 2023 hello 9 started
# Wed Jul 26 15:01:10 2023 hello 0 done
# Wed Jul 26 15:01:10 2023 hello 2 done
# Wed Jul 26 15:01:10 2023 hello 6 done
# Wed Jul 26 15:01:10 2023 hello 5 done
# Wed Jul 26 15:01:10 2023 hello 8 done
# Wed Jul 26 15:01:10 2023 hello 7 done
# Wed Jul 26 15:01:10 2023 hello 1 done
# Wed Jul 26 15:01:10 2023 hello 3 done
# Wed Jul 26 15:01:10 2023 hello 4 done
# Wed Jul 26 15:01:10 2023 hello 9 done
# Time: 4.01 sec

import asyncio
import time
# สร้างฟังก์ชั่น hello ขึ้นมาเพื่อ Print วัน เดือน ปี เวลา
# Start รอ และ done
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# สร้างฟังก์ชั่น main
# สร้างตัวแปร coros ให้วนค่า hello 0-9 และ ให้ทำงานพร้อมกัน โดยใช้ syncio.gather จะได้ไม่ต้องใช้หลายบรรทัด
async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

# ทำการ Run ฟังก์ชั่น main(), จับเวลา, print เวลา
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')