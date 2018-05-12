import math
import numpy as np
from random import randint
import random
import copy

# DISTANCIA EUCLIDIANA ENTRE DOIS PONTOS
def dist_euclid(x1, y1, x2, y2):
	return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

# CRIA MATRIZ DE DISTANCIA ENTRE OS NOS 
def cria_matriz_de_distancia(tamanho, matriz):
	# cria matriz e preenche com 0
	n_matriz = np.zeros((tamanho+1,tamanho+1), dtype = int)

	# preenche primeira linha e primeira coluna com o numero do nó
	for row in range(0,tamanho+1):
		for col in range(0,tamanho+1):
			if (col == 0 and row == 0):
				n_matriz[row][col] = 0
			if (col == 0 and row != 0):
				n_matriz[row][col] = row 
			if (row == 0 and col != 0):
				n_matriz[row][col] = col


	# preenche a n_matriz com as distancias entre os pontos
	for x in range(0, tamanho):
		for i in range(0, tamanho):
			dist = dist_euclid(matriz[x][0], matriz[x][1], matriz[i][0], matriz[i][1])
			n_matriz[x+1][i+1] = dist

	#print(n_matriz)

	return n_matriz

# GERA POPULACAO
def gen_pop(N, tamanho):
	populacao = []
	individuo = random.sample(range(1, N+1),N)
	random.shuffle(individuo)
	for x in range(0,tamanho):
		populacao.append(copy.copy(individuo))
		random.shuffle(individuo)

	return populacao

# VERIFICA O CUSTO DO INDIVIDUO
def fitness(individuo, matriz_dist):
	# CUSTO ENTRE O PRIMEIRO NO E O ULTIMO
	custo = matriz_dist[individuo[0]][individuo[len(individuo)-1]]

	#PERCORRE O VETOR INDIVIDUO E CALCULA O CUSTO ENTRE OS NÓS	
	for i in range(len(individuo)-1):
		custo = custo + matriz_dist[individuo[i]][individuo[i+1]] 

	return custo

# FAZ ALGUMA COISA
def acumular(v):
    res = []
    acum = 0
    for i in v:
        res.append(i + acum)
        acum = res[-1]
    return res


# SELECIONA INDIVIDUO 
def random_select(pop, f):
    fit = map(f, pop)
    soma = sum(fit)
    norm = map(lambda x: x/soma, fit)
    acm = acumular(norm)
    r = random.random()
    
    for i in range(len(acm)):
        if r < acm[i]:
            break
    
    return pop[i]


# REPRODUCAO DE UM INDIVIDUO
# def reproducao(pai, mae):

# MUTACAO DE UM INDIVIDUO
# def mutacao(individuo):
	
# Open input file
infile = open('a280.tsp', 'r')

# Read instance header
Name = infile.readline().strip().split()[1] # NAME
FileType = infile.readline().strip().split()[1] # TYPE
Comment = infile.readline().strip().split()[1] # COMMENT
Dimension = infile.readline().strip().split()[1] # DIMENSION
EdgeWeightType = infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
infile.readline()

# Read node list
node_list = []
N = int(Dimension)
for i in range(0, int(Dimension)):
    x,y = infile.readline().strip().split()[1:]
    node_list.append([int(x), int(y)])

matriz = cria_matriz_de_distancia(N, node_list)
pop = gen_pop(N, 10)

#print (pop)
#print(matriz)
#fitness(pop[0], matriz)
individuo = random_select(pop, fitness)
print(individuo)


# Close input file
infile.close()

