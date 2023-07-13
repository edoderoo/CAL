#use a class to read all source and process from there

from NAVobject import navsrc



src = navsrc()
#filename = r'C:/temp/tmpExample.txt'
filename = r'C:/temp/smallCAL.txt'
#filename = '/home/edo/Downloads/RMS.txt'
src.readsource(filename, 'r')
src.parse()
