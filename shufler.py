import random

a = {i for i in range(18)}
a.remove(5)
a.remove(12)  # мемы взяли

groups = list(range(1, 11))
for group in groups:
    task = random.choice(list(a))
    a.remove(task)
    print(f'{group=}: {task=}')



# 4 - отсутсовал
# Dmitriy, [12.09.2024 20:45]
# Проект
# Василенко Дмитрий @adaptabiIity 🌟