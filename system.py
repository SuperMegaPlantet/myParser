from Bit import highValue,lowValue



def systemStart(a,b):
	##generate list 1*30
	list1=[0]*30
	#fill in variables
	list1[0]="0xA1"
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)


	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;

def systemEnd(a,b):
	##generate list 1*30
	list1=[0]*30
	#fill in variables
	list1[0]="0xA2"
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;


