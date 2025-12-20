#!/usr/bin/env python3
import random
import time


def game_event_generater(num_event: int) -> object:
    """ランダムでイベントを生成"""

    # 1.イベントデータ
    names = ["alice", "bob", "charlie", "dave"]
    actions = ["killed monster", " found treasure", "leveled up", "died"]

    # 2.イベントの作成と出力
    for i in range(1, num_event + 1):
        # 3.イベントデータからランダムに抽出
        name = random.choice(names)
        level = random.randint(1, 20)
        action = random.choice(actions)

        # 4.文字列を組み立てる
        event = (f"Event {i}: Player {name} (level {level}) {action}")

        # 5.一つだけ返す
        yield event


def put_fibonacci(num: int) -> object:
    """gen_fibonacci"""

    a = 0
    b = 1
    for _ in range(num):
        yield a
        a, b = b, a + b


def put_prime(num: int) -> object:
    """gen_prime"""

    count = 0
    i = 2
    while count < num:
        i_i = 2
        while i % i_i:
            i_i += 1
        if i == i_i:
            yield i
            count += 1
        i += 1


def main() -> None:
    """ゲームイベントDEMO"""

    print("=== Game Data Stream Processor ===\n")

    # 集計用変数の初期化
    num_event = 1000
    total_events = 0
    tresure_events = 0
    level_up_events = 0
    high_level_count = 0

    # 1.指定した数のイベントを"都度"出力
    start_time = time.time()
    print(f"Processing {num_event} game events...")
    for event in game_event_generater(num_event):
        # 1-1.受け取って出力
        print(event)

        # 1-2.文字列から集計
        total_events += 1

        # 1-3.found_treasureの集計
        if "found treasure" in event:
            tresure_events += 1

        # 1-2.leveled upの集計
        if "leveled up" in event:
            level_up_events += 1

        # 1-3.hige-level-playerの集計
        if "level " in event:
            parts = event.split("(level ")
            if 1 < len(parts):
                level_part = parts[1].split(")")[0]
                if 10 <= int(level_part):
                    high_level_count += 1
    end_time = time.time()
    print()

    # 2.Analytics
    print("=== Stream Analytics ===\n"
          f"Total events processed: {num_event}\n"
          f"High-level players (10+): {high_level_count}\n"
          f"Treasure events: {tresure_events}\n"
          f"Level-up events: {level_up_events}\n"
          )

    event = game_event_generater(1)
    if type(event).__name__ == "generator":
        mem_str = "Constant (streaming)"
    else:
        mem_str = "Linear (all loaded)"
    print(f"Memory usage: {mem_str}\n"
          f"Processing time: {end_time - start_time:.3f} seconds\n")

    # 3.=== Generator Demonstration ===
    print("=== Generator Demonstration ===")

    # 3-3.フィボナッチ配列
    num = 10
    print(f"Fibonacci sequence (first {num}): ", end="")
    count = 0
    for i in put_fibonacci(num):
        count += 1
        print(f"{i}", end="")
        if count < num:
            print(", ", end="")
    print()

    # 3-4.素数
    num = 5
    print(f"Prime numbers (first {num}): ", end="")
    count = 0
    for i in put_prime(num):
        count += 1
        print(f"{i}", end="")
        if count < num:
            print(", ", end="")
    print()


if __name__ == "__main__":
    main()
