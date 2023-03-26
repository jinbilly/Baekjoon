dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

dwarf_sum = sum(dwarfs)
for i in range(8):
    for j in range(i+1, 9):
        if dwarf_sum - dwarfs[i] - dwarfs[j] == 100:
            fake_dwarfs = [dwarfs[i], dwarfs[j]]
            dwarfs.remove(fake_dwarfs[0])
            dwarfs.remove(fake_dwarfs[1])
            dwarfs.sort()
            for dwarf in dwarfs:
                print(dwarf)
            break
    if len(dwarfs) == 7:
        break