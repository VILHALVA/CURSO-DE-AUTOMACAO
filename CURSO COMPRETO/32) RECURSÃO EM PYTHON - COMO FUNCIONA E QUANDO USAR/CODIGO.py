def fatorial(n):
    if n == 0:  # Caso base
        return 1
    else:
        # Chamada recursiva
        return n * fatorial(n - 1)
