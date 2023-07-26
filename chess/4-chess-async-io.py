import asyncio
import time

my_compute_time = 1
opponent_compute_time = 0
opponents = 1
move_pairs = 1


# Again notice that I declare the main() function as a async function
async def main(x):
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # Don't use time.sleep in a async function. I'm using it because in reality you aren't thinking about making a
        # move on 24 boards at the same time, and so I need to block the event loop.
        time.sleep(my_compute_time)
        print(f"Waiting on opponent on board {x}.")
        # Here our opponent is making their turn and now we can move onto the next board.
        await asyncio.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


async def async_io():
    # Again same structure as in async-io.py
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")
    # คูณ 5 เดินเลย ไม่ต้องรอ Client เลยไม่ต้องนำ 55 วิมาคิด
    # คูณ 24 คือ จำนวนกระดาน
    # คูณ 30 คือ จำนวนการเดิน
    # นำมาหาร 3600 เพราะ จะให้คิดเป็นชั่วโมง
    print(f"เสร็จที่เวลา {(round(time.perf_counter() - start_time) *5 *24 *30)/3600} ชั่วโมง")