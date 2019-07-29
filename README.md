# Graph_Theoretic_Text_Analysis
This seeks out representative keywords from the literary text given by constructing co-occurence graphs in trigram model. For example, when applied to the english transcript of```Sonar Kella```, a bengali detective story, the following top 10 keywords are given:
```
feluda, mukul, hajra, jatayu, bose, dr, rajasthan, fort, mandar, also
```
These words are:
  * Protagonists (feluda, mukul, jatayu, bose)
  * Antagonists (dr hajra)
  * Important geaographic locations (rajasthan, fort, mandar)
  * Some descripancies (also)

This project aims to tag a text with keywords or find representative keywords for a text. The same can be applied to News articles and online articles to tag them in order to be able to group them based on keywords.

Some Sample generated Graphs are present in the folder "images".

For a more detailed analysis view the PDF "Graph_Theoretic_Text_Analysis.pdf" in this repository.

Instructions to run:
1. Download all files
2. Put the Text file you want to analyse under the "Texts" folder
3. Run formTokens('Texts/filename.txt') in "text_filterer.py" to filter the text from filename.txt (your file)
4. Open main_run_notebook.ipynb in jupyter notebooks and run the program with gram3Generator("FilteredTexts/filename.txt")
5. You will be given the top tagwords based on Betweenness Centrality, Closeness Centrality, Degree Centrality
6. Also two graphs will be generated based on the former two factors where bigger the node size, more central to the story the    word is.
