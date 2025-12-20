#!/usr/bin/env python3
import sys
import math


def main() -> None:
    """座標間距離計算"""

    print("=== Game Coordinate System ===")
    print()

    ac = len(sys.argv)
    zero_position = (0, 0, 0)

    # 1.Demo-mode
    # 1-1.argv == "10.20.5"
    str_list = "10,20,5"
    # 1-2.","でsplitしてtupleの各要素に分ける
    position = tuple(int(s) for s in str_list.split(","))
    print(f"Position created: {position}")
    # 1-3.positioをx, y, zの変数に分ける
    x1, y1, z1 = position
    x2, y2, z2 = zero_position
    # 1-4.distanceを計算
    distance = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    print(f"Distance between {zero_position} and {position}: {distance:.2f}\n")

    # 2.parsing_argv
    try:
        if 1 < ac:
            str_list = sys.argv[1]
            print(f'Parsing coordinates: "{str_list}"')
            position = tuple(int(s) for s in str_list.split(","))
            print(f"Parsed position: {position}")
            x1, y1, z1 = position
            x2, y2, z2 = zero_position
            distance = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
            print(
                f"Distance between {zero_position} "
                f"and {position}: {distance:.2f}\n"
                )
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    # 3.invaild_cordinates
    try:
        str_list = "abc,def,ghi"
        print(f'Parsing invalid coordinates: "{str_list}"')
        position = tuple(int(s) for s in str_list.split(","))
        print(f"Parsed position: {position}")
        x1, y1, z1 = position
        x2, y2, z2 = zero_position
        distance = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
        print(
            f"Distance between {zero_position} "
            f"and {position}: {distance:.2f}\n"
            )
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    # 4.Unpacking demonstration:????
    print("\nUnpacking demonstration:")
    position = (3, 4, 0)
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
