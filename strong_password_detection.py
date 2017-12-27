import re
#import
import sys
from nt import read

def pass_detection():

 while True:
    print ' '*20

    password = raw_input("enter password:\n\n")
    reg_exp = re.compile(r'''([a-z]+[A-Z]|[A-Z]+[a-z])+
    ([0-9]+[!@\$#%]|[!@\$#%]+[0-9])''')
    mo = reg_exp.search(password)
    print mo.group()
    if mo == None:
        print "password must contain atleast one capital,small letter and ends with numeric and special character out of these !@$#% \n "
        print "You need to enter new password"
        continue
    elif len(password) >= 6:
        print "password is strong"
        break

if __name__ == '__main__':
    pass_detection()


