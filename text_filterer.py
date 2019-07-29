import nltk
import string
from nltk.corpus import brown
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

# Lemmatisation
def get_wordnet_pos(word):
	"""
	Map POS tag to first character lemmatize() accepts
	"""
	tag=nltk.pos_tag([word])[0][1][0].upper()
	tag_dict = {"J": wordnet.ADJ,
				"N": wordnet.NOUN,
				"V": wordnet.VERB,
				"R": wordnet.ADV}
	return tag_dict.get(tag, wordnet.NOUN)

def formTokens(fromFileName,toFileName='Filtered'+fromFileName):
	"""
	Forms tokens from the text named fromFileName and stores them into the file named toFileName.
	The tokens are stored in such a way that all tokens from a sentence are stored in a single line.
	These tokens can be used to make co-occurence graphs as they have been utilised later in this project.
	"""
	
	# Load Text from File
	file = open(fromFileName, 'rt')
	text = file.read()
	file.close()

	# Tokenise into words
	text=sent_tokenize(text)
	text[:]=[word_tokenize(sentence) for sentence in text]

	# remove punctuation from each word
	table=str.maketrans('-',' ',string.punctuation.replace("-",""))
	text[:]=[[w.translate(table) for w in sent if w.translate(table)!=''] for sent in text]

	# convert to lower case
	for sentence in text:
		sentence[:]=[word.lower() for word in sentence]


	#lemmatization of words using Parts of Speech tag in the sentence
	lem = WordNetLemmatizer()
	lemmatized=[]
	for sentence in text:
		sentence[:]=[lem.lemmatize(word,get_wordnet_pos(word)) for word in sentence]
	# for sentence in text:
	# 	print(sentence)

	# Remove remaining tokens that are not alphabetic
	for sentence in text:
		sentence[:]=[word for word in sentence if word.isalpha()]

	# Remove Stopwords
	stop_words=set(stopwords.words('english'))
	for sentence in text:
		sentence[:]=[word for word in sentence if not word in stop_words]

	# Create Frequency Table

	# Uncomment this part to create Frequency Table based on frequency of nltk brown
	# and comment the text frequency part
	######################        BY NLTK BROWN         #############################
	# freq=nltk.FreqDist(word.lower() for word in brown.words())
	# res=[]
	# for sen in text:
	# 	arr=[]
	# 	for word in sen:
	# 		temp=word
	# 		for syn in wordnet.synsets(word):
	# 			for l in syn.lemmas():
	# 				if freq[temp]<freq[l.name().lower()]:
	# 					temp=l.name().lower()
	# 		arr.append(temp)
	# 	res.append(arr)
	#################################################################################


	# Uncomment this part to create Frequency Table based on frequency of given text
	# and comment the nltk brown frequency part
	######################        BY TEXT FREQUENCY         #########################
	freq={}
	for sentence in text:
		for word in sentence:
			if word not in freq:
				freq[word]=0
			freq[word]+=1
	# print(freq)

	def takekey(elem):
		return freq[elem]

	res=[]
	for sentence in text:
		# print(sentence)
		temp=[]
		for word in sentence:
			syns=wordnet.synsets(word)
			sortedSynonyms=[]
			for s in syns:
				if s.lemmas()[0].name() in freq:
					sortedSynonyms.append(s.lemmas()[0].name())
			if len(sortedSynonyms) is not 0:
				sortedSynonyms.sort(key=takekey,reverse=True)
				temp.append(sortedSynonyms[0])
			else:
				temp.append(word)
		res.append(temp)
		# sentence[:]=temp
	#################################################################################



	# Store processed data in a file
	file1=open(toFileName,'w')
	for sentence in res:
		for word in sentence:
			file1.write(" "+word)
		file1.write("\n")
	file1.close()

if __name__=="__main__":
	formTokens('Texts/THE RED-HEADED LEAGUE.txt','filteredText.txt')
