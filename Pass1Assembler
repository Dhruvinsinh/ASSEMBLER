#MOT TABLE
MOT_TABLE=[['STOP','IS','00','1'],['ADD','IS','01','1'],['SUB','IS','02','1'],['MULTI','IS','03','1'],['MOVER','IS','04','1'],['MOVEM','IS','05','1'],['COMB','IS','06','1'],['BC','IS','07','1'],['DIV','IS','08','1'],['READ','IS','09','1'],['PRINT','IS','10','1'],
           ['START','AD','01'],['END','AD','02'],['ORIGIN','AD','03'],['EQU','AD','04'],['LTORG','AD','05'],
           ['DS','DL','01'],['DC','DL','02','1'],
           ['AREG','RG','01'],['BREG','RG','02'],['CREG','RG','03'],
           ['EQ','CC','01'],['LT','CC','02'],['GT','CC','03'],['LE','CC','04'],['GE','CC','05'],['NE','CC','06']]
#TAKING INPUT FROM COMPILER AS ASSEMBLY PROGRAM
INPUT=[]
while(True):
  input_data=input("")
  if(input_data=="break"):
    break
  else:
    INPUT.append(input_data)
print(INPUT)
def KEYWORDS():
  data=[]
  global MOT_TABLE
  for i in MOT_TABLE:
    data.append(i[0])
  return data
keywords=KEYWORDS()
print(keywords)
#DATA STRUCTURE AND LC
LC=[['']]
PT=[0]
ST=[]
LT=[]
c=0
addr=0
entered_symbol=[]
LABEL=[]
def LABEL_OR_SYMBOL_OR_LITERAl(i,addr):
  global keywords,ST,entered_symbol,LT,LABEL
  if("END" in i):
    return
  if(i=="A MULTI BREG,TERM"):
    print(len(i))
  if(len(i)>=2):
    for j in keywords:
      if(j in i):
        i=i.replace(j,'')
    i=i.split(",")
    if(len(i)==1):
      i=i[0].split(" ")
      
      for j in i:
          if(j.strip()==''):
            i.remove(j)
        #print(i)
      if(len(i)==1):
        if("=" in i[0].strip()):
          temp=[]
          temp_data=i[0].strip().split("=")
          temp.append(temp_data[1])
          temp.append("-")
          LT.append(temp)
        else:
          temp=[]
          temp.append(i[0].strip())
          temp.append("-")
          if(i[0] not in entered_symbol):
            ST.append(temp)
            entered_symbol.append(i[0])
      else:
        if("=" in i[0].strip()):
          temp=[]
          temp_data=i[0].strip().split("=")
          temp.append(temp_data[1])
          temp.append("-")
          LT.append(temp)
        
        else:
          try:
            
            isvalid=int(i[1].strip())
            
            for j in ST:
              if(i[0].strip()==j[0]):
                j[1]=addr
                
                break
          except:
            if(i[1].strip() not in entered_symbol):
              temp=[]
              temp.append(i[1].strip())
              temp.append("-")
              ST.append(temp)
              entered_symbol.append(i[1].strip())
              
    else:
      label=i[0].strip()
      symbol=i[1].strip()
      temp=[]
      if(len(label)>=1):
        if(label not in entered_symbol):
          temp.append(label)
          temp.append(addr)
          ST.append(temp)
          entered_symbol.append(label)
          if(label not in LABEL):
            LABEL.append(label)
      if(symbol not in entered_symbol):
          temp.append(symbol)
          temp.append("-")
          ST.append(temp)
          entered_symbol.append(symbol)


for i in INPUT:
  if(c==0):
    c=c+1
    addr=int(i.split(" ")[1])
    continue
  temp=[]
  temp.append(i)
  temp.append(addr)
  LC.append(temp)
  if('LTORG' in i):
    literal_table_length=len(LT)
    PT.append(literal_table_length)
    for j in LT:
      if(j[1]=="-"):
        j[1]=addr
        addr=addr+1

  elif('ORIGIN' in i):
      temp=i.split(" ")[1]
      if("+" in temp):
        temp=temp.split("+")
        for j in ST:
          if(j[0]==temp[0]):
            addr=int(j[1])+int(temp[1])
            break
      elif("-" in temp):
        temp=temp.split("-")
        for j in ST:
          if(j[0]==temp[0]):
            addr=int(j[1])-int(temp[1])
            break
      elif("*" in temp):
        temp=temp.split("*")
        for j in ST:
          if(j[0]==temp[0]):
            addr=int(j[1])*int(temp[1])
            break
      elif("/" in temp):
        temp=temp.split("/")
        for j in ST:
          if(j[0]==temp[0]):
            addr=int(j[1])/int(temp[1])
            break
  else:
    LABEL_OR_SYMBOL_OR_LITERAl(i,addr)
    addr=addr+1

print("location counter")
for i in LC:
  print(i)
print("Pool Table")
for i in PT:
  print(i)
print("Symbol Table")
for i in ST:
  print(i)
print("Literal Table")
for i in LT:
  print(i)
#intermediate code generation
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
IC=[]
for i in INPUT:
  temp_data=word_tokenize(i)
  temp=[]
  for j1 in temp_data:
    
    for j in MOT_TABLE:
      if(j[0]==j1):
        temp.append(j[1])
        temp.append(j[2])
        
    if('=' in j1):
      d1=j1.split("=")[0]
      for j in MOT_TABLE:
          if(j[0]==d1):
            temp.append(j[1])
            temp.append(j[2])
      d1=j1.split("=")[1]
      d1=d1.replace("'","")
      d1="'"+d1+"'"
      counter=0
      for j in LT:
        if(j[0]==d1):
          temp.append('L')
          temp.append(counter)
          
        counter=counter+1
      
    counter=0
    for j in ST:
      
      if(j1==j[0]):  
        temp.append('S')
        temp.append(counter)
      counter=counter+1
    try:
      d1=int(j1)
      temp.append("C")
      temp.append(str(d1))
    except:
      print("")
  IC.append(temp)
#To Handle LTORG
counter=1
already_visited=[]
dummy_IC=[]
for i in IC:
  if('AD' in i):
    ind=i.index('AD')+1
    if(i[ind]=='05'):
      
      
      value=PT[counter]
      counter=counter+1
      for i in range(0,value):
        if(LT[i][0] not in already_visited):
          temp=[]
          temp.append('AD')
          temp.append('05')
          temp.append('DL')
          temp.append('02')
          temp.append('C')
          temp.append(LT[i][0])
          already_visited.append(LT[i][0])
          dummy_IC.append(temp)
    else:
      dummy_IC.append(i)
  else:
    dummy_IC.append(i)
dummy_IC
IC=dummy_IC


print("Intermediate code")
for i in IC:
  print(i)
#output
START 100
MOVER AREG,X
ADD BREG,Y
SUB AREG,Z
X DC 5
Y DC 1
Z DC 2
END
break
['START 100', 'MOVER AREG,X', 'ADD BREG,Y', 'SUB AREG,Z', 'X DC 5', 'Y DC 1', 'Z DC 2', 'END']
['STOP', 'ADD', 'SUB', 'MULTI', 'MOVER', 'MOVEM', 'COMB', 'BC', 'DIV', 'READ', 'PRINT', 'START', 'END', 'ORIGIN', 'EQU', 'LTORG', 'DS', 'DC', 'AREG', 'BREG', 'CREG', 'EQ', 'LT', 'GT', 'LE', 'GE', 'NE']
17
location counter
['']
['READ N', 100]
["MOVER BREG='1'", 101]
['MOVEM BREG,TERM', 102]
['A MULTI BREG,TERM', 103]
['LTORG', 104]
["MOVER CREG='2'", 105]
["MOVEM BREG='5'", 106]
['LTORG', 107]
['N DS 1', 109]
['TERM DS 1', 110]
['END', 111]
Pool Table
0
1
3
Symbol Table
['N', 109]
['TERM', 110]
['A', 103]
Literal Table
["'1'", 104]
["'2'", 107]
["'5'", 108]
Intermediate code
['AD', '01', 'C', '100']
['IS', '09', 'S', 0]
['IS', '04', 'RG', '02', 'L', 0]
['IS', '05', 'RG', '02', 'S', 1]
['S', 2, 'IS', '03', 'RG', '02', 'S', 1]
['AD', '05', 'DL', '02', 'C', "'1'"]
['IS', '04', 'RG', '03', 'L', 1]
['IS', '05', 'RG', '02', 'L', 2]
['AD', '05', 'DL', '02', 'C', "'2'"]
['AD', '05', 'DL', '02', 'C', "'5'"]
['S', 0, 'DL', '01', 'C', '1']
['S', 1, 'DL', '01', 'C', '1']
['AD', '02']
