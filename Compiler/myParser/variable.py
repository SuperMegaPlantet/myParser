from Bit import highValue,lowValue



def serviceMethodSetVariable(variable,NID_1,NID_2,NID_3,NID_4,NID_5,NID_6,service,method,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA5"
	list1[1]="0x03"
	list1[2]=variable
	list1[3]=NID_6
	list1[4]=NID_5
	list1[5]=NID_4
	list1[6]=NID_3
	list1[7]=NID_2
	list1[8]=NID_1
	list1[9]=highValue(service)
	list1[10]=lowValue(service)
	list1[11]=highValue(method)
	list1[12]=lowValue(method)
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;

def serviceMethodToVariable(variable,NID_1,NID_2,NID_3,NID_4,NID_5,NID_6,service,method,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA5"
	list1[1]="0x02"
	list1[2]=variable
	list1[3]=NID_6
	list1[4]=NID_5
	list1[5]=NID_4
	list1[6]=NID_3
	list1[7]=NID_2
	list1[8]=NID_1
	list1[9]=highValue(service)
	list1[10]=lowValue(service)
	list1[11]=highValue(method)
	list1[12]=lowValue(method)
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;

def serviceSetValue(NID_1,NID_2,NID_3,NID_4,NID_5,NID_6,service,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA5"
	list1[1]="0x05"
	list1[2]=NID_6
	list1[3]=NID_5
	list1[4]=NID_4
	list1[5]=NID_3
	list1[6]=NID_2
	list1[7]=NID_1
	list1[8]=highValue(service)
	list1[9]=lowValue(service)
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;

def setVariableValue(input,variable,a,b):
	#split input to int and decimal
	input=str(input)
	integer=input.split('.')[0]
	decimal=input.split('.')[1]
	#print integer
	#print decimal

	#convert integer into 16bit
	bit=hex(int(integer))
	bit=bit.split('x')[1]
	#print bit
	n=len(bit)

	#add zeros
	if n==1:
		bit='0000000'+bit
	if n==2:
		bit='000000'+bit
	if n==3:
		bit='00000'+bit
	if n==4:
		bit='0000'+bit
	if n==5:
		bit='000'+bit
	if n==6:
		bit='00'+bit
	if n==7:
		bit='0'+bit

	#set values
	bit=list(bit)
	value_4=bit[0]+bit[1]
	value_3=bit[2]+bit[3]
	value_2=bit[4]+bit[5]
	value_1=bit[6]+bit[7]

	##generate list 1*30
	list1=[0]*22

	#fill in inputs
	list1[0]="0xA5"
	list1[1]="0x01"
	list1[2]=variable
	list1[3]=value_4
	list1[4]=value_3
	list1[5]=value_2
	list1[6]=value_1
	list1[7]=decimal	
	list1[18]=highValue(a)
	list1[19]=lowValue(a)
	list1[20]=highValue(b)	
	list1[21]=lowValue(b)
	#print list1

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;



def variable2ToVariable1(variable_1,variable_2,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA5"
	list1[1]="0x04"
	list1[2]=variable_1
	list1[3]=variable_2
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	return output_bytes;
