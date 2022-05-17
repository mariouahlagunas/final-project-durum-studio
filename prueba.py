import random


enemies = ["enemigo1", "enemigo2", "enemigo3", "enemigo4", "enemigo5", "enemigo6", "enemigo7", "enemigo8", "enemigo9", "enemigo10", "enemigo11", "enemigo12"]
dificultad = "normal"

num_enemies = 0
if dificultad == "facil":
    num_enemies = int(len(enemies) * (1 / 3))
elif dificultad == "normal":
    num_enemies = int(len(enemies) * (1 / 2))
else: # dificultad == dificil
    num_enemies = int(len(enemies) * (2 / 3))
print(num_enemies)

if random.randint(1, 12) > 9:
    num_enemies += 1
print(num_enemies)
print()

for i in range(num_enemies):
    #print(f"i = {i}.   enemies = {enemies}")

    aux = random.randint(0, len(enemies) - 1)
    print(aux)
    print(enemies.pop(aux))


