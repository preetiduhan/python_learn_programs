##This is basic program to find patterns of text without using regular expression##
##This cumbersome program leads us to use of regular expressions##

from sre_parse import isdigit
import sys
from test.test_binop import isnum, isint
def isphoneNumber(mesg):
    if len(mesg)!=12:
        #print "length is less than 12 "
        return False

    for i in range(0,3):
        if not isint(i):
            #print "number is not a digit"
            return False
    if mesg[3]!='-':
        return False
    for j in range(3,6):
         if not isint(i):
            return False
    if mesg[7] != '-':
        return False
    for k in range(8,12):
        if not isint(k):
            return False
    #print "if it has reached here"
    return True

if __name__ == '__main__':
    print "enter the message and check if phone number is there in message\n"
    mesg= "hello my number is 988-689-9567\n"
    #print len(mesg)
    for i in range(0,len(mesg)):
        #print i
        chunk= mesg[i:i+12]
        #print chunk
        a=isphoneNumber(chunk)
        if a:
            print ("yes this is phone number%s", chunk)
            sys.exit()
    print "there is no phone number\n"






