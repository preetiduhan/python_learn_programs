'''
Created on Oct 14, 2018

@author: preeti
'''
INF = 2147483647
def min_cost_station(cost):
    n=len(cost)
    min_cost=[0 for i in range(n)]
    min_cost[1]=cost[0][1]
    for i in range(2,n):
        min_cost[i]=cost[0][i]
        for j in range(1,i):
            if(min_cost[i] > min_cost[j]+cost[j][i]):
                min_cost[i]=min_cost[j]+cost[j][i]
        #print(i,' =',min_cost[i])
    return min_cost[3]
if __name__ == '__main__':
    cost= [ [0, 15, 80, 90],
            [INF, 0, 40, 50],
            [INF, INF, 0, 70],
            [INF, INF, INF, 0]]

    result=min_cost_station(cost)
    print(result)