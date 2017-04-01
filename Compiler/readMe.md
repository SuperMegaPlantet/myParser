## demo2.py ##


**tokennizer()**

初步对文本进行分词处理。


-内容

grammar里不同功能函数的分词器都在这个功能里调用。

-输出
```
{((['a','=','1',{}),2,7),((['b','=','2',{}),9,14),....
```
取词后得到的列表。
格式是Pyparsing的scanString()格式，包含提取的分词，和文本内的起始位置。
输出的取词顺序和文档不相符，需要进一步整理。


**cleanScanStringResult()**

对得到的分词列表排序

输出

```
[['A','=','1'],['B','=','2']...]
```


**identifier()**

从排好序的分词列表依次生成报文。

内部从myParser调用生成报文的功能。


输出

```
['0xA1000000002550255','0xA50x01A000000002550255',...]
```

## myParser/newOperation.py ##

**fourBit()**

将整数或浮点自动转成16BIT格式，同时自动存储小数点后数字

在输入为整数时，自动加小数点

**addition()**


**substraction()**


**multiply()**


**division()**

输入算式，输出报文。


会考虑变量和数值做运算的四种情况。内容略重复。



## /myParser/variable.py ##

**setVariableValue()**


内容和四则运算相同


## tokenizer.py ##

**tokenizer()**
遍历输入代码的每一行。分别放到grammar里的不同功能函数分词器，输出的分词结果存到列表里。此时未按原文顺序排序。


**startEnd()**

在已排序的分词列表内自动添加程序开始和程序结束的报文，和自动的行号。

**cleanScanStringResult()**

对未排序的分词列表进行排序，同时把相应的行号存入列表。



## identifier.py ##

**identifier()**

识别分词列表内的内容，调用myParser内生成相应报文的指令。

**equation()**
**addIdentifier()**
**subsIdentifier()**
**multiIdentifier()**
**diviIdentifier()**
**start()**
**end()**
和myParser内报文生成的指令一一对应，拿分词内的关键词填写报文
