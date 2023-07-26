import time

my_compute_time = 1
opponent_compute_time = 1
opponents = 1
move_pairs = 1


def main(x):
    # Loops 30 times to simulate both players making a move
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        # The opponent thinks for 5 seconds.
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    for j in range(opponents):
        main(j)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")
    # นำเวลามาคูณ 60 วินาที เพราะ เราเดิน 5 วิ + อีกฝั่ง 55 วิ เป็น 60 วินาที
    # (จริง ๆ ต้องเป็น 5*55 แต่เพื่อให้เลขดู สวย เลขนำมาคูณ 60 แล้วไป หาร 2 ทีหลัง)
    # คูณ 24 คือ จำนวนกระดาน
    # คูณ 30 คือ จำนวนการเดิน
    # นำมาหาร 3600 เพราะ จะให้คิดเป็นชั่วโมง
    print(f"เสร็จที่เวลา {(round(time.perf_counter() - start_time) *60 *24 *30)/7200} ชั่วโมง")