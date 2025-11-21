# tp6_ejercicios.py
# Alumno: Joel Vitrano - Comisión 12
# Actividad de cierre unidad 6
# Práctico 6: Estructuras de datos complejas
# Resolución de los ejercicios 1 a 10

from typing import Dict, List, Tuple, Set

def ejercicio_1_y_2():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    return precios_frutas

def ejercicio_3(precios_frutas: Dict[str, int]) -> List[str]:
    return list(precios_frutas.keys())

def ejercicio_4():
    agenda = {}
    for i in range(5):
        nombre = input(f"Nombre {i+1}: ").strip()
        numero = input(f"Número de {nombre}: ").strip()
        agenda[nombre] = numero
    buscar = input("Ingrese un nombre a buscar: ").strip()
    if buscar in agenda:
        print(f"Número de {buscar}: {agenda[buscar]}")
    else:
        print(f"No existe el contacto '{buscar}'.")
    return agenda

def ejercicio_5(frase: str = None):
    if frase is None:
        frase = input("Ingresá una frase: ").strip()
    palabras = frase.lower().split()
    conjunto_unico = set(palabras)
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    print("Palabras únicas:", conjunto_unico)
    print("Conteo:", conteo)
    return conjunto_unico, conteo

def ejercicio_6():
    registro = {}
    for i in range(3):
        nombre = input(f"Ingresá el nombre del alumno {i+1}: ").strip()
        notas = []
        for j in range(3):
            nota = float(input(f"  Nota {j+1} de {nombre}: "))
            notas.append(nota)
        registro[nombre] = tuple(notas)
    promedios = {alumno: sum(notas)/len(notas) for alumno, notas in registro.items()}
    for a, p in promedios.items():
        print(f"{a}: promedio {p:.2f}")
    return registro, promedios

def ejercicio_7():
    s1 = set(input("Aprobados P1 (separados por comas): ").replace(" ", "").split(","))
    s2 = set(input("Aprobados P2 (separados por comas): ").replace(" ", "").split(","))
    print("Ambos:", s1 & s2)
    print("Solo uno:", s1 ^ s2)
    print("Al menos uno:", s1 | s2)
    return {'parcial1': s1, 'parcial2': s2}

def ejercicio_8():
    stock = {}
    while True:
        op = input("Operación (consultar/agregar/nuevo/salir): ").strip().lower()
        if op == "salir":
            break
        elif op == "consultar":
            prod = input("Producto: ").strip()
            print(stock.get(prod, 0))
        elif op == "agregar":
            prod = input("Producto: ").strip()
            unidades = int(input("Unidades: "))
            stock[prod] = stock.get(prod, 0) + unidades
        elif op == "nuevo":
            prod = input("Nuevo producto: ").strip()
            unidades = int(input("Stock inicial: "))
            stock[prod] = unidades
    return stock

def ejercicio_9():
    agenda = {}
    for i in range(3):
        dia = input("Día: ").strip()
        hora = input("Hora: ").strip()
        evento = input("Evento: ").strip()
        agenda[(dia, hora)] = evento
    dia_q = input("Consultar día: ").strip()
    hora_q = input("Consultar hora: ").strip()
    print(agenda.get((dia_q, hora_q), "No hay evento."))
    return agenda

def ejercicio_10(paises_a_capital: Dict[str, str] = None):
    if paises_a_capital is None:
        paises_a_capital = {}
        while True:
            pais = input("País: ").strip()
            if pais == "":
                break
            capital = input("Capital: ").strip()
            paises_a_capital[pais] = capital

    capital_a_pais = {}
    for pais, capital in paises_a_capital.items():
        if capital in capital_a_pais:
            if isinstance(capital_a_pais[capital], list):
                capital_a_pais[capital].append(pais)
            else:
                capital_a_pais[capital] = [capital_a_pais[capital], pais]
        else:
            capital_a_pais[capital] = pais
    print(capital_a_pais)
    return capital_a_pais

def main():
    print("TP6 - Elegí ejercicio (1-10)")
    op = input("Opción: ").strip()
    if op == "1" or op == "2":
        print(ejercicio_1_y_2())
    elif op == "3":
        print(ejercicio_3(ejercicio_1_y_2()))
    elif op == "4":
        ejercicio_4()
    elif op == "5":
        ejercicio_5()
    elif op == "6":
        ejercicio_6()
    elif op == "7":
        ejercicio_7()
    elif op == "8":
        ejercicio_8()
    elif op == "9":
        ejercicio_9()
    elif op == "10":
        ejercicio_10()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
