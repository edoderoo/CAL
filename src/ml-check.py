
type = ''

def getObjectType(line):
  type='?'
  if line[0:5].upper() == 'TABLE':
     type = 'T'
  if line[0:4].upper() == 'PAGE':
     type = 'P'
  if line[0:8].upper() == 'CODEUNIT':
     type = 'C'
  if line[0:6].upper() == 'REPORT':
     type = 'R'
  if line[0:7].upper() == 'XMLPORT':
     type = 'X'
  if line[0:9].upper() == 'MENUSUITE':
     type = 'X'
  if type=='?'   : print(line)

def process_line(line):
  if line[0:6].upper() == 'OBJECT':
     getObjectType(line[7:])
  

#source = open('/home/edo/Downloads/RMS.txt', 'rb') #
source = open('/home/edo/Downloads/RMS.txt', encoding='cp1252')
for line in source:
    process_line(line)
