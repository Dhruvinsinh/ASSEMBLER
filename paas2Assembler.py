IC.pop()
print(IC)
#MACHINE CODE GENERATION
MC=[]
counter_ltorg=1
processed_literals=[]
for i in IC:
  temp=[]
  if('DL' in i):
    ind1=i.index('DL')+1
    if(i[ind1]=='01'):
      continue
  if('AD' in i):
    ind=i.index('AD')+1
    if(i[ind]=='05'):
        temp=[]
        temp.append('00')
        temp.append('00')
        ind=i.index('C')+1
        temp.append(i[ind])
        MC.append(temp)
        continue
    elif(i[ind]=='01'):
      continue
  for j in range(0,len(i),2):

    if(i[j]=='S'):
      if(ST[i[j+1]][0] not in LABEL):
        temp.append(str(ST[i[j+1]][1]))
    elif(i[j]=='L'):
      temp.append(str(LT[i[j+1]][1]))
    else:
      temp.append(i[j+1])
  MC.append(temp)
print("Machine Code")
for i in MC:
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
[['AD', '01', 'C', '100'], ['IS', '09', 'S', 0], ['IS', '04', 'RG', '02', 'L', 0], ['IS', '05', 'RG', '02', 'S', 1], ['S', 2, 'IS', '03', 'RG', '02', 'S', 1], ['AD', '05', 'DL', '02', 'C', "'1'"], ['IS', '04', 'RG', '03', 'L', 1], ['IS', '05', 'RG', '02', 'L', 2], ['AD', '05', 'DL', '02', 'C', "'2'"], ['AD', '05', 'DL', '02', 'C', "'5'"], ['S', 0, 'DL', '01', 'C', '1'], ['S', 1, 'DL', '01', 'C', '1']]
Machine Code
['09', '109']
['04', '02', '104']
['05', '02', '110']
['03', '02', '110']
['00', '00', "'1'"]
['04', '03', '107']
['05', '02', '108']
['00', '00', "'2'"]
['00', '00', "'5'"]
