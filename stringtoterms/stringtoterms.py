import re
from porter2stemmer import Porter2Stemmer

#for stemming
stemmer = Porter2Stemmer()

#function to get the list of all terms from one doc
def stringtoterms(string, stemming=False):

	#for refining input content
	delimiters = " ",".","(c)","?","-","#","*","_","/","(",")","!","'",'"',",",";",":","&","<",">","\r","\n","\t"
	regexPattern = '|'.join(map(re.escape, delimiters))
	refinedlist = re.split(regexPattern, string)

	termlist = []

	for word in refinedlist:
        if stemming == True:
		          word = stemmer.stem(word)
		termlist.append(word)

	termlist = filter(None,termlist)
	#print termlist
	return list(termlist)
