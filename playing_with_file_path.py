import os
import shutil
import zipfile
filename =['prt.txt','prt1.py','ptr2.py','prt3.py']
for file1 in filename:
    print os.path.join('usr','bin','path',file1)
    #print os.getcwd()
    os.chdir("C:\eclipse452-64-rtc5-j7-director\eclipse")
   # print os.getcwd()
#os.makedirs("C:\eclipse452-64-rtc5-j7-director\eclipse\preeti_prt")
print os.getcwd()
print os.path.exists('C:\eclipse452-64-rtc5-j7-director\eclipse')
print os.path.isdir('C:\eclipse452-64-rtc5-j7-director\eclipse')
print os.path.isfile('C:\eclipse452-64-rtc5-j7-director\eclipse')

p= open('C:\preeti\hello.txt','r')
a=p.read()
p.close()
for i in os.listdir():
    os.unlink(filenam.txt)
    os.rmdir(path)
shutil.rmtree(path)
os.chdir('path')
file_zipfile=zipfile.ZipFile('zipfile.txz')
file_zipfile.extractall()
file_zipfile.getinfo('file.zip')
file_zipfile.close()


print a
