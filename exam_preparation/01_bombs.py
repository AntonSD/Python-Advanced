from collections import deque


def is_bombs_pouch_filled(crafted_bombs):
    for type, count in crafted_bombs.items():
        if count < 3:
            return False
    return True


bomb_effects = deque([int(x) for x in input().split(', ')])
bombs_casings = list([int(x) for x in input().split(", ")])

bombs_table = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}
crafted_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
while bomb_effects and bombs_casings and not is_bombs_pouch_filled(crafted_bombs):
    bomb_effect = bomb_effects[0]
    bombs_casing = bombs_casings[-1]
    result = bomb_effect + bombs_casing
    if result in bombs_table:
        bomb_effects.popleft()
        bombs_casings.pop()
        bomb_type = bombs_table[result]
        crafted_bombs[bomb_type] += 1
    else:
        bombs_casings[-1] -= 5

if is_bombs_pouch_filled(crafted_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bombs_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bombs_casings])}")
else:
    print("Bomb Casings: empty")
for key, value in sorted(crafted_bombs.items()):
    print(f'{key}: {value}')