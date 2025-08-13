game_level = 2
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    if game_level < 5:
       new_enemy = enemies[0]
    print(new_enemy)       