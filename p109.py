import numpy as np
from typing import List, Callable

def matrix_multiplication (m_1: np.ndarray, m_2: np.ndarray) : 
    return np.multiply(m_1, m_2)

def rec_bb (t, f, l, key) : 
    
    if f>l : 
        return None
    
    mid = (f+l) // 2
    
    if key==t[mid] : 
        return mid
    elif key<t[mid] : 
        return rec_bb (t, f, mid-1, key)
    else : 
        return rec_bb (t, mid+1, l, key)

def bb(t: list, f: int, l: int, key: int) -> int:
    while f < l:

        mid = (f + l) // 2

        if t[mid] == key:
            return mid
        elif t[mid] < key:
            f = mid + 1
        else:
            l = mid - 1

def min_heapify(h: np.ndarray, i: int):
    
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

def insert_min_heap(h: np.ndarray, k: int) -> np.ndarray : 

    if h == None: 
        h == []
    
    h += [k]
    j = len(h) - 1
    
    #parent = (j-1)/2
    while j>=1 and h[(j-1)//2] > h[j]:
        h[(j-1)//2], h[j] = h[j], h[(j-1)//2]
        j = (j-1)//2
    
    return h

def create_min_heap (h:np.ndarray): 
    
    if (len(h)==0): 
        return
    
    i = ((len(h)-1)-1)/2
    
    while i > -1: 
        min_heapify (h, i)
        i = i - 1

def pq_ini() : 
    pq = []
    return pq 
  
def pq_insert (h: np.ndarray, k:int)-> np.ndarray :  
    
    if len(h)==0 : 
        return None
    
    return insert_min_heap (h, k)

def pq_remove(h: np.ndarray) : 
    if len(h)==0 : 
        return (h[0], h)
    
    k = h[0]
    h[0] = h[-1]
    min_heapify (h, 0)
    
    return (k, h)

def select_min_heap(h: np.ndarray, k: int)-> int: 
    h_aux = []
    
    for i in range (0, k) : 
      insert_min_heap (h_aux, -h[i])

    for i in range (0, len(h)) : 
      if -h[i] > h_aux[0] : 
        h_aux = pq_remove (h_aux)[1]
        h_aux = insert_min_heap(h_aux, -h[i])
    
    return -h_aux[0]