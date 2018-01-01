'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2
'''

def count_substring(str1, str2):
    n=len(str2)
    count=0
    for i in range(len(str1)):
        index=str1.find(str2)
    #print index

    #print str1
        if index==-1:
            continue
        else:
            index2=index+len(str2)
        #print index2
            str1=str1[index2-1:]
            #print str1
            count=count+1
#print count
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count