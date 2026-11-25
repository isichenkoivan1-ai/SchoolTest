import random
import time

# ==============================
#        LOOT HUNTER
# ==============================

coins = 100
luck = 0
opened = 0
inventory = []

loot_table = [
    {"name": "Старий камінь", "rarity": "Common", "chance": 60, "price": 5},
    {"name": "Срібний перстень", "rarity": "Uncommon", "chance": 25, "price": 20},
    {"name": "Кристал", "rarity": "Rare", "chance": 10, "price": 75},
    {"name": "Магічний меч", "rarity": "Epic", "chance": 4, "price": 250},
    {"name": "Корона дракона", "rarity": "Legendary", "chance": 1, "price": 1000},
]

colors = {
    "Common": "\033[37m",
    "Uncommon": "\033[32m",
    "Rare": "\033[34m",
    "Epic": "\033[35m",
    "Legendary": "\033[33m",
}

RESET = "\033[0m"


def title():
    print("\n" + "=" * 35)
    print("         🎲 LOOT HUNTER")
    print("=" * 35)


def show_stats():
    print(f"\n💰 Монети: {coins}")
    print(f"🍀 Удача: +{luck}%")
    print(f"📦 Відкрито скринь: {opened}")
    print(f"🎒 Предметів у сумці: {len(inventory)}")


def open_chest():
    global coins, opened

    cost = 25

    if coins < cost:
        print("\n❌ Недостатньо монет!")
        return

    coins -= cost
    opened += 1

    # Удача підвищує шанси рідкісних предметів
    weights = []

    for item in loot_table:
        chance = item["chance"]

        if item["rarity"] == "Common":
            chance = max(5, chance - luck * 0.3)
        else:
            chance = chance * (1 + luck / 100)

        weights.append(chance)

    item = random.choices(loot_table, weights=weights, k=1)[0]

    color = colors[item["rarity"]]

    print("\n🔓 Відкриваємо скриню...")
    time.sleep(0.7)
    print("...")
    time.sleep(0.5)

    print(f"\n{color}✨ ТИ ОТРИМАВ: {item['name']}!{RESET}")
    print(f"Рідкість: {color}{item['rarity']}{RESET}")
    print(f"Вартість: {item['price']} монет")

    inventory.append(item)


def show_inventory():
    if not inventory:
        print("\n🎒 Інвентар порожній.")
        return

    print("\n========== ІНВЕНТАР ==========")

    for i, item in enumerate(inventory, 1):
        color = colors[item["rarity"]]
        print(
            f"{i}. {color}{item['name']}{RESET} "
            f"[{item['rarity']}] - {item['price']} монет"
        )

    print("==============================")


def sell_items():
    global coins

    if not inventory:
        print("\nНемає предметів для продажу.")
        return

    total = sum(item["price"] for item in inventory)

    print(f"\n🛒 Ти продав {len(inventory)} предметів!")
    print(f"💰 Отримано: {total} монет")

    coins += total
    inventory.clear()


def upgrade_luck():
    global coins, luck

    cost = 150 + luck * 2

    print(f"\n🍀 Покращення удачі")
    print(f"Поточна удача: {luck}%")
    print(f"Ціна: {cost} монет")

    if luck >= 200:
        print("✨ Удача вже максимальна!")
        return

    if coins < cost:
        print("❌ Недостатньо монет!")
        return

    answer = input("Купити покращення? (y/n): ").lower()

    if answer == "y":
        coins -= cost
        luck += 20
        print("✨ Удачу збільшено на 20%!")


def show_odds():
    print("\n========== ШАНСИ ЛУТУ ==========")

    for item in loot_table:
        chance = item["chance"]

        if item["rarity"] == "Common":
            chance = max(5, chance - luck * 0.3)
        else:
            chance *= (1 + luck / 100)

        print(f"{item['rarity']:10} | {item['name']}")

    print(f"\n🍀 Твій бонус удачі: +{luck}%")
    print("===============================")


def main():
    while True:
        title()
        show_stats()

        print("\n[1] 🔓 Відкрити скриню (25 монет)")
        print("[2] 🎒 Інвентар")
        print("[3] 🛒 Продати всі предмети")
        print("[4] 🍀 Покращити удачу")
        print("[5] 📊 Рідкості")
        print("[0] 🚪 Вийти")

        choice = input("\nТвій вибір: ")

        if choice == "1":
            open_chest()

        elif choice == "2":
            show_inventory()

        elif choice == "3":
            sell_items()

        elif choice == "4":
            upgrade_luck()

        elif choice == "5":
            show_odds()

        elif choice == "0":
            print("\n👋 Дякую за гру в Loot Hunter!")
            break

        else:
            print("\n❌ Невідомий пункт меню.")

        input("\nНатисни Enter, щоб продовжити...")


if __name__ == "__main__":
    main()
