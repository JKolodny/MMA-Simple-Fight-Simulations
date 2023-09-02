import numpy as np

LIFES = 30
SIMULATIONS = 650

life_value = []
for _ in range(LIFES):
    life_time_value = 0
    for _ in range(SIMULATIONS):
        AT_BAT = np.random.randint(0, 10)
        if AT_BAT > 7:
            life_time_value += 1

    life_value.append(life_time_value)

MIN = min(life_value)
MAX = max(life_value)
MEAN = int(np.mean(life_value))


print("MIN:", MIN)
print("MEAN:", MEAN)
print("MAX:", MAX)
print("MAX - MIN:", MAX - MIN)


