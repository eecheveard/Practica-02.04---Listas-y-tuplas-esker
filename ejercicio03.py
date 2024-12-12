asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input("¿Qué nota he sacado en " + asignatura + "?")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " he sacado un " + notas[i])