import random
import time

TAMANHOS_N = [1000, 5000, 10000, 20000, 50000]
LIMITE_RANDOM = 100000


def insertion_sort(lista):
    """
    Ordena uma lista utilizando o algoritmo de Insertion Sort.

    Args:
        lista (list): A lista de elementos a ser ordenada.

    Returns:
        list: A lista ordenada.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


def main():
    """
    Executa a comparação de performance entre Insertion Sort e Timsort.
    """
    print(f"{'Tamanho (n)':<15} | {'Insertion Sort (s)':<20} | {'Timsort (s)':<20}")
    print("-" * 62)

    for n in TAMANHOS_N:
        lista_original = [random.randint(0, LIMITE_RANDOM) for _ in range(n)]
        lista_insertion = lista_original.copy()
        lista_timsort = lista_original.copy()

        # Insertion Sort
        inicio_insertion = time.time()
        insertion_sort(lista_insertion)
        fim_insertion = time.time()
        tempo_insertion = fim_insertion - inicio_insertion

        # Timsort (built-in sorted)
        inicio_timsort = time.time()
        sorted(lista_timsort)
        fim_timsort = time.time()
        tempo_timsort = fim_timsort - inicio_timsort

        print(f"{n:<15} | {tempo_insertion:<20.6f} | {tempo_timsort:<20.6f}")


if __name__ == "__main__":
    main()