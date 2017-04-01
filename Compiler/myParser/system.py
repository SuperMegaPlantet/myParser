from Bit import highValue,lowValue



def systemStart(a,b):
	##generate list 1*30
	list1=[0]*22
	#fill in variables
	list1[0]="0xA1"
	list1[18]=highValue(a)
	list1[19]=lowValue(a)
	list1[20]=highValue(b)
	list1[21]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;

def systemEnd(a,b):
	##generate list 1*30
	list1=[0]*22
	#fill in variables
	list1[0]="0xA2"
	list1[18]=highValue(a)
	list1[19]=lowValue(a)
	list1[20]=highValue(b)
	list1[21]=lowValue(b)
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;



