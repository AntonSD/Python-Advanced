from collections import deque

elves_energy = deque([int(x) for x in input().split(' ')])
boxes_materials = [int(x) for x in input().split(' ')]
turns_count = 0
total_energy_spent = 0
toys_count = 0

while boxes_materials and elves_energy:

    while elves_energy and elves_energy[0] < 5:
        elves_energy.popleft()

    if not elves_energy:
        break
    box = boxes_materials.pop()
    elf_energy = elves_energy.popleft()
    turns_count += 1

   
    if turns_count % 15 == 0 and (2 * box) <= elf_energy:
        toys_count += 0
        total_energy_spent += 2 * box
        elves_energy.append(elf_energy - (2 * box))

    elif turns_count % 5 == 0 and box <= elf_energy:
        toys_count += 0
        total_energy_spent += 1 * box
        elves_energy.append(elf_energy - box)
    elif turns_count % 3 == 0 and (2 * box) <= elf_energy:
        toys_count += 2
        total_energy_spent += 2 * box
        elves_energy.append(elf_energy - (2 * box) + 1)

    elif box <= elf_energy and turns_count % 3 > 0:
        toys_count += 1
        total_energy_spent += box
        elves_energy.append(elf_energy - box + 1)
    else:
        boxes_materials.append(box)
        elves_energy.append(elf_energy * 2)

elves_energy_as_string = [str(x) for x in elves_energy]
print(f"Toys: {toys_count}")
print(f"Energy: {total_energy_spent}")
print(f"Elves left: {', '.join(elves_energy_as_string)}")