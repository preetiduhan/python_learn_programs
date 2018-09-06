'''
Created on Sep 6, 2018

@author: preeti
'''
from operator import itemgetter

def sort_file():
    with open('student_data','rt') as f:
        lines= [line.split(' ') for line in f]

    for line in sorted(lines, key=itemgetter(2)):
        print(line)
        print(' '.join(line))

if __name__ == '__main__':
    sort_file()