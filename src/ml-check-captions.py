#use a class to read all source and process from there

from NAVobject import navsrc


import platform
match platform.platform(terse=True)[0:5]:
  case 'Linux':
     filename = '/home/edo/Downloads/RMS.txt'
  case 'Windo': 
    #filename = r'C:/temp/tmpExample.txt'
    filename = r'C:/temp/smallCAL.txt'
  case _:
    print(platform.platform(terse=True))


src = navsrc()
src.readsource(filename, 'r')
src.parse()
