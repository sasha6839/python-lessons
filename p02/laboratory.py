print('----------------------------------')
print("Розрахунок лабораторій для Грю")
print('\n\n----------------------------------')
pl_ar = int(input('Площа планети:'))
bg_lab = 5
md_lab = 3
sm_lab = 1
num_lab_bg = pl_ar // bg_lab
area = pl_ar - num_lab_bg * bg_lab
num_lab_md = area // md_lab
num_lab_sm = area - num_lab_md * md_lab

print(f"Кількість великих лабораторій: {num_lab_bg}")
print(f"Кількість середніх лабораторій: {num_lab_md}")
print(f"Кількість малих лабораторій: {num_lab_sm}")
