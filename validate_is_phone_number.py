''''A valid mobile number is a ten digit number starting with a or .

Concept

A valid mobile number is a ten digit number starting with a or .

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

Input Format

The first line contains an integer , the number of inputs.
lines follow, each containing some string.

Constraints

Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input

2
9587456281
1252478965

Sample Output

YES
NO'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def valid_phone_number(a):
    str1=a[0]
    pattern1=re.compile(r'[789]')
    mo1=pattern1.search(str1)
    pattern=re.compile(r'\d{10}')

    mo=pattern.search(a)
    if mo == None or mo1 == None:
        return 'False'
    else:
        return 'True'

if __name__ == '__main__':
    n=int(raw_input())
    numbers=[]
    for k in range(0,n):
        number=raw_input()
        numbers.append(number)

    #a=numbers.split()
    flag=[]
    for i in range(len(numbers)):
        flag1=valid_phone_number(numbers[i])
        flag.append(flag1)
    print flag
    for j in range(0,n):
        flag2=flag[j]
        if flag2=='False':
            print 'NO'
        else:
            print 'YES'