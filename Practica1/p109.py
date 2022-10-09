import numpy as np
from typing import List, Callable


def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray) -> np.ndarray:
    """Multiplica 2 matrices.

    Devuelve la matriz multiplicada.

    Args: 
        m_1 (np.ndarray): una matriz para multiplicar.

        m_2 (np.ndarray): una matriz para multiplicar. 

    Returns: 

        m_3 (np.ndarray): la matriz resultado de la multiplicacion de m_1 * m_2

    """
    return np.multiply(m_1, m_2)


def rec_bb(t: list, f: int, l: int, key: int) -> int:
    """Busca un elemento en un array ordenado.

    Divide el array por la mitad, comprueba si el elemento que ocupa la posicion en la mitad es mayor o menor que el elemento que queremos insertar, 
    y dependiendo de lo que sea, volvemos a dividir y ejecutar el mismo proceso con la mitad superior o inferior de la tabla.

    Args: 
        t (list): la lista en la que queremos buscar el elemento.

        f (int): el indice del primer elemento de la tabla. 

        l (int): el indice del ultimo elemento de la tabla. 

        key (int): el elemento que queremos buscar

    Returns: 
        p (int): la posicion del elemento que queremos buscar

    """

    if f > l:
        return None

    mid = (f+l) // 2

    if key == t[mid]:
        return mid
    elif key < t[mid]:
        return rec_bb(t, f, mid-1, key)
    else:
        return rec_bb(t, mid+1, l, key)


def bb(t: list, f: int, l: int, key: int) -> int:
    """Busca un elemento en un array ordenado.

    Divide el array por la mitad, comprueba si el elemento que ocupa la posicion en la mitad es mayor o menor que el elemento que queremos insertar, 
    y dependiendo de lo que sea, volvemos a dividir y ejecutar el mismo proceso con la mitad superior o inferior de la tabla.

    Args: 
        t (list): la lista en la que queremos buscar el elemento.

        f (int): el indice del primer elemento de la tabla. 

        l (int): el indice del ultimo elemento de la tabla. 

        key (int): el elemento que queremos buscar

    Returns: 
        p (int): la posicion del elemento que queremos buscar

    """
    while f <= l:

        mid = (f + l) // 2

        if t[mid] == key:
            return mid
        elif t[mid] < key:
            f = mid + 1
        else:
            l = mid - 1


def min_heapify(h: np.ndarray, i: int):
    """Comprueba que los hijos son menores del padre que ocupa la posicion i.

    Modifica el heap de tal forma que el elemento de la posicion i, sus hijos sean menores que él.

    Args: 
        h (np.ndarray): un heap.

        i (int): la posicion del elemento el cual se quiere hacer heapify. 

    """

    while 2*i+1 < len(h):
        n_i = i
        if h[int(n_i)] > h[int(2*i+1)]:
            n_i = 2*i+1
        if 2*i+2 < len(h) and h[int(n_i)] > h[int(2*i+2)]:
            n_i = 2*i+2
        if n_i > i:
            h[int(i)], h[int(n_i)] = h[int(n_i)], h[int(i)]
            i = n_i
        else:
            return


def insert_min_heap(h: np.ndarray, k: int) -> np.ndarray:
    """Inserta un nuevo nodo.

    Inserta un nuevo nodo en un min heap existente.

    Args: 
        h (np.ndarray): el min heap.

        k (int): el nuevo nodo/valor a insertar. 

    Returns: 
        h (np.ndarray): el min heap con el nodo insertado.

    """
    h = np.append(h, k)
    create_min_heap(h)

    return h


def create_min_heap(h: np.ndarray):
    """Crea un min heap.

    Crea un min heap sobre el array que le es pasado por argumento.

    Args: 
        h (np.ndarray): un array de Numpy.

    """

    if (len(h) == 0):
        return

    i = ((len(h)-1)-1)/2

    while i > -1:
        min_heapify(h, i)
        i = i - 1


def pq_ini():
    """Inicializa una cola de prioridad. 

    Returns: 
        pq (lista): la cola de prioridad vacia.

    """
    pq = []
    return pq


def pq_insert(h: np.ndarray, k: int) -> np.ndarray:
    """Inserta un nuevo valor en la cola de prioridad.

    Inserta un nuevo nodo en un min heap existente.

    Args: 
        h (np.ndarray): la cola de prioridad en la que hay que insertar el valor.

        k (int): el nuevo nodo/valor a insertar. 

    Returns: 
        h (np.ndarray): la lista con el nuevo nodo insertado.

    """

    return insert_min_heap(h, k)


def pq_remove(h: np.ndarray) -> [int, np.ndarray]:
    """Extrae la raiz.

    Elimina la raiz, la reemplaza por el ultimo nodo y comprueba si sigue siendo un min heap.

    Args: 
        h (np.ndarray): la cola de prioridad en la que hay que extraer la raiz.

    Returns: 
        tuple[int, np.ndarray]: la cola de prioridad sin la raiz original y el valor extraido

    """
    if len(h) == 0:
        return (h[0], h)

    k = h[0]
    h[0] = h[-1]
    h = np.delete(h, -1)
    min_heapify(h, 0)

    return (k, h)


def select_min_heap(h: np.ndarray, k: int) -> int:
    """Retorna el valor que ocuparia la posicion k en un array ordenado.

    Args: 
        h (np.ndarray): el min heap.

        k (int): la posicion que ocuparia

    Returns: 
        j (int): el elemento que ocuparia la posicion k en un array ordenado

    """

    h_aux = np.array([])
    h_aux = list(map(lambda n: -n, h))

    first_k_elem = h_aux[:k]

    create_min_heap(first_k_elem)

    for i in h_aux[k:]:
        if i > first_k_elem[0]:
            first_k_elem[0] = i
            min_heapify(first_k_elem, 0)
    return -first_k_elem[0]
