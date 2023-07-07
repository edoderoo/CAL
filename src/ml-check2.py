#use a class to read all source and process from there

class navsrc:
  source = ['']
  curline = 0
  cursor = 0
  maxline = 0

  def readsource(self, filename, method):
     infile = open(filename, method)
     for line in infile:
        self.source.append(line[0:len(line)-1])
        self.maxline += 1

  def print(self):
    for line in self.source:
       print(line)



def process_line(line):
   if (False):
     print('')


src = navsrc()
src.readsource('C:/temp/smallCAL.txt', 'r')
src.print()

#source = open('C:/temp/smallCAL.txt', 'r') #
#source = open('C:/temp/RMS.txt', 'r') #
#source = open('C:/temp/tmpExample.txt', 'r') #
#source = open('/home/edo/Downloads/RMS.txt', encoding='cp1252')
