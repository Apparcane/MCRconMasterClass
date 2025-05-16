def get_kit_command(player, kit_name):
    if kit_name == "start":
        return [
            f"give {player} minecraft:stone_sword 1",
            f"give {player} minecraft:stone_pickaxe 1",
            f"give {player} minecraft:stone_axe 1",
            f"give {player} minecraft:stone_shovel 1",
            f"give {player} minecraft:torch 16",
            f"give {player} minecraft:bread 10",
            f"give {player} minecraft:leather_helmet 1",
            f"give {player} minecraft:leather_chestplate 1",
            f"give {player} minecraft:leather_leggings 1",
            f"give {player} minecraft:leather_boots 1",
        ]
    elif kit_name == "premium":
        return [
            f"give {player} minecraft:diamond_sword 1",
            f"give {player} minecraft:diamond_pickaxe 1",
            f"give {player} minecraft:diamond_axe 1",
            f"give {player} minecraft:diamond_shovel 1",
            f"give {player} minecraft:torch 64",
            f"give {player} minecraft:cooked_beef 16",
            f"give {player} minecraft:iron_helmet 1",
            f"give {player} minecraft:iron_chestplate 1",
            f"give {player} minecraft:iron_leggings 1",
            f"give {player} minecraft:iron_boots 1",
        ]
    else:
        return None
