'''
Created on Sep 6, 2018

@author: preeti
'''
import random
import string
import gzip

def read_file():
    with open('text_file','rt') as f:
        data=f.read()
    return data

def write_file_doesnt_exit():
    with open('text_file123','xt') as f:
        data=''.join(random.choice(string.ascii_letters) for _ in range(5))
        f.write(data)
        return f

def read_gzip_file():
    with gzip.open('file.gz','rt') as f:
        text=f.read()

def read_in_blocks():
    pass


if __name__ == '__main__':
    t=read_file()
    text1=''.join(random.choice(string.ascii_letters+string.digits) for i in range(5))
    f=open('text_file','at')
    f.writelines(text1)
    f1=write_file_doesnt_exit()
    f=open('text_file1','rt')
    print(f.read())
