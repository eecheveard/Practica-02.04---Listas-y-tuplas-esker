import math

def calcular_media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

def calcular_desviacion_tipica(lista_numeros, media):
    varianza = sum((x - media) ** 2 for x in lista_numeros) / len(lista_numeros)
    return math.sqrt(varianza)

def main():
    
    entrada = input("Introduce una lista de números separados por comas: ")
    
    try:
        
        numeros = [float(numero) for numero in entrada.split(",")]
        
        
        media = calcular_media(numeros)
        desviacion_tipica = calcular_desviacion_tipica(numeros, media)
        
        
        print(f"Media: {media:.2f}")
        print(f"Desviación típica: {desviacion_tipica:.2f}")
    except ValueError:
        print("Por favor, introduce únicamente números separados por comas.")

if __name__ == "__main__":
    
    main()