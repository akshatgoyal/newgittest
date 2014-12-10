Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> import xlrd
>>> from xlrd import open_workbook,cellname
>>> book=open_workbook('security.xls')
>>> ques=[]
>>> for s in book.sheets():
	for i in range(s.nrows):
		for j in range(s.ncols):
			if 'Questions' == s.cell_value(i,j):
				r=i+1
				for r in range(s.nrows):
					if s.cell_value(r,j)!='':
						ques.append(s.cell_value(r,j))

						
>>> import nltk
>>> from nltk.tokenize import word_tokenize
>>> matrix=[]
>>> for i in range(0,len(ques)):
	text=word_tokenize(ques[i])
	new=nltk.pos_tag(text)
	numrows=len(new)
	numcols=len(new)
	arr=[]
	for x in range(0,numrows):
		if new[x][1].startswith('NN') or new[x][1].startswith('JJ') or new[x][1].startswith('VB'):
			arr.append(new[x][0])
	matrix.append(arr)

	

>>> matrix[2]
[u'Do', u'have', u'internal/external', u'reviews', u'security', u'program', u'processes', u'facility', u'service', u'bureau', u'e.g.', u'Internal', u'Audit', u'Bank', u'Regulatory', u'Agency', u'Independent', u'SAS70', u'review', u'etc', u'Please', u'list', u'apply', u'including', u'conducts', u'review', u'frequency', u'review', u'last', u'review', u'date']
>>> numrows=len(matrix)
>>> print numrows
210
>>> numcols=len(matrix)
>>> print numcols
210
>>> matrix[1]
[u'recognised', u'standards', u'are', u'information', u'security', u'practices', u'compliant', u'adhering']
>>> for t in range(0,len(arr)):
	arrr=[]
	arrr.append('aabssdas')
    arr.append(arrr)
    
  File "<pyshell#40>", line 4
    arr.append(arrr)
                   ^
IndentationError: unindent does not match any outer indentation level
>>> for t in range(0,len(arr)):
	arrr=[]
	arrr.append('akshat')

	
>>> for t in range(0,len(arr)):
	arrr=[]
	arrr.append('askaht')
	arr.append(arr)

	
>>> matrix[2][2][1]
u'n'
>>> for t in range(0,len(arr)):
	
KeyboardInterrupt
>>> matrix[2,2]

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    matrix[2,2]
TypeError: list indices must be integers, not tuple
>>> import nltk
>>> from nltk.tokenize import word_tokenize
>>> matrix=[]
>>> for i in range(0,len(ques)):
	text=word_tokenize(ques[i])
	new=nltk.pos_tag(text)
	numrows=len(new)
	numcols=len(new)
	arr=[]
	for x in range(0,numrows):
		if new[x][1].startswith('NN') or new[x][1].startswith('JJ') or new[x][1].startswith('VB'):
			arr2=[]
			arr2.append(new[x][0])
			arr2.append('akshat')
		arr.append(arr2)
	matrix.append(arr)

	
>>> matrix[2][2][1]
'akshat'
>>> matrix[2]
[[u'Do', 'akshat'], [u'Do', 'akshat'], [u'have', 'akshat'], [u'have', 'akshat'], [u'internal/external', 'akshat'], [u'reviews', 'akshat'], [u'reviews', 'akshat'], [u'reviews', 'akshat'], [u'security', 'akshat'], [u'program', 'akshat'], [u'program', 'akshat'], [u'processes', 'akshat'], [u'processes', 'akshat'], [u'processes', 'akshat'], [u'facility', 'akshat'], [u'facility', 'akshat'], [u'service', 'akshat'], [u'bureau', 'akshat'], [u'bureau', 'akshat'], [u'e.g.', 'akshat'], [u'e.g.', 'akshat'], [u'Internal', 'akshat'], [u'Audit', 'akshat'], [u'Audit', 'akshat'], [u'Bank', 'akshat'], [u'Regulatory', 'akshat'], [u'Agency', 'akshat'], [u'Agency', 'akshat'], [u'Independent', 'akshat'], [u'SAS70', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'etc', 'akshat'], [u'etc', 'akshat'], [u'etc', 'akshat'], [u'Please', 'akshat'], [u'list', 'akshat'], [u'list', 'akshat'], [u'list', 'akshat'], [u'apply', 'akshat'], [u'apply', 'akshat'], [u'including', 'akshat'], [u'including', 'akshat'], [u'conducts', 'akshat'], [u'conducts', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'frequency', 'akshat'], [u'frequency', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'last', 'akshat'], [u'review', 'akshat'], [u'date', 'akshat'], [u'date', 'akshat']]
>>> matrix[2][2]
[u'have', 'akshat']
>>> import nltk
>>> from nltk.tokenize import word_tokenize
>>> matrix=[]
>>> for i in range(0,len(ques)):
	text=word_tokenize(ques[i])
	new=nltk.pos_tag(text)
	numrows=len(new)
	numcols=len(new)
	arr=[]
	for x in range(0,numrows):
		if new[x][1].startswith('NN') or new[x][1].startswith('JJ') or new[x][1].startswith('VB'):
			arr2=[]
			arr2.append('akshat')
		arr.append(new[x][0])
		arr.append(arr2)
	matrix.append(arr)

	
>>> matrix[2]
[[u'Do', 'akshat'], [u'Do', 'akshat'], [u'have', 'akshat'], [u'have', 'akshat'], [u'internal/external', 'akshat'], [u'reviews', 'akshat'], [u'reviews', 'akshat'], [u'reviews', 'akshat'], [u'security', 'akshat'], [u'program', 'akshat'], [u'program', 'akshat'], [u'processes', 'akshat'], [u'processes', 'akshat'], [u'processes', 'akshat'], [u'facility', 'akshat'], [u'facility', 'akshat'], [u'service', 'akshat'], [u'bureau', 'akshat'], [u'bureau', 'akshat'], [u'e.g.', 'akshat'], [u'e.g.', 'akshat'], [u'Internal', 'akshat'], [u'Audit', 'akshat'], [u'Audit', 'akshat'], [u'Bank', 'akshat'], [u'Regulatory', 'akshat'], [u'Agency', 'akshat'], [u'Agency', 'akshat'], [u'Independent', 'akshat'], [u'SAS70', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'etc', 'akshat'], [u'etc', 'akshat'], [u'etc', 'akshat'], [u'Please', 'akshat'], [u'list', 'akshat'], [u'list', 'akshat'], [u'list', 'akshat'], [u'apply', 'akshat'], [u'apply', 'akshat'], [u'including', 'akshat'], [u'including', 'akshat'], [u'conducts', 'akshat'], [u'conducts', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'frequency', 'akshat'], [u'frequency', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'review', 'akshat'], [u'last', 'akshat'], [u'review', 'akshat'], [u'date', 'akshat'], [u'date', 'akshat']]
>>> matrix[2][2]
[u'have', 'akshat']
>>> arr[0].append(arr2)

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    arr[0].append(arr2)
AttributeError: 'unicode' object has no attribute 'append'
>>> matrix[1]
[[u'Questions', 'akshat'], [u'Questions', 'akshat'], [u'recognised', 'akshat'], [u'standards', 'akshat'], [u'are', 'akshat'], [u'are', 'akshat'], [u'information', 'akshat'], [u'security', 'akshat'], [u'practices', 'akshat'], [u'compliant', 'akshat'], [u'compliant', 'akshat'], [u'compliant', 'akshat'], [u'adhering', 'akshat'], [u'adhering', 'akshat'], [u'adhering', 'akshat']]
>>> import nltk
>>> from nltk.tokenize import word_tokenize
>>> matrix=[]
>>> for i in range(0,len(ques)):
	text=word_tokenize(ques[i])
	new=nltk.pos_tag(text)
	numrows=len(new)
	numcols=len(new)
	arr=[]
	fro x in range(0,numrows):
		
SyntaxError: invalid syntax
>>> import nltk
>>> from nltk.tokenize import word_tokenize
>>> matrix=[]
>>> for i in range(0,len(ques)):
	text=word_tokenize(ques[i])
	new=nltk.pos_tag(text)
	numrows=len(new)
	numcols=len(new)
	arr=[]
	count=0
	for x in range(0,numrows):
		if new[x][1].startswith('NN') or new[x][1].startswith('JJ') or new[x][1].startswith('VB'):
			arr[count]=new[x][0]
			count=count+1
			arr2=[]
			arr2.append('akshat')
			arr2.append('ayush')
		arr[count].append(arr2)
	matrix.append(arr)

	

Traceback (most recent call last):
  File "<pyshell#113>", line 10, in <module>
    arr[count]=new[x][0]
IndexError: list assignment index out of range
>>> import nltk
>>> from nltk.tokenize import word_tokenize
>>> matrix=[]
>>> for i in range(0,len(ques)):
	text=word_tokenize(ques[i])
	new=nltk.pos_tag(text)
	numrows=len(new)
	numcols=len(new)
	arr=[]
	count=0
	for x in range(0,numrows):
		if new[x][1].startswith('NN') or new[x][1].startswith('JJ') or new[x][1].startswith('VB'):
			arr.append(new[x][0])
			arr2=[]
			arr2.append('akshat')
			arr2.append('ayush')
		arr[count].append(arr2)
		count=count+1
	matrix.append(arr)

	

Traceback (most recent call last):
  File "<pyshell#125>", line 14, in <module>
    arr[count].append(arr2)
AttributeError: 'unicode' object has no attribute 'append'
>>> import nltk
>>> from nltk.tokenize import word_tokenize
>>> matrix=[]for i in range(0,len(ques)):
	text=word_tokenize(ques[i])
	new=nltk.pos_tag(text)
	numrows=len(new)
	numcols=len(new)
	arr=[]
	count=0
	for x in range(0,numrows):
		if new[x][1].startswith('NN') or new[x][1].startswith('JJ') or new[x][1].startswith('VB'):
			arr.append(new[x][0])
			arr2=[]
			arr2.append('akshat')
			arr2.append('ayush')
		arr[count].append(arr2)
		count=count+1
	matrix.append(arr)
	
>>> 
>>> import nltk
>>> from nltk.tokenize import word_tokenize
>>> matrix=[]
>>> for i in range(0,len(ques)):
	text=word_tokenize(ques[i])
	new=nltk.pos_tag(text)
	numrows=len(new)
	numcols=len(new)
	arr=[]
	count=0
	for x in range(0,numrows):
		arr.append(new[x][0])
		
		if new[x][1].startswith('NN') or new[x][1].startswith('JJ') or new[x][1].startswith('VB'):
			
