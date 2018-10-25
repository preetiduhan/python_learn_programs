def count_paths(m,n):
    '''if rightward and downward movement is allowed'''
    if(m==1 or n==1):
        return 1
    else:
        return count_paths(m-1,n)+count_paths(m,n-1)

def count_paths_2(m,n):
    '''if rightward,downward and diagnol movement are allowed'''
    if(m==1 or n==1):
        return 1
    else:
        return count_paths_2(m-1,n)+count_paths_2(m,n-1)+count_paths_2(m-1, n-1)

result=count_paths(2,2)
print(result,end=' ')
result=count_paths(2,3)
print(result,end=' ')
result=count_paths(3,3)
print(result,end=' ')
result=count_paths_2(2,2)
print(result,end=' ')
result=count_paths_2(2,3)
print(result,end=' ')
result=count_paths_2(3,3)
print(result,end=' ')