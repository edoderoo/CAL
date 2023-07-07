#DSA - updated
objectType = ''
cursor = 0
objectNr = 0
objectNr = 0
objectName = ''

def getObjectName(line):
   print('%s_^_%s_!_%s' % (objectType, objectNr, line))

def getObjectNr(line):
   global cursor 
   foundobjectNr = ''

   while line[cursor:cursor+1] in '0123456789':
      foundobjectNr += line[cursor:cursor+1]
      cursor += 1
   return(foundobjectNr)   

def getObjectType(line):
  global objectType
  global objectNr
  global objectName
  global cursor
  #print('>>'+line[0:5].upper()+'<<')
  objectType='?'
  if line[7:12].upper() == 'TABLE':
     objectType = 'T'
     cursor = 13
  if line[7:11].upper() == 'PAGE':
     objectType = 'P'
     cursor = 12
  if line[7:15].upper() == 'CODEUNIT':
     objectType = 'C'
     cursor = 16
  if line[7:13].upper() == 'REPORT':
     objectType = 'R'
     cursor = 14
  if line[7:12].upper() == 'QUERY':
     objectType = 'Q'
     cursor = 13
  if line[7:14].upper() == 'XMLPORT':
     objectType = 'X'
     cursor = 15
  if line[7:16].upper() == 'MENUSUITE':
     objectType = 'M'
     cursor = 17
  if objectType=='?': 
     print(line)
     error(line)
  objectNr = getObjectNr(line)
  objectName = getObjectName(line)

def process_line(line):
  cursor = 0
  if line[0:6].upper() == 'OBJECT':
     getObjectType(line)
  #   print(line[0:6]+'><'+line[7:])
  #else:
  #   print('>>%s<<' % line[0:6])

source = open('C:/temp/RMS.txt', 'r') #
#source = open('C:/temp/tmpExample.txt', 'r') #
#source = open('/home/edo/Downloads/RMS.txt', encoding='cp1252')
for line in source:
    process_line(line)
