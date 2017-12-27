import re
#
def isPhoneNumber(chunk):
    reg_exp_object=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    print chunk
    match_object = reg_exp_object.search(chunk)
    print match_object
    if match_object == None:
        return False
    print ("match object", match_object.group())
    return True

if __name__ == '__main__':
    print "enter the message and check if phone number is there in message\n"
    mesg= "hello my number is 988-689-9567\n"
    #print len(mesg)
    for i in range(0,len(mesg)):
        #print i
        chunk= mesg[i:i+12]
        #print chunk
        a=isPhoneNumber(chunk)
        if not a:
            print ("not found in chunk",chunk)



