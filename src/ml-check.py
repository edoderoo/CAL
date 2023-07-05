
#source = open('/home/edo/Downloads/RMS.txt', 'rb') #
source = open('/home/edo/Downloads/RMS.txt', encoding='cp1252')
for line in source:
    print(line)
