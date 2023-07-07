#DSA
type = ''
cursor = 0
objectNr = 0
objectName = ''

def getObjectNr(line):
   print(line)

def getObjectType(line):
  type='?'
  if line[0:5].upper() == 'TABLE':
     type = 'T'
     cursor = 6
  if line[0:4].upper() == 'PAGE':
     type = 'P'
     cursor = 5
  if line[0:8].upper() == 'CODEUNIT':
     type = 'C'
     cursor = 9
  if line[0:6].upper() == 'REPORT':
     type = 'R'
     cursor = 7
  if line[0:7].upper() == 'XMLPORT':
     type = 'X'
     cursor = 8
  if line[0:9].upper() == 'MENUSUITE':
     type = 'X'
     cursor = 10
  if type=='?'   : error(line)
  objectNr = getObjectNr(line[cursor:])

def process_line(line):
  cursor = 0
  if line[0:6].upper() == 'OBJECT':
     getObjectType(line[7:])
  

#source = open('/home/edo/Downloads/RMS.txt', 'rb') #
source = open('/home/edo/Downloads/RMS.txt', encoding='cp1252')
for line in source:
    process_line(line)
