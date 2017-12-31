#Let's learn about list comprehensions! You are given three integers and representing the dimensions of a cuboid along with an integer .
# You have to print a list of all possible coordinates given by on a 3D grid where the sum of is not equal to . Here,
#Input Format

#Four integers X,Y,Z,N and each on four separate lines, respectively.

#Constraints

#Print the list in lexicographic increasing order.

#Sample Input

#1
#1
#1
#2

#Sample Output

#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
#without using list comprehension
#x = int ( raw_input("enter x\n"))
#y = int ( raw_input("enter y \n"))
#n = int ( raw_input("enter z\n"))
#ar = []
#p = 0
#for i in range ( x + 1 ) :
 #   for j in range( y + 1):
  #      if i+j != n:
   #         ar.append([])
    #        ar[p] = [ i , j ]
     #       p+=1
#print ar

#Code using list comprehensions:

x = int ( raw_input("enter x\n"))
y = int ( raw_input("enter y\n"))
z= int( raw_input("enter z\n"))
n = int ( raw_input("enter n\n"))
print [ [ i, j,k] for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j + k ) != n )]
