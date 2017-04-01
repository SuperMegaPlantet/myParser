from Bit import highValue,lowValue

def fourBit(inp):
#Automatically add decimal 0.0 on integer
#change value into 16 bit formal + decimal value

	inp=str(inp)
	if "." not in inp:
		inp=inp+".0"
	integer=inp.split('.')[0]
	decimal=inp.split('.')[1]
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
	return (value_4,value_3,value_2,value_1,decimal)

#print fourbit('34.5')

def addition(A,B,C,a,b):
	if str(A).isalpha()==True and str(B).isalpha()==True:
		print "variable+variable"
		algorithm_mode="0x04"
		NID_A2=0
		NID_A1=0
		Service_AH=0
		Service_AL=0
		Method_AH=0
		Method_AL=A
		NID_B2=0
		NID_B1=0
		Service_BH=0
		Service_BL=0
		Method_BH=0
		Method_BL=B

	if str(A).isalpha()==True and any(i.isdigit() for i in str(B))==True:	
		print "variable+value"		
		algorithm_mode="0x05"
		NID_A2=0
		NID_A1=0
		Service_AH=0
		Service_AL=0
		Method_AH=0
		Method_AL=A
		NID_B2=0
		NID_B1=fourBit(B)[0]
		Service_BH=fourBit(B)[1]
		Service_BL=fourBit(B)[2]
		Method_BH=fourBit(B)[3]
		Method_BL=fourBit(B)[4]

	if any(i.isdigit() for i in str(A))==True and any(i.isdigit() for i in str(B))==True:
		print "value+value"
		algorithm_mode="0x07"
		NID_A2=0
		NID_A1=fourBit(A)[0]
		Service_AH=fourBit(A)[1]
		Service_AL=fourBit(A)[2]
		Method_AH=fourBit(A)[3]
		Method_AL=fourBit(A)[4]
		NID_B2=0
		NID_B1=fourBit(B)[0]
		Service_BH=fourBit(B)[1]
		Service_BL=fourBit(B)[2]
		Method_BH=fourBit(B)[3]
		Method_BL=fourBit(B)[4]
	if any(i.isdigit() for i in str(A))==True and str(B).isalpha()==True:
		print "value+variable"
		algorithm_mode="0x09"
		NID_A2=0
		NID_A1=fourBit(A)[0]
		Service_AH=fourBit(A)[1]
		Service_AL=fourBit(A)[2]
		Method_AH=fourBit(A)[3]
		Method_AL=fourBit(A)[4]
		NID_B2=0
		NID_B1=0
		Service_BH=0
		Service_BL=0
		Method_BH=0
		Method_BL=B

	##generate list 1*30
	list1=[0]*22

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x01"
	list1[2]=algorithm_mode
	list1[3]=NID_A2
	list1[4]=NID_A1
	list1[5]=Service_AH
	list1[6]=Service_AL
	list1[7]=Method_AH
	list1[8]=Method_AL
	list1[9]=NID_B2
	list1[10]=NID_B1
	list1[11]=Service_BH
	list1[12]=Service_BL
	list1[13]=Method_BH
	list1[14]=Method_BL
	list1[15]=C
	list1[16]=0
	list1[17]=0
	list1[18]=highValue(a)
	list1[19]=lowValue(a)
	list1[20]=highValue(b)
	list1[21]=lowValue(b)
	

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def substraction(A,B,C,a,b):
	if str(A).isalpha()==True and str(B).isalpha()==True:
		print "variable+variable"
		algorithm_mode="0x04"
		NID_A2=0
		NID_A1=0
		Service_AH=0
		Service_AL=0
		Method_AH=0
		Method_AL=A
		NID_B2=0
		NID_B1=0
		Service_BH=0
		Service_BL=0
		Method_BH=0
		Method_BL=B

	if str(A).isalpha()==True and any(i.isdigit() for i in str(B))==True:	
		print "variable+value"		
		algorithm_mode="0x05"
		NID_A2=0
		NID_A1=0
		Service_AH=0
		Service_AL=0
		Method_AH=0
		Method_AL=A
		NID_B2=0
		NID_B1=fourBit(B)[0]
		Service_BH=fourBit(B)[1]
		Service_BL=fourBit(B)[2]
		Method_BH=fourBit(B)[3]
		Method_BL=fourBit(B)[4]

	if any(i.isdigit() for i in str(A))==True and any(i.isdigit() for i in str(B))==True:
		print "value+value"
		algorithm_mode="0x07"
		NID_A2=0
		NID_A1=fourBit(A)[0]
		Service_AH=fourBit(A)[1]
		Service_AL=fourBit(A)[2]
		Method_AH=fourBit(A)[3]
		Method_AL=fourBit(A)[4]
		NID_B2=0
		NID_B1=fourBit(B)[0]
		Service_BH=fourBit(B)[1]
		Service_BL=fourBit(B)[2]
		Method_BH=fourBit(B)[3]
		Method_BL=fourBit(B)[4]
	if any(i.isdigit() for i in str(A))==True and str(B).isalpha()==True:
		print "value+variable"
		algorithm_mode="0x09"
		NID_A2=0
		NID_A1=fourBit(A)[0]
		Service_AH=fourBit(A)[1]
		Service_AL=fourBit(A)[2]
		Method_AH=fourBit(A)[3]
		Method_AL=fourBit(A)[4]
		NID_B2=0
		NID_B1=0
		Service_BH=0
		Service_BL=0
		Method_BH=0
		Method_BL=B

	##generate list 1*30
	list1=[0]*22

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x02"
	list1[2]=algorithm_mode
	list1[3]=NID_A2
	list1[4]=NID_A1
	list1[5]=Service_AH
	list1[6]=Service_AL
	list1[7]=Method_AH
	list1[8]=Method_AL
	list1[9]=NID_B2
	list1[10]=NID_B1
	list1[11]=Service_BH
	list1[12]=Service_BL
	list1[13]=Method_BH
	list1[14]=Method_BL
	list1[15]=C
	list1[16]=0
	list1[17]=0
	list1[18]=highValue(a)
	list1[19]=lowValue(a)
	list1[20]=highValue(b)
	list1[21]=lowValue(b)
	

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def multiply(A,B,C,a,b):
	if str(A).isalpha()==True and str(B).isalpha()==True:
		print "variable+variable"
		algorithm_mode="0x04"
		NID_A2=0
		NID_A1=0
		Service_AH=0
		Service_AL=0
		Method_AH=0
		Method_AL=A
		NID_B2=0
		NID_B1=0
		Service_BH=0
		Service_BL=0
		Method_BH=0
		Method_BL=B

	if str(A).isalpha()==True and any(i.isdigit() for i in str(B))==True:	
		print "variable+value"		
		algorithm_mode="0x05"
		NID_A2=0
		NID_A1=0
		Service_AH=0
		Service_AL=0
		Method_AH=0
		Method_AL=A
		NID_B2=0
		NID_B1=fourBit(B)[0]
		Service_BH=fourBit(B)[1]
		Service_BL=fourBit(B)[2]
		Method_BH=fourBit(B)[3]
		Method_BL=fourBit(B)[4]

	if any(i.isdigit() for i in str(A))==True and any(i.isdigit() for i in str(B))==True:
		print "value+value"
		algorithm_mode="0x07"
		NID_A2=0
		NID_A1=fourBit(A)[0]
		Service_AH=fourBit(A)[1]
		Service_AL=fourBit(A)[2]
		Method_AH=fourBit(A)[3]
		Method_AL=fourBit(A)[4]
		NID_B2=0
		NID_B1=fourBit(B)[0]
		Service_BH=fourBit(B)[1]
		Service_BL=fourBit(B)[2]
		Method_BH=fourBit(B)[3]
		Method_BL=fourBit(B)[4]
	if any(i.isdigit() for i in str(A))==True and str(B).isalpha()==True:
		print "value+variable"
		algorithm_mode="0x09"
		NID_A2=0
		NID_A1=fourBit(A)[0]
		Service_AH=fourBit(A)[1]
		Service_AL=fourBit(A)[2]
		Method_AH=fourBit(A)[3]
		Method_AL=fourBit(A)[4]
		NID_B2=0
		NID_B1=0
		Service_BH=0
		Service_BL=0
		Method_BH=0
		Method_BL=B

	##generate list 1*30
	list1=[0]*22

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x03"
	list1[2]=algorithm_mode
	list1[3]=NID_A2
	list1[4]=NID_A1
	list1[5]=Service_AH
	list1[6]=Service_AL
	list1[7]=Method_AH
	list1[8]=Method_AL
	list1[9]=NID_B2
	list1[10]=NID_B1
	list1[11]=Service_BH
	list1[12]=Service_BL
	list1[13]=Method_BH
	list1[14]=Method_BL
	list1[15]=C
	list1[16]=0
	list1[17]=0
	list1[18]=highValue(a)
	list1[19]=lowValue(a)
	list1[20]=highValue(b)
	list1[21]=lowValue(b)
	

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def division(A,B,C,a,b):
	if str(A).isalpha()==True and str(B).isalpha()==True:
		#print "variable+variable"
		algorithm_mode="0x04"
		NID_A2=0
		NID_A1=0
		Service_AH=0
		Service_AL=0
		Method_AH=0
		Method_AL=A
		NID_B2=0
		NID_B1=0
		Service_BH=0
		Service_BL=0
		Method_BH=0
		Method_BL=B

	if str(A).isalpha()==True and any(i.isdigit() for i in str(B))==True:	
		#print "variable+value"		
		algorithm_mode="0x05"
		NID_A2=0
		NID_A1=0
		Service_AH=0
		Service_AL=0
		Method_AH=0
		Method_AL=A
		NID_B2=0
		NID_B1=fourBit(B)[0]
		Service_BH=fourBit(B)[1]
		Service_BL=fourBit(B)[2]
		Method_BH=fourBit(B)[3]
		Method_BL=fourBit(B)[4]

	if any(i.isdigit() for i in str(A))==True and any(i.isdigit() for i in str(B))==True:
		#print "value+value"
		algorithm_mode="0x07"
		NID_A2=0
		NID_A1=fourBit(A)[0]
		Service_AH=fourBit(A)[1]
		Service_AL=fourBit(A)[2]
		Method_AH=fourBit(A)[3]
		Method_AL=fourBit(A)[4]
		NID_B2=0
		NID_B1=fourBit(B)[0]
		Service_BH=fourBit(B)[1]
		Service_BL=fourBit(B)[2]
		Method_BH=fourBit(B)[3]
		Method_BL=fourBit(B)[4]
	if any(i.isdigit() for i in str(A))==True and str(B).isalpha()==True:
		#print "value+variable"
		algorithm_mode="0x09"
		NID_A2=0
		NID_A1=fourBit(A)[0]
		Service_AH=fourBit(A)[1]
		Service_AL=fourBit(A)[2]
		Method_AH=fourBit(A)[3]
		Method_AL=fourBit(A)[4]
		NID_B2=0
		NID_B1=0
		Service_BH=0
		Service_BL=0
		Method_BH=0
		Method_BL=B

	##generate list 1*30
	list1=[0]*22

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x04"
	list1[2]=algorithm_mode
	list1[3]=NID_A2
	list1[4]=NID_A1
	list1[5]=Service_AH
	list1[6]=Service_AL
	list1[7]=Method_AH
	list1[8]=Method_AL
	list1[9]=NID_B2
	list1[10]=NID_B1
	list1[11]=Service_BH
	list1[12]=Service_BL
	list1[13]=Method_BH
	list1[14]=Method_BL
	list1[15]=C
	list1[16]=0
	list1[17]=0
	list1[18]=highValue(a)
	list1[19]=lowValue(a)
	list1[20]=highValue(b)
	list1[21]=lowValue(b)
	

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

