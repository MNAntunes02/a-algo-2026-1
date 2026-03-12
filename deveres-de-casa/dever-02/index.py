import time
import sys

# Aumentando o limite de recursão do Python para evitar RecursionError com n=1000
sys.setrecursionlimit(2000)

def fatorial_recursivo(n):
    """
    Calcula o fatorial de um número n de forma recursiva.
    """
    if n == 0 or n == 1:
        return 1
    

    else:
        return n * fatorial_recursivo(n - 1)

valores_n = [10, 100, 500, 1000]

for n in valores_n:
    inicio = time.perf_counter() 
    resultado = fatorial_recursivo(n) 
    fim = time.perf_counter()
    tempo_execucao = fim - inicio
    
    print(f"Fatorial de n = {n:<4} calculado em {tempo_execucao:.8f} segundos.")