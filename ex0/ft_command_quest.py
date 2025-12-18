#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")

    ac = len(sys.argv)
    # 1.No_argments
    if ac == 1:
        print("No arguments provided!")

    # 2.put_program_name
    print(f"Program name: {sys.argv[0]}")

    # 3.put_argments
    if 1 < ac:
        count = 1
        print(f"Arguments received: {ac - 1}")
        for av in sys.argv[1:]:
            print(f"Argument {count}: {av}")
            count += 1

    # 4.Total_argmets
    print(f"Total arguments: {ac}")


if __name__ == "__main__":
    main()
