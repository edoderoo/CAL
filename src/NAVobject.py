def isValidObjectChar(onechar):
   return ((onechar.lower() in '\"abcdefghijklmnopqrstuvwxyz_0123456789') and not (onechar.lower() in ' \n'))



class objectProperties:
  date = ''
  time = ''
  modified = False
  version = ''
class navField:
  fieldNr = 0
  fieldName = ''
  fieldType = ''
  fieldMLname = ''
  fieldMLoption = ''
    
class navObj:
   objectType = ''
   objectNr = 0
   objectName = ''
   fieldList = []
   codeList = []

class navSrc:
   source = ['']
   curline = 0
   cursor = 0
   maxline = 0
   objectType = ''
   objectNr = 0
   objectName = ''
   captionMustList = ['NLD','ENU']

   def parseObjectProperties():
     pass

   def readsource(self, filename, method):
     infile = open(filename, method)
     for line in infile:
        self.source.append(line[0:len(line)-1])
        self.maxline += 1

   def print(self):
    for line in self.source:
       print(line)
  
   def nextchar(self):
     if self.cursor >= len(self.source[self.curline]):
       self.cursor = 1
       self.curline += 1
       while self.source[self.curline][self.cursor:self.cursor+1]==' ':
         self.cursor += 1
     else:
       self.cursor += 1
     return(self.source[self.curline][self.cursor:self.cursor+1])

   def buildCaptionML(self):
     CaptionStr = ''
     nextchar = ''
     while nextchar!='[':
       nextchar = self.nextchar()
     nextchar = self.nextchar()  
     while nextchar != ']':
       CaptionStr += nextchar
       nextchar = self.nextchar()
     return(CaptionStr)  
   def checkCaption(self, Caption):
     pos=0
     lnglist=[]
     while pos<len(Caption):
       lng = Caption[pos:pos+3]
       lnglist.append(lng)
       while (pos+1<len(Caption)) and (Caption[pos:pos+1] != ';'):
         pos += 1
       pos += 1  
     for language in self.captionMustList:
       if not language in lnglist:
         print('%s: %s%s %s' % (language,self.objectType,self.objectNr, Caption)) 
      
   def processCaptionML(self):
      CaptionStr = self.buildCaptionML()
      self.checkCaption(CaptionStr)
      #print('<%s>' % CaptionStr)   

   def processOptionCaptionML(self):
      CaptionStr = self.buildCaptionML()
      self.checkCaption(CaptionStr)
      #print('!%s!' % CaptionStr)   
     
   def getObjectName(self):
     foundName = ''

     while not isValidObjectChar(self.source[self.curline][self.cursor:self.cursor+1]):
        self.cursor += 1

     while isValidObjectChar(self.source[self.curline][self.cursor:self.cursor+1]):
       foundName += self.source[self.curline][self.cursor:self.cursor+1]
       self.cursor += 1

     self.objectName = foundName

   def getObjectNr(self):
     foundobjectNr = ''

     while self.source[self.curline][self.cursor:self.cursor+1] in '0123456789':
        foundobjectNr += self.source[self.curline][self.cursor:self.cursor+1]
        self.cursor += 1
     if foundobjectNr!='':
       self.objectNr = int(foundobjectNr, base=10)

   def getObjectType(self):
    self.objectType='?'
    if self.source[self.curline][7:12].upper() == 'TABLE':
       self.objectType = 'T'
       self.cursor = 13
    if self.source[self.curline][7:11].upper() == 'PAGE':
       self.objectType = 'P'
       self.cursor = 12
    if self.source[self.curline][7:15].upper() == 'CODEUNIT':
       self.objectType = 'C'
       self.cursor = 16
    if self.source[self.curline][7:13].upper() == 'REPORT':
       self.objectType = 'R'
       self.cursor = 14
    if self.source[self.curline][7:12].upper() == 'QUERY':
       self.objectType = 'Q'
       self.cursor = 13
    if self.source[self.curline][7:14].upper() == 'XMLPORT':
       self.objectType = 'X'
       self.cursor = 15
    if self.source[self.curline][7:16].upper() == 'MENUSUITE':
       self.objectType = 'M'
       self.cursor = 17
    if self.objectType=='?': 
       print(self.source[self.curline])
       error(self.source[self.curline])
    self.getObjectNr()
    self.getObjectName()

   def parse(self):
     while self.curline<self.maxline:
        if self.source[self.curline][0:6].upper() == 'OBJECT':
          self.getObjectType()
        self.cursor = self.source[self.curline].lower().find('optioncaptionml=[')
        if self.cursor > 0:
           self.processOptionCaptionML()
        else:
          self.cursor = self.source[self.curline].lower().find('captionml=[')
          if self.cursor > 0:
             self.processCaptionML()
          else:
            if False:
              pass
        self.curline+=1
