# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:06:39 2022

@author: PICHAU
"""

"""Setting the file path or remote execution"""
import os

caminho = os.path.abspath(os.path.dirname(__file__))


from buscaSeq_direta import BuscaSeq as b

import time as t


vector = []

import random as r

for i in range(10000000):
    
    value = r.randint(1, 10000)
    
    vector.append(value)
    
vector.sort()

time_start = t.time()    
                
x= b(vector, 9999, False)

x.busca_chave()

time_end = t.time()

timer= time_end - time_start

print('\n')


print(f'O tempo de execução do algoritmo  de Busca Sequencial é: {timer}')


from buscaBin import BuscaBin as bb


time_start = t.time() # importing and starting the counter for calculation of the code execution

y= bb(vector, 9999, 0, 0)

y.busca()

y.printValues()

time_end = t.time()

timer = 0

timer = time_end - time_start

print('\n')


print(f'O tempo de execução do algoritmo Busca Binária é: {timer}')