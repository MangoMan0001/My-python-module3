#!/usr/bin/env python3

def main() -> None:
    print("=== Player Inventory System ===\n")

    # 1.インベントリ作成
    alice = {
        "info": {
            "golds": 950,
            "total_amount": 7,
        },
        "sword": {
            "Name": "sword",
            "Rarity": "rare",
            "Type": "weapon",
            "Gold": 500,
            "Amount": 1
        },
        "potion": {
            "Name": "potion",
            "Rarity": "common",
            "Type": "consumable",
            "Gold": 50,
            "Amount": 5
        },
        "shield": {
            "Name": "shield",
            "Rarity": "uncommon",
            "Type": "armor",
            "Gold": 200,
            "Amount": 1
        }
    }
    bob = {
        "info": {
            "golds": 100,
            "total_amount": 1,
        },
        "magic_ring": {
            "Name": "magic_ring",
            "Rariry": "rare",
            "Type": "magic",
            "Gold": 100,
            "Amount": 1
        }
    }

    # 2.<アリス> アイテムごとのゴールド計算
    print("=== Alice's Inventory ===")
    for data in alice.values():
        try:
            name = data["Name"]
            rarity = data["Rarity"]
            type = data["Type"]
            gold = data["Gold"]
            amount = data["Amount"]

            golds = gold * amount
            print(f'{name} ({type}, {rarity}): '
                  f'{amount}x @ {gold} gold each = {golds} gold'
                  )
        except KeyError:
            continue
    print()

    # 3.<アリス> 総ゴールド、総アイテム数計算
    golds = 0
    amount = 0
    weapon = 0
    consumble = 0
    armor = 0
    for data in alice.values():
        try:
            golds += data["Gold"] * data["Amount"]
            amount += data["Amount"]
            if data["Type"] == "weapon":
                weapon += data["Amount"]
            if data["Type"] == "consumable":
                consumble += data["Amount"]
            if data["Type"] == "armor":
                armor += data["Amount"]
        except KeyError:
            continue
    alice["info"]["golds"] = golds
    print(f'Inventory value: {alice["info"]["golds"]} gold')
    print(f"Item count: {amount} items")
    print(f"Categories: weapon({weapon}), "
          f"consumable({consumble}), armor({armor})"
          )

    # 4.AliceからBobにポーションを渡す
    print("=== Transaction: Alice gives Bob 2 potions ===")
    alice["potion"]["Amount"] -= 2
    alice["info"]["golds"] = \
        alice["potion"]["Gold"] * alice["potion"]["Amount"]
    bob.update(alice["potion"])
    bob["potion"]["Amount"] += 2
    bob["golds"] = bob["potion"]["gold"] * bob["potion"]["amount"]
    print("Transaction successful!")
    print()

    # 5.改めてポーション数を出力
    print("=== Updated Inventories ===")
    print(f'Alice potions: {alice["Potion"].get("Amount")}')
    print(f'Bob potions: {bob["Potion"].get("Amount")}')
    print()

    # 6.=== Inventory Analytics ===
    print("=== Inventory Analytics ===")
    players = {"Alice": alice, "Bob": bob}
    rare_item = set()
    gold_champion = "Alice"
    for player_name, inventry in players.items():
        if players[gold_champion].get(gold) < inventry["gold"]:
            champion = player_name
        for item_name, item_data in inventry.items():
            if item_data["Rarity"] == "rare":
                rare_item += item_name
    print(f"Most valuable player: "
          f'{champion} ({players[gold_champion].get("gold")} gold)')


if __name__ == "__main__":
    main()
