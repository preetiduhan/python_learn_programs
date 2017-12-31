#Question:1-->You have a record of students. Each record contains the student's name, and their percent marks in Maths,
#Physics and Chemistry. The marks can be floating values. The user enters some integer followed by the names
# and marks for students. You are required to save the record in a dictionary data type. The user then enters
# a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        #print line
        name, scores = line[0], line[1:]
        #print scores
        scores = map(float, scores)
        #print scores
        student_marks[name] = scores
    query_name = raw_input()
    length=len(student_marks[query_name])
    avg=0
    for i in range(length):
        avg=avg+student_marks[query_name][i]

    print ("%.2f" %(avg/length))