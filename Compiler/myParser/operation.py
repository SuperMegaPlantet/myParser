from Bit import highValue,lowValue

def absoluteValue(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=abs(ZA)	
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x10"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def acos(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.acos(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x05"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def addition(algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,ZA,ZB,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x01"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=ZA+ZB
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def AND(algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,ZA,ZB,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x20"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=ZA and ZB
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	print output_bytes
	return output_bytes;

def asin(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.asin(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x04"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def atan(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.atan(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x06"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def cos(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.cos(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x02"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def cosh(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.cosh(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x08"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def divide(algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,ZA,ZB,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x04"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=ZA/ZB
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def equal(ZA,ZB,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,a,b):


	if ZA ==ZB:
		result_C=1
	else:
		result_C=0

	print result_C

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA7"
	list1[1]="0x05"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)
	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def greater(ZA,ZB,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,a,b):


	if ZA > ZB:
		result_C=1
	else:
		result_C=0

	print result_C

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA7"
	list1[1]="0x03"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)
	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def greaterEqual(ZA,ZB,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,a,b):


	if ZA >=ZB:
		result_C=1
	else:
		result_C=0

	print result_C

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA7"
	list1[1]="0x04"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)
	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def less(ZA,ZB,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,a,b):
	if ZA<ZB :
		result_C=1
	else:
		result_C=0

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA7"
	list1[1]="0x01"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)
	

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def lessEqual(ZA,ZB,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,a,b):

	if ZA <= ZB:
		result_C=1
	else:
		result_C=0

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA7"
	list1[1]="0x02"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)
	#print list1

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def multiply(algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,ZA,ZB,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x03"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=ZA*ZB
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def NOT(algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,ZA,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x22"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)

	list1[23]=not ZA
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def notEqual(ZA,ZB,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,a,b):


	if not(ZA==ZB):
		result_C=1
	else:
		result_C=0

	#print result_C

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA7"
	list1[1]="0x06"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)
	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def OR(algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,ZA,ZB,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x21"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=ZA or ZB
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def rand(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#generate random int of range [0,ZA]
	#result_C=random.randint(0,ZA)
	#print result_C

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x12"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def rand(ZA,ZB,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#generate random int of range [ZA,ZB]
	#result_C=random.randint(ZA,ZB)
	#print result_C

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA9"
	list1[1]="0x01"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def residue(algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,ZA,ZB,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x05"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=ZA%ZB
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def selfDecrease(result_C,a,b):

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x07"
	list1[2]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def selfIncrease(result_C,a,b):

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x06"
	list1[2]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def sin(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.sin(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x01"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def sinh(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.sinh(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x07"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def squareRoot(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.sqrt(ZA)	
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x11"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def substraction(algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,NID_B1,NID_B2,NID_B3,NID_B4,NID_B5,NID_B6,service_B,method_B,ZA,ZB,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA6"
	list1[1]="0x02"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[13]=NID_B6
	list1[14]=NID_B5
	list1[15]=NID_B4
	list1[16]=NID_B3
	list1[17]=NID_B2
	list1[18]=NID_B1
	list1[19]=highValue(service_B)
	list1[20]=lowValue(service_B)
	list1[21]=highValue(method_B)
	list1[22]=lowValue(method_B)
	list1[23]=ZA-ZB
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def tan(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.tan(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x03"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;


def tanh(ZA,algorithm_mode,NID_A1,NID_A2,NID_A3,NID_A4,NID_A5,NID_A6,service_A,method_A,result_C,a,b):
	#result_C=math.tanh(ZA)

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA8"
	list1[1]="0x09"
	list1[2]=algorithm_mode
	list1[3]=NID_A6
	list1[4]=NID_A5
	list1[5]=NID_A4
	list1[6]=NID_A3
	list1[7]=NID_A2
	list1[8]=NID_A1
	list1[9]=highValue(service_A)
	list1[10]=lowValue(service_A)
	list1[11]=highValue(method_A)
	list1[12]=lowValue(method_A)
	list1[23]=result_C
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	#print list1
	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;



