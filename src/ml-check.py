#DSA - updated

objectType = ''
cursor = 0
objectNr = 0
objectNr = 0
objectName = ''
indentlevel = 0
inString = False
inLineComment = False
inMultiLineComment = False
printline = ''

class bcolors:
   STRING = '\033[96m'
   LCOMMENT = '\033[92m'
   SCOMMENT = '\033[94m'

def charprint(char):
   global printline
   printline += char   
   if char=='\n':
      print(printline)
      printline = ''

def parseChar(char):
  global indentlevel, inString, inLineComment, inMultiLineComment

  if inString or (not (inLineComment or inMultiLineComment)):
    if ((not inString) and (char=='{')):
       indentlevel += 1
    if ((not inString) and (char=='}')):
       indentlevel -= 1
    if ((not inString) and (not inLineComment) and (not inMultiLineComment) and (char=='\'')):
       inString = True

  if inString:
    charprint(char)     


def parseLine(line):
   global cursor
   
   cursor=0
   for char in line:
      parseChar(char)
      cursor += 1

def isValidObjectChar(onechar):
   return ((onechar.lower() in '\"abcdefghijklmnopqrstuvwxyz_0123456789') and not (onechar.lower() in ' \n'))

def getObjectName(line):
   global cursor
   foundName = ''

   while not isValidObjectChar(line[cursor:cursor+1]):
      cursor += 1

   while isValidObjectChar(line[cursor:cursor+1]):
     foundName += line[cursor:cursor+1]
     cursor += 1

   return(foundName)

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
  else:
     parseLine(line)  

source = open('C:/temp/RMS.txt', 'r') #
#source = open('C:/temp/tmpExample.txt', 'r') #
#source = open('/home/edo/Downloads/RMS.txt', encoding='cp1252')
for line in source:
    process_line(line)
