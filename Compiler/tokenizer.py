from pyparsing import *
from grammar.trigonometric import *
from grammar.Variable import *
from grammar.operation import *
def tokenizer(input):
	save=[]
	###############Operation#####################
	for s in add().scanString(input):
		save.append(s)
	for s in substraction().scanString(input):
		save.append(s)
	for s in multiply().scanString(input):
		save.append(s)
	for s in division().scanString(input):
		save.append(s)
	###############Variable##########################
	for s in equal().scanString(input):
		save.append(s)
        ###########trigonometric######################
	for s in sin().scanString(input):
		save.append(s)

	for s in cos().scanString(input):
		save.append(s)

	for s in tan().scanString(input):
		save.append(s)

	for s in asin().scanString(input):
		save.append(s)

	for s in acos().scanString(input):
		save.append(s)

	for s in atan().scanString(input):
		save.append(s)
	
	return save


def startEnd(ins):
	ins.insert(0,['systemStart'])
	ins.append(['systemEnd'])
	return ins

def cleanScanStringResult(inp):
##Usage: form list of useful tokens in order

	###### obtain start index from scanString ######
	index=[]
	for i in range(0,len(inp)):
		index.append(inp[i][1])
	#print "index:",index

	###### ordered index #######
	sortedIndex=sorted(index)
	#print "sortedIndex:",sortedIndex

	###### ordered scanString output ######

	sortedSave=[None]*len(inp)

	for i in range(0,len(sortedIndex)):
		for j in range(0,len(inp)):	
			if inp[j][1]==sortedIndex[i]:
				sortedSave[i]=inp[j]

	#print "sortedSave:",sortedSave

	###### unpack tuple ######

	cleanSortedSave=[None]*len(sortedSave)
	for i in range(0,len(sortedSave)):
		cleanSortedSave[i]=sortedSave[i][0]

	#print "cleanSortedSave:",cleanSortedSave

	######  clearn list ######
	strin=str(cleanSortedSave)
	strin=strin.replace("(","").replace(", {})","")
	#print "strin:",strin
	x=eval(strin)
	x=startEnd(x)
	for i in range(0,len(x)):
		x[i].insert(0,i+1)
	return x

