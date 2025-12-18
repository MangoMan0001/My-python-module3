#!/usr/bin/env python3
import sys
import math


def main() -> None:
    print("=== Game Coordinate System ===")
    ac = len(sys.argv)
    zero_position = (0, 0, 0)

    # 1.Demo-mode
    str_list = "10,20,5"
    position = tuple(int(s) for s in str_list.split(","))
    print(f"Position created: {position}")
    x1, y1, z1 = position
    x2, y2, z2 = zero_position
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

    # 3.invaild_cordinates
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





if __name__ == "__main__":
    main()
