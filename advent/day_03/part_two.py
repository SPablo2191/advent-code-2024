import re
from advent.tools.reader import read_output

INPUT_DATA = "advent/day_03/input.txt"
regex = r"mul\((\d{1,3}),(\d{1,3})\)"
delimiters = r"don't\(\)|do\(\)"


def main():
    # Leer la entrada
    lines = read_output(INPUT_DATA)

    # Unimos todas las líneas en una sola cadena para un procesamiento secuencial
    memory = "".join(lines)

    # Inicializar acumulador y estado de habilitación
    acc = 0
    enabled = True  # Las multiplicaciones están habilitadas al inicio

    # Índice para recorrer la cadena
    i = 0
    while i < len(memory):
        # Verificar si encontramos una instrucción `do()`
        if memory[i : i + 4] == "do()":
            enabled = True
            i += 4  # Avanzar el índice después de esta instrucción
        # Verificar si encontramos una instrucción `don't()`
        elif memory[i : i + 7] == "don't()":
            enabled = False
            i += 7  # Avanzar el índice después de esta instrucción
        else:
            # Intentar encontrar una instrucción `mul(X,Y)` a partir de la posición actual
            match = re.match(regex, memory[i:])
            if match:
                # Si encontramos una instrucción válida y está habilitada, procesarla
                if enabled:
                    x, y = map(int, match.groups())
                    acc += x * y
                # Avanzar el índice hasta el final de la instrucción `mul(X,Y)`
                i += match.end()
            else:
                # Si no es una instrucción válida, avanzar un carácter
                i += 1

    # Imprimir el resultado final
    print(acc)


if __name__ == "__main__":
    main()
