# 1-1-simple-sync.py
# โปรแกรมทำงานอย่างไร

# ผลที่ได้จากการ Run

# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.01
# Task B: Computing 1+2
# Time: 3.03
# Task B: Computing 3+3
# Time: 4.03
# Task B: Sum = 6

# Time: 5.04 sec

import time

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# สร้างฟังก์ชั่นรับค่าตัวแปร 2 ตัว เป็นชื่อ และ เลข 
# สร้างตัวแปรมาเก็บค่า คือ total
# ทำการบวกเลข เก็บในตัวแปร total โดยวนลูปจาก ตัวแปร numbers 

def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    # Print ชื่อ Task, ผล Sum ที่ได้ (และ enter บรรทัด)
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
# สร้างตัวแปรลิส กำหนดค่าและใช้ฟังก์ชั่น sum() 
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3]),
]
end = time.time()
print(f'Time: {end-start:.2f} sec')