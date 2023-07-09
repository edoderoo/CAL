#use a class to read all source and process from there

def isValidObjectChar(onechar):
   return ((onechar.lower() in '\"abcdefghijklmnopqrstuvwxyz_0123456789') and not (onechar.lower() in ' \n'))

class navsrc:
   source = ['']
   curline = 0
   cursor = 0
   maxline = 0
   objectType = ''
   objectNr = 0
   objectName = ''

   def readsource(self, filename, method):
     infile = open(filename, method)
     for line in infile:
        self.source.append(line[0:len(line)-1])
        self.maxline += 1

   def print(self):
    for line in self.source:
       print(line)
  
   def processCaptionML(self):
     print('%s\n' % self.source[self.curline][self.cursor:])

   def processOptionCaptionML(self):
     print('%s\n' % self.source[self.curline][self.cursor:])
     
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
     self.objectNr = foundobjectNr

   def getObjectType(self):
    self.objectType='?'
    if self.source[self.curline][7:12].upper() == 'TABLE':
       self.objectType = 'T'
       cursor = 13
    if self.source[self.curline][7:11].upper() == 'PAGE':
       self.objectType = 'P'
       cursor = 12
    if self.source[self.curline][7:15].upper() == 'CODEUNIT':
       self.objectType = 'C'
       cursor = 16
    if self.source[self.curline][7:13].upper() == 'REPORT':
       self.objectType = 'R'
       cursor = 14
    if self.source[self.curline][7:12].upper() == 'QUERY':
       self.objectType = 'Q'
       cursor = 13
    if self.source[self.curline][7:14].upper() == 'XMLPORT':
       self.objectType = 'X'
       cursor = 15
    if self.source[self.curline][7:16].upper() == 'MENUSUITE':
       self.objectType = 'M'
       cursor = 17
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
           self.processCaptionML()
        else:
          self.cursor = self.source[self.curline].lower().find('captionml=[')
          if self.cursor > 0:
             self.processOptionCaptionML()
          else:
            if False:
              void#
        self.curline+=1

src = navsrc()
#src.readsource('C:/temp/smallCAL.txt', 'r')
src.readsource('tmpExample.txt', 'r')
src.parse()
