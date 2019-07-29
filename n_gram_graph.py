import networkx as nx
import matplotlib.pyplot as plt
import heapq

def gram3Generator(fileName):
	"""
	This function creates a co-occurence graph from a filtered text.
	The graph generated is 3-gram word wise.

	"""
	# Read text
	text=[]
	with open(fileName) as f:
		for line in f:
			text.append(line.split())

	# Create a set of words for creation of unique nodes
	st=set()
	for sent in text:
		for word in sent:
			st.add(word)

	# Create Graph
	G=nx.Graph()

	#Add Nodes
	G.add_nodes_from(st)

	#Add Edges based on 3-gram model word wise
	for sent in text:
		for i,word in enumerate(sent):
			if i+2<len(sent):
				if(G.has_edge(sent[i],sent[i+1])):
					G.edges[sent[i],sent[i+1]]['weight']+=1
				else:
					G.add_edge(sent[i],sent[i+1],weight=1)
				if(G.has_edge(sent[i+1],sent[i+2])):
					G.edges[sent[i+1],sent[i+2]]['weight']+=1
				else:
					G.add_edge(sent[i+1],sent[i+2],weight=1)
				if(G.has_edge(sent[i],sent[i+2])):
					G.edges[sent[i],sent[i+2]]['weight']+=1
				else:
					G.add_edge(sent[i],sent[i+2],weight=1)
			elif i+1<len(sent):
				if(G.has_edge(sent[i],sent[i+1])):
					G.edges[sent[i],sent[i+1]]['weight']+=1
				else:
					G.add_edge(sent[i],sent[i+1],weight=1)

	# print("No of Nodes : "+str(G.number_of_nodes()))
	# print("No of Edges : "+str(G.number_of_edges()))
	return G


if __name__=="__main__":
	G=gram3Generator('filteredText.txt')
