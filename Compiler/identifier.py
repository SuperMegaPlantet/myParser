from myParser.variable import *
from myParser.system import *
from myParser.newOperation import *

##identify list of tokens, output list of messages
def identifier(ins):
	length=len(ins)
	message=[None]*length
	for i in range(0,length):
		currentList=ins[i]
		##################################################################
		#####feature extraction and message generation func put here #####
		if len(currentList)==2:
			if currentList[1]=="systemStart":
				message[i]=start(currentList)
	
			if currentList[1]=="systemEnd":
				message[i]=end(currentList)
		
		if len(currentList)==4:	
			if currentList[2]=="=":		
				message[i]=equation(currentList)

		if len(currentList)==6:
			if currentList[4]=="+":
				message[i]=addIdentifier(currentList)
			if currentList[4]=="-":
				message[i]=subsIdentifier(currentList)
			if currentList[4]=="*":
				message[i]=multiIdentifier(currentList)
			if currentList[4]=="/":
				message[i]=diviIdentifier(currentList)
			
	return message



#given equation tokens, output message
def equation(ins):
	#if ins[2]=="=":
	variable=ins[1]
	value=ins[3]
	if "." not in value:
		value=value+".0"
		#print "value",value
	out=setVariableValue(value,variable,0,ins[0]+1)
	return out

def addIdentifier(ins):
	result=ins[1]
	value1=ins[3]
	value2=ins[5]
	out=addition(value1,value2,result,0,ins[0]+1)
	return out

def subsIdentifier(ins):
	result=ins[1]
	value1=ins[3]
	value2=ins[5]
	out=substraction(value1,value2,result,0,ins[0]+1)
	return out

def multiIdentifier(ins):
	result=ins[1]
	value1=ins[3]
	value2=ins[5]
	out=multiply(value1,value2,result,0,ins[0]+1)
	return out

def diviIdentifier(ins):
	result=ins[1]
	value1=ins[3]
	value2=ins[5]
	out=division(value1,value2,result,0,ins[0]+1)
	return out

def start(ins):
	out=systemStart(0,ins[0]+1)
	return out

def end(ins):
	out=systemEnd(0,ins[0])
	return out

#a=[['B','=','2'],['A','=','1'],['C','=','3']]
a=[1,'B','=','2']
print equation(a)
