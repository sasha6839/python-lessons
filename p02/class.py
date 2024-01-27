print("Розрахунок співвідношення дівчат і хлопців в класі")

boys = input('\nКількість хлопців в класі: ')
girls = input('\nКількість дівчат в класі: ')
all_students = int(girls) + int(boys)
girls_percent = int(girls) * 100 / int(all_students)
boys_percent = 100 - int(girls_percent)

print(f"В класі {boys_percent}% хлопців і {girls_percent}% дівчат")