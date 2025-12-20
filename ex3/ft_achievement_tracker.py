#!/usr/bin/env python3

def main() -> None:
    """アチーブメント管理システム"""

    print("=== Achievement Tracker System ===")
    print()

    # 1.gen_achievement
    alice = set(('first_kill', 'level_10', 'treasure_hunter', 'speed_demon'))
    bob = set(('first_kill', 'level_10', 'boss_slayer', 'collector'))
    charlie = set((
        'level_10', 'treasure_hunter',
        'boss_slayer', 'speed_demon',
        'perfectionist'
        ))
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()

    # 2.=== Achievement Analytics ===
    print("=== Achievement Analytics ===")
    all_achievements = alice.union(bob, charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print()

    # 3.put_common
    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    rare = ((alice - bob - charlie) |
            (bob - alice - charlie) |
            (charlie - alice - bob)
            )
    print(f"Rare achievements (1 player): {rare}")
    print()

    # 4.vs
    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    main()
