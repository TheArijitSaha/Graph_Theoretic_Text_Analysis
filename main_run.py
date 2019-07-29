from text_filterer import formTokens
from n_gram_graph import gram3Generator
from clustering_coefficient import wordsByClusteringCoefficient
from betweenness_centrality import wordsByBetweennessCentrality
from degree_centrality import wordsByDegreeCentrality


# formTokens('Texts/THE RED-HEADED LEAGUE.txt')
G=gram3Generator('Dataset/NewsArticles/FilteredNews1.txt')
wordsByClusteringCoefficient(G)
wordsByBetweennessCentrality(G)
wordsByDegreeCentrality(G)
print()
