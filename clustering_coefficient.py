import networkx as nx
import matplotlib.pyplot as plt
import heapq

def wordsByClusteringCoefficient(G):
	"""
	From a generated co-occurence graph, this returns sorted the highest and lowest
	15 words ranked on the basis of Clustering Coefficient.
	"""

	c=nx.clustering(G)

	hola=[]
	for w in c:
		if c[w]!=0 and c[w]!=1:
			hola.append((c[w],w))
	hola.sort()

	print("\n\nCLUSTERING COEFFICIENT :")
	print("------------------------")

	print("Lowest 15 :")
	for i in range(0,15):
		print(hola[i][1],end="  ")

	print("\n\nHighest 15 :")
	for i in range(len(hola)-1,len(hola)-1-15,-1):
		print(hola[i][1],end="  ")

	print()
