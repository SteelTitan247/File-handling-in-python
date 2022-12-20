'''
This will create a new file and will write on it. If the file exists, it will overwrite it.

myfile=open('country', 'a')
myfile.write('\nThis is a new line')
'''
try:
    myfile=open('country', 'a')
    myfile.write('\nThis is a new line')
except:
    print('Some Error occured')
else:
    print('New line appended')