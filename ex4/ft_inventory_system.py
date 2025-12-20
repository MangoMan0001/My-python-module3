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
            "Rarity": "rare",
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
    print()

    # 4.AliceからBobにポーションを渡す
    print("=== Transaction: Alice gives Bob 2 potions ===")
    alice["potion"]["Amount"] -= 2
    alice["info"]["golds"] -= \
        alice["potion"]["Gold"] * 2
    alice["info"]["total_amount"] -= 2
    bob["potion"] = alice["potion"].copy()
    bob["potion"]["Amount"] = 2
    bob["info"]["golds"] = bob["potion"]["Gold"] * bob["potion"]["Amount"]
    print("Transaction successful!")
    print()

    # 5.改めてポーション数を出力
    print("=== Updated Inventories ===")
    print(f'Alice potions: {alice["potion"].get("Amount")}')
    print(f'Bob potions: {bob["potion"].get("Amount")}')
    print()

    # 6.=== Inventory Analytics ===
    print("=== Inventory Analytics ===")
    players = {"Alice": alice, "Bob": bob}
    rare_item = set()
    gold_champion = "Alice"
    amount_champion = "Alice"
    for player_name, inventry in players.items():
        if players[gold_champion]["info"]["golds"] < inventry["info"]["golds"]:
            gold_champion = player_name
        if players[amount_champion]["info"]["total_amount"] < \
                inventry["info"]["total_amount"]:
            amount_champion = player_name
        for item_name, item_data in inventry.items():
            try:
                if item_data["Rarity"] == "rare":
                    rare_item.add(item_name)
            except KeyError:
                continue
    print(f"Most valuable player: "
          f'{gold_champion} ({players[gold_champion]["info"]["golds"]} gold)')
    print(f'Most items: {amount_champion} '
          f'({players[amount_champion]["info"]["total_amount"]} items)')
    print(f'Rarest items: {rare_item}')


if __name__ == "__main__":
    main()
