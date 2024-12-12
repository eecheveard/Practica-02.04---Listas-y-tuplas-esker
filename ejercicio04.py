premiado = []
for i in range(6):
    premiado.append(int(input("Introduce un número ganador: ")))
premiado.sort()
print("Los números ganadores son " + str(premiado))