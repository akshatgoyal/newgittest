import xlrd
from xlrd import open_workbook,cellname
book=open_workbook('C:\Python27\security.xls')
ques=[]
ans=[]
for s in book.sheets():
    for i in range(s.nrows):
        for j in range(s.ncols):
            if 'Questions' == s.cell_value(i,j):
                r=i+1
                for r in range(s.nrows):
                    if s.cell_value(r,j)!='':
                        ques.append(s.cell_value(r,j))
for s in book.sheets():
    for i in range(s.nrows):
        for j in range(s.ncols):
            if 'Supplier Response' == s.cell_value(i,j):
                r=i+1
                for r in range(s.nrows):
                    if s.cell_value(r,j)!='':
                        ans.append(s.cell_value(r,j))
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
stop = stopwords.words('english')
matrix=[]
for i in range(0,len(ques)):
    text=word_tokenize(ques[i])    
    new=nltk.pos_tag(text)
    numrows=len(new)
    arr=[]
    for x in range(0,numrows):
        if new[x][1].startswith('NN') or new[x][1].startswith('JJ') or new[x][1].startswith('VB'):
            if new[x][0].lower() not in stop:
                y=lemmatizer.lemmatize(new[x][0], 'v')
                arr.append(y)
    matrix.append(arr)

var = raw_input("Input Question")
text1 = word_tokenize(var)
new1 = nltk.pos_tag(text1)
numrows1=len(new1)
arr1 = []
for x in range(0,numrows1):
    if new1[x][1].startswith('NN') or new1[x][1].startswith('JJ') or new1[x][1].startswith('VB'):
        if new1[x][0].lower() not in stop:
            y=lemmatizer.lemmatize(new1[x][0], 'v')
            arr1.append(y)

c=0
count = []
from nltk.corpus import wordnet as wn
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        for k in range(0,len(arr1)):
            if matrix[i][j]==(arr1[k]):
                c=c+1
    count.append(c)
    c=0

max=count[0]
for i in range(1,len(count)):
    if count[i] > max:
        max = count[i]
        j=i

print ques[j]
print ans[j]
